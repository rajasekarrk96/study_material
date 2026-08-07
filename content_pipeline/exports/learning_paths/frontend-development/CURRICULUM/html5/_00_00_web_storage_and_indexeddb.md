# Web Storage And Indexeddb

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

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

---

Inspect client storage in Chrome DevTools:
- Open DevTools (`F12`) $\rightarrow$ Click **Application** tab $\rightarrow$ Inspect **Local Storage**, **Session Storage**, and **IndexedDB**.

---

---

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

---

### IndexedDB Transaction Architecture
```mermaid
flowchart TD
    App[Web Application JS] -->|openDB| IDB[IndexedDB Storage Engine]
    IDB -->|Begin Transaction| TX[Transaction: readwrite]
    TX -->|Access| Store[ObjectStore: 'sensor_logs']
    Store -->|Put Record| Record[Record: {id: 101, temp: 24.5}]
```

---

---

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

---

- **IndexedDB**: Powers offline Progressive Web Apps (PWAs) like VS Code for Web, Figma, and offline IoT telemetry loggers.

---

---

1. Save code as `storage_demo.html`.
2. Click **Save Telemetry to IndexedDB**.
3. Open DevTools (`F12`) $\rightarrow$ Application $\rightarrow$ IndexedDB $\rightarrow$ Inspect `IoT_Database` records.

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`QuotaExceededError`** | LocalStorage exceeds ~5MB limit. | Migrate large datasets to IndexedDB. |

---

---

- **Use IndexedDB for Large Datasets**: Exceeds 250MB+ storage.
- **Never Store Passwords**: Never store raw tokens in LocalStorage without encryption.

---

---

### Q1: Why is IndexedDB preferred over LocalStorage for offline-first web apps?
**Answer**: LocalStorage is synchronous and limited to ~5MB of string data, blocking the main thread during heavy reads/writes. IndexedDB is asynchronous, non-blocking, transactional, and supports hundreds of megabytes of complex objects and binary blobs.

---

---

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

---

Build an offline-first telemetry logger using IndexedDB.

---

---

**Front**: What JS method serializes objects before saving to LocalStorage?
**Back**: `JSON.stringify(object)`
<!-- flashcard:end -->

---

---

```javascript
localStorage.setItem('key', 'value');
```

---
