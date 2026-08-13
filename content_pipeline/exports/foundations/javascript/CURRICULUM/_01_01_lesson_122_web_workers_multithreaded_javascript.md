# Lesson 12.2 Web Workers & Multithreaded JavaScript

> **Course**: Javascript | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 12.1 Proxy & Reflect](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_42_proxy_and_reflect_api_metaprogramming.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain how **Web Workers** execute JavaScript code on background OS threads.
2. Instantiate Dedicated Workers and pass messages via `postMessage()`.
3. Offload heavy CPU computations (image processing, cryptography) to prevent UI main thread freezing.
4. Utilize **`SharedArrayBuffer`** and **`Atomics`** for zero-copy shared memory thread communication.

---

---

Open Browser DevTools Console & Sources panel.

---

---

### 3.1 Single-Threaded Main Loop vs Worker Threads
JavaScript's UI thread executes DOM manipulation and user event handlers. Executing a heavy 5-second CPU loop directly on the main thread freezes the entire browser UI.

**Web Workers** run in isolated background thread execution contexts with zero DOM access, communicating asynchronously via message passing:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MAIN UI THREAD VS WEB WORKER THREAD                    │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Feature         │ Main UI Thread                   │ Web Worker Thread      │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ DOM Access      │ Full (`document`, `window`)      │ NO DOM Access (`self`) │
│ Purpose         │ UI Rendering & Event Handling    │ Heavy CPU Computation  │
│ Communication   │ Direct execution                 │ `postMessage()` API    │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

---

```mermaid
flowchart LR
    Main[Main UI Thread: Smooth 60 FPS!] -->|postMessage arrayData| Worker[Web Worker Thread: CPU Intensive Math]
    Worker -->|Computes Math Result| Worker
    Worker -->|postMessage calculationResult| Main
```

---

---

### File 1: `worker.js` (Background Thread)

```javascript
// Web Worker Execution Context (self)
self.onmessage = function(event) {
  const { numbers } = event.data;
  console.log("[Worker Thread]: Processing heavy computation...");

  // Heavy CPU Computation: Summing array
  const total = numbers.reduce((acc, num) => acc + num, 0);

  // Send result back to Main UI Thread
  self.postMessage({ result: total });
};
```

### File 2: `main.js` (UI Thread)

```javascript
// Main UI Thread
if (window.Worker) {
  const worker = new Worker("worker.js");

  // Send payload to worker thread
  const largeDataset = Array.from({ length: 1000000 }, (_, i) => i + 1);
  worker.postMessage({ numbers: largeDataset });

  // Listen for worker calculation result
  worker.onmessage = function(event) {
    console.log("[Main Thread Received]: Total Sum =", event.data.result);
    worker.terminate(); // Terminate worker thread when finished!
  };
}
```

---

---

- **Client-Side Image/Video Processing & Cryptography**: Heavy canvas image filtering, PDF generation, or client-side encryption algorithms execute inside Web Workers to maintain 60 FPS smooth scrolling.

---

---

1. Save `worker.js` and `main.js`.
2. Run in browser dev server $\to$ Observe heavy computation executing without dropping main thread UI frames!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ReferenceError: document is not defined`** | Attempting to access `document` or `window` inside a Web Worker file. | Perform DOM updates strictly on the Main UI thread using `postMessage()` callbacks. |

---

---

- **Terminate Unused Workers**: Call `worker.terminate()` when background tasks finish to release OS thread resources.

---

---

### Q1: What capabilities and Web APIs are accessible inside a Web Worker?
**Answer**: Web Workers have access to `navigator`, `location` (read-only), `fetch()`, `IndexedDB`, `setTimeout()`, `WebSockets`, and `WebAssembly`. They do NOT have access to the DOM, `window`, `document`, or parent page elements.

---

---

```json
{
  "quiz_title": "Lesson 12.2 Web Workers Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which method sends messages between the Main UI thread and a Web Worker?",
      "options": ["sendMessage()", "postMessage()", "dispatch()", "emit()"],
      "correct_answer_index": 1,
      "explanation": "postMessage() sends message payloads between threads."
    }
  ]
}
```

---

---

Offload a heavy CSV data parser module to a Web Worker thread.

---

---

**Front**: How do you terminate a Web Worker thread from the main thread?
**Back**: `worker.terminate()`.
<!-- flashcard:end -->

---

---

```javascript
const worker = new Worker("worker.js");
worker.postMessage(data);
worker.onmessage = e => console.log(e.data);
```

---
