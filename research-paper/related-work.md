# Related Work

## 1. Knowledge Tracing Models Overview

Knowledge Tracing (KT) aims to model a student's evolving mastery of concepts from a sequence of learning interactions in order to predict future performance on educational tasks. An early model used to accomplish this was Bayesian Knowledge Tracing (BKT), which is a probabilistic method that maintains a hidden state representing a student's mastery of a skill and updates this state after each question based on whether the student answered correctly or incorrectly (Corbett & Anderson, 1994). Although BKT is highly interpretable and provides a clear probabilistic representation of student learning, it assumes that skills are independent and cannot model complex relationships among concepts. Despite these limitations, BKT established the foundation for modern knowledge tracing by introducing a framework for estimating student knowledge from sequences of learning interactions.

The introduction of Deep Knowledge Tracing (DKT) marked a major shift toward deep learning and the use of recurrent neural networks (RNNs). DKT employed Long Short-Term Memory (LSTM) networks to learn student knowledge directly from past interaction sequences rather than relying on manually specified probabilistic assumptions. DKT's use of an LSTM allows the model to automatically learn latent representations of student knowledge and complex patterns in learning behavior without requiring predefined skill transition assumptions (Piech et al., 2015). While DKT achieved significantly higher predictive performance than previous probabilistic models, its hidden representations are difficult to interpret.

Subsequent work introduced external memory components and increasingly sophisticated architectures to address the limitations of recurrent models (Zhang et al., 2017). More recently, Transformer-inspired architectures have become increasingly influential in knowledge tracing, replacing recurrent computation with attention mechanisms. Shen et al. (2021) review the development of attention-based knowledge tracing models and discuss how attention mechanisms allow models to capture long-range dependencies in student interaction sequences.

## 2. Attention-Based Knowledge Tracing

Attention-based knowledge tracing models were proposed to overcome limitations of recurrent neural networks, particularly their tendency to compress an entire learning history into a single hidden representation. Self-Attentive Knowledge Tracing (SAKT) introduced multi-head self-attention, allowing the model to assign different importance weights to previous question-response interactions when predicting future responses rather than treating all historical interactions equally (Pandey & Karypis, 2019).

Attentive Knowledge Tracing (AKT) extended SAKT by incorporating educational psychology into the attention mechanism (Ghosh et al., 2020). AKT introduced monotonic attention, which models forgetting by gradually decreasing the influence of older interactions, and Rasch-inspired difficulty embeddings that explicitly represent question difficulty. These embeddings allow the model to distinguish between a student's lack of knowledge and difficulty caused by encountering a more challenging problem. These additions improve prediction accuracy while providing representations that are more aligned with educational concepts such as forgetting and problem difficulty.

The survey by Shen et al. (2021) reviews the development of attention-based architectures in knowledge tracing and discusses their ability to model long-range dependencies within student interaction sequences.

## 3. Interpretability in Knowledge Tracing

As predictive performance has improved, researchers have increasingly focused on making knowledge tracing models interpretable (Shen et al., 2021; Abdelrahman et al., 2022). Rather than producing only predictions of future correctness, interpretable models seek to explain which concepts influence student performance and why predictions are made.

One important direction is Prerequisite-Driven Deep Knowledge Tracing (PDKT), which explicitly incorporates prerequisite relationships among concepts into the knowledge tracing process rather than treating concepts independently. By modeling prerequisite concept relationships as constraints on student knowledge estimation, PDKT aims to improve concept mastery prediction and address the limitations caused by sparse student interaction data (Chen et al., 2018). This work demonstrates how knowledge tracing models can incorporate relationships among mathematical concepts to produce more educationally meaningful representations of student knowledge.

However, interpretability alone does not establish whether educational interpretations are reliable for different types of learners. A model may identify the same prerequisite gap for two students while the reliability of that diagnosis differs depending on their underlying level of mathematical ability. Thus, evaluating the reliability of model-generated educational diagnoses across learner groups represents an important extension of existing work on interpretability in knowledge tracing.

