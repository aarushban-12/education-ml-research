# Context-Aware Attentive Knowledge Tracing (AKT) – Paper Summary

## Citation

Ghosh, A., Heffernan, N., & Lan, A. S. (2020). *Context-Aware Attentive Knowledge Tracing*. Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining.

---

## Research Problem

Knowledge tracing aims to predict whether a student will answer the next exercise correctly based on previous learning interactions. Earlier attention-based models such as SAKT improved over recurrent neural networks by focusing on relevant past interactions rather than compressing the entire history into a hidden state. However, SAKT treats all previous interactions equally regardless of how long ago they occurred. In reality, students forget information over time, so older interactions should often have less influence on future predictions.

---

## Main Idea

The authors propose Attentive Knowledge Tracing (AKT), an attention-based knowledge tracing model that incorporates educational theory into the Transformer architecture. The key innovation is a monotonic attention mechanism that combines exercise similarity with a time-decay function. As interactions become more distant in the learning history, their attention weights naturally decrease. AKT also incorporates the Rasch model from psychometrics to learn question difficulty while keeping the model interpretable and parameter-efficient.

---

## Model Architecture

The model consists of several major components.

**Embedding Layer:** Student interactions, exercises, and problem identifiers are converted into dense vector embeddings. The Rasch model regularizes these embeddings so that questions of different difficulty are represented appropriately.

**Monotonic Multi-Head Attention:** Instead of standard self-attention, AKT uses monotonic attention. Attention weights depend on both the similarity between exercises and their relative position in the sequence. Older interactions receive exponentially smaller attention weights, reflecting the idea that knowledge decays over time.

**Feed-Forward Network:** The attended representations pass through a fully connected feed-forward network to combine information and learn higher-level representations.

**Output Layer:** A final linear layer followed by a sigmoid activation predicts the probability that the student will answer the next exercise correctly.

---

## Datasets

The paper evaluates AKT on several benchmark knowledge tracing datasets, including ASSISTments 2009, ASSISTments 2015, ASSISTments 2017, Statics2011, and synthetic datasets. These datasets contain sequences of student responses collected from intelligent tutoring systems and online learning platforms.

---

## Results

AKT consistently outperforms previous knowledge tracing models, including Bayesian Knowledge Tracing (BKT), Deep Knowledge Tracing (DKT), Dynamic Key-Value Memory Networks (DKVMN), and Self-Attentive Knowledge Tracing (SAKT). In some datasets, the model improves AUC by as much as 6% over previous methods while also providing more interpretable attention patterns.

---

## Strengths

AKT combines modern attention mechanisms with ideas from educational psychology. The monotonic attention mechanism models forgetting by reducing the influence of older interactions, while the Rasch-based embeddings account for differences in question difficulty. These additions improve both predictive performance and interpretability.

---

## Limitations

Although AKT models forgetting better than SAKT, it still predicts student performance rather than explicitly discovering prerequisite concept relationships. The monotonic decay assumption may also underestimate the importance of some older interactions that remain highly relevant to a student's future performance.

---

## What I Learned

AKT extends SAKT rather than replacing it. Both models use attention instead of recurrent neural networks, but AKT modifies the attention mechanism to better reflect how students learn. The most important innovation is monotonic attention, which assumes that more recent learning experiences are generally more useful than older ones. This makes the model more consistent with human learning and forgetting while maintaining the computational advantages of Transformer-based attention. I also learned that combining machine learning architectures with educational theories, such as the Rasch model, can improve both accuracy and interpretability.
