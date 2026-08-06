# 02 03 Lorawan Soil Moisture Agricultural Node

> **Course**: Iot Projects | **Module**: End-to-End IoT Systems | **Difficulty**: advanced

---

In this lesson, you will build and deploy **02 03 Lorawan Soil Moisture Agricultural Node** as a capstone IoT Hardware & Software System.

### End-to-End System Architecture

```
[Sensors / Actuators] -> [ESP32 / Microcontroller] -> [WiFi / BLE / LoRa / Cellular] -> [Cloud / MQTT Broker] -> [Dashboard / Web App]
```

### Complete Firmware Implementation

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "WIFI_SSID";
const char* password = "WIFI_PASSWORD";
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi Connected!");
    client.setServer(mqtt_server, 1883);
}

void loop() {
    if (!client.connected()) {
        client.connect("ESP32Client");
    }
    client.loop();
    client.publish("iot/sensor/telemetry", "{\"status\":\"OK\",\"temp\":24.5}");
    delay(5000);
}
```

---

1. Flashing firmware to an ESP32 dev board, verifying serial monitor output, and viewing live MQTT telemetry on an online dashboard.

---
