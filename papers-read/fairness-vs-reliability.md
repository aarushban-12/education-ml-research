# Literature Review Note: Fairness vs. Ability-Stratified Reliability

Recent work has begun examining fairness in knowledge tracing models across demographic and student-specific characteristics. For example, an EDM 2025 paper investigates fairness in Bayesian Knowledge Tracing with respect to reading ability, demonstrating that fairness across learner groups is an active area of educational data mining research. This indicates that demographic and learner-characteristic fairness is already being explored within the knowledge tracing literature.

In contrast, I found substantially less work evaluating whether **prerequisite-gap identification** is equally reliable across students with different levels of prior mathematical ability. Existing prerequisite-aware and interpretable knowledge tracing models primarily focus on improving prediction accuracy or generating better explanations, rather than analyzing whether those explanations remain equally trustworthy for struggling and advanced learners. My research therefore focuses on evaluating the reliability of prerequisite-gap identification across ability groups rather than proposing another prerequisite-aware knowledge tracing architecture.

---

# Draft Metric Definition: Ability-Stratified Prerequisite Diagnosis Reliability

For each prediction made by the knowledge tracing model, the attention weights are used to identify the top-*k* prerequisite concepts receiving the highest attention. These concepts are interpreted as the model's predicted prerequisite knowledge relevant to the target concept.

A predicted prerequisite concept is considered **correct** if an independent ground-truth criterion indicates that the student demonstrates insufficient mastery of that concept. Ground truth may be determined using later concept-level assessment performance, repeated failures on concept-tagged exercises, or an expert-defined prerequisite graph, depending on the dataset.

For each student, prerequisite diagnosis accuracy is computed as the proportion of correctly identified prerequisite concepts among the top-*k* attended concepts. Students are then stratified into ability groups using a predefined ability estimation method, such as historical mastery rate or an Item Response Theory (IRT) estimate.

For each ability group, the following metric is computed:

**Prerequisite Diagnosis Reliability = (Number of correct prerequisite diagnoses) ÷ (Total number of prerequisite diagnoses).**

Comparing this metric across low-, medium-, and high-ability groups allows evaluation of whether prerequisite-aware knowledge tracing models provide equally reliable prerequisite-gap identification for students with different levels of prior mathematical ability.
