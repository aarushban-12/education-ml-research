# 3. Methodology

## 3.1 Dataset

This study uses the ASSISTments 2009 dataset, a widely used educational benchmark in knowledge tracing research. The dataset was collected through the ASSISTments intelligent tutoring system and contains records of students working through mathematics exercises. In order to be usable by the knowledge-tracing models involved in the study, the dataset was truncated to remove some unneccessary metrics. Now, each row contains a student identifier, the skill associated with the problem, whether the student answered correctly, and an order identifier that reflects the original sequence of the problem log.

Before analysis, the dataset was further cleaned by removing rows that lacked a skill_id or contained other missing/invalid values. Skill IDs were then standardized to an integer representation, and each student's interactions were ordered chronologically using the order_id field. The central focus of this study is on how student ability relates to the reliability of knowledge-tracing predictions, so only interactions with an associated skill were retained, since skill information is required by all four models evaluated here.

## 3.2 Train-Test Split

Students were randomly divided into a training set and a test set using an 80/20 split, with a fixed random seed of 42 to ensure reproducibility. Crucially, the split was performed at the student level. All interactions belonging to a given student were assigned to the same partition, so no student appeared in both the training and test sets.

This design choice reflects how knowledge-tracing models are actually used. In practice, a deployed model must make predictions for students it has never seen before. An interaction-level split would allow a model to observe some of a student's interactions during training and then be tested on the same student's later interactions, which would produce an unrealistically optimistic picture of generalization. The student-level split avoids this by evaluating each model only on students whose full interaction history was withheld from training. All four models in this study were evaluated using this same split.

## 3.3 Knowledge Tracing Models

Four models were evaluated: Logistic Regression, Bayesian Knowledge Tracing (BKT), Deep Knowledge Tracing (DKT), and Self-Attentive Knowledge Tracing (SAKT). These models span a broad range of approaches—from a simple feature-based classifier to sophisticated neural architectures—which allows the study to examine whether any reliability differences across ability groups are specific to a particular type of model or reflect a more general pattern in the field.

### 3.3.1 Logistic Regression

Logistic Regression served as the simplest baseline. Rather than modeling the sequential structure of student interactions, it predicts the probability of a correct response from four hand-crafted features: the student's overall accuracy up to that point, their accuracy on the current skill, the number of times they had previously attempted that skill, and the number of interactions since their last attempt on any skill (derived from the order_id field). This baseline is useful because it establishes a performance floor. If more complex models cannot substantially outperform it, the added complexity may not be justified.

### 3.3.2 Bayesian Knowledge Tracing

BKT is one of the oldest and most interpretable knowledge-tracing models. It treats student knowledge as a hidden binary state, either mastered or not mastered, and updates its estimate of that state after each observed response. The model is parameterized by four values: the initial probability that a student has already mastered a skill, the probability of transitioning to mastery after a practice opportunity, the probability of guessing correctly without mastery, and the probability of making an error despite having mastered the skill.

BKT was fitted using pyBKT 1.4.3, with parameters estimated separately for each of the 123 skills in the dataset using expectation-maximization on the training data. Predictions were then generated for the held-out test students.

### 3.3.3 Deep Knowledge Tracing

DKT was the first major deep learning approach to knowledge tracing and remains a standard benchmark. Rather than explicitly defining a knowledge state, DKT uses a Long Short-Term Memory (LSTM) recurrent neural network to learn a latent representation of student knowledge directly from the sequence of past interactions. The model takes a student's history of skill-response pairs as input and outputs a probability of correct response for the next skill.

DKT was implemented using the [HCNOH knowledge-tracing-collection-pytorch](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) repository and trained with a hidden size of 128, a single LSTM layer, a dropout rate of 0.2, a batch size of 128, and a learning rate of 0.001 using the Adam optimizer for 100 epochs. The checkpoint with the highest validation ROC-AUC was retained for evaluation.

