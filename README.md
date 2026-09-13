# Education ML Research

This repository documents my independent research project in knowledge tracing, including the machine learning foundations, literature review, model implementations, experiments, and research paper developed throughout the project.

## Research Question

**How does student ability affect the reliability of knowledge tracing models?**

## Project Overview

Knowledge tracing (KT) models use a student's history of learning interactions to predict future performance. While these models are often evaluated using aggregate metrics, this may not show whether their predictions are equally reliable for students with different levels of ability.

This project investigates this question using the ASSISTments 2009 dataset. Four models were evaluated across four student-ability quartiles:

* Logistic Regression
* Bayesian Knowledge Tracing (BKT)
* Deep Knowledge Tracing (DKT)
* Self-Attentive Knowledge Tracing (SAKT)

Model performance was evaluated using AUC and Brier Score.

## Key Findings

The results showed that model performance varied across student-ability groups. DKT performed strongest overall and across the lower three ability groups, while BKT performed strongest for the highest-ability group. Brier Scores also showed generally lower prediction error for higher-ability students.

These results suggest that evaluating knowledge tracing models only using aggregate performance may overlook differences between student populations.

### Results

| Model               |    Q1 AUC |    Q2 AUC |    Q3 AUC |    Q4 AUC |  Q1 Brier |  Q2 Brier |  Q3 Brier |  Q4 Brier |
| ------------------- | --------: | --------: | --------: | --------: | --------: | --------: | --------: | --------: |
| Logistic Regression |     0.684 |     0.583 |     0.574 |     0.692 |     0.207 |     0.242 |     0.192 |     0.111 |
| BKT                 |     0.730 |     0.736 |     0.714 | **0.813** |     0.218 |     0.204 |     0.168 | **0.089** |
| DKT                 | **0.818** | **0.758** | **0.761** |     0.765 |     0.175 | **0.195** |     0.163 |     0.126 |
| SAKT                |     0.812 |     0.746 |     0.751 |     0.760 | **0.166** |     0.199 | **0.156** |     0.103 |

## Methodology

Students were divided into four ability quartiles based on overall interaction accuracy, with Q1 representing the lowest-ability students and Q4 representing the highest-ability students.

The models were evaluated separately on each ability group using:

* AUC — measures discrimination between correct and incorrect future responses.
* Brier Score — measures the accuracy of predicted probabilities.

Item Response Theory (IRT) was also used as a robustness check of the accuracy-based dataset quartiles.

## Repository Structure

### `python-review/`

Contains foundational Python work, including programming exercises and practice with NumPy and pandas.

### `ml-review/`

Contains implementations and experiments covering fundamental machine learning concepts such as linear regression, logistic regression, random forest, and model evaluation.

### `deep-learning/`

Contains implementations used to develop the deep learning background for the project, including neural networks, optimization, LSTMs, and transformer/self-attention concepts.

### `papers-read/`

Contains notes and summaries of research papers related to knowledge tracing, attention-based models, interpretability, and fairness.

### `knowledge-tracing/`

Contains the implementations, experiments, and dataset exploration used to develop and evaluate the knowledge tracing models in the study.

### `reliability-experiment/`

Contains the experiments used to divide students by ability and evaluate model performance separately across the four quartiles, including the IRT robustness analysis.

### `research-paper/`

Contains the  research paper, including the introduction, related work, methodology, results, discussion, and figures.

## Research Process

The project developed through several stages:

1. Building Python and machine learning foundations
2. Studying deep learning and sequence modeling
3. Reviewing knowledge tracing literature
4. Exploring and preprocessing the ASSISTments 2009 dataset
5. Implementing four knowledge tracing approaches
6. Developing the ability-stratified evaluation
7. Conducting the reliability experiments
8. Analyzing and documenting the results
9. Completing the research paper
