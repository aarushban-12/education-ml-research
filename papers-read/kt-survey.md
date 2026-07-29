# A Survey of Knowledge Tracing (Liu et al., 2021) – Paper Map

## Citation

Shen, S., Liu, Q., Huang, Z., Zheng, Y., Yin, M., Wang, M., & Chen, E. (2021). *A Survey of Knowledge Tracing: Models, Variants, and Applications*. arXiv:2105.15106.

---

# Overview

This survey reviews the evolution of Knowledge Tracing (KT) methods from traditional probabilistic models to modern deep learning architectures. Rather than proposing a new algorithm, the paper organizes existing research, summarizes benchmark datasets, compares evaluation metrics, and discusses future research opportunities.

---

# Model Evolution

| Model                            | Key Idea                                                                                  | Common Dataset(s)                    |      Typical AUC* |
| -------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------ | ----------------: |
| Bayesian Knowledge Tracing (BKT) | Bayesian Hidden Markov Model with mastery, guessing, slipping, and learning probabilities | ASSISTments 2009, Algebra            |        ~0.65–0.68 |
| Deep Knowledge Tracing (DKT)     | Uses an LSTM to model the sequence of student interactions                                | ASSISTments, Synthetic, Khan Academy |        ~0.81–0.86 |
| DKVMN                            | Memory network with separate key and value memories for concepts                          | ASSISTments, STATICS                 |        ~0.84–0.87 |
| SAKT                             | Multi-head self-attention focuses on the most relevant previous interactions              | ASSISTments, STATICS                 |        ~0.85–0.87 |
| AKT                              | Monotonic attention + Rasch-inspired difficulty embeddings                                | ASSISTments 2009/2015/2017, STATICS  |        ~0.86–0.88 |
| Graph-based KT (GKT, GIKT, etc.) | Uses graph neural networks to model relationships between concepts                        | ASSISTments, EdNet                   | Varies by dataset |

*The survey reports results from many different papers and experimental settings. Exact AUC values are not directly comparable because preprocessing, train/test splits, and dataset versions differ.

---

# Benchmark Datasets

The survey identifies several datasets that appear repeatedly throughout the literature.

**ASSISTments 2009**

* Most widely used benchmark.
* Mathematics tutoring data.
* Student-question interaction sequences.

**ASSISTments 2012 / 2015 / 2017**

* Larger and newer versions of the ASSISTments platform.
* Frequently used for modern deep learning models.

**STATICS2011**

* Engineering mechanics course.
* Often used alongside ASSISTments for benchmarking.

**Junyi Academy**

* Large-scale mathematics learning platform from Taiwan.
* Long student interaction sequences.

**EdNet**

* One of the largest publicly available KT datasets.
* Millions of student interactions.
* Supports large Transformer-based models.

---

# Evaluation Metrics

The primary evaluation metric throughout the literature is:

**AUC (Area Under the ROC Curve)**

Since KT predicts whether the next answer will be correct or incorrect, it is fundamentally a binary classification problem. AUC measures how well a model separates correct from incorrect responses across all classification thresholds.

Other reported metrics include:

* Accuracy
* Precision
* Recall
* RMSE
* Cross-entropy loss

However, AUC remains the standard benchmark for comparing KT models.

---

# Main Research Gaps

The survey identifies several open problems in knowledge tracing.

**1. Better representations**

Most models rely on one-hot encoded questions or learned embeddings while ignoring rich information such as question text, diagrams, and mathematical expressions.

**2. Explainability**

Deep learning models achieve higher predictive performance than traditional approaches, but their predictions are difficult for teachers and students to interpret.

**3. Limited datasets**

Most public datasets come from mathematics tutoring systems. More diverse datasets from different subjects, countries, and educational settings are needed.

**4. Richer student behavior**

Current models mainly use correctness labels while often ignoring other useful signals such as response time, hint usage, confidence, and learning resources accessed.

**5. Better educational applications**

Most research focuses on prediction accuracy rather than using KT models for recommendation, diagnosis, curriculum planning, or identifying prerequisite knowledge gaps.

---

# What I Learned

This survey helped me understand the progression of knowledge tracing research. The field has evolved from probabilistic models (BKT) to recurrent neural networks (DKT), then memory networks (DKVMN), attention-based models (SAKT and AKT), and more recently graph-based approaches. Despite impressive improvements in predictive accuracy, the literature still focuses primarily on predicting whether a student will answer the next question correctly. The survey also highlights that explainability, richer educational data, and practical applications remain open research challenges. These gaps closely align with my research goal of investigating whether attention-based knowledge tracing models can identify prerequisite knowledge gaps rather than only predicting future correctness.
