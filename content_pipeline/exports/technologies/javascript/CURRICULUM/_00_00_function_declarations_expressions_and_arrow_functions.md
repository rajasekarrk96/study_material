# Function Declarations Expressions And Arrow Functions

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 3.3 Iteration Protocols](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_10_iteration_protocols_iterators_and_generators.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Contrast Function Declarations with Function Expressions and their hoisting rules.
2. Write concise **Arrow Functions** (`() => {}`) with implicit return values.
3. Explain how Arrow Functions inherit **Lexical `this` Binding**.
4. Implement Immediately Invoked Function Expressions (IIFE).

---

---

Open Node.js REPL to execute function definitions.

---

---

### 3.1 Declarations vs Expressions vs Arrow Functions

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       FUNCTION DEFINITION VARIETIES MATRIX                  │
├─────────────────┬──────────────────┬─────────────────┬──────────────────────┤
│ Type            │ Hoisted?         │ Has Own `this`? │ Constructor (`new`)? │
├─────────────────┼──────────────────┼─────────────────┼──────────────────────┤
│ Declaration     │ YES (Full Body)  │ YES             │ YES                  │
│ Expression      │ Variable only    │ YES             │ YES                  │
│ Arrow Function  │ Variable only    │ NO (Lexical)    │ NO                   │
└─────────────────┴──────────────────┴─────────────────┴──────────────────────┘
```

> [!IMPORTANT]
> **Lexical `this` Binding**: Arrow functions do NOT have their own `this` keyword, `arguments` object, or `super` binding. They capture `this` from the enclosing scope at creation time!

---

---

```mermaid
flowchart TD
    Regular[Regular Function: Dynamic 'this' determined by HOW function is called]
    Arrow[Arrow Function: Lexical 'this' inherited from WHERE function was created]
```

---

---

```javascript
// Function Syntax & Lexical 'this' Demonstration

// 1. Function Declaration (Hoisted!)
function add(a, b) {
  return a + b;
}

// 2. Arrow Function with Implicit Return
const multiply = (a, b) => a * b;

// 3. Lexical 'this' in Object Methods
const timer = {
  seconds: 0,
  start() {
    // Arrow function preserves outer 'timer' object 'this'!
    setInterval(() => {
      this.seconds++;
      console.log(`Elapsed: ${this.seconds}s`);
    }, 1000);
  }
};

// 4. IIFE (Immediately Invoked Function Expression)
(() => {
  console.log("IIFE Executed Immediately on Load!");
})();
```

---

---

- **React Event Handlers & Node Async Callbacks**: Arrow functions prevent traditional `const self = this` or `.bind(this)` boilerplate when registering event listeners inside class components or modules.

---

---

1. Save code as `fn_demo.js`.
2. Run `node fn_demo.js` $\to$ Observe lexical `this` binding in timer interval!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: X is not a constructor`** | Attempting to instantiate an Arrow function with `new ArrowFn()`. | Use regular functions or ES6 `class` definitions for constructors. |

---

---

- **Use Arrow Functions for Callbacks**: Eliminates manual `this` binding.

---

---

### Q1: How does the `this` keyword behave differently in Arrow Functions compared to Regular Functions?
**Answer**: In regular functions, `this` is dynamically bound based on *how* the function is invoked at runtime. In arrow functions, `this` is lexically bound, capturing the `this` value of the enclosing scope where the arrow function was defined.

---

---

```json
{
  "quiz_title": "Lesson 4.1 Functions Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Do Arrow Functions have their own `this` binding?",
      "options": ["Yes", "No (Lexical inheritance)", "Only in strict mode", "Only when passed arguments"],
      "correct_answer_index": 1,
      "explanation": "Arrow functions inherit lexical 'this' from their enclosing scope."
    }
  ]
}
```

---

---

Refactor a legacy `.bind(this)` codebase to modern ES6 arrow functions.

---

---

**Front**: Can arrow functions be instantiated using the `new` keyword?
**Back**: No. Arrow functions lack `[[Construct]]` internal methods.
<!-- flashcard:end -->

---

---

```javascript
const add = (a, b) => a + b;
```

---
