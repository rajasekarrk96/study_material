# Lesson 6.1 Asynchronous Execution, Callbacks, & Event Queue

> **Course**: Javascript | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 5.4 Keyed Collections](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_18_keyed_collections_map_set_weakmap_weakset.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain how single-threaded JavaScript achieves concurrency via **Web APIs** and the **Event Loop**.
2. Differentiate between **Macrotasks** (`setTimeout`, `setInterval`) and **Microtasks** (`Promise`, `queueMicrotask`).
3. Trace the exact execution priority: Synchronous Stack $\to$ Microtask Queue $\to$ Macrotask Queue.
4. Identify the pitfalls of Callback Hell and Inversion of Control.

---

---

Open Node.js REPL to test event loop queue priority order.

---

---

### 3.1 The Event Loop & Task Queue Priority
JavaScript executes single-threaded synchronously on the Call Stack. When an asynchronous Web API call (`setTimeout`, `fetch`) is invoked, the browser offloads the work to background threads and pushes the completed callback into task queues:

1. **Call Stack**: Executes synchronous code line by line until empty.
2. **Microtask Queue** (HIGHEST PRIORITY): Processed **completely** before any rendering or macrotask! (`Promise.then()`, `queueMicrotask()`, `process.nextTick()`).
3. **Macrotask Queue** (LOWER PRIORITY): Processed one task per event loop turn (`setTimeout()`, `setInterval()`, `setImmediate()`).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       EVENT LOOP QUEUE PRIORITY ORDER                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Synchronous Call Stack Execution (Immediate)                             │
│ 2. ALL Microtasks (Promise callbacks, queueMicrotask) - Emptied completely! │
│ 3. ONE Macrotask (setTimeout, setInterval)                                  │
│ 4. Re-render UI (if browser environment)                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    CallStack[Call Stack: Synchronous Code] -->|Stack Empty| Micro[Microtask Queue: Promises & queueMicrotask]
    Micro -->|Queue Emptied| Macro[Macrotask Queue: setTimeout]
    Macro -->|Execute 1 Task| CallStack
```

---

---

```javascript
// Event Loop Queue Priority Demonstration

console.log("1. Synchronous Start");

// Macrotask (Timer)
setTimeout(() => {
  console.log("4. Macrotask (setTimeout)");
}, 0);

// Microtask (Promise)
Promise.resolve().then(() => {
  console.log("3. Microtask (Promise.then)");
});

console.log("2. Synchronous End");

/* Expected Execution Output Order:
1. Synchronous Start
2. Synchronous End
3. Microtask (Promise.then)
4. Macrotask (setTimeout)
*/
```

---

---

- **UI Render Smoothness (60fps)**: Starving the Event Loop by chaining infinite microtasks blocks the browser main thread, freezing DOM rendering and user interactions.

---

---

1. Save code as `eventloop_demo.js`.
2. Run `node eventloop_demo.js` $\to$ Verify Microtask precedes Macrotask output!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Main Thread Freeze** | Executing heavy synchronous CPU loops or infinite microtask chains. | Offload CPU-heavy computation to Web Workers or `worker_threads`. |

---

---

- **Understand Queue Priorities**: Microtasks execute before Macrotasks regardless of timeout values.

---

---

### Q1: What is the difference between the Macrotask Queue and Microtask Queue in the JavaScript Event Loop?
**Answer**: The Microtask Queue handles high-priority asynchronous callbacks (Promises, `queueMicrotask`). The event loop empties the *entire* Microtask Queue completely before moving on to process a single task from the Macrotask Queue (`setTimeout`, `setInterval`).

---

---

```json
{
  "quiz_title": "Lesson 6.1 Event Loop Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which task queue is emptied completely before the Event Loop executes a `setTimeout` callback?",
      "options": ["Macrotask Queue", "Microtask Queue", "Render Queue", "Worker Queue"],
      "correct_answer_index": 1,
      "explanation": "The Microtask Queue is emptied completely before any Macrotask is processed."
    }
  ]
}
```

---

---

Predict and verify the execution output order of 8 mixed synchronous, Promise, and timer logs.

---

---

**Front**: Is `setTimeout(fn, 0)` guaranteed to execute in exactly 0 milliseconds?
**Back**: No. It waits until the Call Stack and all Microtasks are completely clear.
<!-- flashcard:end -->

---

---

```javascript
queueMicrotask(() => console.log("Microtask"));
```

---
