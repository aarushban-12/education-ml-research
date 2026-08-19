# Methodology
## Dataset

This study uses the ASSISTments 2009 dataset, a widely used educational dataset containing student interactions with mathematics exercises. Each interaction records a student identifier, problem/skill information, response correctness, and an interaction-order identifier. Because the objective of this study is to examine how student ability relates to the reliability of knowledge-tracing predictions, the analysis focuses on interactions for which a skill identifier is available.

The dataset was preprocessed by removing interactions with missing skill identifiers and invalid response values. Skill identifiers were converted to a consistent integer representation, and interactions were ordered chronologically within each student using order_id. After preprocessing, the resulting dataset was divided into training and testing sets at the student level. This ensured that all interactions belonging to a given student remained in the same partition.

## Train-Test Split

The data were divided using an 80/20 random student-level split. Students were randomly shuffled using a fixed random seed of 42, with 80% assigned to the training set and 20% assigned to the testing set. Importantly, the split was performed on students rather than individual interactions. Thus, no student appeared in both the training and testing sets.

A student-level split was selected because an interaction-level random split could place earlier interactions from a student in the training set and later interactions from the same student in the test set. This would allow models to encounter the same students during training and evaluation and could produce an overly optimistic estimate of generalization. The student-level split instead evaluates how well the models generalize to students whose interactions were not observed during training.

All models were evaluated using the same general 80/20 student-level random-split methodology.

## Knowledge Tracing Models

Four models were evaluated: Logistic Regression, Bayesian Knowledge Tracing (BKT), Deep Knowledge Tracing (DKT), and Self-Attentive Knowledge Tracing (SAKT). These models provide a range of approaches, from relatively simple performance-based prediction to neural sequential knowledge-tracing architectures.

### Logistic Regression

Logistic Regression was implemented as a non-sequential baseline using four features derived from a student's interaction history: overall student accuracy, accuracy on the current skill, the number of previous attempts on the current skill, and the number of interactions since the student's previous attempt on any skill, computed from the order_id field. The model predicts the probability that the student will answer the next interaction correctly.

This baseline establishes whether more complex knowledge-tracing models provide predictive information beyond relatively simple measures of student performance and experience.

### Bayesian Knowledge Tracing

BKT was used as a traditional knowledge-tracing baseline. BKT represents student knowledge of each skill as a latent state and estimates the probability that the student has mastered the skill based on previous responses. The model estimates parameters including the initial probability of mastery, learning probability, guessing probability, and slipping probability.

The BKT implementation was performed using pyBKT 1.4.3. Parameters were estimated using the model's expectation-maximization procedure on the training data, and predictions were evaluated on the held-out students.

### Deep Knowledge Tracing

DKT was implemented using the HCNOH knowledge-tracing-collection-pytorch repository. DKT represents student interactions as a sequence and uses a recurrent neural network with an LSTM to maintain a hidden representation of the student's evolving knowledge state. The model receives the student's previous skill-response interactions and predicts the probability of a correct response for subsequent skills.

For the ASSISTments 2009 experiment, the model was trained with a batch size of 128 for 100 epochs using the repository's DKT implementation. Model performance was evaluated using ROC-AUC at each epoch, and the model checkpoint corresponding to the highest validation/test AUC was recorded.

### Self-Attentive Knowledge Tracing

SAKT was also implemented using the HCNOH knowledge-tracing-collection-pytorch repository. Unlike DKT's recurrent architecture, SAKT uses an attention mechanism to identify previous interactions that are most relevant to predicting the student's response to the current skill. The architecture uses skill embeddings and response representations followed by self-attention and feed-forward layers to generate the prediction.

For the ASSISTments 2009 experiment, the SAKT model was trained with a sequence length of 100, five attention heads, an embedding dimension of 125, a dropout rate of 0.2, a batch size of 128, and a learning rate of 0.0001 using the Adam optimizer for 100 training epochs. Model performance was evaluated using ROC-AUC at each epoch, and the checkpoint corresponding to the highest validation AUC was recorded.

Using both DKT and SAKT allows the study to compare two different neural approaches to modeling student interaction sequences: recurrent modeling through an LSTM and attention-based modeling.

## Model Evaluation

Model performance was evaluated using the area under the receiver operating characteristic curve (ROC-AUC). ROC-AUC measures a model's ability to distinguish between correct and incorrect future responses across different prediction thresholds. It was selected because knowledge-tracing predictions are probabilistic and because ROC-AUC does not require selecting a single classification threshold.

## Student Ability and Prediction Reliability

The central analysis examines whether prediction reliability varies as a function of student ability. Student ability is operationalized as historical mastery rate, defined as the proportion of correct responses across all of a student's training interactions. Students will be divided into four quartiles based on this measure, with the lowest quartile representing students with the weakest demonstrated prior performance and the highest quartile representing the strongest. ROC-AUC will be computed separately within each quartile for all four models. To assess whether observed differences across quartiles are statistically meaningful, confidence intervals will be reported for each group's ROC-AUC estimate.

This analysis allows the study to move beyond overall model performance and determine whether models perform consistently across students with different levels of demonstrated ability. Differences in AUC across ability groups will be examined for each of the four models to determine whether particular knowledge-tracing approaches are more or less reliable for students at different ability levels.

## References

HCNOH. (2021). knowledge-tracing-collection-pytorch [Software]. GitHub. https://github.com/hcnoh/knowledge-tracing-collection-pytorch