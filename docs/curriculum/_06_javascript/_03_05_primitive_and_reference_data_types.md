```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD02-LES02"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-02-variables-types-operators"
  module_title: "Module 2 - Variables, Data Types, & Operators"
  lesson_slug: "primitive-and-reference-data-types"
  lesson_title: "Lesson 2.2 Primitive & Reference Data Types"
  sort_order: 202

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
    - "JS-MOD02-LES01"
  required_skills:
    - "Variable Declarations & Call Stack vs Heap Storage"

skills_acquired:
  - "7 Primitive Types Inspection (`Number`, `String`, `Boolean`, `Undefined`, `Null`, `Symbol`, `BigInt`)"
  - "Reference Types Handling (`Object`, `Array`, `Function`)"
  - "Pass-by-Value vs Pass-by-Reference Assignment Mechanics"
  - "Type Checking Methods (`typeof`, `instanceof`, `Array.isArray()`)"
  - "Symbol Use Cases & BigInt Arbitrary Precision Operations"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "JavaScript Data Types: 7 Primitives vs Reference Types & Pass-by-Reference"
  meta_description: "Master JavaScript data types: Number, String, Boolean, Undefined, Null, Symbol, BigInt primitives vs Object reference types, typeof, and instanceof."
  keywords: ["JavaScript Data Types", "Primitive vs Reference", "Pass-by-Value", "Symbol", "BigInt", "typeof", "Array.isArray"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 2.2 Primitive & Reference Data Types

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 2.1 Variable Declarations](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_04_variable_declarations_and_scoping.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Identify JavaScript's 7 primitive data types (`Number`, `String`, `Boolean`, `Undefined`, `Null`, `Symbol`, `BigInt`).
2. Differentiate Pass-by-Value (Primitives) from Pass-by-Reference (Objects/Arrays).
3. Safely check data types using `typeof`, `instanceof`, and `Array.isArray()`.
4. Create unique object property keys using `Symbol()`.
5. Perform high-precision integer calculations using `BigInt` (e.g. `9007199254740991n`).

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL to execute type checking commands.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Primitives vs Reference Types

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PRIMITIVES VS REFERENCE TYPES MATRIX                    │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Characteristic  │ Primitive Types (7 Types)        │ Reference Types        │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Types           │ Number, String, Boolean,         │ Object, Array,         │
│                 │ Undefined, Null, Symbol, BigInt  │ Function, Date, RegEx  │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Memory Storage  │ Call Stack (Direct Value)        │ Memory Heap (Pointer)  │
│ Immutability    │ Immutable (Value cannot change)  │ Mutable                │
│ Assignment      │ Copied by VALUE                  │ Copied by REFERENCE    │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

> [!CAUTION]
> **`typeof null` Bug**: `typeof null` returns `"object"` due to a legacy 1995 V8/JS C-pointer implementation detail. To check for `null`, use strict equality: `val === null`.

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
graph TD
    subgraph Pass-by-Value [Primitives: Copy Value]
        A["a = 10"] -->|Copy Value| B["b = 10 (Independent Memory)"]
    end

    subgraph Pass-by-Reference [Reference: Copy Pointer]
        Obj1["obj1 = { x: 1 }"] -->|Copy Heap Address| Obj2["obj2 = { x: 1 } (Shared Heap Target!)"]
    end
```

---

## 5. Code & Hardware Implementation [id: syntax]

```javascript
// 1. Symbol & BigInt
const ID_KEY = Symbol("id");
const sensorNode = {
  [ID_KEY]: 101,
  name: "ESP32 Gateway"
};

const massiveInteger = 9007199254740995n; // BigInt literal

// 2. Type Checking Matrix
console.log(typeof "hello"); // "string"
console.log(typeof 42);      // "number"
console.log(typeof null);    // "object" (Legacy quirk!)
console.log(Array.isArray([1, 2, 3])); // true (Safe array check!)
console.log(sensorNode instanceof Object); // true
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **64-bit BigInt Telemetry IDs**: High-throughput distributed systems (Kafka, PostgreSQL 64-bit BIGINTs) use JavaScript `BigInt` to prevent integer overflow truncation.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `types_demo.js`.
2. Run `node types_demo.js` $\to$ Inspect type outputs in console.

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`typeof []` returns `"object"`** | Arrays are objects in JavaScript. | Use `Array.isArray(arr)` to verify arrays. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `Array.isArray()`**: Never rely on `typeof` for checking array instances.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What are the 7 primitive data types in JavaScript?
**Answer**: Number, String, Boolean, Undefined, Null, Symbol, and BigInt.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 2.2 Data Types Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which method is the reliable standard for checking if a value is an Array?",
      "options": ["typeof val === 'array'", "Array.isArray(val)", "val instanceof Array", "val.type === 'array'"],
      "correct_answer_index": 1,
      "explanation": "Array.isArray(val) safely checks if an entity is an Array."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a deep-clone utility function that recursively copies nested objects without reference mutation.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What does `typeof null` return in JavaScript?
**Back**: `"object"` (a historical language bug; check `val === null` instead).
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
Array.isArray(data); // True
val === null; // True null check
```
