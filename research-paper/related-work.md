# Related Work

## 1. Knowledge Tracing Models Overview

Knowledge Tracing (KT) aims to model a student's evolving mastery of concepts from a sequence of learning interactions in order to predict future performance on educational tasks. An early model used to accomplish this was Bayesian Knowledge Tracing (BKT), which is a probabilistic method that maintains a hidden state representing a student's mastery of a skill and updates this state after each question based on whether the student answered correctly or incorrectly (Corbett & Anderson, 1994). Although BKT is highly interpretable and provides a clear probabilistic representation of student learning, it assumes that skills are independent and cannot model complex relationships among concepts. Despite these limitations, BKT established the foundation for modern knowledge tracing by introducing a framework for estimating student knowledge from sequences of learning interactions.

The introduction of Deep Knowledge Tracing (DKT) marked a major shift toward deep learning and the use of recurrent neural networks (RNNs). DKT employed Long Short-Term Memory (LSTM) networks to learn student knowledge directly from past interaction sequences rather than relying on manually specified probabilistic assumptions. DKT's use of an LSTM allows the model to automatically learn latent representations of student knowledge and complex patterns in learning behavior without requiring predefined skill transition assumptions (Piech et al., 2015). While DKT achieved significantly higher predictive performance than previous probabilistic models, its hidden representations are difficult to interpret.

Subsequent work proposed increasingly sophisticated neural architectures. Dynamic Key-Value Memory Networks (DKVMN) introduced external memory components that allowed concept-specific knowledge representations, addressing the limitation of recurrent models that represent student knowledge through a single latent state (Zhang et al., 2017). This allowed the model to represent individual concepts separately rather than combining all knowledge into a single hidden state. More recently, Transformer-inspired architectures have become increasingly influential in knowledge tracing, replacing recurrent computation with attention mechanisms. Shen et al. (2021) review the development of attention-based knowledge tracing models and discuss how attention mechanisms allow models to capture long-range dependencies in student interaction sequences.

## 2. Attention-Based Knowledge Tracing

Attention-based knowledge tracing models were proposed to overcome limitations of recurrent neural networks, particularly their tendency to compress an entire learning history into a single hidden representation. Self-Attentive Knowledge Tracing (SAKT) introduced multi-head self-attention, allowing the model to assign different importance weights to previous question-response interactions when predicting future responses rather than treating all historical interactions equally (Pandey & Karypis, 2019).

Attentive Knowledge Tracing (AKT) extended SAKT by incorporating educational psychology into the attention mechanism (Ghosh et al., 2020). AKT introduced monotonic attention, which models forgetting by gradually decreasing the influence of older interactions, and Rasch-inspired difficulty embeddings that explicitly represent question difficulty. These embeddings allow the model to distinguish between a student's lack of knowledge and difficulty caused by encountering a more challenging problem. These additions improve prediction accuracy while providing representations that are more aligned with educational concepts such as forgetting and problem difficulty.

The survey by Shen et al. (2021) reviews the development of attention-based architectures in knowledge tracing and discusses their ability to model long-range dependencies within student interaction sequences.

## 3. Interpretability in Knowledge Tracing

As predictive performance has improved, researchers have increasingly focused on making knowledge tracing models interpretable (Shen et al., 2021; Abdelrahman et al., 2022). Rather than producing only predictions of future correctness, interpretable models seek to explain which concepts influence student performance and why predictions are made.

One important direction is Prerequisite-Driven Deep Knowledge Tracing (PDKT), which explicitly incorporates prerequisite relationships among concepts into the knowledge tracing process rather than treating concepts independently. By modeling prerequisite concept relationships as constraints on student knowledge estimation, PDKT aims to improve concept mastery prediction and address the limitations caused by sparse student interaction data (Chen et al., 2018). However, while PDKT evaluates whether prerequisite information improves knowledge estimation, it does not investigate whether prerequisite diagnoses remain reliable across students with different ability levels.

More recent interpretable approaches continue this trend by combining attention mechanisms, concept graphs, probabilistic reasoning, and educational domain knowledge to produce explanations alongside predictions. These models move beyond simple next-question prediction toward educational diagnosis, providing teachers with more informative descriptions of student learning. The recent KT surveys by Shen et al. (2021) and Abdelrahman et al. (2022) identify interpretability and explainability as important research directions for the field, reflecting a shift from maximizing predictive performance toward generating educationally meaningful insights.

