# STM32CubeMX

> **Course**: STM32 | **Module**: STM32 Introduction | **Difficulty**: beginner

---

STM32CubeMX is a graphical configuration tool for allocating GPIO pins, configuring clock trees, setting up peripheral drivers, and generating C code initialization.

---



---

STM32CubeMX simplifies STM32 setup by providing a visual chip pinout view. Engineers assign pin functions (GPIO, USART, SPI, I2C, PWM, ADC), resolve pin conflicts, configure DMA channels and NVIC interrupt priorities, and auto-generate C code.

---

STM32CubeMX Workflow Steps:
1. Pinout & Configuration  : Select MCU part & assign pin modes (GPIO_Output, USART1_TX)
2. Clock Configuration     : Enter crystal value (HSE), configure PLL, set SYSCLK
3. Project Manager Settings: Name project, select Toolchain = STM32CubeIDE
4. Code Generation         : Click 'GENERATE CODE' (Ctrl + S)

---

### Configuring GPIO Output in CubeMX and Controlling via HAL Code

Assign PC13 pin as `GPIO_Output` with label `LED_BLUE` in CubeMX.

```c
// Auto-generated main.h macro:
// #define LED_BLUE_Pin GPIO_PIN_13
// #define LED_BLUE_GPIO_Port GPIOC

// User Control Code in main.c:
HAL_GPIO_WritePin(LED_BLUE_GPIO_Port, LED_BLUE_Pin, GPIO_PIN_SET);   // Turn ON
HAL_Delay(250);
HAL_GPIO_WritePin(LED_BLUE_GPIO_Port, LED_BLUE_Pin, GPIO_PIN_RESET); // Turn OFF
```

---

1. **Pin Assignment Conflict**: Attempting to use the same pin for both USART1_TX and SPI1_MOSI simultaneously.
2. **Forgetting to Enable Global Interrupt in NVIC Tab**: Enabling UART or Timer interrupts in code fails if the global interrupt checkbox was not enabled in CubeMX.
3. **Generating Copying All IP Libraries**: Copying full HAL driver repositories bloats project repository size unnecessarily.

---

**Q1: Can STM32CubeMX be launched directly inside STM32CubeIDE?**
A: Yes, double-clicking the `.ioc` project configuration file opens embedded CubeMX directly.

**Q2: What is the difference between Peripheral Drivers HAL vs LL in CubeMX?**
A: HAL (Hardware Abstraction Layer) is high-level and portable; LL (Low-Layer) is lightweight, fast, and close to bare-metal register access.

**Q3: How do you configure a pin as an external interrupt (EXTI) in CubeMX?**
A: Click the pin, select `GPIO_EXTIx`, then enable its line in NVIC tab.

---



---



---



---



---
