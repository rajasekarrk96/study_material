# Variable Declarations And Scoping

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

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

---

Open Node.js REPL or VS Code terminal to execute variable scope code.

---

---

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

---

```mermaid
graph TD
    BlockStart[Start Block Scope '{'] --> TDZ[Temporal Dead Zone - Accessing throws ReferenceError]
    TDZ --> DeclLine["let x = 42 (Declaration Line)"]
    DeclLine --> Valid[Variable Valid & Accessible]
```

---

---

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

---

- **Production Code Guidelines**: Modern JS style guides (Airbnb, Google) ban `var` completely. Use `const` by default, and `let` only when variable re-assignment is explicitly required.

---

---

1. Save code as `scope_demo.js`.
2. Run `node scope_demo.js` $\to$ Observe block scope enforcement!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ReferenceError: Cannot access X before initialization`** | Attempting to read a `let` / `const` variable inside the Temporal Dead Zone. | Declare variables at the top of their block scope. |

---

---

- **Default to `const`**: Prevents accidental re-assignments.

---

---

### Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
**Answer**: The TDZ is the region of a block scope from the start of the block until the line where a `let` or `const` variable is declared. Accessing the variable within the TDZ throws a `ReferenceError`.

---

---

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

---

Refactor a legacy `var`-based code repository to modern block-scoped `const`/`let` architecture.

---

---

**Front**: Does `const` make objects completely immutable?
**Back**: No. `const` locks the variable memory reference, but object properties can still be mutated.
<!-- flashcard:end -->

---

---

```javascript
const user = { name: "Alice" }; // Preferred default
let count = 0; // Use when re-assigning
```

---
