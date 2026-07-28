```yaml
schema_version: "2.0"
metadata:
  lesson_id: "IOT-MOD05-LES02"
  course_slug: "course-06-iot-hardware"
  course_title: "Course 6: Embedded Systems, ESP32, FreeRTOS, & Hardware IoT"
  module_slug: "mod-05-wifi-connectivity"
  module_title: "Module 5 - Wi-Fi Networking & Wireless Connectivity"
  lesson_slug: "non-blocking-wifi-reconnect-and-events"
  lesson_title: "Lesson 5.2 Non-Blocking Auto-Reconnect & Wi-Fi Event Handlers"
  sort_order: 502

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "IOT-MOD05-LES01"
  required_skills:
    - "ESP32 Wi-Fi Station Mode Basics"

skills_acquired:
  - "Registering System Wi-Fi Event Handlers (`WiFi.onEvent()`)"
  - "Handling Disconnections (`ARDUINO_EVENT_WIFI_STA_DISCONNECTED`)"
  - "Non-Blocking Exponential Backoff Reconnect Logic"
  - "Wi-Fi Modem Power Saving Modes (`WiFi.setSleep()`)"

dependencies:
  software:
    - "VS Code"
    - "PlatformIO"
  hardware:
    - "ESP32 DevKit v1 Board"

seo_and_social:
  meta_title: "ESP32 Wi-Fi Events: WiFi.onEvent, Auto-Reconnect & Exponential Backoff"
  meta_description: "Master Robust ESP32 Wi-Fi Connections: WiFi.onEvent() event handlers, non-blocking auto-reconnect with exponential backoff, and modem power sleep modes."
  keywords: ["ESP32 WiFi.onEvent", "Wi-Fi Auto-Reconnect", "Exponential Backoff", "WIFI_STA_DISCONNECTED", "ESP32 Power Management"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 5.2 Non-Blocking Auto-Reconnect & Wi-Fi Event Handlers

## 1. Overview & Learning Objectives [id: overview]

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

## 2. Environment & Prerequisites [id: prerequisites]

Open PlatformIO in VS Code.

---

## 3. Theoretical Foundations [id: theory]

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

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Event[Router Reboots / Disconnects] --> Trigger["WiFi.onEvent: ARDUINO_EVENT_WIFI_STA_DISCONNECTED"]
    Trigger --> Callback[Executes WiFiStationDisconnected Callback]
    Callback --> Backoff[Schedule Non-blocking Reconnect with Exponential Backoff]
    Backoff --> MainLoop[Main loop() & FreeRTOS tasks continue running!]
```

---

## 5. Code & Hardware Implementation [id: syntax]

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

## 6. Enterprise Real-World Applications [id: examples]

- **Mission-Critical Commercial IoT Gateways**: Remote cellular and Wi-Fi IoT gateways implement non-blocking exponential backoff auto-reconnect logic to prevent network storming when power is restored to a facility after a blackout.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Upload program via PlatformIO.
2. Turn off your Wi-Fi router or hotspot $\to$ Observe non-blocking disconnect log and doubling reconnect backoff intervals!
3. Turn router back on $\to$ Observe automatic reconnection and IP assignment without resetting ESP32!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Network Storming / Rapid Reconnect Loop** | Attempting `WiFi.begin()` 100 times per second without backoff delays when router is down. | Always implement non-blocking exponential backoff intervals (`2s`, `4s`, `8s`, `16s`...). |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Register `WiFi.onEvent()` First**: Always register event handlers before calling `WiFi.begin()`.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is Exponential Backoff and why is it essential for IoT Wi-Fi reconnect logic?
**Answer**: Exponential backoff is an algorithm that progressively increases the delay between retry attempts (e.g., 2s, 4s, 8s, 16s, up to a max cap like 60s) after a connection failure. In IoT, if a facility loses power and 1,000 ESP32 sensor nodes attempt to reconnect simultaneously every 100ms when power returns, they will crash the router with a Denial-of-Service storm. Exponential backoff spreads out reconnect attempts smoothly.

---

## 11. Self-Assessment Quiz [id: quiz]

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

## 12. Portfolio Assignment & Challenge [id: lab]

Implement `WiFi.onEvent()` logging `ARDUINO_EVENT_WIFI_STA_GOT_IP` and non-blocking backoff reconnects.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What Wi-Fi system event constant is triggered when an ESP32 receives an IP address from DHCP?
**Back**: `ARDUINO_EVENT_WIFI_STA_GOT_IP`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```cpp
WiFi.onEvent([](WiFiEvent_t e) {
    if (e == ARDUINO_EVENT_WIFI_STA_GOT_IP) Serial.println(WiFi.localIP());
});
```
