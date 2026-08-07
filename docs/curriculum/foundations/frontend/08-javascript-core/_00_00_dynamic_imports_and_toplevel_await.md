# Dynamic Imports And Toplevel Await

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 10.1 ES6 Modules](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_35_es6_modules_export_and_import_syntax.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Lazy-load JavaScript modules on demand using **Dynamic `import()`**.
2. Implement **Code Splitting** to reduce initial bundle download sizes.
3. Utilize **Top-Level Await** inside ES Modules without wrapping code in async IIFE blocks.

---

---

Open Node.js REPL or VS Code.

---

---

### 3.1 Static Imports vs Dynamic `import()`
Static `import` statements must appear at the top level of a file and evaluate synchronously on page load. **Dynamic `import(modulePath)`** is a function-like expression that returns a Promise, allowing conditional on-demand lazy loading:

```javascript
// Dynamic On-Demand Import Expression
if (userClickedChartButton) {
  const ChartModule = await import("./heavyChartLibrary.js");
  ChartModule.render();
}
```

### 3.2 Top-Level Await
In ES Modules, the `await` keyword can be used directly at the top level of a module file without wrapping code inside an `async function main() {}`:

```javascript
// Top-Level Await inside an ES Module
const dbConnection = await connectToDatabase();
export { dbConnection };
```

---

---

```mermaid
flowchart TD
    App[Initial Page Load: Downloads Small 50KB Bundle] --> Event{User Clicks Analytics Dashboard}
    Event --> Dynamic[Executes await import('./analytics.js')]
    Dynamic --> Download[Downloads 500KB Analytics Bundle ON DEMAND!]
```

---

---

```javascript
// Top-Level Await & Dynamic Import Demonstration (ES Module)

// 1. Top-Level Await (No async function wrapper required!)
console.log("Initializing Application...");

const isProduction = process.env.NODE_ENV === "production";

// 2. Conditional Dynamic Import (Code Splitting!)
let loggerModule;

if (isProduction) {
  loggerModule = await import("./prodLogger.js");
} else {
  loggerModule = await import("./devLogger.js");
}

// Access default or named exports from dynamic module
loggerModule.log("Application started successfully.");
```

---

---

- **Route-Based Code Splitting in Single-Page Apps**: Web applications split large JavaScript bundles into separate route chunks (e.g. `/admin`, `/dashboard`), lazy-loading components only when a user navigates to that route.

---

---

1. Save code as `app.mjs`.
2. Run `node app.mjs` $\to$ Observe clean dynamic import resolution!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`SyntaxError: await is only valid in async functions`** | Using Top-Level Await inside a standard non-module script. | Ensure file is loaded as an ES Module (`type="module"` or `.mjs` extension). |

---

---

- **Use Dynamic Imports for Heavy Libraries**: Lazy load heavy charting or PDF export libraries only when requested by the user.

---

---

### Q1: What is Code Splitting and how do Dynamic Imports facilitate it?
**Answer**: Code Splitting is a web performance technique that breaks a large JavaScript bundle into smaller chunks that can be loaded on demand. Dynamic `import()` expressions allow bundlers (Vite, Webpack) to automatically extract imported modules into separate lazy-loaded chunks.

---

---

```json
{
  "quiz_title": "Lesson 10.2 Dynamic Imports Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What data type does the dynamic `import(path)` expression return?",
      "options": ["Module Object", "Promise", "Function", "Boolean"],
      "correct_answer_index": 1,
      "explanation": "import() returns a Promise fulfilling to the module object."
    }
  ]
}
```

---

---

Build a route-based dynamic component loader using `import()`.

---

---

**Front**: Can Top-Level Await be used in standard CommonJS files (`.js` with `require`)?
**Back**: No. Top-Level Await is supported ONLY inside ES Modules (`.mjs` or `"type": "module"`).
<!-- flashcard:end -->

---

---

```javascript
const { render } = await import("./chart.js");
```

---
