# Data Science & Analytics Learning Path
# Referenced Courses

> These courses are **shared/reusable** across multiple Learning OS paths.  
> They are **NOT included** in this export package.  
> Contributors working on this path must complete these prerequisites independently.  
> When the returned package is merged into the Learning OS, these references resolve automatically.

---

## Reusable Courses — Do Not Duplicate

| # | Course | Source Folder | Syllabus | Status | Reason |
|---|---|---|---|---|---|
| 1 | Computer Fundamentals | — | `docs/syllabus/_01_computer_fundamentals.md` | Shared Course — Not Included | Foundational prerequisite for all paths |
| 2 | Engineering Mathematics | — | `docs/syllabus/_02_engineering_mathematics.md` | Shared Course — Not Included | Linear algebra, calculus, probability — shared |
| 3 | Core Python | `docs/curriculum/09-python-core/` | `docs/syllabus/_06_python_full_stack.md` | Shared Course — Not Included | Reused by Web, Backend, and DS paths |
| 4 | Git Version Control | `docs/curriculum/03-git-version-control/` | `docs/syllabus/_03_git_version_control.md` | Shared Course — Not Included | Shared across all engineering paths |
| 5 | Database Technologies (MySQL) | `docs/curriculum/13-mysql-database/` | `docs/syllabus/_15_database_technologies.md` | Shared Course — Not Included | Reused by Backend and Data paths |
| 6 | Statistics & DS Mathematics | `docs/curriculum/38-ds-math-statistics/` | None (part of _27_data_analytics.md) | Shared Course — Not Included | 24 complete lessons — reusable |
| 7 | MongoDB for Data Science | `docs/curriculum/15-mongodb-nosql/` | None | Shared Course — Not Included | Optional NoSQL course — reusable |

---

## Learning Path Prerequisite Chain

```
Computer Fundamentals
        ↓
Engineering Mathematics
        ↓
Core Python  ←──────────────────┐
        ↓                       │
Git Version Control             │  (reusable shared courses)
        ↓                       │
Statistics & DS Mathematics     │
        ↓                       │
Database Technologies ──────────┘
        ↓
    [DATA SCIENCE PATH BEGINS]
        ↓
Data Analytics → Data Science → Machine Learning
        ↓
Deep Learning → Computer Vision → NLP & Generative AI
        ↓
MLOps Engineering
```

---

## How References Are Resolved at Merge Time

When a contributor returns the completed package:

1. The Learning OS audit team verifies all stubs are complete
2. `CURRICULUM/` content is merged into the corresponding `docs/curriculum/` folder
3. Referenced courses remain in their original locations — untouched
4. The DS learning path config points to these shared courses by reference, not by copy

This prevents content duplication and ensures that improvements to Core Python (for example) automatically benefit all paths that reference it.

---

## Contributor Guidance

You do NOT need to:
- Write notes for any course listed above
- Reference the content of those courses
- Copy or import those files

You SHOULD:
- Assume the student has completed all prerequisites listed above
- Write notes at the appropriate difficulty level assuming that background
- Cross-reference shared concepts using `> **Prerequisite:** See Core Python — Module X`


---

## Canonical Data-Science Courses (promoted to `technologies/` on 2026-08-08)

> These courses previously lived inside this learning path. Per the canonical rule (one course = one location) they now live in `exports/technologies/` and are **referenced** here, not duplicated.

| # | Course | Canonical Location | Syllabus |
|---|---|---|---|
| 1 | Data Analytics & Business Intelligence | `exports/technologies/data-analytics` | `exports/technologies/data-analytics/SYLLABUS/data-analytics.md` |
| 2 | Data Science & Predictive Analytics | `exports/technologies/data-science` | `exports/technologies/data-science/SYLLABUS/data-science.md` |
| 3 | Tableau | `exports/technologies/tableau` | `exports/technologies/tableau/SYLLABUS/tableau.md` |
| 4 | Excel for Data Analysis | `exports/technologies/excel-data-analysis` | `exports/technologies/excel-data-analysis/SYLLABUS/excel-data-analysis.md` |
| 5 | Cloud AI Services | `exports/technologies/cloud-ai-services` | `exports/technologies/cloud-ai-services/SYLLABUS/cloud-ai-services.md` |
| 6 | Big Data Fundamentals | `exports/technologies/big-data-fundamentals` | `exports/technologies/big-data-fundamentals/SYLLABUS/big-data-fundamentals.md` |
| 7 | Apache Spark | `exports/technologies/apache-spark` | `exports/technologies/apache-spark/SYLLABUS/apache-spark.md` |
| 8 | Apache Airflow | `exports/technologies/apache-airflow` | `exports/technologies/apache-airflow/SYLLABUS/apache-airflow.md` |
| 9 | MLflow | `exports/technologies/mlflow` | `exports/technologies/mlflow/SYLLABUS/mlflow.md` |
| 10 | Kubeflow | `exports/technologies/kubeflow` | `exports/technologies/kubeflow/SYLLABUS/kubeflow.md` |
| 11 | Data Warehousing | `exports/technologies/data-warehousing` | `exports/technologies/data-warehousing/SYLLABUS/data-warehousing.md` |
| 12 | Snowflake | `exports/technologies/snowflake` | `exports/technologies/snowflake/SYLLABUS/snowflake.md` |
| 13 | Feature Engineering | `exports/technologies/feature-engineering` | `exports/technologies/feature-engineering/SYLLABUS/feature-engineering.md` |
| 14 | Data Visualization | `exports/technologies/data-visualization` | `exports/technologies/data-visualization/SYLLABUS/data-visualization.md` |

### Overlap courses — RESOLVED (2026-08-08)

| Course | Canonical Location | Disposition |
|---|---|---|
| computer-vision | specializations/computer-vision | path copy removed (strict subset) — reference canonical |
| deep-learning | specializations/deep-learning | path copy removed (strict subset) — reference canonical |
| machine-learning | specializations/machine-learning | path copy removed (strict subset) — reference canonical |
| power-bi | specializations/power-bi | path copy removed (subset) — reference canonical |
| mlops-engineering | specializations/mlops-ai-deployment | path copy removed (strict subset) — reference canonical |
| nlp-generative-ai | technologies/nlp-generative-ai | promoted (richer/unique) — reference canonical |
