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
