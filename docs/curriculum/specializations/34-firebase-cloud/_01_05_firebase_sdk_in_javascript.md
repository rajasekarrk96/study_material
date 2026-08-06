# Firebase SDK in JavaScript

> **Course**: Firebase | **Module**: Firebase Introduction | **Difficulty**: beginner

---

Building real-time web dashboards using JavaScript Firebase SDK to monitor and control IoT nodes.

---



---

Web dashboards subscribe to Firebase real-time listeners to update UI gauges instantly when sensor values change.

---

JS Realtime Listener:
onValue(ref(db, 'sensors/temp'), (snapshot) => { updateUI(snapshot.val()); })

---

### Real-Time Web Dashboard Gauge Listener

```javascript
import { getDatabase, ref, onValue } from 'firebase/database';
const db = getDatabase();
onValue(ref(db, 'sensors/temperature'), (snapshot) => {
    document.getElementById('temp-val').innerText = snapshot.val() + ' °C';
});
```

---

Creating duplicate event listeners causing memory leaks in single-page apps.

---

**Q1: How does `onValue()` enable real-time UI updates?**
A: Pushes WebSocket data updates from server to browser automatically without page refreshes.

---



---



---



---



---
