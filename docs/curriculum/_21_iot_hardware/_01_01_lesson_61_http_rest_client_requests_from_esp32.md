# Lesson 6.1 HTTP REST Client Requests from ESP32

> **Course**: Iot Hardware | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 5.2 Auto-Reconnect](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_11_non_blocking_wifi_reconnect_and_events.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Issue outbound HTTP GET and POST requests using **`HTTPClient`**.
2. Construct and serialize JSON payloads using the **`ArduinoJson`** library.
3. Parse HTTP status codes (`200 OK`, `201 Created`) and payload strings.
4. Establish secure HTTPS connections using **`WiFiClientSecure`**.

---

---

Include `bblanchon/ArduinoJson @ ^7.0.0` in `platformio.ini`.

---

---

### 3.1 Embedded HTTP Client Architecture
To send sensor data to a backend microservice (such as a Flask or FastAPI server), the ESP32 operates as an **HTTP Client**.

The **`HTTPClient`** library manages socket creation, HTTP request header formatting, Content-Type headers (`application/json`), and response payload parsing:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ESP32 HTTP POST PAYLOAD FLOW                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. `ArduinoJson` serializes C++ struct ──► `{"node_id":"E1","temp":24.5}`   │
│ 2. `HTTPClient.POST(jsonBuffer)`       ──► Sends POST to `/api/v1/telemetry` │
│ 3. Server responds HTTP 201 Created   ──► `http.end()` closes socket        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Sensor[Read Sensor Hardware] --> Serialize["ArduinoJson: doc['temp'] = 24.5"]
    Serialize --> HTTP["HTTPClient.begin(serverUrl)"]
    HTTP --> Send["http.POST(jsonString)"]
    Send --> Server[FastAPI / Flask Backend Server]
    Server --> Response["Server returns HTTP 201 Created"]
    Response --> Close["http.end(): Release Socket"]
```

---

---

```cpp
// ESP32 HTTP REST Client & ArduinoJson Serialization (main.cpp)
#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char *WIFI_SSID = "YOUR_WIFI_SSID";
const char *WIFI_PASS = "YOUR_WIFI_PASSWORD";

// Target REST API Endpoint URL (Replace with your backend IP!)
const char *API_ENDPOINT = "http://192.168.1.100:8000/api/v1/telemetry/ingest";

void sendTelemetryREST(float temperature, float humidity) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("[HTTP Error]: Cannot send REST request — Wi-Fi Disconnected!");
    return;
  }

  // 1. Construct JSON Payload using ArduinoJson 7
  JsonDocument doc;
  doc["node_id"] = "ESP32-NODE-101";
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  doc["timestamp"] = millis();

  String jsonString;
  serializeJson(doc, jsonString);

  // 2. Initialize HTTPClient
  HTTPClient http;
  http.begin(API_ENDPOINT);
  http.addHeader("Content-Type", "application/json");

  Serial.printf("[HTTP POST]: Sending JSON to %s...\n", API_ENDPOINT);
  Serial.printf("  -> Payload: %s\n", jsonString.c_str());

  // 3. Execute HTTP POST Request
  int httpResponseCode = http.POST(jsonString);

  if (httpResponseCode > 0) {
    Serial.printf("[HTTP Success]: Response Code = %d\n", httpResponseCode);
    String responseBody = http.getString();
    Serial.printf("  -> Server Reply: %s\n", responseBody.c_str());
  } else {
    Serial.printf("[HTTP Error]: POST Failed! Error = %s\n",
                  http.errorToString(httpResponseCode).c_str());
  }

  // 4. Always Close Connection Socket!
  http.end();
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n[Wi-Fi Connected!]: Ready for REST requests.");
}

void loop() {
  // Send telemetry every 10 seconds
  sendTelemetryREST(24.8, 58.2);
  delay(10000);
}
```

---

---

- **Cloud Microservice Telemetry Ingestion**: Remote IoT gateways aggregate sensor readings, format structured JSON DTO payloads via `ArduinoJson`, and POST data to cloud REST API endpoints over HTTPS.

---

---

1. Set `platformio.ini` dependency: `lib_deps = bblanchon/ArduinoJson@^7.0.0`.
2. Replace `API_ENDPOINT` with your active FastAPI backend URL.
3. Upload firmware $\to$ Inspect backend server logs receiving the JSON payload!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`http.end()` Omitted / Socket Leak** | Forgetting to call `http.end()` after completing an HTTP request. | Always invoke `http.end()` to release memory and close TCP sockets. |

---

---

- **Use `ArduinoJson 7` `JsonDocument`**: In `ArduinoJson 7`, use `JsonDocument` without hardcoding static memory buffer sizes.

---

---

### Q1: Why is `http.end()` mandatory after executing an HTTP request with `HTTPClient` on the ESP32?
**Answer**: `HTTPClient.begin()` allocates internal memory buffers and opens a TCP network socket connection to the target server. If `http.end()` is omitted, the socket remains open in memory. Calling HTTP requests repeatedly without `http.end()` quickly exhausts ESP32 heap memory and available socket descriptors, causing the microcontroller to crash.

---

---

```json
{
  "quiz_title": "Lesson 6.1 ESP32 HTTP Client Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which library method closes TCP sockets and releases memory after an HTTPClient request?",
      "options": ["http.close()", "http.end()", "http.stop()", "http.disconnect()"],
      "correct_answer_index": 1,
      "explanation": "http.end() closes HTTPClient sockets and frees memory."
    }
  ]
}
```

---

---

Use `ArduinoJson` and `HTTPClient` to POST sensor telemetry to a REST endpoint.

---

---

**Front**: What function in `ArduinoJson 7` serializes a `JsonDocument` object into a C++ `String`?
**Back**: `serializeJson(doc, jsonString)`.
<!-- flashcard:end -->

---

---

```cpp
HTTPClient http;
http.begin("http://api/v1/data");
http.addHeader("Content-Type", "application/json");
int code = http.POST(jsonStr);
http.end();
```

---
