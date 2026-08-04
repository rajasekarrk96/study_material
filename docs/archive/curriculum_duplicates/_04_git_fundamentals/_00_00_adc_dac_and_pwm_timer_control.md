# Adc Dac And Pwm Timer Control

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 2.1 GPIO & Interrupts](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_03_gpio_digital_io_and_interrupts.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Read analog voltage levels using the 12-bit **Analog-to-Digital Converter (ADC)**.
2. Navigate the hardware conflict between **ADC1** and **ADC2** (Wi-Fi co-existence).
3. Generate hardware Pulse Width Modulation (PWM) signals using the **LEDC peripheral**.
4. Produce true analog voltage outputs using the 8-bit **Digital-to-Analog Converter (DAC)** pins.

---

---

Gather ESP32, 10k Potentiometer, LED, and Jumper Wires.

---

---

### 3.1 12-Bit Analog-to-Digital Conversion (ADC)
The ESP32 features two 12-bit Successive Approximation Register (SAR) ADCs:
- **Resolution**: $2^{12} = 4096$ quantization levels (returns integer values from `0` to `4095`).
- **Input Voltage Range**: Default 0.0V to 3.3V.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ESP32 ADC ARCHITECTURE MATRIX                      │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ ADC Unit        │ Channels & Wi-Fi Co-existence Rules                       │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ **ADC1**        │ 8 Channels (GPIO 32, 33, 34, 35, 36, 39)                  │
│                 │ *Safe to use anytime (Does NOT conflict with Wi-Fi)*      │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ **ADC2**        │ 10 Channels (GPIO 0, 2, 4, 12, 13, 14, 15, 25, 26, 27)    │
│                 │ *RESTRICTED: Cannot be used while Wi-Fi is active!*       │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

### 3.2 Hardware PWM via LEDC Peripheral
ESP32 does not use traditional software PWM. It features 16 independent hardware **LEDC (LED Control)** PWM channels capable of driving LEDs, servos, and motor controllers without CPU intervention:

$$\text{Duty Cycle Voltage} = V_{\text{max}} \times \left( \frac{\text{Duty Value}}{2^{\text{Resolution}} - 1} \right)$$

---

---

```mermaid
flowchart TD
    Pot[Potentiometer Analog Voltage: 0V - 3.3V] --> ADC1["ESP32 ADC1 Channel 6 (GPIO 34)"]
    ADC1 --> RawVal["analogRead(): Returns 0 - 4095"]
    RawVal --> Scale["Map 12-bit ADC (0-4095) to 8-bit PWM (0-255)"]
    Scale --> LEDC["LEDC PWM Timer Channel"]
    LEDC --> LED["Dim LED brightness on GPIO 2"]
```

---

---

```cpp
// ESP32 ADC Reading & LEDC PWM Control (main.cpp)
#include <Arduino.h>

const gpio_num_t POT_PIN = GPIO_NUM_34; // ADC1 Channel 6 (Safe with Wi-Fi!)
const gpio_num_t LED_PIN = GPIO_NUM_2;   // PWM Output Pin

const uint32_t PWM_FREQ = 5000;         // 5 kHz Frequency
const uint8_t PWM_RESOLUTION = 8;       // 8-bit resolution (0 - 255)

void setup() {
  Serial.begin(115200);

  // Configure ADC Pin
  pinMode(POT_PIN, INPUT);

  // Attach LED Pin to LEDC PWM Hardware Engine (Arduino Core 3.0+ API)
  ledcAttach(LED_PIN, PWM_FREQ, PWM_RESOLUTION);

  Serial.println("[ADC & PWM Initialized]: Turn potentiometer connected to GPIO 34.");
}

void loop() {
  // 1. Read 12-bit Raw ADC Value (0 - 4095)
  uint16_t rawAdc = analogRead(POT_PIN);

  // Read calibrated voltage in millivolts (mV)
  uint32_t milliVolts = analogReadMilliVolts(POT_PIN);

  // 2. Map 12-bit ADC (0-4095) to 8-bit PWM Duty Cycle (0-255)
  uint8_t pwmDuty = map(rawAdc, 0, 4095, 0, 255);

  // 3. Write Duty Cycle to LEDC PWM Hardware Engine
  ledcWrite(LED_PIN, pwmDuty);

  Serial.printf("[ADC Raw]: %4u | [Voltage]: %4u mV | [PWM Duty]: %3u/255\n",
                rawAdc, milliVolts, pwmDuty);

  delay(200);
}
```

---

---

- **Smart Lighting & Motor Controllers**: Industrial automation gateways sample 0–10V industrial analog pressure sensors via voltage divider circuits into ADC1 and control high-speed BLDC motor drivers using LEDC PWM timers.

---

---

1. Wire Potentiometer outer pins to 3.3V and GND, center wiper pin to GPIO 34.
2. Upload program via PlatformIO.
3. Open Serial Monitor $\to$ Turn potentiometer knob $\to$ Observe smooth LED dimming and real-time millivolt readout!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`analogRead()` Fails or Returns 0 when Wi-Fi is On** | Reading analog sensors connected to **ADC2** pins (e.g. GPIO 4 or 14) while Wi-Fi is connected. | Connect all analog sensors to **ADC1** pins (GPIO 32, 33, 34, 35, 36, 39). |

---

---

- **Always Use ADC1 for Sensors**: Always map analog sensors to ADC1 channels to avoid Wi-Fi driver channel pre-emption conflicts.

---

---

### Q1: Why should embedded engineers avoid connecting analog sensors to ADC2 pins on the ESP32 in connected IoT applications?
**Answer**: ADC2 is shared internally with the ESP32's 2.4 GHz Wi-Fi transceiver hardware controller. When Wi-Fi is actively sending or receiving packets, the Wi-Fi driver takes priority and locks ADC2, causing `analogRead()` calls on ADC2 pins to return invalid zero values or throw runtime errors. Analog sensors should always be connected to ADC1 (GPIO 32–39).

---

---

```json
{
  "quiz_title": "Lesson 2.2 ADC & PWM Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the native bit resolution of the ESP32 Analog-to-Digital Converter (ADC)?",
      "options": ["8-bit (0-255)", "10-bit (0-1023)", "12-bit (0-4095)", "16-bit"],
      "correct_answer_index": 2,
      "explanation": "ESP32 ADC has 12-bit resolution returning 0-4095."
    }
  ]
}
```

---

---

Read ADC1 channel 6 and write scaled PWM duty cycles to an LED.

---

---

**Front**: Which hardware pins on the ESP32 support 8-bit true Digital-to-Analog (DAC) voltage output?
**Back**: GPIO 25 (DAC1) and GPIO 26 (DAC2).
<!-- flashcard:end -->

---

---

```cpp
uint16_t adc = analogRead(34);
ledcAttach(2, 5000, 8);
ledcWrite(2, 128);
```

---
