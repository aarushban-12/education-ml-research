## What is Machine Learning?

Machine learning is a branch of artificial intelligence that allows computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task. Instead of following a fixed set of rules, a machine learning model identifies relationships within data and uses those patterns to make predictions on new, unseen examples.

---

## Supervised Learning

Supervised learning is the most common type of machine learning. In supervised learning, the model is trained using **labeled data**, meaning that each training example includes both the input and the correct output (label).

The objective is to learn a mapping from inputs to outputs so that the model can accurately predict the labels of new, unseen data.

Examples include:

- Predicting whether a student will answer a question correctly.
- Predicting housing prices.
- Classifying emails as spam or not spam.
- Detecting fraudulent financial transactions.

Because the correct answers are known during training, the model can measure its errors and gradually improve its predictions.

---

## Unsupervised Learning

Unsupervised learning uses **unlabeled data**, where no correct output is provided. Instead of making predictions, the goal is to discover hidden patterns, relationships, or structures within the data.

Common unsupervised learning tasks include:

- Clustering similar observations together.
- Discovering hidden patterns in large datasets.
- Reducing the dimensionality of data for visualization or preprocessing.
- Identifying unusual or anomalous observations.

Examples include:

- Grouping customers based on purchasing behavior.
- Organizing news articles by topic.
- Identifying groups of students with similar learning behaviors.

Unlike supervised learning, there is no "correct" answer during training. The algorithm must discover meaningful structure on its own.

---

## Regression

Regression is a supervised learning task in which the target variable is **continuous**, meaning it can take any numerical value within a range.

The goal is to predict numerical quantities.

Regression models attempt to minimize the difference between predicted values and actual values.

---

## Classification

Classification is a supervised learning task in which the target variable belongs to one of several predefined categories.

Instead of predicting a numerical value, the model predicts a class label.

Some classification problems involve two classes (binary classification), while others involve three or more classes (multiclass classification).

---

## Training and Test Sets

A machine learning model should be evaluated on data that it has never seen before. To accomplish this, datasets are divided into separate subsets before training.

### Training Set

The training set is the portion of the data used to teach the model. During training, the model learns patterns by adjusting its internal parameters to reduce prediction error.

Typically, the training set contains the majority of the available data.

---

### Validation Set

The validation set is used during model development to evaluate different model configurations and choose a model based on how each one performs on the data.

---

### Test Set

The test set is reserved until the model has been fully trained. It provides an unbiased estimate of how well the model performs on completely unseen data. If the model performs well on the test data, it is able to make accurate predictions about the dataset.

The test set should never influence model design or parameter tuning.

---

## Why Split the Data?

If a model is evaluated only on the data it was trained on, it may simply memorize the training examples instead of learning general patterns. This phenomenon is known as **overfitting**.

By evaluating the model on unseen data, we can determine whether it has learned relationships that generalize beyond the training dataset.

---

## Summary

Machine learning enables computers to learn from data instead of relying solely on manually written rules. Supervised learning uses labeled examples to make predictions, while unsupervised learning discovers patterns within unlabeled data. Supervised learning problems are typically divided into regression, which predicts continuous values, and classification, which predicts categorical labels. To ensure reliable evaluation and prevent overfitting, datasets are divided into training, validation, and test sets before model development.