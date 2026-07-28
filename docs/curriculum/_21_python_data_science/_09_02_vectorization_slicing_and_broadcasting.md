```yaml
schema_version: "2.0"
metadata:
  lesson_id: "DS-MOD01-LES02"
  course_slug: "course-09-python-data-science"
  course_title: "Course 2: Python Data Science Ecosystem (NumPy, Pandas, & Visualization)"
  module_slug: "mod-01-numpy-vectorized-computing"
  module_title: "Module 1 - High-Performance Vectorized Computing with NumPy"
  lesson_slug: "vectorization-slicing-and-broadcasting"
  lesson_title: "Lesson 1.2 Vectorization, Slicing, & Broadcasting Mechanics"
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
    - "NumPy Core Architecture & ndarray Basics"

skills_acquired:
  - "Writing Vectorized Code using Universal Functions (`ufunc`)"
  - "Mastering NumPy Broadcasting Rules & Axis Expansion (`np.newaxis`)"
  - "Performing Boolean Mask Indexing & Fancy Indexing"
  - "Array Reshaping & Memory Copies vs Views (`reshape()`, `ravel()`)"

dependencies:
  software:
    - "VS Code / Jupyter Notebook"
    - "Python 3.12+"
    - "numpy"
  hardware: []

seo_and_social:
  meta_title: "NumPy Vectorization: Broadcasting Rules, ufuncs & Boolean Indexing"
  meta_description: "Master NumPy Vectorized Computing: broadcasting rules, np.newaxis, universal functions (ufunc), boolean masking, and array views vs copies."
  keywords: ["NumPy Broadcasting", "Vectorization", "ufunc", "Boolean Indexing", "np.newaxis", "NumPy Reshape", "Views vs Copies"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 1.2 Vectorization, Slicing, & Broadcasting Mechanics

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 1.1 NumPy Architecture](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_09_python_data_science/_09_01_numpy_core_architecture_and_ndarray.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Replace explicit Python `for` loops with **Universal Functions (`ufunc`)**.
2. Apply **NumPy Broadcasting Rules** to operate on arrays of mismatched shapes.
3. Filter data using **Boolean Mask Indexing** and **Fancy Indexing**.
4. Manipulate array shapes (`reshape()`, `ravel()`, `np.newaxis`) while understanding **Views vs Memory Copies**.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Python REPL or VS Code.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 NumPy Broadcasting Rules
Broadcasting describes how NumPy handles element-wise operations between arrays of different shapes without physically allocating duplicate memory.

Two dimensions are **compatible** for broadcasting if:
1. They are **equal**, OR
2. One of the dimensions is **$1$**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NUMPY BROADCASTING COMPATIBILITY                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ Matrix A Shape : (3, 4) ──►  3 x 4                                          │
│ Vector B Shape :    (4,) ──►  1 x 4 (Leading dimension padded with 1!)      │
│ Result Shape   : (3, 4) ──►  Vector B broadcasted across 3 rows!           │
└─────────────────────────────────────────────────────────────────────────────┘
```

> [!WARNING]
> **Views vs Copies**: Standard array slicing (`arr[0:2, :]`) returns a **View** (shares memory with original array!). Modifying a view mutates the original array. Use `arr.copy()` to force a deep memory copy!

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    ArrA["Array A: Shape (3, 4)"] --> Op[Element-wise Addition +]
    ArrB["Vector B: Shape (1, 4)"] --> Broadcast[Virtual Expansion along Axis 0 to (3, 4)]
    Broadcast --> Op
    Op --> Result["Result Array: Shape (3, 4) Zero Extra Memory Allocated!"]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```python
# NumPy Vectorization, Broadcasting, & Masking (vectorization_demo.py)
import numpy as np

# 1. Broadcasting Matrix Feature Normalization
matrix = np.array([
    [10.0, 200.0, 30.0],
    [20.0, 400.0, 60.0],
    [30.0, 600.0, 90.0]
])

# Compute mean per column (axis=0, keepdims=True maintains 2D shape (1, 3))
col_means = np.mean(matrix, axis=0, keepdims=True)
print(f"Column Means Shape: {col_means.shape}") # (1, 3)

# Broadcast subtraction (3, 3) - (1, 3)
centered_matrix = matrix - col_means
print(f"Centered Matrix (Broadcasting Output):\n{centered_matrix}\n")

# 2. Boolean Mask Indexing (Vectorized Filtering!)
scores = np.array([45, 88, 92, 60, 71, 34, 99])
pass_mask = scores >= 70

print(f"Boolean Mask Array: {pass_mask}")
print(f"Filtered High Scores: {scores[pass_mask]}")

# 3. Vectorized Math with ufuncs (No for loops!)
angles_rad = np.array([0, np.pi/4, np.pi/2])
sin_vals = np.sin(angles_rad)
print(f"Vectorized Sine Output: {sin_vals}")

# 4. View vs Copy Safeguard
original = np.array([1, 2, 3, 4, 5])
view_slice = original[0:3] # Shares memory!
view_slice[0] = 999        # Mutates original array!
print(f"Original Array after View Mutation: {original}")
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Deep Learning Tensor Normalization**: Neural network training frameworks normalize multi-gigabyte mini-batch tensors (`X - mean / std`) across batch dimensions using NumPy broadcasting rules in C-speed.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `vectorization_demo.py`.
2. Run `python vectorization_demo.py`.
3. Observe how `col_means` of shape `(1, 3)` broadcasts across `(3, 3)` matrix rows seamlessly!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ValueError: operands could not be broadcast together`** | Attempting to operate on non-compatible array shapes (e.g. `(3, 4)` and `(3,)`). | Expand dimensions using `vector[:, np.newaxis]` to align axes to `(3, 1)`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `keepdims=True`**: Pass `keepdims=True` in aggregation functions (`mean`, `sum`) to keep dimensions compatible for downstream broadcasting.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What are the two conditions under which two array dimensions are compatible for NumPy broadcasting?
**Answer**: Two dimensions are compatible for broadcasting if they are equal, or if one of the dimensions is equal to $1$. If an array has fewer dimensions than another, $1$s are prepended to its shape until both shapes have equal rank.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 1.2 Broadcasting & Vectorization Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the resulting shape when broadcasting a matrix of shape (5, 4) with a vector of shape (1, 4)?",
      "options": ["(5, 1)", "(5, 4)", "(1, 4)", "ValueError"],
      "correct_answer_index": 1,
      "explanation": "The (1, 4) vector broadcasts across the 5 rows resulting in (5, 4)."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Broadcasting-normalize a 4x3 dataset matrix by subtracting row means using `keepdims=True`.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: How do you add a new 1-length axis to a 1D array to convert shape `(N,)` to `(N, 1)`?
**Back**: `arr[:, np.newaxis]` or `arr.reshape(-1, 1)`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```python
x = np.array([[1], [2], [3]]) # (3, 1)
y = np.array([10, 20, 30])    # (3,) -> (1, 3)
res = x + y                   # (3, 3)
```
