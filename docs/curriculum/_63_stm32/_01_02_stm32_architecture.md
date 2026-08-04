# STM32 Architecture

> **Course**: STM32 | **Module**: STM32 Introduction | **Difficulty**: beginner

---

The STM32 internal architecture features a high-speed AHB/APB bus matrix, nested vectored interrupt controller (NVIC), flexible clock tree, and memory-mapped peripherals.

---



---

STM32 microcontrollers are built around the 32-bit Harvard architecture ARM Cortex-M core. Key architectural components:
- **Bus Matrix**: Connects CPU, DMA controllers, Flash, SRAM, and AHB/APB peripherals concurrently.
- **NVIC (Nested Vectored Interrupt Controller)**: Low-latency nested interrupt handler with 16 priority levels.
- **Clock Tree**: RCC (Reset and Clock Control) manages HSI (internal RC), HSE (external crystal), and PLL clock multipliers.

---

Memory Map Addresses (ARM Cortex-M Standard):
0x0000_0000 - 0x07FF_FFFF : Flash Memory Aliased Boot Area
0x0800_0000 - 0x0807_FFFF : Internal Flash Memory (Main Code)
0x2000_0000 - 0x2001_C000 : SRAM Memory (Variables & Stack)
0x4000_0000 - 0x4000_7FFF : APB1 Peripherals (TIM2-7, USART2/3, SPI2, I2C1/2)
0x4001_0000 - 0x4001_47FF : APB2 Peripherals (TIM1, USART1, SPI1, ADC1)
0x4002_0000 - 0x4002_3FFF : AHB1 Peripherals (GPIOA-H, RCC, DMA1/2)

---

### Configuring Clock Tree (HSE 8MHz to 72MHz System Clock via PLL)

```c
// C Code HAL Clock Initialization for STM32F103 (72MHz System Clock)
RCC_OscInitTypeDef RCC_OscInitStruct = {0};
RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

// 1. Enable External 8MHz Crystal (HSE)
RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
RCC_OscInitStruct.HSEState = RCC_HSE_ON;
RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9; // 8MHz x 9 = 72MHz
HAL_RCC_OscConfig(&RCC_OscInitStruct);

// 2. Select PLL as System Clock Source
RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK; // 72MHz
HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2);
```

---

1. **Forgetting Flash Wait States**: Increasing SYSCLK to 72MHz without setting 2 Flash Latency Wait States causes memory read corruption and HardFault crashes.
2. **Unenabled Peripheral Bus Clock**: Attempting to read/write peripheral registers (e.g. GPIOA) before enabling its clock in RCC causes immediate bus fault.
3. **APB1 Bus Frequency Limits**: APB1 peripheral bus has lower maximum speed limits (e.g. 36MHz or 42MHz) than APB2 and AHB.

---

**Q1: What is the function of the NVIC in ARM Cortex-M?**
A: Handles hardware interrupts with automatic hardware state saving/restoring and dynamic priority preemption.

**Q2: What is the difference between HSI and HSE clocks?**
A: HSI is High-Speed Internal RC oscillator (~1-2% accuracy); HSE is High-Speed External crystal oscillator (high precision for USB/CAN).

**Q3: What is SysTick?**
A: A 24-bit system timer built into the ARM Cortex-M core used for OS tick generation and `HAL_Delay()`.

**Q4: What is a HardFault Exception?**
A: Top-level error handler triggered by illegal memory access, divide-by-zero, unaligned access, or executing invalid instructions.

---



---



---



---



---
