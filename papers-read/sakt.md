# A Self-Attentive Model for Knowledge Tracing (SAKT) – Paper Summary

## Citation

Pandey, S., & Karypis, G. (2019). *A Self-Attentive Model for Knowledge Tracing*. arXiv:1907.06837.

---

## Research Problem

Knowledge Tracing aims to predict whether a student will correctly answer the next exercise based on their previous learning history. Earlier deep learning approaches, such as Deep Knowledge Tracing (DKT), used recurrent neural networks (LSTMs) to process the entire sequence of student interactions. Although these models achieved strong predictive performance, they often struggled with sparse educational data because they attempted to compress an entire learning history into a single hidden state. The authors argue that only a small subset of previous interactions is actually relevant when predicting performance on a new exercise.

---

## Main Idea

The main contribution of SAKT is replacing the recurrent architecture with a self-attention mechanism inspired by the Transformer. Instead of remembering every previous interaction equally, SAKT learns which past exercises are most relevant to the current question. The model computes attention weights that measure how strongly each previous interaction should influence the prediction. By focusing only on important past exercises, SAKT handles sparse educational data more effectively and improves prediction accuracy.

---

## Model Architecture

The model consists of four primary components.

**Embedding Layer:** Student interactions and the current exercise are converted into dense vector embeddings. Position embeddings are also added so the model knows the order of interactions.

**Multi-Head Self-Attention:** The current exercise acts as the query, while previous student interactions serve as the keys and values. Multiple attention heads learn different relationships simultaneously, allowing the model to focus on several relevant past interactions at once.

**Feed-Forward Network:** The attention output passes through a fully connected neural network that combines and refines the information extracted by the attention layer.

**Output Layer:** A final linear layer followed by a sigmoid function produces the probability that the student will answer the next exercise correctly.

---

## Datasets

The paper evaluates SAKT on several real-world educational datasets, including ASSISTments and synthetic datasets used in previous knowledge tracing research. The authors compare SAKT against Bayesian Knowledge Tracing, Deep Knowledge Tracing, Dynamic Key-Value Memory Networks, and other baseline methods.

---

## Results

SAKT consistently outperforms previous knowledge tracing models, achieving an average improvement of approximately 4.4% in AUC over the previous state of the art. The model also trains more efficiently than recurrent approaches because the attention mechanism can process interactions in parallel while focusing only on the most relevant past exercises.

---

## Strengths

Unlike DKT, SAKT does not rely on compressing an entire student history into a single hidden state. Instead, it explicitly identifies which previous exercises are important for predicting the next response. This makes the model more effective on sparse educational data and provides greater insight into which prior interactions influenced each prediction.

---

## Limitations

Although SAKT improves predictive performance, the attention mechanism still does not explicitly model prerequisite relationships between concepts. High attention weights indicate that previous interactions were useful for prediction, but they do not necessarily imply a causal prerequisite relationship. In addition, the model remains less interpretable than traditional probabilistic approaches such as Bayesian Knowledge Tracing.

---

## What I Learned

The biggest conceptual difference between SAKT and DKT is how they remember the past. DKT summarizes the entire interaction history in the hidden state of an LSTM, while SAKT directly compares the current exercise with previous interactions using self-attention. Instead of assuming every previous exercise is equally important, SAKT learns which past exercises are most relevant to the current prediction. This attention mechanism is the central innovation of the paper and forms the foundation for many later knowledge tracing models.
