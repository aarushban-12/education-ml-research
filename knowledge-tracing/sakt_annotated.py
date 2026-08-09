import os

import numpy as np
import torch

from torch.nn import Module, Parameter, Embedding, Sequential, Linear, ReLU, \
    MultiheadAttention, LayerNorm, Dropout
from torch.nn.init import kaiming_normal_
from torch.nn.functional import binary_cross_entropy
from sklearn import metrics


class SAKT(Module):
    '''
        This implementation has a reference from: \
        https://pytorch.org/docs/stable/_modules/torch/nn/modules/transformer.html#TransformerEncoderLayer

        Args:
            num_q: the total number of the questions(KCs) in the given dataset
            n: the length of the sequence of the questions or responses
            d: the dimension of the hidden vectors in this model
            num_attn_heads: the number of the attention heads in the \
                multi-head attention module in this model
            dropout: the dropout rate of this model
    '''
    def __init__(self, num_q, n, d, num_attn_heads, dropout):
        super().__init__()
        self.num_q = num_q
        self.n = n
        self.d = d
        self.num_attn_heads = num_attn_heads
        self.dropout = dropout

        # Embedding for question-response interactions.
        # Correct and incorrect responses are represented separately.
        self.M = Embedding(self.num_q * 2, self.d)

        # Embedding for the current query question/skill.
        self.E = Embedding(self.num_q, d)

        # Learnable positional embeddings for the sequence.
        self.P = Parameter(torch.Tensor(self.n, self.d))

        kaiming_normal_(self.P)

        # Multi-head attention allows the model to determine which
        # previous question-response interactions are most relevant
        # when predicting the current query.
        self.attn = MultiheadAttention(
            self.d, self.num_attn_heads, dropout=self.dropout
        )

        self.attn_dropout = Dropout(self.dropout)
        self.attn_layer_norm = LayerNorm(self.d)

        # Feed-forward network applied after the attention layer.
        self.FFN = Sequential(
            Linear(self.d, self.d),
            ReLU(),
            Dropout(self.dropout),
            Linear(self.d, self.d),
            Dropout(self.dropout),
        )

        self.FFN_layer_norm = LayerNorm(self.d)

        # Final linear layer used to produce the prediction.
        self.pred = Linear(self.d, 1)

    def forward(self, q, r, qry):
        '''
            Args:
                q: the question(KC) sequence with the size of [batch_size, n]
                r: the response sequence with the size of [batch_size, n]
                qry: the query sequence with the size of [batch_size, m], \
                    where the query is the question(KC) what the user wants \
                    to check the knowledge level of

            Returns:
                p: the predicted probability of answering the query correctly
                attn_weights: the attention weights from the multi-head \
                    attention module
        '''

        # Encode each historical interaction as a combination of
        # the question/skill ID and the student's response.
        # Multiplying the response by num_q creates separate embedding
        # indices for correct and incorrect responses.
        x = q + self.num_q * r

        # Embed the historical question-response interactions.
        M = self.M(x).permute(1, 0, 2)

        # Embed the current query question/skill.
        E = self.E(qry).permute(1, 0, 2)

        # Add learnable positional information to the sequence.
        P = self.P.unsqueeze(1)

        # Create a causal mask so the model cannot attend to future
        # interactions when making a prediction.
        causal_mask = torch.triu(
            torch.ones([E.shape[0], M.shape[0]]), diagonal=1
        ).bool()

        # Add positional embeddings to the historical interactions.
        M = M + P

        # Attention allows the query to attend to relevant historical
        # question-response interactions.
        #
        # attn_weights contains the attention weights produced by SAKT.
        # These weights describe how strongly each historical interaction
        # contributes to the attention calculation.
        S, attn_weights = self.attn(E, M, M, attn_mask=causal_mask)

        S = self.attn_dropout(S)

        S = S.permute(1, 0, 2)
        M = M.permute(1, 0, 2)
        E = E.permute(1, 0, 2)

        # Residual connection followed by layer normalization.
        S = self.attn_layer_norm(S + M + E)

        # Apply the feed-forward network and another residual connection.
        F = self.FFN(S)
        F = self.FFN_layer_norm(F + S)

        # Convert the final representation into a probability between
        # 0 and 1 representing the predicted probability that the student
        # answers the next/query question correctly.
        p = torch.sigmoid(self.pred(F)).squeeze()

        return p, attn_weights

    def train_model(
        self, train_loader, test_loader, num_epochs, opt, ckpt_path
    ):
        '''
            Args:
                train_loader: the PyTorch DataLoader instance for training
                test_loader: the PyTorch DataLoader instance for test
                num_epochs: the number of epochs
                opt: the optimization to train this model
                ckpt_path: the path to save this model's parameters
        '''

        aucs = []
        loss_means = []

        max_auc = 0

        for i in range(1, num_epochs + 1):
            loss_mean = []

            for data in train_loader:
                q, r, qshft, rshft, m = data

                self.train()

                # Generate predictions for the next question using
                # the student's previous question-response history.
                p, _ = self(q.long(), r.long(), qshft.long())

                # Keep only valid target interactions indicated by the mask.
                p = torch.masked_select(p, m)
                t = torch.masked_select(rshft, m)

                opt.zero_grad()

                # Binary cross-entropy trains the model to predict
                # whether the student will answer the next question correctly.
                loss = binary_cross_entropy(p, t)

                loss.backward()
                opt.step()

                loss_mean.append(loss.detach().cpu().numpy())

            with torch.no_grad():
                for data in test_loader:
                    q, r, qshft, rshft, m = data

                    self.eval()

                    # Generate next-question correctness probabilities
                    # on the held-out test interactions.
                    p, _ = self(q.long(), r.long(), qshft.long())

                    p = torch.masked_select(p, m).detach().cpu()
                    t = torch.masked_select(rshft, m).detach().cpu()

                    # AUC measures how well the model ranks correct responses
                    # above incorrect responses.
                    #
                    # Importantly, AUC measures discrimination rather than
                    # probability calibration or reliability.
                    auc = metrics.roc_auc_score(
                        y_true=t.numpy(), y_score=p.numpy()
                    )

                    loss_mean = np.mean(loss_mean)

                    print(
                        "Epoch: {},   AUC: {},   Loss Mean: {}"
                        .format(i, auc, loss_mean)
                    )

                    # Save the model whenever it achieves a new maximum
                    # test AUC during training.
                    if auc > max_auc:
                        torch.save(
                            self.state_dict(),
                            os.path.join(
                                ckpt_path, "model.ckpt"
                            )
                        )

                        max_auc = auc

                    aucs.append(auc)
                    loss_means.append(loss_mean)

        return aucs, loss_means
