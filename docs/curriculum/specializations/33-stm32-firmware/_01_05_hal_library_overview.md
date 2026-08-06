# HAL Library Overview

> **Course**: STM32 | **Module**: STM32 Introduction | **Difficulty**: beginner

---

ST's Hardware Abstraction Layer (HAL) provides standardized API functions (`HAL_GPIO_...`, `HAL_UART_...`, `HAL_SPI_...`) across all STM32 microcontroller families.

---



---

The HAL library abstracts hardware registers behind unified C structure handles (`UART_HandleTypeDef`, `SPI_HandleTypeDef`). HAL functions support three programming models:
1. **Blocking (Polling)**: Function waits until transfer completes (`HAL_UART_Transmit`).
2. **Non-Blocking (Interrupt)**: Function initiates transfer and exits; callback handles completion (`HAL_UART_Transmit_IT`).
3. **Non-Blocking (DMA)**: Hardware transfers data in background without CPU (`HAL_UART_Transmit_DMA`).

---

Common HAL Return Status:
HAL_OK       = 0x00 (Operation completed successfully)
HAL_ERROR    = 0x01 (Parameter or hardware error)
HAL_BUSY     = 0x02 (Peripheral is busy processing another transfer)
HAL_TIMEOUT  = 0x03 (Operation timed out)

Standard API Pattern:
HAL_<PERIPHERAL>_Init(handle_ptr)
HAL_<PERIPHERAL>_Transmit(handle_ptr, data_ptr, size, timeout_ms)
HAL_<PERIPHERAL>_Receive(handle_ptr, data_ptr, size, timeout_ms)

---

### Polling vs Interrupt vs DMA HAL UART Transmission Pattern

```c
uint8_t msg[] = "Hello STM32 IoT\r\n";

// Mode 1: Blocking Polling (CPU waits up to 100ms)
HAL_UART_Transmit(&huart2, msg, sizeof(msg)-1, 100);

// Mode 2: Non-Blocking Interrupt (CPU continues immediately)
HAL_UART_Transmit_IT(&huart2, msg, sizeof(msg)-1);

// Interrupt Completion Callback Callback Function:
void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart) {
    if (huart->Instance == USART2) {
        // Transmission complete!
    }
}
```

---

1. **Calling Blocking HAL Functions inside ISRs**: Calling `HAL_Delay()` or `HAL_UART_Transmit()` with long timeouts inside an interrupt handler deadlocks SysTick.
2. **Re-entering Non-Blocking HAL Functions while BUSY**: Calling `HAL_UART_Transmit_IT()` before the previous transfer finishes returns `HAL_BUSY` and drops data.
3. **HAL Overhead**: High abstraction overhead can slow down ultra-fast microsecond timing loops; switch to LL or direct register access for critical paths.

---

**Q1: Why does `HAL_Delay()` freeze if called inside an interrupt with higher priority than SysTick?**
A: `HAL_Delay()` depends on `uwTick` updated by SysTick ISR. If a higher-priority ISR blocks SysTick, `uwTick` stops incrementing.

**Q2: What is the handle structure (`huart2`, `hspi1`)?**
A: C struct holding configuration parameters, register base address, and state tracking for a specific peripheral instance.

**Q3: How do HAL callbacks work?**
A: Weak functions (`__weak`) in HAL drivers that developers override in `main.c` to handle completion events.

---



---



---



---



---
