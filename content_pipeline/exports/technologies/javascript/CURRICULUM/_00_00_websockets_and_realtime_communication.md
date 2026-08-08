# Websockets And Realtime Communication

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 9.3 IndexedDB](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_33_client_side_storage_with_indexeddb.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain the full-duplex, low-latency **WebSocket Protocol** (`wss://`).
2. Trace the HTTP-to-WebSocket **Handshake Upgrade** header negotiation.
3. Manage WebSocket connections using `onopen`, `onmessage`, `onerror`, and `onclose`.
4. Implement **Exponential Backoff Reconnection Strategies** for reliable network telemetry streaming.

---

---

Open Node.js REPL or Browser DevTools Console.

---

---

### 3.1 HTTP Polling vs WebSockets
HTTP is a request-response protocol where the client must initiate every interaction. For real-time applications (IoT telemetry, live chat, financial tickers), HTTP polling introduces massive header overhead and latency.

**WebSockets** initiate via an HTTP upgrade request, establishing a persistent, bi-directional, full-duplex TCP socket connection:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HTTP POLLING VS WEBSOCKETS                         │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Metric          │ HTTP Polling / Long Polling      │ WebSocket (`wss://`)   │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Connection      │ Repeated short-lived HTTP requests│ Single persistent TCP  │
│ Overhead        │ 500+ Bytes per HTTP header       │ 2–10 Bytes per frame   │
│ Direction       │ Half-duplex (Client pulls data)  │ Full-duplex (Bi-dir)   │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Client[Browser Client] -->|GET /ws HTTP/1.1 Upgrade: websocket| Server[WebSocket Server]
    Server -->|HTTP/1.1 101 Switching Protocols| Switch[Bi-directional TCP Socket Opened]
    Switch <-->|Server pushes telemetry frame| Client
    Switch <-->|Client sends command frame| Server
```

---

---

```javascript
// WebSocket Client with Exponential Backoff Reconnection

class ResilientWebSocket {
  #url;
  #socket = null;
  #retryCount = 0;
  #maxRetryDelay = 30000; // 30s Max Delay

  constructor(url) {
    this.#url = url;
    this.connect();
  }

  connect() {
    console.log(`Connecting to WebSocket: ${this.#url}...`);
    this.#socket = new WebSocket(this.#url);

    this.#socket.onopen = () => {
      console.log("[WebSocket Connected] Operational.");
      this.#retryCount = 0; // Reset retry counter on success
    };

    this.#socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("[Telemetry Packet Received]:", data);
    };

    this.#socket.onclose = () => {
      console.warn("[WebSocket Disconnected] Attempting reconnection...");
      this.#reconnect();
    };

    this.#socket.onerror = (error) => {
      console.error("[WebSocket Error]:", error);
    };
  }

  send(data) {
    if (this.#socket?.readyState === WebSocket.OPEN) {
      this.#socket.send(JSON.stringify(data));
    }
  }

  #reconnect() {
    // Exponential Backoff: 1s, 2s, 4s, 8s, 16s... up to max 30s
    const delay = Math.min(1000 * Math.pow(2, this.#retryCount), this.#maxRetryDelay);
    this.#retryCount++;
    console.log(`Reconnecting in ${delay}ms (Attempt #${this.#retryCount})...`);
    setTimeout(() => this.connect(), delay);
  }
}

// Example Execution (Using public echo WebSocket test endpoint)
const client = new ResilientWebSocket("wss://echo.websocket.events");
```

---

---

- **IoT Fleet Live Telemetry**: Industrial dashboards maintaining WebSocket connections to MQTT/WebSocket gateways streaming 1,000 sensor telemetry readings per second.

---

---

1. Open DevTools Console on any site.
2. Run `const ws = new WebSocket('wss://echo.websocket.events'); ws.onmessage = e => console.log(e.data);` $\to$ Inspect live echo frames!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`INVALID_STATE_ERR`** | Calling `.send()` before the WebSocket `onopen` event fires. | Check `if (ws.readyState === WebSocket.OPEN)` before sending data. |

---

---

- **Always Use `wss://`**: Secure WebSocket encrypted over TLS/SSL.

---

---

### Q1: What is Exponential Backoff and why is it essential for WebSocket reconnection strategies?
**Answer**: Exponential Backoff increases the delay time exponentially between consecutive reconnection attempts (e.g. 1s, 2s, 4s, 8s). It prevents "Thundering Herd" server outages, ensuring thousands of disconnected clients do not overwhelm a recovering backend server with simultaneous reconnection requests.

---

---

```json
{
  "quiz_title": "Lesson 9.4 WebSockets Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which readyState value indicates that a WebSocket is open and ready to send data?",
      "options": ["WebSocket.CONNECTING (0)", "WebSocket.OPEN (1)", "WebSocket.CLOSING (2)", "WebSocket.CLOSED (3)"],
      "correct_answer_index": 1,
      "explanation": "WebSocket.OPEN (1) indicates an active open connection."
    }
  ]
}
```

---

---

Build a real-time collaborative chat room using WebSockets and JSON frame encoding.

---

---

**Front**: What HTTP header signals a client request to upgrade to WebSockets?
**Back**: `Upgrade: websocket` (with `Connection: Upgrade`).
<!-- flashcard:end -->

---

---

```javascript
const ws = new WebSocket("wss://server.com");
ws.onmessage = (e) => console.log(JSON.parse(e.data));
```

---
