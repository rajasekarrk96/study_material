# Gpio Digital Io And Interrupts

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 1.2 Toolchain Setup](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_02_platformio_espidf_toolchain_setup.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure ESP32 GPIO modes (`INPUT`, `OUTPUT`, `INPUT_PULLUP`, `INPUT_PULLDOWN`).
2. Read and write digital signals using `digitalRead()` and `digitalWrite()`.
3. Implement non-blocking hardware event handling using **Interrupt Service Routines (ISR)** via `attachInterrupt()`.
4. Use the **`IRAM_ATTR`** attribute for memory-safe ISR execution.
5. Resolve button contact bounce using software debouncing algorithms.

---

---

Gather ESP32, Push Button, 10k Resistor, LED, and Jumper Wires.

---

---

### 3.1 Polling vs Hardware Interrupts
In embedded systems, detecting external button presses or sensor state changes by constantly checking `digitalRead()` inside `loop()` is called **Polling**. Polling wastes CPU cycles and misses short pulses if the loop is delayed.

An **Interrupt Service Routine (ISR)** is a hardware-triggered function that pauses normal CPU execution instantly when a pin voltage state transition occurs (`RISING`, `FALLING`, `CHANGE`).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HARDWARE INTERRUPT EXECUTION FLOW                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Normal Code Execution (`loop()`) ──► Button Pressed (FALLING Edge)           │
│                                           │                                 │
│                                           ▼                                 │
│ Hardware Interrupts CPU ──► Executes ISR (`IRAM_ATTR handleButtonPress()`)  │
│                          ──► Resumes `loop()` immediately (< 1 microsecond) │
└─────────────────────────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **`IRAM_ATTR` Requirement**: On ESP32, ISR handler functions MUST be prefixed with `IRAM_ATTR` to place their compiled code into internal Instruction RAM (IRAM) rather than external SPI Flash, ensuring safe execution even during flash write operations.

---

---

```mermaid
flowchart TD
    Button[Push Button Pressed: Voltage drops 3.3V -> 0V] --> Pin[GPIO 14 FALLING Edge]
    Pin --> Interrupt[Hardware Interrupt Triggered]
    Interrupt --> ISR["IRAM_ATTR handle_isr(): Increments volatile counter"]
    ISR --> Resume[Resume main loop() execution]
```

---

---

```cpp
// ESP32 GPIO Interrupt & Debouncing (main.cpp)
#include <Arduino.h>

const gpio_num_t BUTTON_PIN = GPIO_NUM_14;
const gpio_num_t LED_PIN = GPIO_NUM_2;

// Volatile variables modified inside ISR functions
volatile uint32_t interruptCount = 0;
volatile uint32_t lastInterruptTime = 0;
const uint32_t DEBOUNCE_DELAY_MS = 200; // Software debounce threshold

// Interrupt Service Routine (Must have IRAM_ATTR!)
void IRAM_ATTR handleButtonInterrupt() {
  uint32_t currentTime = millis();
  // Software Debounce: Ignore spikes occurring within 200ms
  if (currentTime - lastInterruptTime > DEBOUNCE_DELAY_MS) {
    interruptCount++;
    lastInterruptTime = currentTime;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);

  // Configure Internal Pull-Up Resistor for Button Input
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  // Attach Hardware Interrupt to GPIO Pin on FALLING edge (Button Press to GND)
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), handleButtonInterrupt, FALLING);

  Serial.println("[ISR Ready]: Press button connected to GPIO 14.");
}

void loop() {
  static uint32_t lastPrintedCount = 0;

  if (interruptCount != lastPrintedCount) {
    Serial.printf("[Interrupt Event]: Button Pressed! Total Count = %u\n", interruptCount);
    digitalWrite(LED_PIN, !digitalRead(LED_PIN)); // Toggle LED
    lastPrintedCount = interruptCount;
  }

  delay(10);
}
```

---

---

- **High-Speed Pulse Counting**: Electricity meters and water flow sensors use GPIO hardware interrupts to count high-speed turbine pulses accurately without CPU polling lag.

---

---

1. Wire Push Button between GPIO 14 and GND.
2. Upload firmware via PlatformIO.
3. Open Serial Monitor $\to$ Press button $\to$ Observe instant interrupt execution and LED toggling!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`Guru Meditation Error: Core 1 panic'ed`** | Calling heavy operations (`Serial.println()`, `delay()`, `malloc()`) inside an ISR function. | Keep ISR functions extremely short: set a `volatile` flag in the ISR and process heavy logic inside `loop()`. |

---

---

- **Keep ISR Functions Minimal**: Never use `Serial.print()`, `delay()`, or complex memory allocations inside an ISR function.

---

---

### Q1: Why must ESP32 Interrupt Service Routine (ISR) functions be declared with the `IRAM_ATTR` attribute?
**Answer**: By default, code functions reside in external SPI Flash memory, which is cached into RAM. If a hardware interrupt triggers while the SPI Flash controller is busy writing or erasing data, attempting to read the ISR from Flash causes a crash. `IRAM_ATTR` forces the compiler to store the ISR function permanently in fast internal Instruction RAM (IRAM), guaranteeing instant execution.

---

---

```json
{
  "quiz_title": "Lesson 2.1 GPIO Interrupts Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which attribute places an ISR function into internal RAM on the ESP32?",
      "options": ["RAM_FUNC", "IRAM_ATTR", "FAST_ISR", "DRAM_ATTR"],
      "correct_answer_index": 1,
      "explanation": "IRAM_ATTR places ISR functions into Instruction RAM."
    }
  ]
}
```

---

---

Write an ISR function counting button presses on `FALLING` edge with 150ms debouncing.

---

---

**Front**: What keyword must be used on C++ variables modified inside an ISR function and read inside `loop()`?
**Back**: `volatile` (e.g. `volatile uint32_t counter = 0;`).
<!-- flashcard:end -->

---

---

```cpp
void IRAM_ATTR isr() { flag = true; }
attachInterrupt(digitalPinToInterrupt(14), isr, FALLING);
```

---
