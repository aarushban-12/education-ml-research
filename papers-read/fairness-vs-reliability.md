# Literature Review Note: Fairness vs. Ability-Stratified Reliability

Recent work has begun examining fairness in knowledge tracing models across demographic and student-specific characteristics. For example, an EDM 2025 paper investigates fairness in Bayesian Knowledge Tracing with respect to reading ability, demonstrating that fairness across learner groups is an active area of educational data mining research. This indicates that demographic and learner-characteristic fairness is already being explored within the knowledge tracing literature.

In contrast, I found substantially less work evaluating whether **next-question performance predictions** are equally reliable across students with different levels of prior ability. Existing knowledge tracing research primarily focuses on overall predictive performance, commonly using metrics such as AUC, rather than analyzing whether predicted probabilities are equally trustworthy for students at different ability levels. A model may achieve strong overall predictive performance while systematically overestimating or underestimating performance for a particular ability group. My research therefore focuses on evaluating the reliability of next-question predictions across ability groups using established knowledge tracing approaches rather than proposing another knowledge tracing architecture.

---

# Draft Metric Definition: Ability-Stratified Prediction Reliability

For each student interaction, the knowledge tracing model uses the student's previous interaction history to predict the probability that the student will answer the next question correctly. The model produces a probability between 0 and 1, while the student's actual response provides the observed outcome of either correct or incorrect.

A prediction is considered **reliable** when predicted probabilities correspond closely to observed outcomes across groups of predictions. For example, if a model assigns a probability of approximately 0.80 to a group of predictions, approximately 80% of those predictions should result in correct responses if the model is well calibrated. Reliability can therefore be evaluated using measures such as the Brier score, Expected Calibration Error (ECE), and reliability diagrams.

Students are then stratified into ability groups using a predefined ability estimation method based only on information available before the evaluation predictions, such as historical accuracy or an Item Response Theory (IRT) estimate. Students can be divided into ability quartiles, ranging from the lowest-ability quartile to the highest-ability quartile.

For each ability group, the same reliability metrics are calculated separately for Logistic Regression, Bayesian Knowledge Tracing (BKT), and Self-Attentive Knowledge Tracing (SAKT). Comparing these metrics across ability groups allows evaluation of whether different knowledge tracing models provide equally reliable predictions for students with different levels of prior ability.

**Ability-Stratified Prediction Reliability** therefore measures whether a model's predicted probabilities correspond equally well to actual future performance across student ability groups. Differences in calibration or prediction error between ability quartiles would indicate that a model's predictions are less reliable for some students, even if its overall predictive performance is strong.