## 4. Fairness and Equity in Knowledge Tracing

Another emerging research direction investigates whether knowledge tracing models behave fairly across different groups of learners. Recent work recognizes that high predictive accuracy alone is insufficient if models systematically perform better for some student populations than others.

A recent EDM 2025 study by Stinar et al. investigates whether Bayesian Knowledge Tracing exhibits fairness differences across students with different reading abilities (Stinar et al., 2025). The authors analyzed over 8,500 students using a mathematics adaptive learning system and compared BKT outcomes between emerging and non-emerging readers. While aggregate predictive performance showed limited bias, the authors found that specific skills exhibited disparities related to reading ability, demonstrating that fairness issues may be hidden by overall evaluation metrics (Stinar et al., 2025). Their work demonstrates that fairness across learner populations is becoming an important topic within educational data mining.

Although this work demonstrates the importance of evaluating knowledge tracing across learner groups, relatively little attention has been given to whether knowledge tracing predictions are equally reliable for students with different levels of prior academic ability. In particular, aggregate metrics may conceal differences in predictive reliability between higher- and lower-ability students. Examining model performance separately across ability groups can therefore provide a more detailed understanding of how reliably knowledge tracing models represent student knowledge.

## 5. Research Gap: Ability-Stratified Reliability

The existing literature demonstrates substantial progress in knowledge tracing, including increasingly sophisticated predictive models, attention-based architectures, interpretable approaches, and emerging research on fairness across learner populations. However, most knowledge tracing evaluations continue to emphasize aggregate predictive metrics such as Area Under the ROC Curve (AUC) and overall prediction accuracy. These metrics provide an overall assessment of model performance but may obscure differences in reliability across individual groups of learners.

Fairness research has begun to address this limitation by examining whether knowledge tracing models perform differently across learner populations. For example, Stinar et al. (2025) found that Bayesian Knowledge Tracing exhibited skill-specific differences associated with students' reading ability, demonstrating that aggregate performance can mask disparities between groups. However, reading ability represents only one learner characteristic, and the reliability of knowledge tracing predictions across students with different levels of prior academic ability remains insufficiently studied.

This distinction is important because students enter a learning environment with different levels of prior knowledge. A model that performs well on average may nevertheless produce more reliable predictions for some students than for others. If prediction reliability varies systematically with student ability, aggregate evaluation metrics may give an incomplete picture of model performance and could obscure weaknesses that are particularly relevant when knowledge tracing is used for personalized educational interventions.

Prerequisite-aware approaches provide an additional motivation for examining this issue. PDKT demonstrates that incorporating relationships among concepts can improve knowledge estimation by accounting for prerequisite dependencies (Chen et al., 2018). However, whether knowledge tracing predictions remain equally reliable across students with different ability levels has not been established. Similarly, attention-based models such as SAKT provide strong predictive baselines for modeling student interaction sequences, but they do not explicitly evaluate whether their predictions are equally reliable across ability groups (Pandey & Karypis, 2019).

Therefore, this research investigates whether knowledge tracing models produce equally reliable predictions for students with different levels of prior mathematical ability. Students will be stratified into ability groups, and model prediction performance will be evaluated separately within each group rather than relying solely on aggregate metrics. The study will examine whether measures of predictive performance and reliability differ systematically across ability levels. If substantial differences are observed, the findings would suggest that aggregate evaluation metrics can conceal important limitations in knowledge tracing models and that ability-stratified evaluation should be considered when assessing their suitability for personalized learning.

More broadly, this work extends emerging fairness research in knowledge tracing by examining reliability across learner ability levels. Rather than asking only whether a model is accurate on average, the study asks whether students with different levels of prior mathematical ability can rely on the model's predictions to a similar degree. This provides a more learner-centered perspective on knowledge tracing evaluation and may help identify whether current KT models perform consistently across the range of students they are intended to support.

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