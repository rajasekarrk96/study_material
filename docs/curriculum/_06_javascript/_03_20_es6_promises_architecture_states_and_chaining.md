```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD06-LES02"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-06-async-promises-await"
  module_title: "Module 6 - Asynchronous JavaScript, Promises, & Async/Await"
  lesson_slug: "es6-promises-architecture-states-and-chaining"
  lesson_title: "Lesson 6.2 ES6 Promises Architecture, States, & Chaining"
  sort_order: 602

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
    - "JS-MOD06-LES01"
  required_skills:
    - "Event Loop & Callback Queue Priority"

skills_acquired:
  - "Promise 3 Lifecycle States (`Pending`, `Fulfilled`, `Rejected`)"
  - "Promise Constructor Construction (`new Promise((resolve, reject) => {})`)"
  - "Promise Chaining Mechanics (`.then()`, `.catch()`, `.finally()`)"
  - "Error Propagation Down the Promise Chain"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "ES6 Promises Architecture: Pending, Fulfilled, Rejected, .then & .catch"
  meta_description: "Master ES6 Promises: 3 lifecycle states (Pending, Fulfilled, Rejected), new Promise constructor, chaining .then(), error catching with .catch(), and .finally()."
  keywords: ["ES6 Promises", "Promise states", "Fulfilled Rejected", "Promise Chaining", "then catch finally", "Error Propagation"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 6.2 ES6 Promises Architecture, States, & Chaining

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 6.1 Event Loop](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_19_asynchronous_execution_callbacks_event_queue.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Identify the 3 immutable states of a Promise (`Pending`, `Fulfilled`, `Rejected`).
2. Construct Promises using `new Promise((resolve, reject) => {})`.
3. Chain asynchronous operations using `.then()`, `.catch()`, and `.finally()`.
4. Trace error bubbling down an asynchronous Promise chain.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL to execute Promise chains.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Promise States & Immutability
A **Promise** is a placeholder object for a value that is not yet available. A Promise exists in exactly one of three states:

1. **`Pending`**: Initial state; neither fulfilled nor rejected.
2. **`Fulfilled`**: Operation completed successfully (`resolve(value)`).
3. **`Rejected`**: Operation failed (`reject(error)`).

> [!IMPORTANT]
> **State Settling Immutability**: Once a Promise transitions from `Pending` to either `Fulfilled` or `Rejected`, its state is **Settled** and permanently locked. Calling `resolve()` or `reject()` a second time is ignored.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PROMISE STATE TRANSITIONS                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                          ┌──► Fulfilled (via resolve(val)) ──► .then()     │
│ Pending (Initial State) ─┤                                                  │
│                          └──► Rejected  (via reject(err))  ──► .catch()    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Pending[Pending Promise] -->|resolve| Fulfilled[Fulfilled State]
    Pending -->|reject| Rejected[Rejected State]
    Fulfilled --> Then[Execute .then Callback]
    Rejected --> Catch[Execute .catch Error Handler]
    Then --> Finally[Execute .finally Cleanup]
    Catch --> Finally
```

---

## 5. Code & Hardware Implementation [id: syntax]

```javascript
// Promise Construction & Chaining Demonstration

function fetchIotTelemetry(sensorId) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (!sensorId) {
        reject(new Error("Invalid Sensor ID!"));
      } else {
        resolve({ sensorId, temperature: 26.4, status: "OK" });
      }
    }, 500);
  });
}

// Chaining .then(), .catch(), and .finally()
fetchIotTelemetry("ESP32-NODE-1")
  .then(data => {
    console.log("Step 1 (Raw Data):", data);
    return data.temperature; // Returns value wrapped in a new Fulfilled Promise!
  })
  .then(temp => {
    console.log(`Step 2 (Fahrenheit): ${(temp * 1.8 + 32).toFixed(1)}°F`);
  })
  .catch(err => {
    console.error("Promise Error Caught:", err.message);
  })
  .finally(() => {
    console.log("Cleanup: Telemetry operation finalized.");
  });
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Fetch API HTTP Requests**: Browsers' native `window.fetch()` API returns a Promise that fulfills with a `Response` object or rejects on network disconnects.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `promises_demo.js`.
2. Run `node promises_demo.js` $\to$ Inspect Promise chain step outputs!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`UnhandledPromiseRejection`** | Omitting a `.catch()` block at the end of a Promise chain. | Always append `.catch()` or handle rejections inside async wrappers. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Always Return Values in `.then()`**: Returning a value forwards it to the next `.then()` callback in the chain.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What happens if a `.then()` callback returns a plain scalar value versus another Promise?
**Answer**: If a `.then()` callback returns a scalar value (e.g. `number` or `string`), `.then()` automatically wraps it in a new Fulfilled Promise holding that value. If it returns another Promise, the chain waits for that inner Promise to settle before invoking the next `.then()` in the outer chain.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 6.2 Promises Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which method executes regardless of whether a Promise fulfilled or rejected?",
      "options": [".then()", ".catch()", ".finally()", ".all()"],
      "correct_answer_index": 2,
      "explanation": ".finally() executes cleanup logic on both fulfillment and rejection."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Convert a legacy callback-based `fs.readFile` function into a Promise-returning function (`promisify`).

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: Can a Settled Promise (Fulfilled or Rejected) change its state again?
**Back**: No. State transitions are immutable and permanent once settled.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
new Promise((resolve, reject) => resolve(data))
  .then(res => console.log(res))
  .catch(err => console.error(err));
```