### 3.3.4 Self-Attentive Knowledge Tracing

SAKT is the primary model of interest in this study. Where DKT compresses a student's entire history into a single hidden state, SAKT uses a self-attention mechanism to selectively focus on whichever past interactions are most relevant to the current prediction. This allows the model to identify which earlier skill-response pairs are most informative for predicting performance on a new skill, rather than weighting all past interactions equally.

SAKT was also implemented using the HCNOH repository and trained with a sequence length of 100, five attention heads, an embedding dimension of 125, a dropout rate of 0.2, a batch size of 128, and a learning rate of 0.0001 using the Adam optimizer for 100 epochs. As with DKT, the checkpoint with the highest validation ROC-AUC was retained.

## 3.4 Baseline Model Evaluation

All four models were evaluated using the area under the receiver operating characteristic curve (ROC-AUC). ROC-AUC was chosen because knowledge-tracing predictions are inherently probabilistic. Models output a probability of correctness rather than a binary prediction, and ROC-AUC summarizes discrimination performance across all possible classification thresholds without requiring one to be specified in advance.

## 3.5 Ability-Stratified Dataset Construction

The core analysis in this study requires evaluating each model separately on students with different levels of prior ability. To do this, quartiles were determined using student's ability, which was estimated using their overall accuracy. 4 groups were created, with Q1 being the lowest accuracy and Q4 being the highest. After this, 80% of students from each quartile were taken and randomly combined to created the training set for each model. The remaining 20% of students from each quartile were used as the testing sets. All of a given student's interactions remained within their assigned quartile, and interactions were kept in chronological order using order_id to preserve the temporal structure of each student's history.

To check whether overall accuracy is a reasonable proxy for student ability, IRT theta scores were independently estimated for each student using the py-irt library. IRT is a psychometric method that accounts for item difficulty when estimating ability, providing a more nuanced estimate than raw accuracy alone. The two measures were highly consistent: the Pearson correlation between overall accuracy and IRT theta was r = 0.9016 (p < 0.0001) and the Spearman correlation was ρ = 0.9390 (p < 0.0001). This strong agreement supports the use of overall accuracy as the primary ability measure. The IRT estimates were not used to train or modify any model. They served only as a validation of the quartile construction.

The ability-stratified datasets were constructed before any model evaluation took place. The training data and model parameters remained unchanged throughout all reliability experiments, and no students were reassigned between quartile groups at any point.

## 3.6 Reliability Experiments

With the ability-stratified datasets in place, each of the four models was trained once on the quartile training set and evaluated independently on Q1, Q2, Q3, and Q4. None of the models were retrained for a specific quartile group.

For each interaction in a given quartile, the model generated a probability of a correct response. For sequential models (DKT and SAKT), the student's preceding interactions were provided as context using the same sequence-processing procedure used during baseline evaluation. Each predicted probability was then matched with the student's actual binary outcome for metric computation.

To ensure that any observed differences across ability groups reflect genuine differences in model behavior rather than differences in who is being evaluated, the same ability-stratified test datasets were used for all four models.

Two metrics were computed for each model and each quartile. ROC-AUC was used to measure predictive discrimination: how well the model separates students who will answer correctly from those who will not. Brier Score was used to measure probabilistic calibration: how close the model's predicted probabilities are to the actual observed outcomes. Brier Score is defined as:

$$BS = \frac{1}{n} \sum_{t=1}^{n} (f_t - o_t)^2$$

where $f_t$ is the predicted probability and $o_t$ is the observed binary outcome for interaction $t$. Lower values indicate better-calibrated predictions.

Since the quartiles naturally contain different numbers of students and interactions, all valid interactions within each group were used rather than subsampling to make group sizes equal.
## References

HCNOH. (2021). *knowledge-tracing-collection-pytorch* [Software]. GitHub. https://github.com/hcnoh/knowledge-tracing-collection-pytorch