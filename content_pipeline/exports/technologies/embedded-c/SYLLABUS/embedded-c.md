# Embedded C Programming — Master Syllabus

**Target Role:** Embedded Software Engineer / Firmware Engineer / IoT Systems Developer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 40 Hours  
**Prerequisites:** foundations/c-programming, foundations/electronics-basics  
**Required Courses:** foundations/c-programming, foundations/electronics-basics  
**Optional Courses:** foundations/esp32, technologies/stm32  

---

## Study Flow

### Module 1 — Embedded C Architecture & Memory Model
1. **Embedded Microcontroller Memory Layout** (Flash ROM, SRAM, EEPROM, Stack vs Heap, BSS segment, Data segment)
2. **The `volatile` and `const` Qualifiers** (Hardware register access, preventing compiler optimization, memory-mapped variables)
3. **Pointer Arithmetic for Hardware** (Raw memory addresses, casting integer literals to pointers, alignment constraints)
4. **Linker Scripts & Memory Mapping** (Section placement, startup assembly, vector table allocation)

### Module 2 — Bitwise Manipulation & Register Configuration
1. **Bitwise Operators** (AND, OR, XOR, NOT, Left Shift, Right Shift)
2. **Bitmasking Techniques** (Setting, clearing, toggling, and reading individual bits and multi-bit fields)
3. **C Structures & Bitfields for Peripheral Registers** (Struct overlays, union aliasing for 32-bit registers)
4. **Register Abstraction Header Files** (Defining peripheral base addresses, offset macros, CMSIS-style definitions)

### Module 3 — Memory-Mapped I/O & GPIO Driver Architecture
1. **GPIO Peripheral Architecture** (Input modes: floating, pull-up, pull-down; Output modes: push-pull, open-drain)
2. **Writing Bare-Metal GPIO Drivers** (Direction registers, output data registers, input status registers)
3. **Atomic Register Operations** (Bit-band regions, Set/Reset registers like BSRR)
4. **Debouncing Switch Inputs** (Hardware RC filters vs Software timer debouncing)

### Module 4 — Interrupt Handling & NVIC Mechanics
1. **Interrupt Architecture & Execution Flow** (Polling vs Interrupts, Vector Table, Interrupt Priorities)
2. **Interrupt Service Routines (ISRs)** (Writing clean ISRs, ISR latency, sharing data with main loop via volatile flags)
3. **Nested Vectored Interrupt Controller (NVIC)** (Priority grouping, preemption priorities, subpriorities)
4. **External Interrupts (EXTI)** (Edge detection: rising, falling, dual-edge triggers on GPIO pins)

### Module 5 — Hardware Timers, SysTick & PWM Generation
1. **Timer Counter Architectures** (Prescalers, auto-reload registers, up/down counting)
2. **SysTick System Timer** (Millisecond delay generation, non-blocking software timers)
3. **Pulse Width Modulation (PWM)** (Duty cycle, frequency calculation, motor speed & LED dimming control)
4. **Input Capture & Output Compare** (Measuring pulse width, ultrasonic sensor interfacing, frequency measurement)

### Module 6 — Analog Interfacing & DMA Channels
1. **Analog-to-Digital Conversion (ADC)** (Sampling rate, resolution, reference voltage, single vs continuous conversion)
2. **Sensor Calibration & Fixed-Point Math** (Converting raw ADC counts to physical units without floating-point overhead)
3. **Direct Memory Access (DMA)** (Circular DMA buffers, peripheral-to-memory data transfers with zero CPU overhead)
4. **Digital-to-Analog Conversion (DAC)** (Waveform generation, audio output basics)

### Module 7 — Serial Communication Protocols & Peripheral Drivers
1. **UART Driver Architecture** (Baud rate calculation, circular ring buffers for RX/TX, interrupt-driven UART)
2. **I2C Bus Protocol Driver** (Master/Slave modes, START/STOP conditions, ACK/NACK, reading I2C sensors like MPU6050)
3. **SPI High-Speed Bus Driver** (Clock polarity CPOL/CPHA modes, chip select timing, full-duplex transfers)
4. **Protocol Debugging & Logic Analyzers** (Decoding serial bus packets, diagnosing bus lockups)

### Module 8 — Embedded Software Engineering & State Machines
1. **Finite State Machines (FSM)** (State transition tables, function pointer state machines)
2. **Defensive Programming & Watchdog Timers (WDT)** (Independent watchdog vs Window watchdog, recovery from brownouts)
3. **Low-Power Sleep Modes** (Sleep, Stop, Standby, configuring wakeup sources for battery-powered devices)
4. **Capstone: Production Bare-Metal Environmental Telemetry Node** (Integrated driver project combining GPIO, ADC, I2C, Timers, and Low-Power states)
