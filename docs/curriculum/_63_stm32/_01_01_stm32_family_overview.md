# STM32 Family Overview

> **Course**: STM32 | **Module**: STM32 Introduction | **Difficulty**: beginner

---

The STM32 family of 32-bit ARM Cortex-M microcontrollers by STMicroelectronics is the industry standard for commercial, industrial, and high-performance embedded IoT products.

---



---

STM32 MCUs span from ultra-low-power 8-pin chips up to dual-core 480MHz ARM Cortex-M7 series. Series hierarchy:
- **STM32F0 / F1 / F4**: Mainstream & High-Performance (Cortex-M0/M3/M4F)
- **STM32L0 / L4 / L5**: Ultra-Low Power (Cortex-M0+/M4/M33 for battery IoT)
- **STM32H7**: High Performance (Cortex-M7 @ 480MHz + M4 dual core)
- **STM32WB / WL**: Integrated Wireless (Bluetooth LE, Zigbee, LoRa)

---

STM32 Part Number Decoding (Example: STM32F401RE):
STM32 : 32-bit ARM Family
F     : Family Type (F = Foundation/High-Perf, L = Low-Power, H = High-Perf, W = Wireless)
401   : Sub-line (401 = Cortex-M4 with FPU @ 84MHz)
R     : Pin Count (R = 64 pins, C = 48 pins, V = 100 pins, Z = 144 pins)
E     : Flash Size (E = 512KB, C = 256KB, G = 1MB)

---

### Python Script to Query STM32 Part Selection Matrix

```python
stm32_matrix = [
    {'part': 'STM32F103C8T6', 'core': 'Cortex-M3', 'clock_mhz': 72, 'flash_kb': 64, 'ram_kb': 20},
    {'part': 'STM32F411CEU6', 'core': 'Cortex-M4F', 'clock_mhz': 100, 'flash_kb': 512, 'ram_kb': 128},
    {'part': 'STM32L432KC',   'core': 'Cortex-M4F', 'clock_mhz': 80, 'flash_kb': 256, 'ram_kb': 64},
]

# Filter parts with hardware FPU and >= 128KB Flash
fpu_parts = [p for p in stm32_matrix if 'M4F' in p['core'] and p['flash_kb'] >= 128]
for p in fpu_parts:
    print(f"{p['part']} ({p['core']} @ {p['clock_mhz']}MHz) - {p['flash_kb']}KB Flash")
```

---

1. **Selecting Non-FPU Chips for Heavy Floating-Point Math**: Cortex-M0/M3 emulate float math in software, taking 100x more clock cycles than Cortex-M4F with hardware FPU.
2. **Counterfeit Chips**: Buying cheap 'Blue Pill' STM32F103 boards often yields fake CS32/CKS32 clones with different flash wait states.
3. **Power Pin Layout Mistakes**: Overlooking VCAP capacitors required for internal core voltage regulators causes boot loops.

---

**Q1: What does FPU stand for in ARM Cortex-M4F?**
A: Floating Point Unit — hardware accelerator for single-precision float operations.

**Q2: What is the famous 'Blue Pill' board?**
A: Low-cost development board featuring the STM32F103C8T6 microcontroller.

**Q3: Which STM32 series is designed specifically for LoRa WAN?**
A: STM32WL series with built-in sub-GHz radio transceiver.

**Q4: What is the difference between ARM Cortex-M3 and Cortex-M4?**
A: Cortex-M4 adds DSP instructions and optional single-cycle hardware FPU.

---



---



---



---



---
