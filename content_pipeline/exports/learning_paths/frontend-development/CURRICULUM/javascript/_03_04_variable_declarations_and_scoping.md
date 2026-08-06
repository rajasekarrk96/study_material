```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD02-LES01"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-02-variables-types-operators"
  module_title: "Module 2 - Variables, Data Types, & Operators"
  lesson_slug: "variable-declarations-and-scoping"
  lesson_title: "Lesson 2.1 Variable Declarations & Scoping"
  sort_order: 201

pedagogy:
  difficulty: "beginner"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "JS-MOD01-LES03"
  required_skills:
    - "Execution Context & Hoisting Mechanics"

skills_acquired:
  - "Declaration Keywords (`var`, `let`, `const`)"
  - "Scope Hierarchy (Global, Function, Block Scope)"
  - "Hoisting Behavior (Function vs Variable Hoisting)"
  - "Temporal Dead Zone (TDZ) Boundaries"
  - "Immutability Boundaries of `const` References"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "JavaScript Variables: var vs let vs const, Hoisting & Temporal Dead Zone"
  meta_description: "Master JavaScript variables: var, let, const, global vs function vs block scope, variable/function hoisting, and the Temporal Dead Zone (TDZ)."
  keywords: ["JavaScript Variables", "var let const", "Block Scope", "Hoisting", "Temporal Dead Zone", "TDZ"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 2.1 Variable Declarations & Scoping

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 1.3 Execution Context](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_03_execution_context_call_stack_and_memory_management.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Contrast `var`, `let`, and `const` declaration rules.
2. Differentiate between Global Scope, Function Scope, and Block Scope.
3. Explain Variable and Function **Hoisting** mechanics.
4. Avoid reference crashes caused by the **Temporal Dead Zone (TDZ)**.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL or VS Code terminal to execute variable scope code.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 `var` vs `let` vs `const`

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       VARIABLE DECLARATION COMPARISON                       │
├──────────────┬──────────────────┬─────────────────┬─────────────────────────┤
│ Keyword      │ Scope Level      │ Hoisting State  │ Re-assignment Allowed?  │
├──────────────┼──────────────────┼─────────────────┼─────────────────────────┤
│ `var`        │ Function Scope   │ Hoisted (`undef`)│ YES                    │
├──────────────┼──────────────────┼─────────────────┼─────────────────────────┤
│ `let`        │ Block Scope `{}` │ Hoisted (TDZ)   │ YES                     │
├──────────────┼──────────────────┼─────────────────┼─────────────────────────┤
│ `const`      │ Block Scope `{}` │ Hoisted (TDZ)   │ NO (Reference locked)   │
└──────────────┴──────────────────┴─────────────────┴─────────────────────────┘
```

### 3.2 The Temporal Dead Zone (TDZ)
`let` and `const` are hoisted to the top of their block scope, but remain uninitialized in the **Temporal Dead Zone (TDZ)** until execution reaches the declaration line. Accessing a `let` variable inside the TDZ throws a `ReferenceError`:

```javascript
console.log(x); // ReferenceError: Cannot access 'x' before initialization (TDZ!)
let x = 42;
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
graph TD
    BlockStart[Start Block Scope '{'] --> TDZ[Temporal Dead Zone - Accessing throws ReferenceError]
    TDZ --> DeclLine["let x = 42 (Declaration Line)"]
    DeclLine --> Valid[Variable Valid & Accessible]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```javascript
// Scoping & TDZ Demonstration

function scopeDemo() {
  if (true) {
    var functionScoped = "Accessible outside block";
    let blockScoped = "Trapped in block";
    const constScoped = { metric: 100 };

    // const reference is locked, but mutated internal properties are allowed!
    constScoped.metric = 200; 
  }

  console.log(functionScoped); // Works!
  // console.log(blockScoped); // ReferenceError!
}

scopeDemo();
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Production Code Guidelines**: Modern JS style guides (Airbnb, Google) ban `var` completely. Use `const` by default, and `let` only when variable re-assignment is explicitly required.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `scope_demo.js`.
2. Run `node scope_demo.js` $\to$ Observe block scope enforcement!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ReferenceError: Cannot access X before initialization`** | Attempting to read a `let` / `const` variable inside the Temporal Dead Zone. | Declare variables at the top of their block scope. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Default to `const`**: Prevents accidental re-assignments.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
**Answer**: The TDZ is the region of a block scope from the start of the block until the line where a `let` or `const` variable is declared. Accessing the variable within the TDZ throws a `ReferenceError`.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 2.1 Variable Scoping Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which variable keyword creates Function-scoped variables?",
      "options": ["let", "const", "var", "static"],
      "correct_answer_index": 2,
      "explanation": "var creates function-scoped variables that ignore block {} boundaries."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Refactor a legacy `var`-based code repository to modern block-scoped `const`/`let` architecture.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: Does `const` make objects completely immutable?
**Back**: No. `const` locks the variable memory reference, but object properties can still be mutated.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
const user = { name: "Alice" }; // Preferred default
let count = 0; // Use when re-assigning
```
