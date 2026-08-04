# STM32CubeIDE Setup

> **Course**: STM32 | **Module**: STM32 Introduction | **Difficulty**: beginner

---

STM32CubeIDE is ST's official Eclipse/GCC-based integrated development environment providing code editing, HAL generation, debugging, and flash programming.

---



---

STM32CubeIDE integrates GCC ARM cross-compiler, GDB debugger, STM32CubeMX graphical pinout/clock configurator, and ST-LINK flash utility into a single free platform.

---

Essential STM32CubeIDE Project Files:
Core/Src/main.c      : User application entry point
Core/Src/stm32f4xx_it.c : Interrupt service routine vector functions
Core/Inc/main.h      : Pin definition macros and global headers
STM32F401RETX_FLASH.ld: Linker script mapping code sections into Flash & RAM
Drivers/STM32F4xx_HAL_Driver: ST Hardware Abstraction Layer library files

---

### Standard Structure of main.c in STM32CubeIDE

```c
/* USER CODE BEGIN Header */
/* USER CODE END Header */
#include "main.h"

/* Private function prototypes */
void SystemClock_Config(void);
static void MX_GPIO_Init(void);

int main(void) {
  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* Configure the system clock */
  SystemClock_Config();

  /* Initialize all configured peripherals */
  MX_GPIO_Init();

  /* Infinite loop */
  while (1) {
    /* USER CODE BEGIN WHILE */
    HAL_GPIO_TogglePin(LD2_GPIO_Port, LD2_Pin);
    HAL_Delay(500);
    /* USER CODE END WHILE */
  }
}
```

---

1. **Writing Custom Code Outside `/* USER CODE BEGIN */` Blocks**: Re-running STM32CubeMX code generation will permanently overwrite and delete any code written outside user tags!
2. **ST-LINK Firmware Out of Date**: Old ST-LINK v2 probe firmware fails to connect to newer STM32CubeIDE versions.
3. **Missing SWD Debug Pins in Pinout**: Disabling PA13/PA14 (SWDIO/SWCLK) pins in CubeMX locks out ST-LINK debugging on the next flash!

---

**Q1: What are `/* USER CODE BEGIN */` comments for?**
A: Designated code zones preserved by STM32CubeMX during peripheral re-generation.

**Q2: What probe is used to debug STM32 microcontrollers?**
A: ST-LINK (v2, v3) or J-Link debugger via Serial Wire Debug (SWD) interface.

**Q3: What pins are required for SWD debugging?**
A: SWDIO (Serial Wire Data), SWCLK (Serial Wire Clock), GND, and optionally SWO (Trace).

---



---



---



---



---
