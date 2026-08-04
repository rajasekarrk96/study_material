# Non Blocking Wifi Reconnect And Events

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 5.1 Wi-Fi Modes](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_10_wifi_station_and_access_point_modes.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Intercept system Wi-Fi state changes asynchronously using **`WiFi.onEvent()`**.
2. Handle network disconnections without blocking FreeRTOS sensor loops.
3. Implement non-blocking **Exponential Backoff Reconnect Logic**.
4. Configure Wi-Fi modem sleep modes (`WiFi.setSleep()`) to optimize battery power.

---

---

Open PlatformIO in VS Code.

---

---

### 3.1 Asynchronous System Wi-Fi Events
Using blocking `while (WiFi.status() != WL_CONNECTED)` loops inside an operational embedded device freezes sensor sampling whenever a Wi-Fi router reboots or drops signal.

**`WiFi.onEvent()`** registers asynchronous callback functions that trigger when system Wi-Fi events occur:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ESP32 SYSTEM WI-FI EVENT MATRIX                       │
├───────────────────────────────────┬─────────────────────────────────────────┤
│ System Event Constant             │ Description & Event Cause               │
├───────────────────────────────────┼─────────────────────────────────────────┤
│ `ARDUINO_EVENT_WIFI_STA_GOT_IP`   │ Connected to router & DHCP IP assigned  │
│ `ARDUINO_EVENT_WIFI_STA_DISCONNECTED`│ Signal lost or router rebooted       │
│ `ARDUINO_EVENT_WIFI_STA_START`    │ Wi-Fi Station hardware subsystem started│
└───────────────────────────────────┴─────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Event[Router Reboots / Disconnects] --> Trigger["WiFi.onEvent: ARDUINO_EVENT_WIFI_STA_DISCONNECTED"]
    Trigger --> Callback[Executes WiFiStationDisconnected Callback]
    Callback --> Backoff[Schedule Non-blocking Reconnect with Exponential Backoff]
    Backoff --> MainLoop[Main loop() & FreeRTOS tasks continue running!]
```

---

---

```cpp
// ESP32 Asynchronous Wi-Fi Events & Auto-Reconnect (main.cpp)
#include <Arduino.h>
#include <WiFi.h>

const char *WIFI_SSID = "YOUR_WIFI_SSID";
const char *WIFI_PASS = "YOUR_WIFI_PASSWORD";

// Reconnect Timing Variables
uint32_t lastReconnectAttempt = 0;
uint32_t reconnectIntervalMs = 2000; // Initial 2-second reconnect backoff
const uint32_t MAX_RECONNECT_INTERVAL_MS = 60000; // Cap at 60s max backoff

// 1. Asynchronous Wi-Fi Event Callback
void WiFiEvent(WiFiEvent_t event) {
  switch (event) {
    case ARDUINO_EVENT_WIFI_STA_GOT_IP:
      Serial.println("\n[Wi-Fi Event]: GOT IP!");
      Serial.printf("  -> Assigned IP: %s\n", WiFi.localIP().toString().c_str());
      reconnectIntervalMs = 2000; // Reset backoff interval on success!
      break;

    case ARDUINO_EVENT_WIFI_STA_DISCONNECTED:
      Serial.println("\n[Wi-Fi Event]: DISCONNECTED from router!");
      break;

    default:
      break;
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  // 2. Register Asynchronous Event Handler BEFORE WiFi.begin()
  WiFi.onEvent(WiFiEvent);

  // Enable Modem Sleep mode for power optimization
  WiFi.setSleep(WIFI_PS_MIN_MODEM);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  Serial.println("[Setup Complete]: Wi-Fi Manager initialized.");
}

void loop() {
  uint32_t currentMillis = millis();

  // 3. Non-blocking Reconnect Loop with Exponential Backoff
  if (WiFi.status() != WL_CONNECTED) {
    if (currentMillis - lastReconnectAttempt >= reconnectIntervalMs) {
      lastReconnectAttempt = currentMillis;
      Serial.printf("[Wi-Fi Auto-Reconnect]: Reconnecting (Backoff: %u ms)...\n", reconnectIntervalMs);
      
      WiFi.disconnect();
      WiFi.reconnect();

      // Exponential Backoff doubling
      reconnectIntervalMs = min(reconnectIntervalMs * 2, MAX_RECONNECT_INTERVAL_MS);
    }
  }

  // 4. Main loop continues executing non-blockingly!
  static uint32_t lastLoopPrint = 0;
  if (currentMillis - lastLoopPrint >= 5000) {
    lastLoopPrint = currentMillis;
    Serial.printf("[Main Loop Running]: Free Heap = %u Bytes | WiFi Status = %s\n",
                  ESP.getFreeHeap(),
                  WiFi.status() == WL_CONNECTED ? "CONNECTED" : "DISCONNECTED");
  }
}
```

---

---

- **Mission-Critical Commercial IoT Gateways**: Remote cellular and Wi-Fi IoT gateways implement non-blocking exponential backoff auto-reconnect logic to prevent network storming when power is restored to a facility after a blackout.

---

---

1. Upload program via PlatformIO.
2. Turn off your Wi-Fi router or hotspot $\to$ Observe non-blocking disconnect log and doubling reconnect backoff intervals!
3. Turn router back on $\to$ Observe automatic reconnection and IP assignment without resetting ESP32!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Network Storming / Rapid Reconnect Loop** | Attempting `WiFi.begin()` 100 times per second without backoff delays when router is down. | Always implement non-blocking exponential backoff intervals (`2s`, `4s`, `8s`, `16s`...). |

---

---

- **Register `WiFi.onEvent()` First**: Always register event handlers before calling `WiFi.begin()`.

---

---

### Q1: What is Exponential Backoff and why is it essential for IoT Wi-Fi reconnect logic?
**Answer**: Exponential backoff is an algorithm that progressively increases the delay between retry attempts (e.g., 2s, 4s, 8s, 16s, up to a max cap like 60s) after a connection failure. In IoT, if a facility loses power and 1,000 ESP32 sensor nodes attempt to reconnect simultaneously every 100ms when power returns, they will crash the router with a Denial-of-Service storm. Exponential backoff spreads out reconnect attempts smoothly.

---

---

```json
{
  "quiz_title": "Lesson 5.2 Wi-Fi Events Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which ESP32 Wi-Fi method registers an asynchronous callback function for network events?",
      "options": ["WiFi.onEvent()", "WiFi.setHandler()", "WiFi.attachCallback()", "WiFi.addEventListener()"],
      "correct_answer_index": 0,
      "explanation": "WiFi.onEvent() registers asynchronous system event handlers."
    }
  ]
}
```

---

---

Implement `WiFi.onEvent()` logging `ARDUINO_EVENT_WIFI_STA_GOT_IP` and non-blocking backoff reconnects.

---

---

**Front**: What Wi-Fi system event constant is triggered when an ESP32 receives an IP address from DHCP?
**Back**: `ARDUINO_EVENT_WIFI_STA_GOT_IP`.
<!-- flashcard:end -->

---

---

```cpp
WiFi.onEvent([](WiFiEvent_t e) {
    if (e == ARDUINO_EVENT_WIFI_STA_GOT_IP) Serial.println(WiFi.localIP());
});
```

---
