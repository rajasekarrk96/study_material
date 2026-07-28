```yaml
schema_version: "2.0"
metadata:
  lesson_id: "DS-MOD01-LES02"
  course_slug: "course-01-ds-math"
  course_title: "Course 1: Mathematics & Statistics for Data Science"
  module_slug: "mod-01-linear-algebra-calculus"
  module_title: "Module 1.1 - Linear Algebra & Matrix Calculus"
  lesson_slug: "matrix-inversion-determinants-and-systems"
  lesson_title: "Lesson 1.1.2 Matrix Inversion, Determinants, & Systems of Equations"
  sort_order: 102

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 60

prerequisites:
  required_lesson_ids:
    - "DS-MOD01-LES01"
  required_skills:
    - "Vector Operations & Matrix Multiplication"

skills_acquired:
  - 'Determinant Computation ($\det(A)$)'
  - "Matrix Inversion ($A^{-1}$) & Singular Matrix Detection"
  - "Matrix Rank Calculation ($\text{rank}(A)$)"
  - "Solving Linear Systems $Ax = b$ using OLS & LU Decomposition"
  - "Evaluating Ill-Conditioned Matrices via Condition Numbers"

dependencies:
  software:
    - "VS Code"
    - "Python 3.11+ with NumPy & SciPy"
  hardware: []

seo_and_social:
  meta_title: "Matrix Inversion, Determinants & Solving Ax = b Systems in Python"
  meta_description: "Master matrix inversion, determinants, matrix rank, Gaussian elimination, solving systems of linear equations Ax = b, and condition numbers."
  keywords: ["Matrix Inversion", "Determinant", "Ax = b", "Gaussian Elimination", "Matrix Rank", "Condition Number", "NumPy linalg"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 1.1.2 Matrix Inversion, Determinants, & Systems of Equations

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 1.1.1 Vectors & Matrices](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_08_ds_math/_01_01_vectors_matrices_and_vector_spaces.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Calculate the Determinant $\det(A)$ to evaluate volume scaling and matrix invertibility.
2. Compute the Matrix Inverse $A^{-1}$ ($A A^{-1} = I$).
3. Determine Matrix Rank ($\text{rank}(A)$) to identify full-rank vs degenerate feature sets.
4. Solve linear systems of equations $A\mathbf{x} = \mathbf{b}$ using `np.linalg.solve()` and LU Decomposition.
5. Diagnose ill-conditioned numerical instability using Condition Numbers ($\kappa(A)$).

---

## 2. Environment & Prerequisites [id: prerequisites]

Install SciPy alongside NumPy:
- Run `pip install scipy`.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Determinants & Singular Matrices
The **Determinant** $\det(A)$ measures the scaling factor of the transformation volume defined by matrix $A$:
- If $\det(A) = 0$, the matrix compresses space into a lower dimension, making it **Singular (Non-Invertible)**.
- If $\det(A) \neq 0$, the matrix is **Non-Singular (Invertible)**.

### 3.2 Solving $A\mathbf{x} = \mathbf{b}$
In linear models (e.g. Ordinary Least Squares Regression):

$$A\mathbf{x} = \mathbf{b} \implies \mathbf{x} = A^{-1}\mathbf{b}$$

> [!CAUTION]
> **Performance Rule**: NEVER compute $A^{-1}$ explicitly in production! Inverting a matrix is $O(n^3)$ and numerically unstable. Always use LU Decomposition or `np.linalg.solve(A, b)`!

### 3.3 Condition Number ($\kappa$)
The Condition Number $\kappa(A) = \|A\| \|A^{-1}\|$ measures sensitivity to input noise:
- $\kappa(A) \approx 1$: Well-conditioned matrix.
- $\kappa(A) \gg 1000$: **Ill-conditioned matrix** (multicollinearity in regression data!).

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    CheckDet{det(A) == 0?} -->|Yes| Singular[Singular Matrix: Inverse Does NOT Exist!]
    CheckDet -->|No| Invertible[Non-Singular: Solve Ax = b via LU Decomposition]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```python
import numpy as np
from scipy import linalg

# System of Equations: 2x + 3y = 8, 4x + 9y = 20
A = np.array([[2, 3], [4, 9]], dtype=float)
b = np.array([8, 20], dtype=float)

# 1. Determinant & Rank
det_A = np.linalg.det(A)
rank_A = np.linalg.matrix_rank(A)
cond_A = np.linalg.cond(A)

print(f"Determinant: {det_A:.2f}")
print(f"Matrix Rank: {rank_A}")
print(f"Condition Number: {cond_A:.2f}")

# 2. Optimal Numerical Solver (LU Decomposition)
x = np.linalg.solve(A, b)
print(f"Solution x: {x}") # x = [2., 4.]
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Multicollinearity in Linear Models**: High condition numbers $\kappa(X^T X) > 30$ signal severe multicollinearity in regression feature matrices, necessitating Ridge/Lasso regularization.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `solve_system.py`.
2. Run `python solve_system.py` $\to$ Verify $x = 2$ and $y = 4$.

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`LinAlgError: Singular matrix`** | Attempting to invert a matrix with $\det(A) = 0$ (linearly dependent features). | Remove collinear features or use Pseudo-Inverse `np.linalg.pinv()`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `np.linalg.solve(A, b)`**: Faster and more stable than `np.linalg.inv(A) @ b`.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why should you avoid explicitly computing $A^{-1}$ to solve $A\mathbf{x} = \mathbf{b}$?
**Answer**: Explicit matrix inversion is computationally expensive ($O(n^3)$) and amplifies floating-point rounding errors. Direct solver algorithms (like LU or QR decomposition via `np.linalg.solve`) are faster and numerically stable.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 1.1.2 Systems Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What does a matrix determinant det(A) = 0 signify?",
      "options": ["Matrix is Identity", "Matrix is Singular (Non-Invertible)", "Matrix has full rank", "Matrix is Orthogonal"],
      "correct_answer_index": 1,
      "explanation": "A determinant of 0 indicates a singular non-invertible matrix."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an Ordinary Least Squares (OLS) regression solver using `np.linalg.solve(X.T @ X, X.T @ y)`.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What function solves $A\mathbf{x} = \mathbf{b}$ without explicit matrix inversion in NumPy?
**Back**: `np.linalg.solve(A, b)`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```python
import numpy as np
x = np.linalg.solve(A, b) # Numerical Ax=b solver
```
