# Destructuring Assignment And Spread Rest Operators

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 5.2 Arrays](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_16_dense_sparse_arrays_and_higher_order_methods.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Extract array values using positional **Array Destructuring**.
2. Unpack object properties using **Object Destructuring**, variable renaming, and defaults.
3. Apply Destructuring directly inside **Function Parameter Signatures**.
4. Clone and merge objects and arrays using the **Spread Operator (`...`)**.

---

---

Open Node.js REPL to execute destructuring patterns.

---

---

### 3.1 Unpacking Data Structures
ES6 Destructuring provides a concise syntax for extracting properties from objects or elements from arrays directly into local variables:

```javascript
// Object Destructuring with Renaming & Default
const user = { name: "Alice", role: "ADMIN" };
const { name: userName, role, status = "ACTIVE" } = user;

// Array Destructuring with Rest
const [first, second, ...remaining] = [10, 20, 30, 40, 50];
```

### 3.2 Spread (`...`) for Immutable Merging
The Spread operator shallow-copies elements from an existing object or array into a new target container:

```javascript
const defaults = { theme: "DARK", notifications: true };
const userPrefs = { notifications: false, fontSize: 16 };

// Merging Objects (userPrefs overwrites collision keys in defaults!)
const finalConfig = { ...defaults, ...userPrefs };
```

---

---

```mermaid
flowchart TD
    Obj["Source Object: { name: 'Bob', age: 30 }"] --> Destruct["const { name, age } = Obj"]
    Destruct --> Var1[Local Variable: name = 'Bob']
    Destruct --> Var2[Local Variable: age = 30]
```

---

---

```javascript
// Destructuring & Spread Syntax Demonstration

// 1. Function Parameter Destructuring with Defaults
function renderUserProfile({ id, username, settings: { theme = "LIGHT" } = {} }) {
  console.log(`[User ${id}]: ${username} (Theme: ${theme})`);
}

const userData = {
  id: 101,
  username: "alex_dev",
  settings: { theme: "DARK" }
};

renderUserProfile(userData); // Output: [User 101]: alex_dev (Theme: DARK)

// 2. Swapping Variables without Temporary Storage
let a = 1, b = 2;
[a, b] = [b, a];
console.log(`Swapped: a=${a}, b=${b}`); // a=2, b=1

// 3. Immutable Array Insertion using Spread
const initialList = ["Alpha", "Gamma"];
const updatedList = [initialList[0], "Beta", ...initialList.slice(1)];
console.log("Updated List:", updatedList); // ['Alpha', 'Beta', 'Gamma']
```

---

---

- **React Component Props & State Updates**: Modern React components destructure props in function signatures and use `setStore(prev => ({ ...prev, updatedKey: val }))` for immutable state updates.

---

---

1. Save code as `destructuring_demo.js`.
2. Run `node destructuring_demo.js` $\to$ Inspect destructuring and variable swapping outputs!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: Cannot destructure property X of undefined`** | Attempting to destructure properties from a target that evaluates to `null` or `undefined`. | Provide default fallback objects: `const { x } = target || {};`. |

---

---

- **Destructure Function Parameters**: Makes function signatures self-documenting.

---

---

### Q1: How do you rename a variable during Object Destructuring in ES6?
**Answer**: By placing a colon and the new target variable name after the key: `const { originalKey: newVariableName } = object;`.

---

---

```json
{
  "quiz_title": "Lesson 5.3 Destructuring Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the result of `const [x, , y] = [1, 2, 3];`?",
      "options": ["x=1, y=2", "x=1, y=3", "x=1, y=undefined", "Syntax Error"],
      "correct_answer_index": 1,
      "explanation": "Leaving a comma blank skips the second element (2), setting x=1 and y=3."
    }
  ]
}
```

---

---

Refactor a complex API response handler to extract 10 nested fields via destructuring.

---

---

**Front**: How do you assign a default value during object destructuring?
**Back**: `const { prop = "defaultValue" } = object;`.
<!-- flashcard:end -->

---

---

```javascript
const { name, age } = user;
const clone = { ...original };
```

---
