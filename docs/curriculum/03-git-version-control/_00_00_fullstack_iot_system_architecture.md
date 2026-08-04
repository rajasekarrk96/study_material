# Fullstack Iot System Architecture

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 9.2 AsyncWebServer](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_20_espasyncwebserver_and_rest_control.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Map out an enterprise **Full-Stack End-to-End IoT System Architecture**.
2. Connect embedded ESP32 FreeRTOS firmware to an MQTT message broker.
3. Integrate Python FastAPI microservices with MQTT subscriber daemons (`paho-mqtt`).
4. Relay MQTT telemetry to web browser dashboards via WebSockets.

---

---

Ensure Python 3.12, `fastapi`, `uvicorn`, and `paho-mqtt` are installed in your backend environment.

---

---

### 3.1 End-to-End Full-Stack IoT Data Pipeline
A production IoT platform integrates five distinct technical layers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FULL-STACK END-TO-END IOT ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. HARDWARE LAYER: Analog Sensors / GPIO / ADC                              │
│       │                                                                     │
│       ▼                                                                     │
│ 2. EDGE FIRMWARE: ESP32 Dual-Core FreeRTOS (Queues, Mutexes, WiFi)          │
│       │                                                                     │
│       ▼                                                                     │
│ 3. BROKER LAYER: MQTT Message Broker (Mosquitto / EMQX)                     │
│       │                                                                     │
│       ▼                                                                     │
│ 4. BACKEND MICROSERVICE: FastAPI (SQLAlchemy 2.0, Pydantic, paho-mqtt)       │
│       │                                                                     │
│       ▼                                                                     │
│ 5. FRONTEND DASHBOARD: HTML5 / CSS3 / JS (WebSockets Live Telemetry Chart)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    ESP32[ESP32 Edge Device: FreeRTOS + ADC] -->|MQTT Publish| Broker[MQTT Broker: Mosquitto]
    Broker -->|paho-mqtt Subscriber| FastAPI[FastAPI Backend Microservice]
    FastAPI -->|Async Engine| DB[(SQLite / PostgreSQL Database)]
    FastAPI -->|WebSocket ConnectionManager| Dashboard[Browser HTML5 Live Dashboard]
```

---

---

### File: `backend_bridge.py` (FastAPI + MQTT Ingestion Bridge)

```python
# FastAPI Microservice with Background MQTT Bridge (backend_bridge.py)
import json
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import paho.mqtt.client as mqtt

app = FastAPI(title="Full-Stack IoT Gateway API")

# WebSocket ConnectionManager for Web Browsers
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

# MQTT Callback when telemetry message arrives from ESP32
def on_mqtt_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"[MQTT -> FastAPI Bridge]: Topic '{msg.topic}' | Payload: {payload}")
    
    try:
        data = json.loads(payload)
        # Event loop scheduling for async broadcast
        loop = asyncio.get_event_loop()
        if loop.is_running():
            asyncio.run_coroutine_threadsafe(
                manager.broadcast({"event": "TELEMETRY", "data": data}), loop
            )
    except Exception as e:
        print(f"[Bridge Error]: {e}")

# Initialize Paho MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_mqtt_message
mqtt_client.connect("test.mosquitto.org", 1883, 60)
mqtt_client.subscribe("nodes/+/telemetry")
mqtt_client.loop_start() # Start background thread

@app.websocket("/ws/telemetry-stream")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

---

---

- **Smart City Environmental Monitoring**: Metropolitan air quality networks deploy thousands of ESP32 sensor nodes publishing PM2.5 levels over MQTT, which are ingested by FastAPI microservices and streamed live to public municipal web dashboards over WebSockets.

---

---

1. Run FastAPI bridge: `uvicorn backend_bridge:app --reload`.
2. Connect your ESP32 publishing MQTT telemetry to `test.mosquitto.org`.
3. Open browser to `ws://localhost:8000/ws/telemetry-stream` $\to$ Observe live end-to-end telemetry streaming from ESP32 hardware directly into your web dashboard!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`RuntimeError: There is no current event loop`** | Attempting to call async WebSocket broadcast directly from synchronous `paho-mqtt` callback thread. | Use `asyncio.run_coroutine_threadsafe(manager.broadcast(...), loop)` to bridge thread execution safely. |

---

---

- **Bridge Threads Safely**: Always use `asyncio.run_coroutine_threadsafe()` when bridging synchronous MQTT callbacks into async FastAPI WebSocket handlers.

---

---

### Q1: Why is an MQTT message broker placed between embedded ESP32 devices and backend FastAPI microservices in full-stack IoT architectures?
**Answer**: An MQTT broker decouples edge devices from backend microservices. If the backend microservice restarts or undergoes maintenance, edge devices continue publishing messages to the broker without dropping data or failing. Furthermore, multiple backend services (analytics, database loggers, alert engines) can subscribe to the same broker streams independently without increasing load on the edge microcontrollers.

---

---

```json
{
  "quiz_title": "Lesson 10.1 Full-Stack Architecture Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which Python library bridges synchronous MQTT callbacks into an asynchronous asyncio event loop safely?",
      "options": ["asyncio.run_coroutine_threadsafe()", "asyncio.create_task()", "loop.run_until_complete()", "asyncio.sleep()"],
      "correct_answer_index": 0,
      "explanation": "asyncio.run_coroutine_threadsafe() schedules coroutines from external threads."
    }
  ]
}
```

---

---

Build a Python FastAPI backend subscribing to MQTT sensor telemetry and broadcasting via WebSockets.

---

---

**Front**: What Python library connects FastAPI microservices to MQTT brokers?
**Back**: `paho-mqtt`.
<!-- flashcard:end -->

---

---

```python
mqtt_client.on_message = on_msg
mqtt_client.subscribe("nodes/+/telemetry")
asyncio.run_coroutine_threadsafe(broadcast(data), loop)
```

---
