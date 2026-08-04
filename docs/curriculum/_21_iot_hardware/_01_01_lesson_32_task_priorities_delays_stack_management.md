# Lesson 3.2 Task Priorities, Delays, & Stack Management

> **Course**: Iot Hardware | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 3.1 Task Creation](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_06_iot_hardware/_06_06_freertos_task_creation_and_core_pinning.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure FreeRTOS pre-emptive task priorities (0 = lowest, 24 = highest).
2. Implement precise periodic task scheduling using **`vTaskDelayUntil()`**.
3. Detect stack memory overflow risks using **`uxTaskGetStackHighWaterMark()`**.
4. Control task lifecycles using `vTaskSuspend()`, `vTaskResume()`, and `vTaskDelete()`.

---

---

Open PlatformIO in VS Code.

---

---

### 3.1 Pre-emptive Priority Scheduling
FreeRTOS uses a **Pre-emptive Fixed-Priority Scheduler**. Higher priority tasks instantly pre-empt (pause) lower priority tasks whenever they enter the `Ready` state.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FREERTOS TASK STATE MATRIX                          │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ Task State      │ Description                                               │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ **Running**     │ Currently executing on CPU core                           │
│ **Ready**       │ Prepared to run; waiting for scheduler CPU time           │
│ **Blocked**     │ Waiting for a delay (`vTaskDelay`) or queue event         │
│ **Suspended**   │ Explicitly paused via `vTaskSuspend()`                    │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

### 3.2 `vTaskDelay()` vs `vTaskDelayUntil()`
- **`vTaskDelay(ms)`**: Delays execution for $N$ milliseconds *relative to when the function is called*. Execution drift accumulates over time.
- **`vTaskDelayUntil(&lastWakeTime, ms)`**: Delays execution for an *absolute periodic frequency* (e.g. exactly 100 Hz), guaranteeing zero execution drift regardless of task processing time.

---

---

```mermaid
flowchart TD
    Task[Task Execution Starts] --> Work[Perform Sensor Calculations]
    Work --> StackCheck["uxTaskGetStackHighWaterMark(): Check unused stack bytes"]
    StackCheck --> Delay["vTaskDelayUntil(&lastWakeTime, pdMS_TO_TICKS(100))"]
    Delay --> Sleep[Task Enters Blocked State until exact next tick period]
```

---

---

```cpp
// FreeRTOS Task Priorities, Periodic Delay, & Stack Monitoring (main.cpp)
#include <Arduino.h>

TaskHandle_t TaskHandleHigh = NULL;
TaskHandle_t TaskHandleLow = NULL;

// 1. High-Priority Periodic Task (Runs every 1000ms exactly)
void TaskHighPriorityPeriod(void *pvParameters) {
  TickType_t xLastWakeTime = xTaskGetTickCount();
  const TickType_t xFrequency = pdMS_TO_TICKS(1000);

  for (;;) {
    // Precise periodic delay (Guarantees no drift!)
    vTaskDelayUntil(&xLastWakeTime, xFrequency);

    // Check remaining unused stack memory in words (1 word = 4 bytes)
    UBaseType_t remainingStackWords = uxTaskGetStackHighWaterMark(NULL);
    uint32_t remainingStackBytes = remainingStackWords * sizeof(void*);

    Serial.printf("[HIGH PRIORITY TASK]: Executed Periodic Tick | Remaining Stack: %u Bytes\n", 
                  remainingStackBytes);
  }
}

// 2. Low-Priority Background Task
void TaskLowPriorityBackground(void *pvParameters) {
  for (;;) {
    Serial.println("  -> [LOW PRIORITY TASK]: Idle Processing...");
    vTaskDelay(pdMS_TO_TICKS(2500));
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("[FreeRTOS Stack & Priority Demo Initialized]");

  // High Priority Task (Priority 5)
  xTaskCreatePinnedToCore(
    TaskHighPriorityPeriod,
    "HighPriorityTask",
    2048,               // 2048 bytes stack allocation
    NULL,
    5,                  // High Priority = 5
    &TaskHandleHigh,
    1
  );

  // Low Priority Task (Priority 1)
  xTaskCreatePinnedToCore(
    TaskLowPriorityBackground,
    "LowPriorityTask",
    2048,
    NULL,
    1,                  // Low Priority = 1
    &TaskHandleLow,
    1
  );
}

void loop() {
  vTaskDelete(NULL);
}
```

---

---

- **Flight & Robot Control Loops**: High-precision robotics controllers use `vTaskDelayUntil()` to execute PID motor balance loops at exact 500 Hz intervals without timing jitter.

---

---

1. Save code as `src/main.cpp`.
2. Upload via PlatformIO.
3. Open Serial Monitor $\to$ Observe precise 1000ms high-priority tick executions and unused stack memory reports!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`Stack overflow in task HighPriorityTask` Crash** | Allocating large local array buffers (`char buffer[4000]`) inside a task with only 2048 bytes stack allocation. | Increase stack size in `xTaskCreate` or allocate large arrays dynamically on the heap. |

---

---

- **Use `uxTaskGetStackHighWaterMark()` During Tuning**: Call `uxTaskGetStackHighWaterMark()` to inspect minimum unused stack memory and optimize task stack size allocations.

---

---

### Q1: What is the difference between `vTaskDelay()` and `vTaskDelayUntil()` in FreeRTOS?
**Answer**: `vTaskDelay(ms)` blocks the task for $N$ milliseconds starting from the moment `vTaskDelay` is executed, causing execution time drift if processing time fluctuates. `vTaskDelayUntil(&lastWakeTime, frequency)` calculates the exact absolute tick count for the next execution period, guaranteeing a fixed periodic execution frequency without timing drift.

---

---

```json
{
  "quiz_title": "Lesson 3.2 Stack & Priorities Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which FreeRTOS function queries the minimum amount of unused stack memory remaining for a task since it started running?",
      "options": ["vTaskGetFreeMemory()", "uxTaskGetStackHighWaterMark()", "xTaskGetRemainingStack()", "vTaskStackCheck()"],
      "correct_answer_index": 1,
      "explanation": "uxTaskGetStackHighWaterMark() checks minimum unused stack memory."
    }
  ]
}
```

---

---

Use `vTaskDelayUntil()` to create a 200 Hz periodic task and monitor stack high water mark.

---

---

**Front**: What FreeRTOS function permanently deletes a task and frees its stack memory allocation?
**Back**: `vTaskDelete(taskHandle)`.
<!-- flashcard:end -->

---

---

```cpp
TickType_t last = xTaskGetTickCount();
vTaskDelayUntil(&last, pdMS_TO_TICKS(100));
uint32_t unused = uxTaskGetStackHighWaterMark(NULL);
```

---
