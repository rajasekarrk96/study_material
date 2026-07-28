```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD12-LES03"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-12-advanced-patterns-testing-capstone"
  module_title: "Module 12 - Advanced Patterns, Meta-Programming, & Testing"
  lesson_slug: "service-workers-and-offline-pwa-caching"
  lesson_title: "Lesson 12.3 Service Workers & Offline PWA Caching"
  sort_order: 1203

pedagogy:
  difficulty: "advanced"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 70

prerequisites:
  required_lesson_ids:
    - "JS-MOD12-LES02"
  required_skills:
    - "Fetch API, Promises, & Web Workers Architecture"

skills_acquired:
  - "Service Worker Registration & Lifecycle (`install`, `activate`, `fetch`)"
  - "Cache Storage API (`caches.open()`, `cache.match()`)"
  - "Caching Strategies (Cache-First, Network-First, Stale-While-Revalidate)"
  - "Building Offline-First Progressive Web Applications (PWA)"

dependencies:
  software:
    - "VS Code"
    - "Modern Web Browser with HTTPS / Localhost"
  hardware: []

seo_and_social:
  meta_title: "Service Workers: Offline PWA Caching Strategies & Cache Storage API"
  meta_description: "Master Progressive Web Apps: Service Worker lifecycle, Cache Storage API, and offline caching strategies (Cache First, Network First, Stale-While-Revalidate)."
  keywords: ["Service Workers", "PWA Caching", "Cache Storage API", "Cache First", "Network First", "Stale While Revalidate", "Offline Web App"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 12.3 Service Workers & Offline PWA Caching

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 12.2 Web Workers](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_43_web_workers_and_multithreaded_javascript.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain the **Service Worker** background proxy lifecycle (`install` $\to$ `activate` $\to$ `fetch`).
2. Manage offline network assets using the **Cache Storage API**.
3. Implement 3 core caching strategies: **Cache-First**, **Network-First**, and **Stale-While-Revalidate**.
4. Transform web applications into offline-capable **Progressive Web Apps (PWAs)**.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Browser DevTools Application Tab $\to$ Select Service Workers.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Service Worker Proxy Architecture
A **Service Worker** is a programmable network proxy running in a background thread between your web application and the network. It intercepts outgoing `fetch` network requests, allowing you to serve cached responses when offline:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     3 CORE PWA OFFLINE CACHING STRATEGIES                   │
├────────────────────────┬────────────────────────────────────────────────────┤
│ Strategy               │ Description & Ideal Use Case                       │
├────────────────────────┼────────────────────────────────────────────────────┤
│ **Cache-First**        │ Checks Cache first; falls back to Network.         │
│                        │ Ideal for static assets (images, fonts, CSS).      │
├────────────────────────┼────────────────────────────────────────────────────┤
│ **Network-First**      │ Fetches from Network; falls back to Cache offline.│
│                        │ Ideal for real-time dynamic API data.              │
├────────────────────────┼────────────────────────────────────────────────────┤
│ **Stale-While-Revalidate**│ Returns Cached response immediately, then fetches │
│                        │ fresh copy in background to update cache!          │
└────────────────────────┴────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    App[PWA Client App] -->|fetch request| SW[Service Worker Proxy]
    SW --> Cache{Item in Cache?}
    Cache -->|Yes| Hit[Return Cached Response Immediately!]
    Cache -->|No / Offline| Net[Network Request -> Cache Response]
```

---

## 5. Code & Hardware Implementation [id: syntax]

### File 1: `sw.js` (Service Worker Script)

```javascript
const CACHE_NAME = "telemetry-pwa-v1";
const STATIC_ASSETS = ["/", "/index.html", "/styles.css", "/app.js"];

// 1. Install Event: Cache Static App Shell Assets
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting();
});

// 2. Activate Event: Clean Up Old Cache Versions
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key)))
    )
  );
  self.clients.claim();
});

// 3. Fetch Event: Cache-First Strategy with Network Fallback
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse; // Cache Hit!
      }
      return fetch(event.request); // Cache Miss -> Fetch Network
    })
  );
});
```

### File 2: `app.js` (Register Service Worker)

```javascript
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js")
      .then((reg) => console.log("[Service Worker Registered] Scope:", reg.scope))
      .catch((err) => console.error("[SW Registration Failed]:", err));
  });
}
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Mobile First Progressive Web Apps**: Twitter Lite and Starbucks PWA use Service Workers to load instantly on 2G networks and work 100% offline.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Serve files over `http://localhost:3000`.
2. Open DevTools Application Tab $\to$ Check "Offline" checkbox $\to$ Reload page to verify offline PWA loading!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Service Worker Registration Fails** | Attempting to register a Service Worker over insecure `http://` (non-localhost). | Service Workers strictly require HTTPS or `localhost` for security. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Version Cache Names**: Increment `CACHE_NAME` (`v1` $\to$ `v2`) to trigger activation cleanups on code updates.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: How does the Stale-While-Revalidate caching strategy work?
**Answer**: Stale-While-Revalidate returns the cached response to the client immediately for zero-latency rendering, while simultaneously firing a background network request to fetch the latest version and update the cache for future visits.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 12.3 Service Workers Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which event fires in a Service Worker when static assets are pre-cached during setup?",
      "options": ["install", "activate", "fetch", "sync"],
      "correct_answer_index": 0,
      "explanation": "The install event handles pre-caching static assets."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an offline PWA caching static HTML/CSS shell assets.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What property method registers a Service Worker in modern browsers?
**Back**: `navigator.serviceWorker.register('/sw.js')`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
self.addEventListener("fetch", e => {
  e.respondWith(caches.match(e.request) || fetch(e.request));
});
```
