# 5. Discussion

The results make one thing clear: prediction reliability in knowledge tracing is not uniform across student-ability levels. However, the relationship is more nuanced than a simple pattern of better or worse performance with increasing ability. Model rankings shifted across quartiles, and the effect of student knowledge levels played out differently depending on whether discrimination or probabilistic calibration was being measured. Taken together, these findings suggest that aggregate evaluation metrics can hide meaningful differences in prediction reliability across different groups of students.

## 5.1 Trends in Reliability Metrics

Throughout the experiment, the AUC and Brier Score of the models showed substantially different trends. AUC did not show a consistent relationship with student ability across all models. When each model is taken into account separately, AUC is often high for one quartile and then lower for the others. Brier Score, however, improved more steadily as ability increased.

DKT and SAKT had a spike in AUC around Q1, but it decreased and remained relatively level across the remaining ability groups. Logistic Regression's AUC followed a U-shaped curve, with the highest AUCs being at Q1 and Q4, while Q2 and Q3 had much lower scores. Brier Scores trended downward with increasing quartile number for all three of these models, with a small peak during Q2.

BKT's performance, however, goes against these patterns. Across Q1 through Q3, BKT showed weaker discrimination than DKT and SAKT. Then, in Q4, it outperformed every other model on both metrics. Also, BKT did not exhibit the peak in Brier Score at Q2 while all the other models did. The reasons for this reversal are not immediately clear from the data. Future work could investigate what drives this difference. For example, the reason for this variation could be discovered by examining whether BKT's mastery parameters behave differently for high-ability students, or by analyzing response consistency across ability groups to determine whether simpler models are better suited to more predictable learners.

## 5.2 Implications

The baseline results ranked the models as DKT, SAKT, BKT, and Logistic Regression in descending order of AUC. That ranking did not hold once students were separated by ability. BKT outperformed both neural models in Q4 despite sitting below them in the baseline. A single aggregate score, it turns out, can be misleading about how a model actually performs across the range of students it is meant to serve.

Logistic Regression makes the same point but from the other direction. Its performance collapsed in Q2 and Q3, with AUC values well below the other models. Simple accuracy-based features appear to be insufficient for students in the middle of the ability distribution. It recovered somewhat in Q4, which suggests its features become more informative—but by that point, BKT and the neural models had already demonstrated that more principled approaches to sequential modeling offer real advantages.

The practical implication is straightforward. If a knowledge tracing model is going to be used to support individualized learning decisions, its overall AUC is not enough. Knowing that a model performs reliably for one group of students but not another is essential for informing deployment decisions, and aggregate metrics such as a single AUC do not convey this.

## 5.3 Limitations and Future Directions

This study has a few limitations worth noting. Student ability was measured using overall accuracy, which is a rough proxy for a characteristic that is really continuous and complex. The IRT robustness check showed strong agreement, which is encouraging, but both measures are still approximations. The analysis also used a single dataset, so it is unclear how well the findings would hold across other subjects or platforms.

The unequal number of interactions across quartiles is another concern, since higher-ability students had more recorded interactions on average. Future work could control for this by matching students on sequence length. Adding bootstrapped confidence intervals and additional calibration metrics would also strengthen the analysis.

Despite these limitations, the core finding stands. Knowledge tracing reliability is not uniform across all ability levels, and the models that perform best overall are not always the models that perform best for every student. These findings suggest that subgroup evaluation should be an important part of assessing whether a knowledge tracing system can be trusted across the students it is intended to serve.