```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD02-LES03"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-02-variables-types-operators"
  module_title: "Module 2 - Variables, Data Types, & Operators"
  lesson_slug: "type-coercion-and-comparison-operations"
  lesson_title: "Lesson 2.3 Type Coercion & Comparison Operations"
  sort_order: 203

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Analyze"
  xp_reward: 60

prerequisites:
  required_lesson_ids:
    - "JS-MOD02-LES02"
  required_skills:
    - "Primitive vs Reference Types"

skills_acquired:
  - "Implicit vs Explicit Type Conversion"
  - "Truthy vs Falsy Values Matrix (8 Falsy Values)"
  - "Abstract Equality (`==`) vs Strict Equality (`===`) Mechanics"
  - "Object-to-Primitive Coercion (`valueOf`, `toString`, `[Symbol.toPrimitive]`)"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "JavaScript Type Coercion: Truthy vs Falsy, == vs === & ToPrimitive"
  meta_description: "Master JavaScript type coercion: implicit vs explicit conversion, 8 falsy values, abstract (==) vs strict (===) equality, and ToPrimitive algorithms."
  keywords: ["Type Coercion", "Truthy Falsy", "Equality Operators", "== vs ===", "ToPrimitive", "Implicit Conversion"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 2.3 Type Coercion & Comparison Operations

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 2.2 Primitive & Reference Types](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_05_primitive_and_reference_data_types.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Distinguish between Implicit Coercion (automatic) and Explicit Conversion (manual).
2. Memorize JavaScript's **8 Falsy Values**.
3. Evaluate the Abstract Equality Algorithm (`==`) vs Strict Equality (`===`).
4. Trace Object-to-Primitive Coercion via `[Symbol.toPrimitive]`, `valueOf()`, and `toString()`.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL to test type coercion equality expressions.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 The 8 Falsy Values in JavaScript
Everything in JavaScript is **Truthy** except for these **8 Falsy Values**:

1. `false`
2. `0`
3. `-0`
4. `0n` (BigInt zero)
5. `""` (Empty string)
6. `null`
7. `undefined`
8. `NaN`

> [!NOTE]
> Empty arrays `[]` and empty objects `{}` are **TRUTHY**! `Boolean([])` evaluates to `true`.

### 3.2 Abstract (`==`) vs Strict (`===`) Equality
- `===` (Strict Equality): Checks both **Type** and **Value** without coercion (`"5" === 5` $\to$ `false`).
- `==` (Abstract Equality): Attempts implicit type conversion before comparing values (`"5" == 5` $\to$ `true`).

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Compare["Compare: '5' == 5"] --> TypeCheck{Same Data Types?}
    TypeCheck -->|Yes| CompVal[Compare Values]
    TypeCheck -->|No| Coerce[Coerce '5' string -> 5 number]
    Coerce --> CompVal --> Result[Returns true]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```javascript
// Type Coercion & Comparison Matrix

// 1. Implicit String & Number Coercion
console.log("5" + 2); // "52" (String Concatenation wins on + operator!)
console.log("5" - 2); // 3    (Numeric Subtraction forces Number coercion!)

// 2. Truthy vs Falsy Tricky Comparisons
console.log(Boolean([])); // true (Empty array is Truthy!)
console.log([] == false); // true (Coerced: [] -> "" -> 0, false -> 0 -> 0 == 0!)

// 3. Strict Equality Best Practice
console.log("5" === 5);   // false (No coercion!)
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Production Linter Rules**: Enterprise ESLint rules enforce `eqeqeq: ["error", "always"]` to ban Abstract Equality (`==`) and prevent subtle type coercion bugs.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `coercion_demo.js`.
2. Run `node coercion_demo.js` $\to$ Inspect implicit type conversion results!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Unexpected `==` Coercion Bugs** | Using `==` which implicitly coerces operands. | Always use `===` (Strict Equality). |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Always Use Strict Equality (`===`)**: Eliminates unexpected implicit coercion.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What are the 8 falsy values in JavaScript?
**Answer**: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, and `NaN`.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 2.3 Type Coercion Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What does `Boolean([])` evaluate to in JavaScript?",
      "options": ["false", "true", "undefined", "NaN"],
      "correct_answer_index": 1,
      "explanation": "Empty arrays are objects and evaluate to Truthy."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an explicit type validation pipeline for incoming JSON HTTP request payloads.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What is the result of `"10" - 5` vs `"10" + 5`?
**Back**: `"10" - 5` equals `5` (Number). `"10" + 5` equals `"105"` (String).
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
if (x === true) {} // Always use strict equality ===
```
