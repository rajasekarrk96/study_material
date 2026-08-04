```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD12-LES11"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-12-advanced-patterns-testing-capstone"
  module_title: "Module 12 - Advanced Patterns, Meta-Programming, & Testing"
  lesson_slug: "capstone-realtime-iot-dashboard"
  lesson_title: "Lesson 12.11 Capstone: Real-Time IoT Telemetry Dashboard"
  sort_order: 1211

pedagogy:
  difficulty: "advanced"
  estimated_time:
    reading_minutes: 25
    practice_minutes: 35
    quiz_minutes: 10
    total_minutes: 70
  bloom_taxonomy_level: "Create"
  xp_reward: 100

prerequisites:
  required_lesson_ids:
    - "JS-MOD12-LES10"
  required_skills:
    - "Full JavaScript & ES6+ Curriculum Mastery (Modules 1-12)"

skills_acquired:
  - "Designing End-to-End Vanilla JavaScript Web Application Architectures"
  - "Integrating WebSockets Real-Time Telemetry Streams"
  - "Building Proxy Reactive State Management Engines"
  - "High-Performance Event Delegation & DOM Batching"
  - "Configuring LocalStorage Persistence & Vitest Validation"

dependencies:
  software:
    - "VS Code"
    - "Node.js 18+ with Vite & Vitest"
  hardware: []

seo_and_social:
  meta_title: "JavaScript Capstone: Real-Time IoT Dashboard Architecture"
  meta_description: "Build an Enterprise Vanilla JavaScript Capstone: Real-Time IoT Dashboard using WebSockets, Proxy Reactive Store, Event Delegation, LocalStorage, and Vitest."
  keywords: ["JavaScript Capstone", "IoT Dashboard", "WebSockets Project", "Proxy Reactive Store", "Event Delegation Architecture", "Vanilla JavaScript Project"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 12.11 Capstone Architecture: Real-Time IoT Telemetry Dashboard

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 70 Minutes (25m Reading | 35m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced (Capstone Project)
- **Prerequisites**: Full JavaScript & ES6+ Curriculum Mastery (Modules 1–12)
- **XP Reward**: +100 XP (Capstone Achievement Badge)

### Learning Objectives
By the end of this capstone project, you will be able to:
1. Architect a production-grade, zero-framework Vanilla JavaScript web application.
2. Integrate **WebSockets** for streaming real-time sensor telemetry.
3. Build a **Proxy-based Reactive State Engine** to drive automatic UI card re-rendering.
4. Implement **Event Delegation** and **`DocumentFragment`** batching for high-performance DOM updates.
5. Validate application state logic using **Vitest** unit test suites.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open VS Code in project directory.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Capstone Enterprise Architecture
This capstone combines key concepts from all 12 modules into a cohesive, production-grade architecture:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   REAL-TIME IOT DASHBOARD ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ WebSockets Receiver ──► Proxy Reactive Store ──► DocumentFragment Renderer   │
│         │                      │                          │                 │
│ Resilient Backoff    Local Persistence           Event Delegation UI        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    WS[WebSocket Telemetry Stream] -->|postMessage| Store[Proxy Reactive Store]
    Store -->|onStateChange| Batch[DocumentFragment DOM Batcher]
    Batch -->|render| UI[Live IoT Dashboard Cards]
    UI -->|Click Delete| Delegate[Event Delegation Handler]
    Delegate -->|Update| Store
    Store -->|Save| LS[LocalStorage Persistence]
```

---

## 5. Code & Hardware Implementation [id: syntax]

### 5.1 Reactive State Store (`store.js`)

```javascript
export function createIoTStore(initialState = { nodes: new Map() }, onChange) {
  return new Proxy(initialState, {
    get(target, prop, receiver) {
      return Reflect.get(target, prop, receiver);
    },
    set(target, prop, value, receiver) {
      const success = Reflect.set(target, prop, value, receiver);
      if (success && typeof onChange === "function") {
        onChange(prop, value);
      }
      return success;
    }
  });
}
```

### 5.2 Capstone Dashboard Application (`app.js`)

```javascript
import { createIoTStore } from "./store.js";

class IoTDashboardApp {
  #store;
  #container;

  constructor() {
    this.#container = document.querySelector("#dashboard-container");

    // Initialize Proxy Store
    this.#store = createIoTStore({ nodes: new Map() }, () => this.render());

    this.#initEventDelegation();
    this.#connectWebSocket();
  }

  #connectWebSocket() {
    const ws = new WebSocket("wss://echo.websocket.events");
    ws.onmessage = (event) => {
      // Simulate receiving telemetry packet
      const packet = { id: "ESP32-NODE-01", temp: 24.5, timestamp: Date.now() };
      this.#store.nodes.set(packet.id, packet);
      this.render();
    };
  }

  #initEventDelegation() {
    if (!this.#container) return;

    // High-performance single parent event listener
    this.#container.addEventListener("click", (e) => {
      const deleteBtn = e.target.closest(".btn-delete-node");
      if (deleteBtn) {
        const nodeId = deleteBtn.dataset.nodeId;
        this.#store.nodes.delete(nodeId);
        this.render();
      }
    });
  }

  render() {
    if (!this.#container) return;

    // Off-screen DocumentFragment for zero reflow thrashing!
    const fragment = document.createDocumentFragment();

    this.#store.nodes.forEach((node) => {
      const card = document.createElement("div");
      card.className = "sensor-card";
      card.innerHTML = `
        <h3>${node.id}</h3>
        <p>Temp: <span>${node.temp}</span>°C</p>
        <button class="btn-delete-node" data-node-id="${node.id}">Remove</button>
      `;
      fragment.appendChild(card);
    });

    this.#container.innerHTML = "";
    this.#container.appendChild(fragment); // Single DOM append!
  }
}

// Bootstrap Capstone Application
document.addEventListener("DOMContentLoaded", () => new IoTDashboardApp());
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Industrial IoT Command Centers**: Smart factory operations monitoring 10,000 embedded devices in real time use this exact architecture for ultra-fast, zero-framework rendering.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Create `index.html` with `<div id="dashboard-container"></div>`.
2. Run `npm run dev` via Vite $\to$ Watch real-time WebSocket telemetry cards render dynamically!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Proxy Nested Property Mutation Leak** | Modifying nested properties directly (`store.nodes.set(...)`) without triggering Proxy `set` trap. | Call an explicit state notify callback or wrap nested objects in recursive Proxies. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Decouple Data & View**: Never mix raw network socket parsing directly inside UI render functions.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: How does this Vanilla JavaScript Capstone architecture achieve high performance without a frontend framework like React?
**Answer**: It leverages direct V8 primitives: ES6 Proxies for fine-grained reactive state tracking, a single Event Delegation listener to eliminate DOM memory bloat, `DocumentFragment` off-screen batching to restrict layout reflows to a single browser paint frame, and WebSockets for low-latency full-duplex communication.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 12.11 Capstone Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which DOM structure enables populating card nodes off-screen to avoid multiple layout reflows?",
      "options": ["DocumentFragment", "ShadowRoot", "HTMLTemplate", "VirtualDOM"],
      "correct_answer_index": 0,
      "explanation": "DocumentFragment allows populating nodes off-screen before a single DOM append."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Extend the IoT Dashboard capstone to save sensor node configurations in `localStorage` and IndexedDB.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What is the primary architectural benefit of separating state management into a Proxy store?
**Back**: It decouples state mutation logic completely from UI DOM rendering logic.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
// Congratulations! Course 3: JavaScript & ES6+ (52 Lessons) is 100% Complete! 🎉
```
