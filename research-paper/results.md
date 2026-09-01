# Results

The performance of each knowledge tracing model was evaluated across four student-ability quartiles (Q1–Q4) using Area Under the Receiver Operating Characteristic Curve (AUC) and Brier Score. AUC measures a model’s ability to discriminate between correct and incorrect responses, with higher values indicating better discrimination. Brier Score measures the accuracy of probabilistic predictions, with lower values indicating better performance. The results for Logistic Regression, Bayesian Knowledge Tracing (BKT), Deep Knowledge Tracing (DKT), and Self-Attentive Knowledge Tracing (SAKT) are presented below.

## AUC Across Student-Ability Quartiles

Model performance varied substantially across ability groups. DKT achieved the highest AUC for Q1, Q2, and Q3, while BKT achieved the highest AUC for Q4.

For the lowest-ability group (Q1), DKT achieved the highest AUC at 0.818, followed closely by SAKT at 0.812. BKT achieved an AUC of 0.730, while Logistic Regression performed lowest at 0.684. This indicates that the two neural knowledge tracing models were substantially better at discriminating between correct and incorrect responses for students in the lowest ability quartile.

For Q2, DKT again achieved the highest AUC (0.758), followed by SAKT (0.746) and BKT (0.736). Logistic Regression performed considerably worse, with an AUC of 0.583. A similar pattern was observed for Q3, where DKT achieved an AUC of 0.761 and SAKT achieved 0.751, compared with 0.714 for BKT and 0.574 for Logistic Regression.

The pattern changed for the highest-ability group (Q4). BKT achieved the highest AUC of all models at 0.813, exceeding DKT (0.765), SAKT (0.760), and Logistic Regression (0.692). Thus, although DKT and SAKT performed best for the lower three ability groups, BKT produced the strongest discrimination for the highest-ability students.

Overall, the AUC results do not show a uniform relationship between student ability and model discrimination. Instead, model rankings changed across ability groups, with DKT and SAKT generally performing better for lower- and middle-ability students and BKT showing a substantial improvement for the highest-ability group.

## Brier Score Across Student-Ability Quartiles

The Brier Score results showed a clearer relationship between student ability and probabilistic prediction accuracy. Across the models, Brier Scores generally decreased for higher-ability students, particularly for BKT and the neural knowledge tracing models.

For Q1, SAKT produced the lowest Brier Score at 0.166, followed by DKT at 0.175, Logistic Regression at 0.207, and BKT at 0.218. For Q2, BKT achieved the lowest Brier Score (0.204), closely followed by SAKT (0.199) and DKT (0.195), while Logistic Regression had the highest Brier Score at 0.242.

For Q3, SAKT achieved the lowest Brier Score at 0.156, followed closely by DKT at 0.163 and BKT at 0.168. Logistic Regression again performed worse, with a Brier Score of 0.192.

The largest differences occurred for Q4. BKT achieved a Brier Score of 0.089, the lowest value observed across all models and ability groups. SAKT followed with 0.103, while Logistic Regression and DKT achieved 0.111 and 0.126, respectively. Therefore, BKT demonstrated particularly strong probabilistic accuracy for the highest-ability students.

## Comparison Across Models

Taken together, the AUC and Brier Score results indicate that model performance depends on student ability and that the effect differs depending on the evaluation metric. DKT and SAKT generally provided the strongest discrimination for Q1–Q3, whereas BKT performed best for Q4. In terms of probabilistic accuracy, SAKT performed best for Q1 and Q3, while BKT performed best for Q2 and Q4.

The most notable result was the performance of BKT on Q4. Its AUC increased from 0.730 in Q1 to 0.813 in Q4, while its Brier Score decreased from 0.218 to 0.089. This represents both improved discrimination and substantially more accurate probability estimates for the highest-ability students.

In contrast, Logistic Regression showed relatively weak discrimination across the middle ability groups, with AUC values of 0.583 and 0.574 for Q2 and Q3, respectively, although its probabilistic accuracy improved considerably for Q4. DKT and SAKT showed more consistent AUC performance across the four groups, but neither demonstrated the same improvement in Q4 that was observed for BKT.

Overall, these findings demonstrate that the reliability and predictive performance of knowledge tracing models are not uniform across student-ability groups. The differences between ability groups, particularly the strong improvement of BKT for Q4, suggest that student ability is an important factor to consider when evaluating knowledge tracing models.
