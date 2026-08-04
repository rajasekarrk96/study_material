# Lesson 1.3.4 Non-Parametric Statistical Methods

> **Course**: Ds Math | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 1.3.3 ANOVA & Chi-Square Tests](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_08_ds_math/_01_10_anova_and_chi_square_tests.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Identify when parametric assumptions (normality, equal variance) are violated.
2. Execute the **Mann-Whitney U Test** for non-normal independent samples.
3. Conduct the **Wilcoxon Signed-Rank Test** for paired non-normal data.
4. Execute the **Kruskal-Wallis Test** as a non-parametric alternative to One-Way ANOVA.
5. Apply **Bootstrapping** resampling to estimate empirical confidence intervals.

---

---

Open VS Code and install SciPy.

---

---

### 3.1 Parametric vs Non-Parametric Decision Matrix

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARAMETRIC VS NON-PARAMETRIC MATRIX                      │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Test Purpose    │ Parametric Test (Normal Data)    │ Non-Parametric Test    │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ 2 Indep Groups  │ Two-Sample $t$-test              │ Mann-Whitney U Test    │
│ 2 Paired Groups │ Paired $t$-test                  │ Wilcoxon Signed-Rank   │
│ 3+ Groups       │ One-Way ANOVA                    │ Kruskal-Wallis Test    │
│ Correlation     │ Pearson Correlation ($\rho$)     │ Spearman Rank ($\rho_s$)│
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

### 3.2 Bootstrapping Resampling
Bootstrapping estimates sampling distributions by repeatedly sampling **with replacement** from the original dataset $B$ times (e.g. $B = 10,000$).

---

---

```mermaid
flowchart TD
    OrigData[Original Dataset N=100] --> Resample["Draw 10,000 Bootstrap Samples WITH Replacement"]
    Resample --> Compute["Compute Metric for Each Sample"]
    Compute --> EmpiricalCI["Extract 2.5th and 97.5th Percentiles -> 95% Empirical CI!"]
```

---

---

```python
import numpy as np
from scipy import stats

# Skewed Non-Normal Data (e.g., User Income Distribution)
grp_a = np.array([22, 25, 29, 31, 35, 120, 450]) # Heavily skewed outlier
grp_b = np.array([18, 20, 22, 24, 25, 28, 30])

# 1. Mann-Whitney U Test (Non-parametric alternative to 2-sample t-test)
u_stat, p_val = stats.mannwhitneyu(grp_a, grp_b)
print(f"Mann-Whitney U stat: {u_stat:.2f}, p-value: {p_val:.4f}")

# 2. Bootstrapped 95% Confidence Interval for Median
boot_medians = [np.median(np.random.choice(grp_a, size=len(grp_a), replace=True)) for _ in range(10000)]
ci_lower = np.percentile(boot_medians, 2.5)
ci_upper = np.percentile(boot_medians, 97.5)

print(f"Bootstrapped 95% CI for Median: [{ci_lower:.2f}, {ci_upper:.2f}]")
```

---

---

- **Web Latency & Financial Transaction Analytics**: Server latency logs and user income data contain heavy right-skewed outliers where $t$-tests fail; engineers use Mann-Whitney U tests and Bootstrapping instead.

---

---

1. Save code as `nonparametric_demo.py`.
2. Run `python nonparametric_demo.py` $\to$ Inspect robust bootstrapped median confidence interval!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Using $t$-test on Highly Skewed Data** | Severe outliers violate the normality assumption, distorting sample means. | Switch to Mann-Whitney U test or evaluate medians via Bootstrapping. |

---

---

- **Use Bootstrapping for Complex Metrics**: Ideal for medians, ratios, or custom ML evaluation metrics.

---

---

### Q1: What is Bootstrapping and why is it useful in Data Science?
**Answer**: Bootstrapping is a non-parametric resampling technique that draws repeated samples *with replacement* from observed data to build an empirical sampling distribution. It calculates confidence intervals for complex metrics (like medians or Gini coefficients) without making parametric distribution assumptions.

---

---

```json
{
  "quiz_title": "Lesson 1.3.4 Non-Parametric Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which non-parametric test serves as an alternative to One-Way ANOVA for non-normal data?",
      "options": ["Mann-Whitney U Test", "Wilcoxon Signed-Rank Test", "Kruskal-Wallis Test", "Spearman Correlation"],
      "correct_answer_index": 2,
      "explanation": "Kruskal-Wallis is the non-parametric equivalent of One-Way ANOVA."
    }
  ]
}
```

---

---

Build a custom Bootstrapping engine that calculates 95% CIs for non-normal server latency logs.

---

---

**Front**: What is the non-parametric equivalent of Pearson correlation?
**Back**: Spearman Rank Correlation ($\rho_s$).
<!-- flashcard:end -->

---

---

```python
u_stat, p_val = stats.mannwhitneyu(sample1, sample2)
boot_ci = np.percentile(boot_estimates, [2.5, 97.5])
```

---