## 4. Fairness and Equity in Knowledge Tracing

Another emerging research direction investigates whether knowledge tracing models behave fairly across different groups of learners. Recent work recognizes that high predictive accuracy alone is insufficient if models systematically perform better for some student populations than others.

A recent EDM 2025 study by Stinar et al. investigates whether Bayesian Knowledge Tracing exhibits fairness differences across students with different reading abilities (Stinar et al., 2025). The authors analyzed over 8,500 students using a mathematics adaptive learning system and compared BKT outcomes between emerging and non-emerging readers. While aggregate predictive performance showed limited bias, the authors found that specific skills exhibited disparities related to reading ability, demonstrating that fairness issues may be hidden by overall evaluation metrics (Stinar et al., 2025). Their work demonstrates that fairness across learner populations is becoming an important topic within educational data mining.

Although some knowledge tracing approaches incorporate learner characteristics to improve predictive performance, their primary objective remains improving prediction rather than evaluating whether educational interpretations remain equally trustworthy across different student populations.

## 5. Research Gap: Ability-Stratified Reliability

The existing literature demonstrates substantial progress in four major areas: increasingly accurate knowledge tracing models, attention-based architectures, interpretable prerequisite-aware methods, and fairness across learner populations. However, evaluation practices remain heavily focused on aggregate metrics such as Area Under the ROC Curve (AUC) and overall prediction accuracy.

Existing prerequisite-aware models primarily evaluate whether incorporating prerequisite relationships improves knowledge estimation and prediction performance (Chen et al., 2018). Likewise, current fairness research has begun examining whether knowledge tracing models provide equitable predictions across learner characteristics, such as reading ability (Stinar et al., 2025). However, these studies primarily evaluate fairness in predictive outcomes rather than whether the educational interpretations produced by knowledge tracing models, such as prerequisite-gap identification, remain equally reliable across students with different ability levels.

Attention-based models such as SAKT provide strong predictive baselines for modeling student interaction sequences, but they do not explicitly encode prerequisite relationships between concepts (Pandey & Karypis, 2019). Therefore, combining attention-based knowledge tracing with prerequisite information provides an opportunity to investigate whether improved predictive models can also produce reliable educational diagnoses.

This research investigates whether prerequisite-aware extensions of knowledge tracing models provide equally reliable prerequisite-gap identification across students with different levels of prior mathematical ability. Specifically, students will be stratified according to estimated ability, and prerequisite diagnosis reliability will be evaluated separately within each group. If substantial differences exist between ability groups, aggregate evaluation metrics may obscure important limitations in current knowledge tracing systems. Therefore, this work extends fairness evaluation in knowledge tracing from predictive outcomes to the reliability of educational diagnoses, particularly for the students who would benefit most from personalized educational interventions.

## References

Corbett, A. T., & Anderson, J. R. (1994). Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge. In Proceedings of the 6th International Conference on User Modeling, 121–130.

Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, J. (2015). Deep Knowledge Tracing. Advances in Neural Information Processing Systems.

Zhang, J., Shi, X., King, I., & Yeung, D. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. Proceedings of the 26th International Conference on World Wide Web.

Pandey, S., & Karypis, G. (2019). A Self-Attentive Model for Knowledge Tracing. Proceedings of the 12th International Conference on Educational Data Mining.

Ghosh, A., Heffernan, N., & Lan, A. S. (2020). Context-Aware Attentive Knowledge Tracing. Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.

Shen, S., Liu, Q., Huang, Z., Zheng, Y., Yin, M., Wang, M., & Chen, E. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. arXiv preprint arXiv:2105.15106.

Abdelrahman, G., Wang, Q., & Nunes, B. P. (2022). Knowledge Tracing: A Survey. ACM Computing Surveys.

Chen, P., Lu, Y., Zheng, V. W., & Pian, Y. (2018). Prerequisite-Driven Deep Knowledge Tracing. Proceedings of the 2018 IEEE International Conference on Data Mining (ICDM), 39–48.

Stinar, F., Lee, H., Belitz, C., Nasiar, N., Fancsali, S. E., Ritter, S., Almoubayyed, H., Baker, R. S., Ocumpaugh, J., & Bosch, N. (2025). Fairness of Bayesian Knowledge Tracing for Math Learners of Different Reading Ability. Proceedings of the 18th International Conference on Educational Data Mining, 170–181.