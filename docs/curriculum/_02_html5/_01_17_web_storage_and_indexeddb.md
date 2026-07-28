```yaml
schema_version: "2.0"
metadata:
  lesson_id: "HTML5-MOD07-LES01"
  course_slug: "course-01-html5"
  course_title: "Course 1: HTML5"
  module_slug: "mod-07-advanced-apis-storage"
  module_title: "Module 7 - HTML5 Advanced APIs & Storage Mechanisms"
  lesson_slug: "web-storage-and-indexeddb"
  lesson_title: "Lesson 7.1 Web Storage & IndexedDB"
  sort_order: 701

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
    - "HTML5-MOD01-LES01"
  required_skills:
    - "Client-Side Data Storage Concepts"

skills_acquired:
  - "Cookies vs LocalStorage vs SessionStorage vs IndexedDB Comparison"
  - "LocalStorage API Implementation (`setItem`, `getItem`, `removeItem`, `clear`)"
  - "SessionStorage Lifecycle Management"
  - "Storage Event Synchronization across Tabs"
  - "IndexedDB Async Object Store Transactions"

dependencies:
  software:
    - "VS Code"
    - "Chrome DevTools Application Tab"
  hardware: []

seo_and_social:
  meta_title: "HTML5 Web Storage (LocalStorage/SessionStorage) & IndexedDB Guide"
  meta_description: "Master client-side storage: LocalStorage, SessionStorage, Storage Events, Quotas, and asynchronous IndexedDB object stores for offline web apps."
  keywords: ["Web Storage", "LocalStorage", "SessionStorage", "IndexedDB", "Storage Event", "Client-side DB", "Offline Web App"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 7.1 Web Storage & IndexedDB

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 1.1 Web Architecture & Protocols](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_01_html5/_01_01_web_architecture_and_protocols.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Compare client-side storage options (Cookies, LocalStorage, SessionStorage, IndexedDB).
2. Execute CRUD operations on `localStorage` and `sessionStorage`.
3. Synchronize state across multiple browser tabs using `storage` events.
4. Perform asynchronous transactional database operations using the **IndexedDB API**.
5. Evaluate storage quota limits, security origins, and data persistence guarantees.

---

## 2. Environment & Prerequisites [id: prerequisites]

Inspect client storage in Chrome DevTools:
- Open DevTools (`F12`) $\rightarrow$ Click **Application** tab $\rightarrow$ Inspect **Local Storage**, **Session Storage**, and **IndexedDB**.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Client Storage Matrix

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CLIENT-SIDE STORAGE MECHANISMS MATRIX                    │
├─────────────────┬──────────────┬──────────────┬──────────────┬──────────────┤
│ Storage Type    │ Quota Size   │ Transmitted  │ Lifespan     │ API Type     │
│                 │              │ on HTTP Req? │              │              │
├─────────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ Cookies         │ ~4 KB        │ YES (Always) │ Expiration   │ Synchronous  │
│ LocalStorage    │ ~5 MB        │ NO           │ Persistent   │ Synchronous  │
│ SessionStorage  │ ~5 MB        │ NO           │ Tab Close    │ Synchronous  │
│ IndexedDB       │ >250 MB+     │ NO           │ Persistent   │ Asynchronous │
└─────────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

### 3.2 LocalStorage & SessionStorage API
- **LocalStorage**: Persists key-value string pairs until explicitly cleared via JS or browser cache deletion.
- **SessionStorage**: Persists key-value string pairs only for the active browser tab session.

```javascript
// Store Data (JSON stringification required for objects)
localStorage.setItem('user_settings', JSON.stringify({ theme: 'dark', rate: 1000 }));

// Retrieve Data
const settings = JSON.parse(localStorage.getItem('user_settings'));

// Remove Item
localStorage.removeItem('user_settings');
```

### 3.3 Storage Event Cross-Tab Sync
When `localStorage` is updated in one tab, other tabs on the same origin receive a `storage` event:

```javascript
window.addEventListener('storage', (event) => {
  console.log(`Key changed: ${event.key} from ${event.oldValue} to ${event.newValue}`);
});
```

### 3.4 IndexedDB Architecture
IndexedDB is a low-level, asynchronous NoSQL database running inside the browser:
- **Object Stores**: Equivalent to database tables storing JS objects.
- **Indexes**: Efficiently query records by property fields.
- **Transactions**: All reads/writes run inside atomic transactions (`readonly`, `readwrite`).

---

## 4. Architecture & Diagram Visualizations [id: diagram]

### IndexedDB Transaction Architecture
```mermaid
flowchart TD
    App[Web Application JS] -->|openDB| IDB[IndexedDB Storage Engine]
    IDB -->|Begin Transaction| TX[Transaction: readwrite]
    TX -->|Access| Store[ObjectStore: 'sensor_logs']
    Store -->|Put Record| Record[Record: {id: 101, temp: 24.5}]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>IndexedDB & Web Storage</title>
</head>
<body>
  <h1>Client Storage Engine</h1>
  <button id="save-btn">Save Telemetry to IndexedDB</button>

  <script>
    // Simple IndexedDB Wrapper
    const request = indexedDB.open('IoT_Database', 1);

    request.onupgradeneeded = (e) => {
      const db = e.target.result;
      if (!db.objectStoreNames.contains('logs')) {
        db.createObjectStore('logs', { keyPath: 'id', autoIncrement: true });
      }
    };

    request.onsuccess = (e) => {
      const db = e.target.result;
      document.getElementById('save-btn').addEventListener('click', () => {
        const tx = db.transaction('logs', 'readwrite');
        const store = tx.objectStore('logs');
        store.add({ timestamp: Date.now(), temp: 24.5, node: 'ESP32' });
        console.log('Record saved to IndexedDB!');
      });
    };
  </script>
</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **IndexedDB**: Powers offline Progressive Web Apps (PWAs) like VS Code for Web, Figma, and offline IoT telemetry loggers.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `storage_demo.html`.
2. Click **Save Telemetry to IndexedDB**.
3. Open DevTools (`F12`) $\rightarrow$ Application $\rightarrow$ IndexedDB $\rightarrow$ Inspect `IoT_Database` records.

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`QuotaExceededError`** | LocalStorage exceeds ~5MB limit. | Migrate large datasets to IndexedDB. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use IndexedDB for Large Datasets**: Exceeds 250MB+ storage.
- **Never Store Passwords**: Never store raw tokens in LocalStorage without encryption.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why is IndexedDB preferred over LocalStorage for offline-first web apps?
**Answer**: LocalStorage is synchronous and limited to ~5MB of string data, blocking the main thread during heavy reads/writes. IndexedDB is asynchronous, non-blocking, transactional, and supports hundreds of megabytes of complex objects and binary blobs.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 7.1 Web Storage & IndexedDB Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the typical storage quota for LocalStorage per origin?",
      "options": ["4 KB", "5 MB", "250 MB", "1 GB"],
      "correct_answer_index": 1,
      "explanation": "LocalStorage is capped at approximately 5 MB per domain origin."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an offline-first telemetry logger using IndexedDB.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What JS method serializes objects before saving to LocalStorage?
**Back**: `JSON.stringify(object)`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
localStorage.setItem('key', 'value');
```
