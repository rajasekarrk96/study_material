# Wifi Station And Access Point Modes

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 4.2 Semaphores & Mutexes](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_09_freertos_semaphores_mutexes_and_locks.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure ESP32 in **Station (STA) Mode** to connect to local 2.4 GHz Wi-Fi routers.
2. Configure ESP32 as a **Soft Access Point (AP) Mode** hotspot (`WiFi.softAP()`).
3. Combine dual **AP + STA Mode (`WIFI_AP_STA`)** for captive portal device onboarding.
4. Scan and report nearby Wi-Fi networks using **`WiFi.scanNetworks()`**.

---

---

Open PlatformIO in VS Code. Have your 2.4 GHz Wi-Fi SSID and password ready.

---

---

### 3.1 ESP32 Wi-Fi Operating Modes
The ESP32 integrated 802.11 b/g/n Wi-Fi radio supports 3 primary operational modes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ESP32 WI-FI OPERATING MODES                        │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Mode Enum       │ Functionality                    │ Example Use Case       │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ **`WIFI_STA`**  │ Station Mode (Connects to router)│ Cloud MQTT / REST      │
│ **`WIFI_AP`**   │ Soft Access Point (Broadcasts SSID)│ Local Web Configuration│
│ **`WIFI_AP_STA`│ Dual Mode (AP and STA active)   │ Wi-Fi Captive Portal   │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

> [!NOTE]
> **2.4 GHz Network Requirement**: The ESP32 hardware radio operates strictly on 2.4 GHz Wi-Fi bands and cannot connect to 5 GHz-only Wi-Fi networks.

---

---

```mermaid
flowchart TD
    ESP32[ESP32 Microcontroller] -->|WIFI_STA Mode| Router[Local Wi-Fi Router 2.4GHz]
    Router --> Cloud[Internet / Cloud Backend API]
    ESP32 -->|WIFI_AP Mode| Smartphone[User Smartphone: 192.168.4.1 Config Portal]
```

---

---

```cpp
// ESP32 Wi-Fi Station (STA) Mode & Network Scanner (main.cpp)
#include <Arduino.h>
#include <WiFi.h>

const char *WIFI_SSID = "YOUR_WIFI_SSID";
const char *WIFI_PASS = "YOUR_WIFI_PASSWORD";

void scanNearbyNetworks() {
  Serial.println("[Wi-Fi Scanner]: Scanning for 2.4 GHz networks...");
  int networkCount = WiFi.scanNetworks();

  if (networkCount == 0) {
    Serial.println("  -> No Wi-Fi networks found.");
  } else {
    Serial.printf("[Scan Complete]: Found %d networks:\n", networkCount);
    for (int i = 0; i < networkCount; i++) {
      Serial.printf("  %2d: SSID='%s' | RSSI=%d dBm | Encrypt=%s\n",
                    i + 1,
                    WiFi.SSID(i).c_str(),
                    WiFi.RSSI(i),
                    WiFi.encryptionType(i) == WIFI_AUTH_OPEN ? "OPEN" : "SECURE");
    }
  }
  Serial.println("");
}

void connectToWiFiStation() {
  Serial.printf("[Wi-Fi STA]: Connecting to SSID '%s'...\n", WIFI_SSID);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  uint8_t attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\n[Wi-Fi Connected!]: Station Mode Active.");
    Serial.printf("  -> Assigned IP Address: %s\n", WiFi.localIP().toString().c_str());
    Serial.printf("  -> Signal Strength (RSSI): %d dBm\n", WiFi.RSSI());
  } else {
    Serial.println("\n[Wi-Fi Error]: Failed to connect to router.");
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  scanNearbyNetworks();
  connectToWiFiStation();
}

void loop() {
  delay(5000);
}
```

---

---

- **Smart Home Provisioning & Provisioning Portals**: Smart appliances start up in `WIFI_AP_STA` mode, serving a local configuration web page (`192.168.4.1`) to the user's phone to enter home Wi-Fi credentials before switching to `WIFI_STA` mode.

---

---

1. Replace `WIFI_SSID` and `WIFI_PASS` with your 2.4 GHz router credentials.
2. Upload firmware via PlatformIO.
3. Open Serial Monitor $\to$ Observe nearby network scan results and assigned DHCP IP address!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`WL_CONNECT_FAILED` / Times Out** | Attempting to connect to a 5 GHz-only Wi-Fi network SSID. | Ensure the target Wi-Fi router broadcasts a 2.4 GHz band network. |

---

---

- **Set `WiFi.mode(WIFI_STA)` Explicitly**: Always set `WiFi.mode()` before calling `WiFi.begin()` to prevent radio state leakage.

---

---

### Q1: What is the difference between Station (STA) Mode and Access Point (AP) Mode on the ESP32?
**Answer**: In Station (STA) mode, the ESP32 acts as a client connecting to an external Wi-Fi router to obtain an IP address via DHCP and reach the Internet. In Access Point (AP / SoftAP) mode, the ESP32 broadcasts its own Wi-Fi network SSID and acts as a local router/DHCP server (`192.168.4.1`), allowing phones or laptops to connect directly to it.

---

---

```json
{
  "quiz_title": "Lesson 5.1 Wi-Fi Modes Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which ESP32 Wi-Fi mode connects the chip to an external Wi-Fi router as a client?",
      "options": ["WIFI_AP", "WIFI_STA", "WIFI_OFF", "WIFI_MESH"],
      "correct_answer_index": 1,
      "explanation": "WIFI_STA (Station Mode) connects to external routers."
    }
  ]
}
```

---

---

Write a network scanner printing available 2.4 GHz SSIDs and RSSI values.

---

---

**Front**: What function returns the assigned IP address of an ESP32 in Station Mode?
**Back**: `WiFi.localIP().toString()`.
<!-- flashcard:end -->

---

---

```cpp
WiFi.mode(WIFI_STA);
WiFi.begin("SSID", "PASS");
while (WiFi.status() != WL_CONNECTED) delay(500);
```

---
