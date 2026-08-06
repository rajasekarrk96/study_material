# IoT Full Stack Engineering — Master Syllabus

**Target Role:** IoT Solutions Architect / Full Stack Embedded Developer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 350 Hours  
**Prerequisites:** electronics-basics, c-programming, networking-fundamentals  
**Required Courses:** embedded-c, esp32, mqtt, react, python-backend-engineering  
**Optional Courses:** tinyml, cloud-computing  

---

## 1. Term 1

### 1.1. Electrical Fundamentals

#### 1.1.1. Module 1 — Basic Electrical Theory

1. **Voltage Current and Resistance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Calculating LED Current Draw on a 3.3V Microcontroller
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Ohms Law**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Designing a Pull-Up Resistor for a Digital Sensor Button
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Kirchhoffs Laws**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Solving a Dual-Resistor Branch with KCL & KVL
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Power and Energy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Calculating ESP32 Battery Life on a 2500 mAh LiPo Cell
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
5. **AC vs DC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Calculating Peak Voltage for 230V AC Mains Transformer Conversion
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References

#### 1.1.2. Module 2 — Circuit Components

1. **Resistors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Python Resistor Color Code Decoder
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
2. **Capacitors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Calculating Decoupling Filter Cutoff Frequency
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
3. **Inductors and Coils**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Calculating Back-EMF Voltage from a De-energized Relay Coil
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
4. **Series and Parallel Circuits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Python Solver for Equivalent Series-Parallel Networks
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
5. **Voltage Dividers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Designing a Battery Voltage Monitor Divider for ESP32 (3.3V ADC)
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References

#### 1.1.3. Module 3 — Practical Electrical Skills

1. **Using a Multimeter**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Standard Procedure for Measuring Microcontroller Current Draw
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
2. **Reading Circuit Diagrams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Interpreting a Microcontroller Button Circuit Schematic
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
3. **Breadboard Prototyping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Best Practices Checklist for Breadboard Assembly
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
4. **Safety and ESD**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Setting Up an ESD-Safe Workstation
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References
5. **Power Supply Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Thermal Calculation for AMS1117-3.3 LDO Regulator
    6. Common Mistakes
    7. Q & A
    8. Q & A
    9. Exercise
    10. Quiz
    11. Summary & Cheat Sheet
    12. References

### 1.2. Electronics Basics

#### 1.2.1. Module 1 — Semiconductor Devices

1. **Diodes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Reverse Polarity Protection Circuit using Schottky Diode
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Rectifiers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Sizing Filter Capacitor for 12V DC 1A Power Supply
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Transistors BJT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Designing an NPN BJT (2N2222) Relay Driver Circuit
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **MOSFETs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - High-Side PWM Motor Control with N-Channel Logic-Level MOSFET (IRLZ44N)
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Zener Diodes and Voltage Regulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Designing 3.3V Zener Voltage Clamp for ADC Overvoltage Protection
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 1.2.2. Module 2 — Operational Amplifiers

1. **Op-Amp Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Unity Gain Voltage Follower (Buffer) Circuit
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Inverting and Non-Inverting Amplifier**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Designing Non-Inverting Amplifier for 0-100mV Strain Gauge Sensor
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Comparator**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Over-Temperature Threshold Detector using LM393 Comparator
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Summing Amplifier**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - -Bit R-2R Ladder DAC Summing Stage
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Op-Amp Applications in IoT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Transimpedance Amplifier (TIA) Photodiode Sensor Interface
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 1.2.3. Module 3 — Digital Electronics

1. **Number Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Python Number Base Conversions & Bitwise Operations
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Logic Gates**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Python Bitwise Operations Equivalent to Logic Gates
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Combinational Circuits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Expanding Microcontroller Analog Inputs using CD74HC4067 16-Channel Analog MUX
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Sequential Circuits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Bit-Banging 8-Bit Data to 74HC595 Shift Register
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Digital IC Families**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Logic Level Shifting between 5V Sensor and 3.3V ESP32
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 1.2.4. Module 4 — Practical Electronics

1. **Soldering Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - -Step Through-Hole Soldering Technique
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **PCB Reading and Assembly**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Assembly Order Checklist for Populating PCBA
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Signal Conditioning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Python Simulation of RC Low-Pass Filter on Noisy ADC Data
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **EMI and Noise Reduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - PCB Layout Rules for Low-Noise Analog Design
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Datasheets and Component Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Component Selection Decision Matrix for Battery IoT Node
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

### 1.3. Embedded C

#### 1.3.1. Module 1 — Introduction to Embedded Systems

1. **What Is an Embedded System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: What Is an Embedded System
    2. Core Concept
        - Core Concept: What Is an Embedded System
    3. Syntax
        - Syntax: What Is an Embedded System
    4. Example
        - Example: What Is an Embedded System
    5. Pitfall
        - Pitfall: What Is an Embedded System
    6. Q & A
        - Q & A: What Is an Embedded System
2. **Embedded vs Desktop Programming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Embedded vs Desktop Programming
    2. Core Concept
        - Core Concept: Embedded vs Desktop Programming
    3. Syntax
        - Syntax: Embedded vs Desktop Programming
    4. Example
        - Example: Embedded vs Desktop Programming
    5. Pitfall
        - Pitfall: Embedded vs Desktop Programming
    6. Q & A
        - Q & A: Embedded vs Desktop Programming
3. **Cross-Compilation Toolchain**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Cross-Compilation Toolchain
    2. Core Concept
        - Core Concept: Cross-Compilation Toolchain
    3. Syntax
        - Syntax: Cross-Compilation Toolchain
    4. Example
        - Example: Cross-Compilation Toolchain
    5. Pitfall
        - Pitfall: Cross-Compilation Toolchain
    6. Q & A
        - Q & A: Cross-Compilation Toolchain
4. **Hex File Flashing Process**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Hex File Flashing Process
    2. Core Concept
        - Core Concept: Hex File Flashing Process
    3. Syntax
        - Syntax: Hex File Flashing Process
    4. Example
        - Example: Hex File Flashing Process
    5. Pitfall
        - Pitfall: Hex File Flashing Process
    6. Q & A
        - Q & A: Hex File Flashing Process
5. **Bare-Metal Programming Concept**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Bare-Metal Programming Concept
    2. Core Concept
        - Core Concept: Bare-Metal Programming Concept
    3. Syntax
        - Syntax: Bare-Metal Programming Concept
    4. Example
        - Example: Bare-Metal Programming Concept
    5. Pitfall
        - Pitfall: Bare-Metal Programming Concept
    6. Q & A
        - Q & A: Bare-Metal Programming Concept

#### 1.3.2. Module 2 — Memory Architecture

1. **Harvard vs Von Neumann Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Harvard vs Von Neumann Architecture
    2. Core Concept
        - Core Concept: Harvard vs Von Neumann Architecture
    3. Syntax
        - Syntax: Harvard vs Von Neumann Architecture
    4. Example
        - Example: Harvard vs Von Neumann Architecture
    5. Pitfall
        - Pitfall: Harvard vs Von Neumann Architecture
    6. Q & A
        - Q & A: Harvard vs Von Neumann Architecture
2. **Flash SRAM EEPROM and Registers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Flash SRAM EEPROM and Registers
    2. Core Concept
        - Core Concept: Flash SRAM EEPROM and Registers
    3. Syntax
        - Syntax: Flash SRAM EEPROM and Registers
    4. Example
        - Example: Flash SRAM EEPROM and Registers
    5. Pitfall
        - Pitfall: Flash SRAM EEPROM and Registers
    6. Q & A
        - Q & A: Flash SRAM EEPROM and Registers
3. **Memory-Mapped I/O**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Memory-Mapped I/O
    2. Core Concept
        - Core Concept: Memory-Mapped I/O
    3. Syntax
        - Syntax: Memory-Mapped I/O
    4. Example
        - Example: Memory-Mapped I/O
    5. Pitfall
        - Pitfall: Memory-Mapped I/O
    6. Q & A
        - Q & A: Memory-Mapped I/O
4. **Stack and Heap in Embedded Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Stack and Heap in Embedded Systems
    2. Core Concept
        - Core Concept: Stack and Heap in Embedded Systems
    3. Syntax
        - Syntax: Stack and Heap in Embedded Systems
    4. Example
        - Example: Stack and Heap in Embedded Systems
    5. Pitfall
        - Pitfall: Stack and Heap in Embedded Systems
    6. Q & A
        - Q & A: Stack and Heap in Embedded Systems
5. **Volatile and Const Qualifiers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Volatile and Const Qualifiers
    2. Core Concept
        - Core Concept: Volatile and Const Qualifiers
    3. Syntax
        - Syntax: Volatile and Const Qualifiers
    4. Example
        - Example: Volatile and Const Qualifiers
    5. Pitfall
        - Pitfall: Volatile and Const Qualifiers
    6. Q & A
        - Q & A: Volatile and Const Qualifiers

#### 1.3.3. Module 3 — Bit Manipulation

1. **Bitwise Operators Review**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Bitwise Operators Review
    2. Core Concept
        - Core Concept: Bitwise Operators Review
    3. Syntax
        - Syntax: Bitwise Operators Review
    4. Example
        - Example: Bitwise Operators Review
    5. Pitfall
        - Pitfall: Bitwise Operators Review
    6. Q & A
        - Q & A: Bitwise Operators Review
2. **Setting Clearing and Toggling Bits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Setting Clearing and Toggling Bits
    2. Core Concept
        - Core Concept: Setting Clearing and Toggling Bits
    3. Syntax
        - Syntax: Setting Clearing and Toggling Bits
    4. Example
        - Example: Setting Clearing and Toggling Bits
    5. Pitfall
        - Pitfall: Setting Clearing and Toggling Bits
    6. Q & A
        - Q & A: Setting Clearing and Toggling Bits
3. **Bit Masking Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Bit Masking Techniques
    2. Core Concept
        - Core Concept: Bit Masking Techniques
    3. Syntax
        - Syntax: Bit Masking Techniques
    4. Example
        - Example: Bit Masking Techniques
    5. Pitfall
        - Pitfall: Bit Masking Techniques
    6. Q & A
        - Q & A: Bit Masking Techniques
4. **Register-Level Programming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Register-Level Programming
    2. Core Concept
        - Core Concept: Register-Level Programming
    3. Syntax
        - Syntax: Register-Level Programming
    4. Example
        - Example: Register-Level Programming
    5. Pitfall
        - Pitfall: Register-Level Programming
    6. Q & A
        - Q & A: Register-Level Programming
5. **Practical Bit Manipulation Exercises**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Practical Bit Manipulation Exercises
    2. Core Concept
        - Core Concept: Practical Bit Manipulation Exercises
    3. Syntax
        - Syntax: Practical Bit Manipulation Exercises
    4. Example
        - Example: Practical Bit Manipulation Exercises
    5. Pitfall
        - Pitfall: Practical Bit Manipulation Exercises
    6. Q & A
        - Q & A: Practical Bit Manipulation Exercises

#### 1.3.4. Module 4 — GPIO Programming

1. **GPIO Concept and Registers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: GPIO Concept and Registers
    2. Core Concept
        - Core Concept: GPIO Concept and Registers
    3. Syntax
        - Syntax: GPIO Concept and Registers
    4. Example
        - Example: GPIO Concept and Registers
    5. Pitfall
        - Pitfall: GPIO Concept and Registers
    6. Q & A
        - Q & A: GPIO Concept and Registers
2. **Input and Output Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Input and Output Configuration
    2. Core Concept
        - Core Concept: Input and Output Configuration
    3. Syntax
        - Syntax: Input and Output Configuration
    4. Example
        - Example: Input and Output Configuration
    5. Pitfall
        - Pitfall: Input and Output Configuration
    6. Q & A
        - Q & A: Input and Output Configuration
3. **Pull-Up and Pull-Down Resistors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Pull-Up and Pull-Down Resistors
    2. Core Concept
        - Core Concept: Pull-Up and Pull-Down Resistors
    3. Syntax
        - Syntax: Pull-Up and Pull-Down Resistors
    4. Example
        - Example: Pull-Up and Pull-Down Resistors
    5. Pitfall
        - Pitfall: Pull-Up and Pull-Down Resistors
    6. Q & A
        - Q & A: Pull-Up and Pull-Down Resistors
4. **LED and Button Interfacing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LED and Button Interfacing
    2. Core Concept
        - Core Concept: LED and Button Interfacing
    3. Syntax
        - Syntax: LED and Button Interfacing
    4. Example
        - Example: LED and Button Interfacing
    5. Pitfall
        - Pitfall: LED and Button Interfacing
    6. Q & A
        - Q & A: LED and Button Interfacing
5. **GPIO Debouncing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: GPIO Debouncing
    2. Core Concept
        - Core Concept: GPIO Debouncing
    3. Syntax
        - Syntax: GPIO Debouncing
    4. Example
        - Example: GPIO Debouncing
    5. Pitfall
        - Pitfall: GPIO Debouncing
    6. Q & A
        - Q & A: GPIO Debouncing

#### 1.3.5. Module 5 — Interrupts

1. **Interrupt Concept and ISR**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Interrupt Concept and ISR
    2. Core Concept
        - Core Concept: Interrupt Concept and ISR
    3. Syntax
        - Syntax: Interrupt Concept and ISR
    4. Example
        - Example: Interrupt Concept and ISR
    5. Pitfall
        - Pitfall: Interrupt Concept and ISR
    6. Q & A
        - Q & A: Interrupt Concept and ISR
2. **Interrupt Vector Table**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Interrupt Vector Table
    2. Core Concept
        - Core Concept: Interrupt Vector Table
    3. Syntax
        - Syntax: Interrupt Vector Table
    4. Example
        - Example: Interrupt Vector Table
    5. Pitfall
        - Pitfall: Interrupt Vector Table
    6. Q & A
        - Q & A: Interrupt Vector Table
3. **External Interrupts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: External Interrupts
    2. Core Concept
        - Core Concept: External Interrupts
    3. Syntax
        - Syntax: External Interrupts
    4. Example
        - Example: External Interrupts
    5. Pitfall
        - Pitfall: External Interrupts
    6. Q & A
        - Q & A: External Interrupts
4. **Interrupt Priority and Nesting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Interrupt Priority and Nesting
    2. Core Concept
        - Core Concept: Interrupt Priority and Nesting
    3. Syntax
        - Syntax: Interrupt Priority and Nesting
    4. Example
        - Example: Interrupt Priority and Nesting
    5. Pitfall
        - Pitfall: Interrupt Priority and Nesting
    6. Q & A
        - Q & A: Interrupt Priority and Nesting
5. **Interrupt-Driven Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Interrupt-Driven Design
    2. Core Concept
        - Core Concept: Interrupt-Driven Design
    3. Syntax
        - Syntax: Interrupt-Driven Design
    4. Example
        - Example: Interrupt-Driven Design
    5. Pitfall
        - Pitfall: Interrupt-Driven Design
    6. Q & A
        - Q & A: Interrupt-Driven Design

#### 1.3.6. Module 6 — Timers and Counters

1. **Timer Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Timer Fundamentals
    2. Core Concept
        - Core Concept: Timer Fundamentals
    3. Syntax
        - Syntax: Timer Fundamentals
    4. Example
        - Example: Timer Fundamentals
    5. Pitfall
        - Pitfall: Timer Fundamentals
    6. Q & A
        - Q & A: Timer Fundamentals
2. **Timer Modes Normal CTC PWM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Timer Modes Normal CTC PWM
    2. Core Concept
        - Core Concept: Timer Modes Normal CTC PWM
    3. Syntax
        - Syntax: Timer Modes Normal CTC PWM
    4. Example
        - Example: Timer Modes Normal CTC PWM
    5. Pitfall
        - Pitfall: Timer Modes Normal CTC PWM
    6. Q & A
        - Q & A: Timer Modes Normal CTC PWM
3. **Delay Generation Using Timers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Delay Generation Using Timers
    2. Core Concept
        - Core Concept: Delay Generation Using Timers
    3. Syntax
        - Syntax: Delay Generation Using Timers
    4. Example
        - Example: Delay Generation Using Timers
    5. Pitfall
        - Pitfall: Delay Generation Using Timers
    6. Q & A
        - Q & A: Delay Generation Using Timers
4. **Event Counting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Event Counting
    2. Core Concept
        - Core Concept: Event Counting
    3. Syntax
        - Syntax: Event Counting
    4. Example
        - Example: Event Counting
    5. Pitfall
        - Pitfall: Event Counting
    6. Q & A
        - Q & A: Event Counting
5. **Watchdog Timer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Watchdog Timer
    2. Core Concept
        - Core Concept: Watchdog Timer
    3. Syntax
        - Syntax: Watchdog Timer
    4. Example
        - Example: Watchdog Timer
    5. Pitfall
        - Pitfall: Watchdog Timer
    6. Q & A
        - Q & A: Watchdog Timer

#### 1.3.7. Module 7 — PWM

1. **PWM Concept and Duty Cycle**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: PWM Concept and Duty Cycle
    2. Core Concept
        - Core Concept: PWM Concept and Duty Cycle
    3. Syntax
        - Syntax: PWM Concept and Duty Cycle
    4. Example
        - Example: PWM Concept and Duty Cycle
    5. Pitfall
        - Pitfall: PWM Concept and Duty Cycle
    6. Q & A
        - Q & A: PWM Concept and Duty Cycle
2. **Hardware PWM Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Hardware PWM Generation
    2. Core Concept
        - Core Concept: Hardware PWM Generation
    3. Syntax
        - Syntax: Hardware PWM Generation
    4. Example
        - Example: Hardware PWM Generation
    5. Pitfall
        - Pitfall: Hardware PWM Generation
    6. Q & A
        - Q & A: Hardware PWM Generation
3. **Software PWM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Software PWM
    2. Core Concept
        - Core Concept: Software PWM
    3. Syntax
        - Syntax: Software PWM
    4. Example
        - Example: Software PWM
    5. Pitfall
        - Pitfall: Software PWM
    6. Q & A
        - Q & A: Software PWM
4. **Motor Speed Control with PWM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Motor Speed Control with PWM
    2. Core Concept
        - Core Concept: Motor Speed Control with PWM
    3. Syntax
        - Syntax: Motor Speed Control with PWM
    4. Example
        - Example: Motor Speed Control with PWM
    5. Pitfall
        - Pitfall: Motor Speed Control with PWM
    6. Q & A
        - Q & A: Motor Speed Control with PWM
5. **LED Dimming with PWM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LED Dimming with PWM
    2. Core Concept
        - Core Concept: LED Dimming with PWM
    3. Syntax
        - Syntax: LED Dimming with PWM
    4. Example
        - Example: LED Dimming with PWM
    5. Pitfall
        - Pitfall: LED Dimming with PWM
    6. Q & A
        - Q & A: LED Dimming with PWM

#### 1.3.8. Module 8 — Communication Protocols

1. **UART Protocol in Embedded C**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: UART Protocol in Embedded C
    2. Core Concept
        - Core Concept: UART Protocol in Embedded C
    3. Syntax
        - Syntax: UART Protocol in Embedded C
    4. Example
        - Example: UART Protocol in Embedded C
    5. Pitfall
        - Pitfall: UART Protocol in Embedded C
    6. Q & A
        - Q & A: UART Protocol in Embedded C
2. **SPI Protocol in Embedded C**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: SPI Protocol in Embedded C
    2. Core Concept
        - Core Concept: SPI Protocol in Embedded C
    3. Syntax
        - Syntax: SPI Protocol in Embedded C
    4. Example
        - Example: SPI Protocol in Embedded C
    5. Pitfall
        - Pitfall: SPI Protocol in Embedded C
    6. Q & A
        - Q & A: SPI Protocol in Embedded C
3. **I2C Protocol in Embedded C**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: I2C Protocol in Embedded C
    2. Core Concept
        - Core Concept: I2C Protocol in Embedded C
    3. Syntax
        - Syntax: I2C Protocol in Embedded C
    4. Example
        - Example: I2C Protocol in Embedded C
    5. Pitfall
        - Pitfall: I2C Protocol in Embedded C
    6. Q & A
        - Q & A: I2C Protocol in Embedded C
4. **Protocol Comparison**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Protocol Comparison
    2. Core Concept
        - Core Concept: Protocol Comparison
    3. Syntax
        - Syntax: Protocol Comparison
    4. Example
        - Example: Protocol Comparison
    5. Pitfall
        - Pitfall: Protocol Comparison
    6. Q & A
        - Q & A: Protocol Comparison
5. **Debugging with UART Serial**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Debugging with UART Serial
    2. Core Concept
        - Core Concept: Debugging with UART Serial
    3. Syntax
        - Syntax: Debugging with UART Serial
    4. Example
        - Example: Debugging with UART Serial
    5. Pitfall
        - Pitfall: Debugging with UART Serial
    6. Q & A
        - Q & A: Debugging with UART Serial

#### 1.3.9. Module 9 — ADC and DAC

1. **ADC Fundamentals Resolution and Sampling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ADC Fundamentals Resolution and Sampling
    2. Core Concept
        - Core Concept: ADC Fundamentals Resolution and Sampling
    3. Syntax
        - Syntax: ADC Fundamentals Resolution and Sampling
    4. Example
        - Example: ADC Fundamentals Resolution and Sampling
    5. Pitfall
        - Pitfall: ADC Fundamentals Resolution and Sampling
    6. Q & A
        - Q & A: ADC Fundamentals Resolution and Sampling
2. **Reading Analog Sensors with ADC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Reading Analog Sensors with ADC
    2. Core Concept
        - Core Concept: Reading Analog Sensors with ADC
    3. Syntax
        - Syntax: Reading Analog Sensors with ADC
    4. Example
        - Example: Reading Analog Sensors with ADC
    5. Pitfall
        - Pitfall: Reading Analog Sensors with ADC
    6. Q & A
        - Q & A: Reading Analog Sensors with ADC
3. **DAC Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DAC Fundamentals
    2. Core Concept
        - Core Concept: DAC Fundamentals
    3. Syntax
        - Syntax: DAC Fundamentals
    4. Example
        - Example: DAC Fundamentals
    5. Pitfall
        - Pitfall: DAC Fundamentals
    6. Q & A
        - Q & A: DAC Fundamentals
4. **ADC and DAC in Embedded C**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ADC and DAC in Embedded C
    2. Core Concept
        - Core Concept: ADC and DAC in Embedded C
    3. Syntax
        - Syntax: ADC and DAC in Embedded C
    4. Example
        - Example: ADC and DAC in Embedded C
    5. Pitfall
        - Pitfall: ADC and DAC in Embedded C
    6. Q & A
        - Q & A: ADC and DAC in Embedded C
5. **Signal Conditioning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Signal Conditioning
    2. Core Concept
        - Core Concept: Signal Conditioning
    3. Syntax
        - Syntax: Signal Conditioning
    4. Example
        - Example: Signal Conditioning
    5. Pitfall
        - Pitfall: Signal Conditioning
    6. Q & A
        - Q & A: Signal Conditioning

#### 1.3.10. Module 10 — Embedded C Patterns

1. **State Machines in Embedded C**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: State Machines in Embedded C
    2. Core Concept
        - Core Concept: State Machines in Embedded C
    3. Syntax
        - Syntax: State Machines in Embedded C
    4. Example
        - Example: State Machines in Embedded C
    5. Pitfall
        - Pitfall: State Machines in Embedded C
    6. Q & A
        - Q & A: State Machines in Embedded C
2. **Circular Buffers and Ring Buffers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Circular Buffers and Ring Buffers
    2. Core Concept
        - Core Concept: Circular Buffers and Ring Buffers
    3. Syntax
        - Syntax: Circular Buffers and Ring Buffers
    4. Example
        - Example: Circular Buffers and Ring Buffers
    5. Pitfall
        - Pitfall: Circular Buffers and Ring Buffers
    6. Q & A
        - Q & A: Circular Buffers and Ring Buffers
3. **Callback Functions in C**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Callback Functions in C
    2. Core Concept
        - Core Concept: Callback Functions in C
    3. Syntax
        - Syntax: Callback Functions in C
    4. Example
        - Example: Callback Functions in C
    5. Pitfall
        - Pitfall: Callback Functions in C
    6. Q & A
        - Q & A: Callback Functions in C
4. **Driver Abstraction Layers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Driver Abstraction Layers
    2. Core Concept
        - Core Concept: Driver Abstraction Layers
    3. Syntax
        - Syntax: Driver Abstraction Layers
    4. Example
        - Example: Driver Abstraction Layers
    5. Pitfall
        - Pitfall: Driver Abstraction Layers
    6. Q & A
        - Q & A: Driver Abstraction Layers
5. **HAL Hardware Abstraction Layer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: HAL Hardware Abstraction Layer
    2. Core Concept
        - Core Concept: HAL Hardware Abstraction Layer
    3. Syntax
        - Syntax: HAL Hardware Abstraction Layer
    4. Example
        - Example: HAL Hardware Abstraction Layer
    5. Pitfall
        - Pitfall: HAL Hardware Abstraction Layer
    6. Q & A
        - Q & A: HAL Hardware Abstraction Layer

#### 1.3.11. Module 11 — Real-Time Concepts

1. **What Is an RTOS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: What Is an RTOS
    2. Core Concept
        - Core Concept: What Is an RTOS
    3. Syntax
        - Syntax: What Is an RTOS
    4. Example
        - Example: What Is an RTOS
    5. Pitfall
        - Pitfall: What Is an RTOS
    6. Q & A
        - Q & A: What Is an RTOS
2. **Tasks Scheduling and Priority**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Tasks Scheduling and Priority
    2. Core Concept
        - Core Concept: Tasks Scheduling and Priority
    3. Syntax
        - Syntax: Tasks Scheduling and Priority
    4. Example
        - Example: Tasks Scheduling and Priority
    5. Pitfall
        - Pitfall: Tasks Scheduling and Priority
    6. Q & A
        - Q & A: Tasks Scheduling and Priority
3. **Semaphores and Mutexes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Semaphores and Mutexes
    2. Core Concept
        - Core Concept: Semaphores and Mutexes
    3. Syntax
        - Syntax: Semaphores and Mutexes
    4. Example
        - Example: Semaphores and Mutexes
    5. Pitfall
        - Pitfall: Semaphores and Mutexes
    6. Q & A
        - Q & A: Semaphores and Mutexes
4. **Queues and Event Groups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Queues and Event Groups
    2. Core Concept
        - Core Concept: Queues and Event Groups
    3. Syntax
        - Syntax: Queues and Event Groups
    4. Example
        - Example: Queues and Event Groups
    5. Pitfall
        - Pitfall: Queues and Event Groups
    6. Q & A
        - Q & A: Queues and Event Groups
5. **FreeRTOS Introduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: FreeRTOS Introduction
    2. Core Concept
        - Core Concept: FreeRTOS Introduction
    3. Syntax
        - Syntax: FreeRTOS Introduction
    4. Example
        - Example: FreeRTOS Introduction
    5. Pitfall
        - Pitfall: FreeRTOS Introduction
    6. Q & A
        - Q & A: FreeRTOS Introduction

#### 1.3.12. Module 12 — Embedded C Projects

1. **Digital Clock Project**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Digital Clock Project
    2. Core Concept
        - Core Concept: Digital Clock Project
    3. Syntax
        - Syntax: Digital Clock Project
    4. Example
        - Example: Digital Clock Project
    5. Pitfall
        - Pitfall: Digital Clock Project
    6. Q & A
        - Q & A: Digital Clock Project
2. **Temperature Display System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Temperature Display System
    2. Core Concept
        - Core Concept: Temperature Display System
    3. Syntax
        - Syntax: Temperature Display System
    4. Example
        - Example: Temperature Display System
    5. Pitfall
        - Pitfall: Temperature Display System
    6. Q & A
        - Q & A: Temperature Display System
3. **Motor Control System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Motor Control System
    2. Core Concept
        - Core Concept: Motor Control System
    3. Syntax
        - Syntax: Motor Control System
    4. Example
        - Example: Motor Control System
    5. Pitfall
        - Pitfall: Motor Control System
    6. Q & A
        - Q & A: Motor Control System
4. **UART Command Interface**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: UART Command Interface
    2. Core Concept
        - Core Concept: UART Command Interface
    3. Syntax
        - Syntax: UART Command Interface
    4. Example
        - Example: UART Command Interface
    5. Pitfall
        - Pitfall: UART Command Interface
    6. Q & A
        - Q & A: UART Command Interface
5. **Sensor Data Logger**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Sensor Data Logger
    2. Core Concept
        - Core Concept: Sensor Data Logger
    3. Syntax
        - Syntax: Sensor Data Logger
    4. Example
        - Example: Sensor Data Logger
    5. Pitfall
        - Pitfall: Sensor Data Logger
    6. Q & A
        - Q & A: Sensor Data Logger

### 1.4. Simulation (Proteus / Wokwi)

#### 1.4.1. Module 1 — Simulation Workflow Foundations

1. **Purpose and Limitations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Simulation versus breadboard and production hardware
    2. Models, assumptions, tolerances, and idealized behavior
    3. Select Proteus or Wokwi based on circuit and firmware needs
2. **Project Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Create a schematic or virtual wiring project
    2. Select boards, components, libraries, and power rails
    3. Build, load, and execute firmware
3. **Measurement Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Virtual oscilloscope, logic analyzer, serial monitor, and probes
    2. Voltage, current, timing, and protocol observation
    3. Lab: verify a digital-output and serial program

#### 1.4.2. Module 2 — Digital and Analog Circuit Simulation

1. **Digital Inputs and Outputs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Buttons, pull resistors, debouncing, LEDs, and logic levels
    2. Interrupt-driven input
    3. Faults caused by floating or conflicting signals
2. **Analog Inputs and PWM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Potentiometers and analog sensors
    2. ADC scaling, reference voltage, and quantization
    3. PWM-based brightness and speed control
3. **Circuit Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Simulate a sensor-controlled output
    2. Measure response and timing
    3. Inject wiring and component faults and diagnose them

#### 1.4.3. Module 3 — Microcontrollers, Sensors, and Actuators

1. **Controller Platforms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Arduino-class and ESP32-class board simulation
    2. GPIO capabilities, pin constraints, and peripheral mapping
    3. Timers, interrupts, and serial logging
2. **Sensor Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Temperature, humidity, distance, light, and motion sensors
    2. Digital and analog interface patterns
    3. Create realistic test inputs and boundary cases
3. **Actuator Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Relays, buzzers, displays, servos, and motors
    2. Driver and flyback-protection concepts
    3. Lab: simulate an automated monitoring-and-control node

#### 1.4.4. Module 4 — Communication Protocols and Debugging

1. **Serial Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. UART, I2C, and SPI wiring and timing
    2. Addressing, chip select, baud rate, and bus contention
    3. Decode frames with virtual instruments
2. **Networked Simulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Wi-Fi setup in Wokwi-supported boards
    2. HTTP and MQTT test workflows
    3. Connect simulated firmware to a local or test service
3. **Systematic Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Compile, startup, wiring, timing, and logic failures
    2. Break problems into power, signal, firmware, and protocol layers
    3. Lab: diagnose a deliberately broken multi-device project

#### 1.4.5. Module 5 — Validation and Capstone

1. **Test Planning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Nominal, boundary, fault, and recovery cases
    2. Expected results and pass/fail criteria
    3. Automate repeatable input scenarios where supported
2. **From Simulation to Hardware**
    - **Course Coverage:** 🟢 Covered in Class
    1. Check voltage, current, pin, timing, and library assumptions
    2. Identify components that require physical validation
    3. Prepare schematic, wiring, BOM, and bring-up checklist
3. **Capstone: Simulated IoT Controller**
    - **Course Coverage:** 🟢 Covered in Class
    1. Integrate sensors, display or actuator, and communication
    2. Demonstrate telemetry, commands, alarms, and fault recovery
    3. Submit project files, firmware, test evidence, and limitations

### 1.5. Sensors & Actuators

#### 1.5.1. Module 1 — Sensor Fundamentals

1. **What Is a Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: What Is a Sensor
    2. Core Concept
        - Core Concept: What Is a Sensor
    3. Syntax
        - Syntax: What Is a Sensor
    4. Example
        - Example: What Is a Sensor
    5. Pitfall
        - Pitfall: What Is a Sensor
    6. Q & A
        - Q & A: What Is a Sensor
2. **Sensor Parameters Range Resolution Accuracy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Sensor Parameters Range Resolution Accuracy
    2. Core Concept
        - Core Concept: Sensor Parameters Range Resolution Accuracy
    3. Syntax
        - Syntax: Sensor Parameters Range Resolution Accuracy
    4. Example
        - Example: Sensor Parameters Range Resolution Accuracy
    5. Pitfall
        - Pitfall: Sensor Parameters Range Resolution Accuracy
    6. Q & A
        - Q & A: Sensor Parameters Range Resolution Accuracy
3. **Analog vs Digital Sensors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Analog vs Digital Sensors
    2. Core Concept
        - Core Concept: Analog vs Digital Sensors
    3. Syntax
        - Syntax: Analog vs Digital Sensors
    4. Example
        - Example: Analog vs Digital Sensors
    5. Pitfall
        - Pitfall: Analog vs Digital Sensors
    6. Q & A
        - Q & A: Analog vs Digital Sensors
4. **Sensor Interfacing Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Sensor Interfacing Methods
    2. Core Concept
        - Core Concept: Sensor Interfacing Methods
    3. Syntax
        - Syntax: Sensor Interfacing Methods
    4. Example
        - Example: Sensor Interfacing Methods
    5. Pitfall
        - Pitfall: Sensor Interfacing Methods
    6. Q & A
        - Q & A: Sensor Interfacing Methods
5. **Sensor Selection Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Sensor Selection Guide
    2. Core Concept
        - Core Concept: Sensor Selection Guide
    3. Syntax
        - Syntax: Sensor Selection Guide
    4. Example
        - Example: Sensor Selection Guide
    5. Pitfall
        - Pitfall: Sensor Selection Guide
    6. Q & A
        - Q & A: Sensor Selection Guide

#### 1.5.2. Module 2 — Environmental Sensors

1. **DHT11 DHT22 Temperature and Humidity**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DHT11 DHT22 Temperature and Humidity
    2. Core Concept
        - Core Concept: DHT11 DHT22 Temperature and Humidity
    3. Syntax
        - Syntax: DHT11 DHT22 Temperature and Humidity
    4. Example
        - Example: DHT11 DHT22 Temperature and Humidity
    5. Pitfall
        - Pitfall: DHT11 DHT22 Temperature and Humidity
    6. Q & A
        - Q & A: DHT11 DHT22 Temperature and Humidity
2. **BME280 Pressure Humidity Temperature**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BME280 Pressure Humidity Temperature
    2. Core Concept
        - Core Concept: BME280 Pressure Humidity Temperature
    3. Syntax
        - Syntax: BME280 Pressure Humidity Temperature
    4. Example
        - Example: BME280 Pressure Humidity Temperature
    5. Pitfall
        - Pitfall: BME280 Pressure Humidity Temperature
    6. Q & A
        - Q & A: BME280 Pressure Humidity Temperature
3. **DS18B20 Waterproof Temperature Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DS18B20 Waterproof Temperature Sensor
    2. Core Concept
        - Core Concept: DS18B20 Waterproof Temperature Sensor
    3. Syntax
        - Syntax: DS18B20 Waterproof Temperature Sensor
    4. Example
        - Example: DS18B20 Waterproof Temperature Sensor
    5. Pitfall
        - Pitfall: DS18B20 Waterproof Temperature Sensor
    6. Q & A
        - Q & A: DS18B20 Waterproof Temperature Sensor
4. **LDR Light Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LDR Light Sensor
    2. Core Concept
        - Core Concept: LDR Light Sensor
    3. Syntax
        - Syntax: LDR Light Sensor
    4. Example
        - Example: LDR Light Sensor
    5. Pitfall
        - Pitfall: LDR Light Sensor
    6. Q & A
        - Q & A: LDR Light Sensor
5. **MQ Series Gas Sensors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQ Series Gas Sensors
    2. Core Concept
        - Core Concept: MQ Series Gas Sensors
    3. Syntax
        - Syntax: MQ Series Gas Sensors
    4. Example
        - Example: MQ Series Gas Sensors
    5. Pitfall
        - Pitfall: MQ Series Gas Sensors
    6. Q & A
        - Q & A: MQ Series Gas Sensors

#### 1.5.3. Module 3 — Motion Sensors

1. **PIR Motion Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: PIR Motion Sensor
    2. Core Concept
        - Core Concept: PIR Motion Sensor
    3. Syntax
        - Syntax: PIR Motion Sensor
    4. Example
        - Example: PIR Motion Sensor
    5. Pitfall
        - Pitfall: PIR Motion Sensor
    6. Q & A
        - Q & A: PIR Motion Sensor
2. **Ultrasonic HC-SR04**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Ultrasonic HC-SR04
    2. Core Concept
        - Core Concept: Ultrasonic HC-SR04
    3. Syntax
        - Syntax: Ultrasonic HC-SR04
    4. Example
        - Example: Ultrasonic HC-SR04
    5. Pitfall
        - Pitfall: Ultrasonic HC-SR04
    6. Q & A
        - Q & A: Ultrasonic HC-SR04
3. **IR Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: IR Sensor
    2. Core Concept
        - Core Concept: IR Sensor
    3. Syntax
        - Syntax: IR Sensor
    4. Example
        - Example: IR Sensor
    5. Pitfall
        - Pitfall: IR Sensor
    6. Q & A
        - Q & A: IR Sensor
4. **MPU6050 Accelerometer and Gyroscope**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MPU6050 Accelerometer and Gyroscope
    2. Core Concept
        - Core Concept: MPU6050 Accelerometer and Gyroscope
    3. Syntax
        - Syntax: MPU6050 Accelerometer and Gyroscope
    4. Example
        - Example: MPU6050 Accelerometer and Gyroscope
    5. Pitfall
        - Pitfall: MPU6050 Accelerometer and Gyroscope
    6. Q & A
        - Q & A: MPU6050 Accelerometer and Gyroscope
5. **Vibration Sensor SW-420**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Vibration Sensor SW-420
    2. Core Concept
        - Core Concept: Vibration Sensor SW-420
    3. Syntax
        - Syntax: Vibration Sensor SW-420
    4. Example
        - Example: Vibration Sensor SW-420
    5. Pitfall
        - Pitfall: Vibration Sensor SW-420
    6. Q & A
        - Q & A: Vibration Sensor SW-420

#### 1.5.4. Module 4 — Industrial and Special Sensors

1. **Flow Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Flow Sensor
    2. Core Concept
        - Core Concept: Flow Sensor
    3. Syntax
        - Syntax: Flow Sensor
    4. Example
        - Example: Flow Sensor
    5. Pitfall
        - Pitfall: Flow Sensor
    6. Q & A
        - Q & A: Flow Sensor
2. **Pressure Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Pressure Sensor
    2. Core Concept
        - Core Concept: Pressure Sensor
    3. Syntax
        - Syntax: Pressure Sensor
    4. Example
        - Example: Pressure Sensor
    5. Pitfall
        - Pitfall: Pressure Sensor
    6. Q & A
        - Q & A: Pressure Sensor
3. **Current Sensor ACS712**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Current Sensor ACS712
    2. Core Concept
        - Core Concept: Current Sensor ACS712
    3. Syntax
        - Syntax: Current Sensor ACS712
    4. Example
        - Example: Current Sensor ACS712
    5. Pitfall
        - Pitfall: Current Sensor ACS712
    6. Q & A
        - Q & A: Current Sensor ACS712
4. **Hall Effect Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Hall Effect Sensor
    2. Core Concept
        - Core Concept: Hall Effect Sensor
    3. Syntax
        - Syntax: Hall Effect Sensor
    4. Example
        - Example: Hall Effect Sensor
    5. Pitfall
        - Pitfall: Hall Effect Sensor
    6. Q & A
        - Q & A: Hall Effect Sensor
5. **Load Cell and HX711**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Load Cell and HX711
    2. Core Concept
        - Core Concept: Load Cell and HX711
    3. Syntax
        - Syntax: Load Cell and HX711
    4. Example
        - Example: Load Cell and HX711
    5. Pitfall
        - Pitfall: Load Cell and HX711
    6. Q & A
        - Q & A: Load Cell and HX711

#### 1.5.5. Module 5 — Connectivity Modules

1. **GPS Module NEO-6M**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: GPS Module NEO-6M
    2. Core Concept
        - Core Concept: GPS Module NEO-6M
    3. Syntax
        - Syntax: GPS Module NEO-6M
    4. Example
        - Example: GPS Module NEO-6M
    5. Pitfall
        - Pitfall: GPS Module NEO-6M
    6. Q & A
        - Q & A: GPS Module NEO-6M
2. **GSM Module SIM800L**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: GSM Module SIM800L
    2. Core Concept
        - Core Concept: GSM Module SIM800L
    3. Syntax
        - Syntax: GSM Module SIM800L
    4. Example
        - Example: GSM Module SIM800L
    5. Pitfall
        - Pitfall: GSM Module SIM800L
    6. Q & A
        - Q & A: GSM Module SIM800L
3. **RFID RC522**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: RFID RC522
    2. Core Concept
        - Core Concept: RFID RC522
    3. Syntax
        - Syntax: RFID RC522
    4. Example
        - Example: RFID RC522
    5. Pitfall
        - Pitfall: RFID RC522
    6. Q & A
        - Q & A: RFID RC522
4. **NFC Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: NFC Module
    2. Core Concept
        - Core Concept: NFC Module
    3. Syntax
        - Syntax: NFC Module
    4. Example
        - Example: NFC Module
    5. Pitfall
        - Pitfall: NFC Module
    6. Q & A
        - Q & A: NFC Module
5. **Fingerprint Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Fingerprint Sensor
    2. Core Concept
        - Core Concept: Fingerprint Sensor
    3. Syntax
        - Syntax: Fingerprint Sensor
    4. Example
        - Example: Fingerprint Sensor
    5. Pitfall
        - Pitfall: Fingerprint Sensor
    6. Q & A
        - Q & A: Fingerprint Sensor

#### 1.5.6. Module 6 — Actuators

1. **Relay Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Relay Module
    2. Core Concept
        - Core Concept: Relay Module
    3. Syntax
        - Syntax: Relay Module
    4. Example
        - Example: Relay Module
    5. Pitfall
        - Pitfall: Relay Module
    6. Q & A
        - Q & A: Relay Module
2. **Servo Motor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Servo Motor
    2. Core Concept
        - Core Concept: Servo Motor
    3. Syntax
        - Syntax: Servo Motor
    4. Example
        - Example: Servo Motor
    5. Pitfall
        - Pitfall: Servo Motor
    6. Q & A
        - Q & A: Servo Motor
3. **Stepper Motor A4988**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Stepper Motor A4988
    2. Core Concept
        - Core Concept: Stepper Motor A4988
    3. Syntax
        - Syntax: Stepper Motor A4988
    4. Example
        - Example: Stepper Motor A4988
    5. Pitfall
        - Pitfall: Stepper Motor A4988
    6. Q & A
        - Q & A: Stepper Motor A4988
4. **DC Motor L298N**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DC Motor L298N
    2. Core Concept
        - Core Concept: DC Motor L298N
    3. Syntax
        - Syntax: DC Motor L298N
    4. Example
        - Example: DC Motor L298N
    5. Pitfall
        - Pitfall: DC Motor L298N
    6. Q & A
        - Q & A: DC Motor L298N
5. **Solenoid Valve**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Solenoid Valve
    2. Core Concept
        - Core Concept: Solenoid Valve
    3. Syntax
        - Syntax: Solenoid Valve
    4. Example
        - Example: Solenoid Valve
    5. Pitfall
        - Pitfall: Solenoid Valve
    6. Q & A
        - Q & A: Solenoid Valve

#### 1.5.7. Module 7 — Display and Output

1. **16x2 LCD I2C Interface**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: 16x2 LCD I2C Interface
    2. Core Concept
        - Core Concept: 16x2 LCD I2C Interface
    3. Syntax
        - Syntax: 16x2 LCD I2C Interface
    4. Example
        - Example: 16x2 LCD I2C Interface
    5. Pitfall
        - Pitfall: 16x2 LCD I2C Interface
    6. Q & A
        - Q & A: 16x2 LCD I2C Interface
2. **OLED SSD1306**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: OLED SSD1306
    2. Core Concept
        - Core Concept: OLED SSD1306
    3. Syntax
        - Syntax: OLED SSD1306
    4. Example
        - Example: OLED SSD1306
    5. Pitfall
        - Pitfall: OLED SSD1306
    6. Q & A
        - Q & A: OLED SSD1306
3. **NeoPixel WS2812B**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: NeoPixel WS2812B
    2. Core Concept
        - Core Concept: NeoPixel WS2812B
    3. Syntax
        - Syntax: NeoPixel WS2812B
    4. Example
        - Example: NeoPixel WS2812B
    5. Pitfall
        - Pitfall: NeoPixel WS2812B
    6. Q & A
        - Q & A: NeoPixel WS2812B
4. **Buzzer and Audio Output**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Buzzer and Audio Output
    2. Core Concept
        - Core Concept: Buzzer and Audio Output
    3. Syntax
        - Syntax: Buzzer and Audio Output
    4. Example
        - Example: Buzzer and Audio Output
    5. Pitfall
        - Pitfall: Buzzer and Audio Output
    6. Q & A
        - Q & A: Buzzer and Audio Output
5. **7-Segment and Matrix Display**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: 7-Segment and Matrix Display
    2. Core Concept
        - Core Concept: 7-Segment and Matrix Display
    3. Syntax
        - Syntax: 7-Segment and Matrix Display
    4. Example
        - Example: 7-Segment and Matrix Display
    5. Pitfall
        - Pitfall: 7-Segment and Matrix Display
    6. Q & A
        - Q & A: 7-Segment and Matrix Display

### 1.6. Arduino

#### 1.6.1. Module 1 — Arduino Introduction

1. **What Is Arduino**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: What Is Arduino
    2. Core Concept
        - Core Concept: What Is Arduino
    3. Syntax
        - Syntax: What Is Arduino
    4. Example
        - Example: What Is Arduino
    5. Pitfall
        - Pitfall: What Is Arduino
    6. Q & A
        - Q & A: What Is Arduino
2. **Arduino Boards Uno Nano Mega Micro**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino Boards Uno Nano Mega Micro
    2. Core Concept
        - Core Concept: Arduino Boards Uno Nano Mega Micro
    3. Syntax
        - Syntax: Arduino Boards Uno Nano Mega Micro
    4. Example
        - Example: Arduino Boards Uno Nano Mega Micro
    5. Pitfall
        - Pitfall: Arduino Boards Uno Nano Mega Micro
    6. Q & A
        - Q & A: Arduino Boards Uno Nano Mega Micro
3. **Arduino IDE Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino IDE Setup
    2. Core Concept
        - Core Concept: Arduino IDE Setup
    3. Syntax
        - Syntax: Arduino IDE Setup
    4. Example
        - Example: Arduino IDE Setup
    5. Pitfall
        - Pitfall: Arduino IDE Setup
    6. Q & A
        - Q & A: Arduino IDE Setup
4. **First Sketch Blink**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: First Sketch Blink
    2. Core Concept
        - Core Concept: First Sketch Blink
    3. Syntax
        - Syntax: First Sketch Blink
    4. Example
        - Example: First Sketch Blink
    5. Pitfall
        - Pitfall: First Sketch Blink
    6. Q & A
        - Q & A: First Sketch Blink
5. **Arduino Pin Diagram**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino Pin Diagram
    2. Core Concept
        - Core Concept: Arduino Pin Diagram
    3. Syntax
        - Syntax: Arduino Pin Diagram
    4. Example
        - Example: Arduino Pin Diagram
    5. Pitfall
        - Pitfall: Arduino Pin Diagram
    6. Q & A
        - Q & A: Arduino Pin Diagram

#### 1.6.2. Module 2 — Digital I/O

1. **Digital Read and Write**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Digital Read and Write
    2. Core Concept
        - Core Concept: Digital Read and Write
    3. Syntax
        - Syntax: Digital Read and Write
    4. Example
        - Example: Digital Read and Write
    5. Pitfall
        - Pitfall: Digital Read and Write
    6. Q & A
        - Q & A: Digital Read and Write
2. **LED Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LED Control
    2. Core Concept
        - Core Concept: LED Control
    3. Syntax
        - Syntax: LED Control
    4. Example
        - Example: LED Control
    5. Pitfall
        - Pitfall: LED Control
    6. Q & A
        - Q & A: LED Control
3. **Button Input**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Button Input
    2. Core Concept
        - Core Concept: Button Input
    3. Syntax
        - Syntax: Button Input
    4. Example
        - Example: Button Input
    5. Pitfall
        - Pitfall: Button Input
    6. Q & A
        - Q & A: Button Input
4. **Debouncing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Debouncing
    2. Core Concept
        - Core Concept: Debouncing
    3. Syntax
        - Syntax: Debouncing
    4. Example
        - Example: Debouncing
    5. Pitfall
        - Pitfall: Debouncing
    6. Q & A
        - Q & A: Debouncing
5. **Multiple LEDs Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Multiple LEDs Pattern
    2. Core Concept
        - Core Concept: Multiple LEDs Pattern
    3. Syntax
        - Syntax: Multiple LEDs Pattern
    4. Example
        - Example: Multiple LEDs Pattern
    5. Pitfall
        - Pitfall: Multiple LEDs Pattern
    6. Q & A
        - Q & A: Multiple LEDs Pattern

#### 1.6.3. Module 3 — Analog I/O

1. **analogRead and Potentiometer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: analogRead and Potentiometer
    2. Core Concept
        - Core Concept: analogRead and Potentiometer
    3. Syntax
        - Syntax: analogRead and Potentiometer
    4. Example
        - Example: analogRead and Potentiometer
    5. Pitfall
        - Pitfall: analogRead and Potentiometer
    6. Q & A
        - Q & A: analogRead and Potentiometer
2. **analogWrite PWM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: analogWrite PWM
    2. Core Concept
        - Core Concept: analogWrite PWM
    3. Syntax
        - Syntax: analogWrite PWM
    4. Example
        - Example: analogWrite PWM
    5. Pitfall
        - Pitfall: analogWrite PWM
    6. Q & A
        - Q & A: analogWrite PWM
3. **LED Dimming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LED Dimming
    2. Core Concept
        - Core Concept: LED Dimming
    3. Syntax
        - Syntax: LED Dimming
    4. Example
        - Example: LED Dimming
    5. Pitfall
        - Pitfall: LED Dimming
    6. Q & A
        - Q & A: LED Dimming
4. **LDR Light Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LDR Light Sensor
    2. Core Concept
        - Core Concept: LDR Light Sensor
    3. Syntax
        - Syntax: LDR Light Sensor
    4. Example
        - Example: LDR Light Sensor
    5. Pitfall
        - Pitfall: LDR Light Sensor
    6. Q & A
        - Q & A: LDR Light Sensor
5. **Analog Signal Mapping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Analog Signal Mapping
    2. Core Concept
        - Core Concept: Analog Signal Mapping
    3. Syntax
        - Syntax: Analog Signal Mapping
    4. Example
        - Example: Analog Signal Mapping
    5. Pitfall
        - Pitfall: Analog Signal Mapping
    6. Q & A
        - Q & A: Analog Signal Mapping

#### 1.6.4. Module 4 — Serial Communication

1. **Serial Monitor Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Serial Monitor Basics
    2. Core Concept
        - Core Concept: Serial Monitor Basics
    3. Syntax
        - Syntax: Serial Monitor Basics
    4. Example
        - Example: Serial Monitor Basics
    5. Pitfall
        - Pitfall: Serial Monitor Basics
    6. Q & A
        - Q & A: Serial Monitor Basics
2. **Printing Sensor Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Printing Sensor Values
    2. Core Concept
        - Core Concept: Printing Sensor Values
    3. Syntax
        - Syntax: Printing Sensor Values
    4. Example
        - Example: Printing Sensor Values
    5. Pitfall
        - Pitfall: Printing Sensor Values
    6. Q & A
        - Q & A: Printing Sensor Values
3. **Reading Serial Input**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Reading Serial Input
    2. Core Concept
        - Core Concept: Reading Serial Input
    3. Syntax
        - Syntax: Reading Serial Input
    4. Example
        - Example: Reading Serial Input
    5. Pitfall
        - Pitfall: Reading Serial Input
    6. Q & A
        - Q & A: Reading Serial Input
4. **Serial Communication Two Arduinos**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Serial Communication Two Arduinos
    2. Core Concept
        - Core Concept: Serial Communication Two Arduinos
    3. Syntax
        - Syntax: Serial Communication Two Arduinos
    4. Example
        - Example: Serial Communication Two Arduinos
    5. Pitfall
        - Pitfall: Serial Communication Two Arduinos
    6. Q & A
        - Q & A: Serial Communication Two Arduinos
5. **Serial Debugging Tips**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Serial Debugging Tips
    2. Core Concept
        - Core Concept: Serial Debugging Tips
    3. Syntax
        - Syntax: Serial Debugging Tips
    4. Example
        - Example: Serial Debugging Tips
    5. Pitfall
        - Pitfall: Serial Debugging Tips
    6. Q & A
        - Q & A: Serial Debugging Tips

#### 1.6.5. Module 5 — Sensors with Arduino

1. **DHT11 Temperature and Humidity**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DHT11 Temperature and Humidity
    2. Core Concept
        - Core Concept: DHT11 Temperature and Humidity
    3. Syntax
        - Syntax: DHT11 Temperature and Humidity
    4. Example
        - Example: DHT11 Temperature and Humidity
    5. Pitfall
        - Pitfall: DHT11 Temperature and Humidity
    6. Q & A
        - Q & A: DHT11 Temperature and Humidity
2. **Ultrasonic Sensor HC-SR04**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Ultrasonic Sensor HC-SR04
    2. Core Concept
        - Core Concept: Ultrasonic Sensor HC-SR04
    3. Syntax
        - Syntax: Ultrasonic Sensor HC-SR04
    4. Example
        - Example: Ultrasonic Sensor HC-SR04
    5. Pitfall
        - Pitfall: Ultrasonic Sensor HC-SR04
    6. Q & A
        - Q & A: Ultrasonic Sensor HC-SR04
3. **PIR Motion Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: PIR Motion Sensor
    2. Core Concept
        - Core Concept: PIR Motion Sensor
    3. Syntax
        - Syntax: PIR Motion Sensor
    4. Example
        - Example: PIR Motion Sensor
    5. Pitfall
        - Pitfall: PIR Motion Sensor
    6. Q & A
        - Q & A: PIR Motion Sensor
4. **LDR and Soil Moisture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: LDR and Soil Moisture
    2. Core Concept
        - Core Concept: LDR and Soil Moisture
    3. Syntax
        - Syntax: LDR and Soil Moisture
    4. Example
        - Example: LDR and Soil Moisture
    5. Pitfall
        - Pitfall: LDR and Soil Moisture
    6. Q & A
        - Q & A: LDR and Soil Moisture
5. **Gas Sensor MQ-2**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Gas Sensor MQ-2
    2. Core Concept
        - Core Concept: Gas Sensor MQ-2
    3. Syntax
        - Syntax: Gas Sensor MQ-2
    4. Example
        - Example: Gas Sensor MQ-2
    5. Pitfall
        - Pitfall: Gas Sensor MQ-2
    6. Q & A
        - Q & A: Gas Sensor MQ-2

#### 1.6.6. Module 6 — Actuators with Arduino

1. **Servo Motor Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Servo Motor Control
    2. Core Concept
        - Core Concept: Servo Motor Control
    3. Syntax
        - Syntax: Servo Motor Control
    4. Example
        - Example: Servo Motor Control
    5. Pitfall
        - Pitfall: Servo Motor Control
    6. Q & A
        - Q & A: Servo Motor Control
2. **DC Motor with L298N**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DC Motor with L298N
    2. Core Concept
        - Core Concept: DC Motor with L298N
    3. Syntax
        - Syntax: DC Motor with L298N
    4. Example
        - Example: DC Motor with L298N
    5. Pitfall
        - Pitfall: DC Motor with L298N
    6. Q & A
        - Q & A: DC Motor with L298N
3. **Stepper Motor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Stepper Motor
    2. Core Concept
        - Core Concept: Stepper Motor
    3. Syntax
        - Syntax: Stepper Motor
    4. Example
        - Example: Stepper Motor
    5. Pitfall
        - Pitfall: Stepper Motor
    6. Q & A
        - Q & A: Stepper Motor
4. **Relay Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Relay Module
    2. Core Concept
        - Core Concept: Relay Module
    3. Syntax
        - Syntax: Relay Module
    4. Example
        - Example: Relay Module
    5. Pitfall
        - Pitfall: Relay Module
    6. Q & A
        - Q & A: Relay Module
5. **Buzzer Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Buzzer Control
    2. Core Concept
        - Core Concept: Buzzer Control
    3. Syntax
        - Syntax: Buzzer Control
    4. Example
        - Example: Buzzer Control
    5. Pitfall
        - Pitfall: Buzzer Control
    6. Q & A
        - Q & A: Buzzer Control

#### 1.6.7. Module 7 — Displays

1. **16x2 LCD with Arduino**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: 16x2 LCD with Arduino
    2. Core Concept
        - Core Concept: 16x2 LCD with Arduino
    3. Syntax
        - Syntax: 16x2 LCD with Arduino
    4. Example
        - Example: 16x2 LCD with Arduino
    5. Pitfall
        - Pitfall: 16x2 LCD with Arduino
    6. Q & A
        - Q & A: 16x2 LCD with Arduino
2. **OLED Display SSD1306**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: OLED Display SSD1306
    2. Core Concept
        - Core Concept: OLED Display SSD1306
    3. Syntax
        - Syntax: OLED Display SSD1306
    4. Example
        - Example: OLED Display SSD1306
    5. Pitfall
        - Pitfall: OLED Display SSD1306
    6. Q & A
        - Q & A: OLED Display SSD1306
3. **7-Segment Display**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: 7-Segment Display
    2. Core Concept
        - Core Concept: 7-Segment Display
    3. Syntax
        - Syntax: 7-Segment Display
    4. Example
        - Example: 7-Segment Display
    5. Pitfall
        - Pitfall: 7-Segment Display
    6. Q & A
        - Q & A: 7-Segment Display
4. **NeoPixel LED Strip**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: NeoPixel LED Strip
    2. Core Concept
        - Core Concept: NeoPixel LED Strip
    3. Syntax
        - Syntax: NeoPixel LED Strip
    4. Example
        - Example: NeoPixel LED Strip
    5. Pitfall
        - Pitfall: NeoPixel LED Strip
    6. Q & A
        - Q & A: NeoPixel LED Strip
5. **Displaying Sensor Data**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Displaying Sensor Data
    2. Core Concept
        - Core Concept: Displaying Sensor Data
    3. Syntax
        - Syntax: Displaying Sensor Data
    4. Example
        - Example: Displaying Sensor Data
    5. Pitfall
        - Pitfall: Displaying Sensor Data
    6. Q & A
        - Q & A: Displaying Sensor Data

#### 1.6.8. Module 8 — Communication Protocols

1. **I2C with Arduino**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: I2C with Arduino
    2. Core Concept
        - Core Concept: I2C with Arduino
    3. Syntax
        - Syntax: I2C with Arduino
    4. Example
        - Example: I2C with Arduino
    5. Pitfall
        - Pitfall: I2C with Arduino
    6. Q & A
        - Q & A: I2C with Arduino
2. **SPI with Arduino**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: SPI with Arduino
    2. Core Concept
        - Core Concept: SPI with Arduino
    3. Syntax
        - Syntax: SPI with Arduino
    4. Example
        - Example: SPI with Arduino
    5. Pitfall
        - Pitfall: SPI with Arduino
    6. Q & A
        - Q & A: SPI with Arduino
3. **UART Serial Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: UART Serial Communication
    2. Core Concept
        - Core Concept: UART Serial Communication
    3. Syntax
        - Syntax: UART Serial Communication
    4. Example
        - Example: UART Serial Communication
    5. Pitfall
        - Pitfall: UART Serial Communication
    6. Q & A
        - Q & A: UART Serial Communication
4. **NRF24L01 Wireless**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: NRF24L01 Wireless
    2. Core Concept
        - Core Concept: NRF24L01 Wireless
    3. Syntax
        - Syntax: NRF24L01 Wireless
    4. Example
        - Example: NRF24L01 Wireless
    5. Pitfall
        - Pitfall: NRF24L01 Wireless
    6. Q & A
        - Q & A: NRF24L01 Wireless
5. **IR Remote Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: IR Remote Control
    2. Core Concept
        - Core Concept: IR Remote Control
    3. Syntax
        - Syntax: IR Remote Control
    4. Example
        - Example: IR Remote Control
    5. Pitfall
        - Pitfall: IR Remote Control
    6. Q & A
        - Q & A: IR Remote Control

#### 1.6.9. Module 9 — Arduino Projects

1. **Temperature Monitoring System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Temperature Monitoring System
    2. Core Concept
        - Core Concept: Temperature Monitoring System
    3. Syntax
        - Syntax: Temperature Monitoring System
    4. Example
        - Example: Temperature Monitoring System
    5. Pitfall
        - Pitfall: Temperature Monitoring System
    6. Q & A
        - Q & A: Temperature Monitoring System
2. **Automatic Street Light**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Automatic Street Light
    2. Core Concept
        - Core Concept: Automatic Street Light
    3. Syntax
        - Syntax: Automatic Street Light
    4. Example
        - Example: Automatic Street Light
    5. Pitfall
        - Pitfall: Automatic Street Light
    6. Q & A
        - Q & A: Automatic Street Light
3. **Water Level Indicator**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Water Level Indicator
    2. Core Concept
        - Core Concept: Water Level Indicator
    3. Syntax
        - Syntax: Water Level Indicator
    4. Example
        - Example: Water Level Indicator
    5. Pitfall
        - Pitfall: Water Level Indicator
    6. Q & A
        - Q & A: Water Level Indicator
4. **Home Automation Relay**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Home Automation Relay
    2. Core Concept
        - Core Concept: Home Automation Relay
    3. Syntax
        - Syntax: Home Automation Relay
    4. Example
        - Example: Home Automation Relay
    5. Pitfall
        - Pitfall: Home Automation Relay
    6. Q & A
        - Q & A: Home Automation Relay
5. **Obstacle Avoiding Robot**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Obstacle Avoiding Robot
    2. Core Concept
        - Core Concept: Obstacle Avoiding Robot
    3. Syntax
        - Syntax: Obstacle Avoiding Robot
    4. Example
        - Example: Obstacle Avoiding Robot
    5. Pitfall
        - Pitfall: Obstacle Avoiding Robot
    6. Q & A
        - Q & A: Obstacle Avoiding Robot

#### 1.6.10. Module 10 — Advanced Arduino

1. **Arduino Interrupts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino Interrupts
    2. Core Concept
        - Core Concept: Arduino Interrupts
    3. Syntax
        - Syntax: Arduino Interrupts
    4. Example
        - Example: Arduino Interrupts
    5. Pitfall
        - Pitfall: Arduino Interrupts
    6. Q & A
        - Q & A: Arduino Interrupts
2. **Timer Libraries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Timer Libraries
    2. Core Concept
        - Core Concept: Timer Libraries
    3. Syntax
        - Syntax: Timer Libraries
    4. Example
        - Example: Timer Libraries
    5. Pitfall
        - Pitfall: Timer Libraries
    6. Q & A
        - Q & A: Timer Libraries
3. **EEPROM Storage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: EEPROM Storage
    2. Core Concept
        - Core Concept: EEPROM Storage
    3. Syntax
        - Syntax: EEPROM Storage
    4. Example
        - Example: EEPROM Storage
    5. Pitfall
        - Pitfall: EEPROM Storage
    6. Q & A
        - Q & A: EEPROM Storage
4. **Arduino with SD Card**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino with SD Card
    2. Core Concept
        - Core Concept: Arduino with SD Card
    3. Syntax
        - Syntax: Arduino with SD Card
    4. Example
        - Example: Arduino with SD Card
    5. Pitfall
        - Pitfall: Arduino with SD Card
    6. Q & A
        - Q & A: Arduino with SD Card
5. **Low Power Arduino**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Low Power Arduino
    2. Core Concept
        - Core Concept: Low Power Arduino
    3. Syntax
        - Syntax: Low Power Arduino
    4. Example
        - Example: Low Power Arduino
    5. Pitfall
        - Pitfall: Low Power Arduino
    6. Q & A
        - Q & A: Low Power Arduino

### 1.7. ESP32

#### 1.7.1. Module 1 — ESP32 Introduction

1. **ESP32 vs ESP8266 vs Arduino**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 vs ESP8266 vs Arduino
    2. Overview
        - Overview: ESP32 vs ESP8266 vs Arduino
    3. Core Concept
        - Core Concept: ESP32 vs ESP8266 vs Arduino
    4. Core Concept
        - Core Concept: ESP32 vs ESP8266 vs Arduino
    5. Syntax
        - Syntax: ESP32 vs ESP8266 vs Arduino
    6. Syntax
        - Syntax: ESP32 vs ESP8266 vs Arduino
    7. Example
        - Example: ESP32 vs ESP8266 vs Arduino
    8. Example
        - Example: ESP32 vs ESP8266 vs Arduino
    9. Pitfall
        - Pitfall: ESP32 vs ESP8266 vs Arduino
    10. Pitfall
        - Pitfall: ESP32 vs ESP8266 vs Arduino
    11. Q & A
        - Q & A: ESP32 vs ESP8266 vs Arduino
    12. Q & A
        - Q & A: ESP32 vs ESP8266 vs Arduino
2. **ESP32 Architecture Dual Core**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 Architecture Dual Core
    2. Overview
        - Overview: ESP32 Architecture Dual Core
    3. Core Concept
        - Core Concept: ESP32 Architecture Dual Core
    4. Core Concept
        - Core Concept: ESP32 Architecture Dual Core
    5. Syntax
        - Syntax: ESP32 Architecture Dual Core
    6. Syntax
        - Syntax: ESP32 Architecture Dual Core
    7. Example
        - Example: ESP32 Architecture Dual Core
    8. Example
        - Example: ESP32 Architecture Dual Core
    9. Pitfall
        - Pitfall: ESP32 Architecture Dual Core
    10. Pitfall
        - Pitfall: ESP32 Architecture Dual Core
    11. Q & A
        - Q & A: ESP32 Architecture Dual Core
    12. Q & A
        - Q & A: ESP32 Architecture Dual Core
3. **Development Boards DevKit WROOM S3**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Development Boards DevKit WROOM S3
    2. Overview
        - Overview: Development Boards DevKit WROOM S3
    3. Core Concept
        - Core Concept: Development Boards DevKit WROOM S3
    4. Core Concept
        - Core Concept: Development Boards DevKit WROOM S3
    5. Syntax
        - Syntax: Development Boards DevKit WROOM S3
    6. Syntax
        - Syntax: Development Boards DevKit WROOM S3
    7. Example
        - Example: Development Boards DevKit WROOM S3
    8. Example
        - Example: Development Boards DevKit WROOM S3
    9. Pitfall
        - Pitfall: Development Boards DevKit WROOM S3
    10. Pitfall
        - Pitfall: Development Boards DevKit WROOM S3
    11. Q & A
        - Q & A: Development Boards DevKit WROOM S3
    12. Q & A
        - Q & A: Development Boards DevKit WROOM S3
4. **ESP-IDF vs Arduino Framework**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP-IDF vs Arduino Framework
    2. Overview
        - Overview: ESP-IDF vs Arduino Framework
    3. Core Concept
        - Core Concept: ESP-IDF vs Arduino Framework
    4. Core Concept
        - Core Concept: ESP-IDF vs Arduino Framework
    5. Syntax
        - Syntax: ESP-IDF vs Arduino Framework
    6. Syntax
        - Syntax: ESP-IDF vs Arduino Framework
    7. Example
        - Example: ESP-IDF vs Arduino Framework
    8. Example
        - Example: ESP-IDF vs Arduino Framework
    9. Pitfall
        - Pitfall: ESP-IDF vs Arduino Framework
    10. Pitfall
        - Pitfall: ESP-IDF vs Arduino Framework
    11. Q & A
        - Q & A: ESP-IDF vs Arduino Framework
    12. Q & A
        - Q & A: ESP-IDF vs Arduino Framework
5. **Pinout and Hardware Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Pinout and Hardware Overview
    2. Overview
        - Overview: Pinout and Hardware Overview
    3. Core Concept
        - Core Concept: Pinout and Hardware Overview
    4. Core Concept
        - Core Concept: Pinout and Hardware Overview
    5. Syntax
        - Syntax: Pinout and Hardware Overview
    6. Syntax
        - Syntax: Pinout and Hardware Overview
    7. Example
        - Example: Pinout and Hardware Overview
    8. Example
        - Example: Pinout and Hardware Overview
    9. Pitfall
        - Pitfall: Pinout and Hardware Overview
    10. Pitfall
        - Pitfall: Pinout and Hardware Overview
    11. Q & A
        - Q & A: Pinout and Hardware Overview
    12. Q & A
        - Q & A: Pinout and Hardware Overview

#### 1.7.2. Module 2 — ESP32 GPIO

1. **Digital I/O on ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Digital I/O on ESP32
    2. Overview
        - Overview: Digital I/O on ESP32
    3. Core Concept
        - Core Concept: Digital I/O on ESP32
    4. Core Concept
        - Core Concept: Digital I/O on ESP32
    5. Syntax
        - Syntax: Digital I/O on ESP32
    6. Syntax
        - Syntax: Digital I/O on ESP32
    7. Example
        - Example: Digital I/O on ESP32
    8. Example
        - Example: Digital I/O on ESP32
    9. Pitfall
        - Pitfall: Digital I/O on ESP32
    10. Pitfall
        - Pitfall: Digital I/O on ESP32
    11. Q & A
        - Q & A: Digital I/O on ESP32
    12. Q & A
        - Q & A: Digital I/O on ESP32
2. **Analog ADC Channels**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Analog ADC Channels
    2. Overview
        - Overview: Analog ADC Channels
    3. Core Concept
        - Core Concept: Analog ADC Channels
    4. Core Concept
        - Core Concept: Analog ADC Channels
    5. Syntax
        - Syntax: Analog ADC Channels
    6. Syntax
        - Syntax: Analog ADC Channels
    7. Example
        - Example: Analog ADC Channels
    8. Example
        - Example: Analog ADC Channels
    9. Pitfall
        - Pitfall: Analog ADC Channels
    10. Pitfall
        - Pitfall: Analog ADC Channels
    11. Q & A
        - Q & A: Analog ADC Channels
    12. Q & A
        - Q & A: Analog ADC Channels
3. **DAC Output**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DAC Output
    2. Overview
        - Overview: DAC Output
    3. Core Concept
        - Core Concept: DAC Output
    4. Core Concept
        - Core Concept: DAC Output
    5. Syntax
        - Syntax: DAC Output
    6. Syntax
        - Syntax: DAC Output
    7. Example
        - Example: DAC Output
    8. Example
        - Example: DAC Output
    9. Pitfall
        - Pitfall: DAC Output
    10. Pitfall
        - Pitfall: DAC Output
    11. Q & A
        - Q & A: DAC Output
    12. Q & A
        - Q & A: DAC Output
4. **Touch Sensors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Touch Sensors
    2. Overview
        - Overview: Touch Sensors
    3. Core Concept
        - Core Concept: Touch Sensors
    4. Core Concept
        - Core Concept: Touch Sensors
    5. Syntax
        - Syntax: Touch Sensors
    6. Syntax
        - Syntax: Touch Sensors
    7. Example
        - Example: Touch Sensors
    8. Example
        - Example: Touch Sensors
    9. Pitfall
        - Pitfall: Touch Sensors
    10. Pitfall
        - Pitfall: Touch Sensors
    11. Q & A
        - Q & A: Touch Sensors
    12. Q & A
        - Q & A: Touch Sensors
5. **GPIO Interrupt on ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: GPIO Interrupt on ESP32
    2. Overview
        - Overview: GPIO Interrupt on ESP32
    3. Core Concept
        - Core Concept: GPIO Interrupt on ESP32
    4. Core Concept
        - Core Concept: GPIO Interrupt on ESP32
    5. Syntax
        - Syntax: GPIO Interrupt on ESP32
    6. Syntax
        - Syntax: GPIO Interrupt on ESP32
    7. Example
        - Example: GPIO Interrupt on ESP32
    8. Example
        - Example: GPIO Interrupt on ESP32
    9. Pitfall
        - Pitfall: GPIO Interrupt on ESP32
    10. Pitfall
        - Pitfall: GPIO Interrupt on ESP32
    11. Q & A
        - Q & A: GPIO Interrupt on ESP32
    12. Q & A
        - Q & A: GPIO Interrupt on ESP32

#### 1.7.3. Module 3 — WiFi

1. **WiFi Station Mode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: WiFi Station Mode
    2. Overview
        - Overview: WiFi Station Mode
    3. Core Concept
        - Core Concept: WiFi Station Mode
    4. Core Concept
        - Core Concept: WiFi Station Mode
    5. Syntax
        - Syntax: WiFi Station Mode
    6. Syntax
        - Syntax: WiFi Station Mode
    7. Example
        - Example: WiFi Station Mode
    8. Example
        - Example: WiFi Station Mode
    9. Pitfall
        - Pitfall: WiFi Station Mode
    10. Pitfall
        - Pitfall: WiFi Station Mode
    11. Q & A
        - Q & A: WiFi Station Mode
    12. Q & A
        - Q & A: WiFi Station Mode
2. **WiFi Access Point Mode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: WiFi Access Point Mode
    2. Overview
        - Overview: WiFi Access Point Mode
    3. Core Concept
        - Core Concept: WiFi Access Point Mode
    4. Core Concept
        - Core Concept: WiFi Access Point Mode
    5. Syntax
        - Syntax: WiFi Access Point Mode
    6. Syntax
        - Syntax: WiFi Access Point Mode
    7. Example
        - Example: WiFi Access Point Mode
    8. Example
        - Example: WiFi Access Point Mode
    9. Pitfall
        - Pitfall: WiFi Access Point Mode
    10. Pitfall
        - Pitfall: WiFi Access Point Mode
    11. Q & A
        - Q & A: WiFi Access Point Mode
    12. Q & A
        - Q & A: WiFi Access Point Mode
3. **Connecting to Router**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Connecting to Router
    2. Overview
        - Overview: Connecting to Router
    3. Core Concept
        - Core Concept: Connecting to Router
    4. Core Concept
        - Core Concept: Connecting to Router
    5. Syntax
        - Syntax: Connecting to Router
    6. Syntax
        - Syntax: Connecting to Router
    7. Example
        - Example: Connecting to Router
    8. Example
        - Example: Connecting to Router
    9. Pitfall
        - Pitfall: Connecting to Router
    10. Pitfall
        - Pitfall: Connecting to Router
    11. Q & A
        - Q & A: Connecting to Router
    12. Q & A
        - Q & A: Connecting to Router
4. **HTTP Client GET and POST**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: HTTP Client GET and POST
    2. Overview
        - Overview: HTTP Client GET and POST
    3. Core Concept
        - Core Concept: HTTP Client GET and POST
    4. Core Concept
        - Core Concept: HTTP Client GET and POST
    5. Syntax
        - Syntax: HTTP Client GET and POST
    6. Syntax
        - Syntax: HTTP Client GET and POST
    7. Example
        - Example: HTTP Client GET and POST
    8. Example
        - Example: HTTP Client GET and POST
    9. Pitfall
        - Pitfall: HTTP Client GET and POST
    10. Pitfall
        - Pitfall: HTTP Client GET and POST
    11. Q & A
        - Q & A: HTTP Client GET and POST
    12. Q & A
        - Q & A: HTTP Client GET and POST
5. **HTTPS SSL TLS on ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: HTTPS SSL TLS on ESP32
    2. Overview
        - Overview: HTTPS SSL TLS on ESP32
    3. Core Concept
        - Core Concept: HTTPS SSL TLS on ESP32
    4. Core Concept
        - Core Concept: HTTPS SSL TLS on ESP32
    5. Syntax
        - Syntax: HTTPS SSL TLS on ESP32
    6. Syntax
        - Syntax: HTTPS SSL TLS on ESP32
    7. Example
        - Example: HTTPS SSL TLS on ESP32
    8. Example
        - Example: HTTPS SSL TLS on ESP32
    9. Pitfall
        - Pitfall: HTTPS SSL TLS on ESP32
    10. Pitfall
        - Pitfall: HTTPS SSL TLS on ESP32
    11. Q & A
        - Q & A: HTTPS SSL TLS on ESP32
    12. Q & A
        - Q & A: HTTPS SSL TLS on ESP32

#### 1.7.4. Module 4 — Bluetooth and BLE

1. **Classic Bluetooth Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Classic Bluetooth Basics
    2. Overview
        - Overview: Classic Bluetooth Basics
    3. Core Concept
        - Core Concept: Classic Bluetooth Basics
    4. Core Concept
        - Core Concept: Classic Bluetooth Basics
    5. Syntax
        - Syntax: Classic Bluetooth Basics
    6. Syntax
        - Syntax: Classic Bluetooth Basics
    7. Example
        - Example: Classic Bluetooth Basics
    8. Example
        - Example: Classic Bluetooth Basics
    9. Pitfall
        - Pitfall: Classic Bluetooth Basics
    10. Pitfall
        - Pitfall: Classic Bluetooth Basics
    11. Q & A
        - Q & A: Classic Bluetooth Basics
    12. Q & A
        - Q & A: Classic Bluetooth Basics
2. **BLE Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BLE Fundamentals
    2. Overview
        - Overview: BLE Fundamentals
    3. Core Concept
        - Core Concept: BLE Fundamentals
    4. Core Concept
        - Core Concept: BLE Fundamentals
    5. Syntax
        - Syntax: BLE Fundamentals
    6. Syntax
        - Syntax: BLE Fundamentals
    7. Example
        - Example: BLE Fundamentals
    8. Example
        - Example: BLE Fundamentals
    9. Pitfall
        - Pitfall: BLE Fundamentals
    10. Pitfall
        - Pitfall: BLE Fundamentals
    11. Q & A
        - Q & A: BLE Fundamentals
    12. Q & A
        - Q & A: BLE Fundamentals
3. **BLE Server and Client**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BLE Server and Client
    2. Overview
        - Overview: BLE Server and Client
    3. Core Concept
        - Core Concept: BLE Server and Client
    4. Core Concept
        - Core Concept: BLE Server and Client
    5. Syntax
        - Syntax: BLE Server and Client
    6. Syntax
        - Syntax: BLE Server and Client
    7. Example
        - Example: BLE Server and Client
    8. Example
        - Example: BLE Server and Client
    9. Pitfall
        - Pitfall: BLE Server and Client
    10. Pitfall
        - Pitfall: BLE Server and Client
    11. Q & A
        - Q & A: BLE Server and Client
    12. Q & A
        - Q & A: BLE Server and Client
4. **BLE Sensor Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BLE Sensor Broadcasting
    2. Overview
        - Overview: BLE Sensor Broadcasting
    3. Core Concept
        - Core Concept: BLE Sensor Broadcasting
    4. Core Concept
        - Core Concept: BLE Sensor Broadcasting
    5. Syntax
        - Syntax: BLE Sensor Broadcasting
    6. Syntax
        - Syntax: BLE Sensor Broadcasting
    7. Example
        - Example: BLE Sensor Broadcasting
    8. Example
        - Example: BLE Sensor Broadcasting
    9. Pitfall
        - Pitfall: BLE Sensor Broadcasting
    10. Pitfall
        - Pitfall: BLE Sensor Broadcasting
    11. Q & A
        - Q & A: BLE Sensor Broadcasting
    12. Q & A
        - Q & A: BLE Sensor Broadcasting
5. **BLE with Mobile App**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BLE with Mobile App
    2. Overview
        - Overview: BLE with Mobile App
    3. Core Concept
        - Core Concept: BLE with Mobile App
    4. Core Concept
        - Core Concept: BLE with Mobile App
    5. Syntax
        - Syntax: BLE with Mobile App
    6. Syntax
        - Syntax: BLE with Mobile App
    7. Example
        - Example: BLE with Mobile App
    8. Example
        - Example: BLE with Mobile App
    9. Pitfall
        - Pitfall: BLE with Mobile App
    10. Pitfall
        - Pitfall: BLE with Mobile App
    11. Q & A
        - Q & A: BLE with Mobile App
    12. Q & A
        - Q & A: BLE with Mobile App

#### 1.7.5. Module 5 — MQTT with ESP32

1. **MQTT Setup on ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT Setup on ESP32
    2. Overview
        - Overview: MQTT Setup on ESP32
    3. Core Concept
        - Core Concept: MQTT Setup on ESP32
    4. Core Concept
        - Core Concept: MQTT Setup on ESP32
    5. Syntax
        - Syntax: MQTT Setup on ESP32
    6. Syntax
        - Syntax: MQTT Setup on ESP32
    7. Example
        - Example: MQTT Setup on ESP32
    8. Example
        - Example: MQTT Setup on ESP32
    9. Pitfall
        - Pitfall: MQTT Setup on ESP32
    10. Pitfall
        - Pitfall: MQTT Setup on ESP32
    11. Q & A
        - Q & A: MQTT Setup on ESP32
    12. Q & A
        - Q & A: MQTT Setup on ESP32
2. **Publishing Sensor Data**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Publishing Sensor Data
    2. Overview
        - Overview: Publishing Sensor Data
    3. Core Concept
        - Core Concept: Publishing Sensor Data
    4. Core Concept
        - Core Concept: Publishing Sensor Data
    5. Syntax
        - Syntax: Publishing Sensor Data
    6. Syntax
        - Syntax: Publishing Sensor Data
    7. Example
        - Example: Publishing Sensor Data
    8. Example
        - Example: Publishing Sensor Data
    9. Pitfall
        - Pitfall: Publishing Sensor Data
    10. Pitfall
        - Pitfall: Publishing Sensor Data
    11. Q & A
        - Q & A: Publishing Sensor Data
    12. Q & A
        - Q & A: Publishing Sensor Data
3. **Subscribing for Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Subscribing for Commands
    2. Overview
        - Overview: Subscribing for Commands
    3. Core Concept
        - Core Concept: Subscribing for Commands
    4. Core Concept
        - Core Concept: Subscribing for Commands
    5. Syntax
        - Syntax: Subscribing for Commands
    6. Syntax
        - Syntax: Subscribing for Commands
    7. Example
        - Example: Subscribing for Commands
    8. Example
        - Example: Subscribing for Commands
    9. Pitfall
        - Pitfall: Subscribing for Commands
    10. Pitfall
        - Pitfall: Subscribing for Commands
    11. Q & A
        - Q & A: Subscribing for Commands
    12. Q & A
        - Q & A: Subscribing for Commands
4. **QoS Levels**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: QoS Levels
    2. Overview
        - Overview: QoS Levels
    3. Core Concept
        - Core Concept: QoS Levels
    4. Core Concept
        - Core Concept: QoS Levels
    5. Syntax
        - Syntax: QoS Levels
    6. Syntax
        - Syntax: QoS Levels
    7. Example
        - Example: QoS Levels
    8. Example
        - Example: QoS Levels
    9. Pitfall
        - Pitfall: QoS Levels
    10. Pitfall
        - Pitfall: QoS Levels
    11. Q & A
        - Q & A: QoS Levels
    12. Q & A
        - Q & A: QoS Levels
5. **MQTT over TLS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT over TLS
    2. Overview
        - Overview: MQTT over TLS
    3. Core Concept
        - Core Concept: MQTT over TLS
    4. Core Concept
        - Core Concept: MQTT over TLS
    5. Syntax
        - Syntax: MQTT over TLS
    6. Syntax
        - Syntax: MQTT over TLS
    7. Example
        - Example: MQTT over TLS
    8. Example
        - Example: MQTT over TLS
    9. Pitfall
        - Pitfall: MQTT over TLS
    10. Pitfall
        - Pitfall: MQTT over TLS
    11. Q & A
        - Q & A: MQTT over TLS
    12. Q & A
        - Q & A: MQTT over TLS

#### 1.7.6. Module 6 — HTTP and REST API

1. **ESP32 HTTP Client**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 HTTP Client
    2. Overview
        - Overview: ESP32 HTTP Client
    3. Core Concept
        - Core Concept: ESP32 HTTP Client
    4. Core Concept
        - Core Concept: ESP32 HTTP Client
    5. Syntax
        - Syntax: ESP32 HTTP Client
    6. Syntax
        - Syntax: ESP32 HTTP Client
    7. Example
        - Example: ESP32 HTTP Client
    8. Example
        - Example: ESP32 HTTP Client
    9. Pitfall
        - Pitfall: ESP32 HTTP Client
    10. Pitfall
        - Pitfall: ESP32 HTTP Client
    11. Q & A
        - Q & A: ESP32 HTTP Client
    12. Q & A
        - Q & A: ESP32 HTTP Client
2. **Posting to Flask API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Posting to Flask API
    2. Overview
        - Overview: Posting to Flask API
    3. Core Concept
        - Core Concept: Posting to Flask API
    4. Core Concept
        - Core Concept: Posting to Flask API
    5. Syntax
        - Syntax: Posting to Flask API
    6. Syntax
        - Syntax: Posting to Flask API
    7. Example
        - Example: Posting to Flask API
    8. Example
        - Example: Posting to Flask API
    9. Pitfall
        - Pitfall: Posting to Flask API
    10. Pitfall
        - Pitfall: Posting to Flask API
    11. Q & A
        - Q & A: Posting to Flask API
    12. Q & A
        - Q & A: Posting to Flask API
3. **JSON Parsing on ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: JSON Parsing on ESP32
    2. Overview
        - Overview: JSON Parsing on ESP32
    3. Core Concept
        - Core Concept: JSON Parsing on ESP32
    4. Core Concept
        - Core Concept: JSON Parsing on ESP32
    5. Syntax
        - Syntax: JSON Parsing on ESP32
    6. Syntax
        - Syntax: JSON Parsing on ESP32
    7. Example
        - Example: JSON Parsing on ESP32
    8. Example
        - Example: JSON Parsing on ESP32
    9. Pitfall
        - Pitfall: JSON Parsing on ESP32
    10. Pitfall
        - Pitfall: JSON Parsing on ESP32
    11. Q & A
        - Q & A: JSON Parsing on ESP32
    12. Q & A
        - Q & A: JSON Parsing on ESP32
4. **ESP32 Web Server**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 Web Server
    2. Overview
        - Overview: ESP32 Web Server
    3. Core Concept
        - Core Concept: ESP32 Web Server
    4. Core Concept
        - Core Concept: ESP32 Web Server
    5. Syntax
        - Syntax: ESP32 Web Server
    6. Syntax
        - Syntax: ESP32 Web Server
    7. Example
        - Example: ESP32 Web Server
    8. Example
        - Example: ESP32 Web Server
    9. Pitfall
        - Pitfall: ESP32 Web Server
    10. Pitfall
        - Pitfall: ESP32 Web Server
    11. Q & A
        - Q & A: ESP32 Web Server
    12. Q & A
        - Q & A: ESP32 Web Server
5. **REST API Command and Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: REST API Command and Control
    2. Overview
        - Overview: REST API Command and Control
    3. Core Concept
        - Core Concept: REST API Command and Control
    4. Core Concept
        - Core Concept: REST API Command and Control
    5. Syntax
        - Syntax: REST API Command and Control
    6. Syntax
        - Syntax: REST API Command and Control
    7. Example
        - Example: REST API Command and Control
    8. Example
        - Example: REST API Command and Control
    9. Pitfall
        - Pitfall: REST API Command and Control
    10. Pitfall
        - Pitfall: REST API Command and Control
    11. Q & A
        - Q & A: REST API Command and Control
    12. Q & A
        - Q & A: REST API Command and Control

#### 1.7.7. Module 7 — ESP32 Sensors

1. **DHT22 Temperature and Humidity**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: DHT22 Temperature and Humidity
    2. Overview
        - Overview: DHT22 Temperature and Humidity
    3. Core Concept
        - Core Concept: DHT22 Temperature and Humidity
    4. Core Concept
        - Core Concept: DHT22 Temperature and Humidity
    5. Syntax
        - Syntax: DHT22 Temperature and Humidity
    6. Syntax
        - Syntax: DHT22 Temperature and Humidity
    7. Example
        - Example: DHT22 Temperature and Humidity
    8. Example
        - Example: DHT22 Temperature and Humidity
    9. Pitfall
        - Pitfall: DHT22 Temperature and Humidity
    10. Pitfall
        - Pitfall: DHT22 Temperature and Humidity
    11. Q & A
        - Q & A: DHT22 Temperature and Humidity
    12. Q & A
        - Q & A: DHT22 Temperature and Humidity
2. **BME280 Environment Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BME280 Environment Sensor
    2. Overview
        - Overview: BME280 Environment Sensor
    3. Core Concept
        - Core Concept: BME280 Environment Sensor
    4. Core Concept
        - Core Concept: BME280 Environment Sensor
    5. Syntax
        - Syntax: BME280 Environment Sensor
    6. Syntax
        - Syntax: BME280 Environment Sensor
    7. Example
        - Example: BME280 Environment Sensor
    8. Example
        - Example: BME280 Environment Sensor
    9. Pitfall
        - Pitfall: BME280 Environment Sensor
    10. Pitfall
        - Pitfall: BME280 Environment Sensor
    11. Q & A
        - Q & A: BME280 Environment Sensor
    12. Q & A
        - Q & A: BME280 Environment Sensor
3. **MPU6050 IMU Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MPU6050 IMU Sensor
    2. Overview
        - Overview: MPU6050 IMU Sensor
    3. Core Concept
        - Core Concept: MPU6050 IMU Sensor
    4. Core Concept
        - Core Concept: MPU6050 IMU Sensor
    5. Syntax
        - Syntax: MPU6050 IMU Sensor
    6. Syntax
        - Syntax: MPU6050 IMU Sensor
    7. Example
        - Example: MPU6050 IMU Sensor
    8. Example
        - Example: MPU6050 IMU Sensor
    9. Pitfall
        - Pitfall: MPU6050 IMU Sensor
    10. Pitfall
        - Pitfall: MPU6050 IMU Sensor
    11. Q & A
        - Q & A: MPU6050 IMU Sensor
    12. Q & A
        - Q & A: MPU6050 IMU Sensor
4. **Hall Effect Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Hall Effect Sensor
    2. Overview
        - Overview: Hall Effect Sensor
    3. Core Concept
        - Core Concept: Hall Effect Sensor
    4. Core Concept
        - Core Concept: Hall Effect Sensor
    5. Syntax
        - Syntax: Hall Effect Sensor
    6. Syntax
        - Syntax: Hall Effect Sensor
    7. Example
        - Example: Hall Effect Sensor
    8. Example
        - Example: Hall Effect Sensor
    9. Pitfall
        - Pitfall: Hall Effect Sensor
    10. Pitfall
        - Pitfall: Hall Effect Sensor
    11. Q & A
        - Q & A: Hall Effect Sensor
    12. Q & A
        - Q & A: Hall Effect Sensor
5. **Capacitive Touch Sensor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Capacitive Touch Sensor
    2. Overview
        - Overview: Capacitive Touch Sensor
    3. Core Concept
        - Core Concept: Capacitive Touch Sensor
    4. Core Concept
        - Core Concept: Capacitive Touch Sensor
    5. Syntax
        - Syntax: Capacitive Touch Sensor
    6. Syntax
        - Syntax: Capacitive Touch Sensor
    7. Example
        - Example: Capacitive Touch Sensor
    8. Example
        - Example: Capacitive Touch Sensor
    9. Pitfall
        - Pitfall: Capacitive Touch Sensor
    10. Pitfall
        - Pitfall: Capacitive Touch Sensor
    11. Q & A
        - Q & A: Capacitive Touch Sensor
    12. Q & A
        - Q & A: Capacitive Touch Sensor

#### 1.7.8. Module 8 — Deep Sleep and Power Management

1. **ESP32 Power Modes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 Power Modes
    2. Overview
        - Overview: ESP32 Power Modes
    3. Core Concept
        - Core Concept: ESP32 Power Modes
    4. Core Concept
        - Core Concept: ESP32 Power Modes
    5. Syntax
        - Syntax: ESP32 Power Modes
    6. Syntax
        - Syntax: ESP32 Power Modes
    7. Example
        - Example: ESP32 Power Modes
    8. Example
        - Example: ESP32 Power Modes
    9. Pitfall
        - Pitfall: ESP32 Power Modes
    10. Pitfall
        - Pitfall: ESP32 Power Modes
    11. Q & A
        - Q & A: ESP32 Power Modes
    12. Q & A
        - Q & A: ESP32 Power Modes
2. **Deep Sleep Timer Wakeup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Deep Sleep Timer Wakeup
    2. Overview
        - Overview: Deep Sleep Timer Wakeup
    3. Core Concept
        - Core Concept: Deep Sleep Timer Wakeup
    4. Core Concept
        - Core Concept: Deep Sleep Timer Wakeup
    5. Syntax
        - Syntax: Deep Sleep Timer Wakeup
    6. Syntax
        - Syntax: Deep Sleep Timer Wakeup
    7. Example
        - Example: Deep Sleep Timer Wakeup
    8. Example
        - Example: Deep Sleep Timer Wakeup
    9. Pitfall
        - Pitfall: Deep Sleep Timer Wakeup
    10. Pitfall
        - Pitfall: Deep Sleep Timer Wakeup
    11. Q & A
        - Q & A: Deep Sleep Timer Wakeup
    12. Q & A
        - Q & A: Deep Sleep Timer Wakeup
3. **Deep Sleep External Wakeup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Deep Sleep External Wakeup
    2. Overview
        - Overview: Deep Sleep External Wakeup
    3. Core Concept
        - Core Concept: Deep Sleep External Wakeup
    4. Core Concept
        - Core Concept: Deep Sleep External Wakeup
    5. Syntax
        - Syntax: Deep Sleep External Wakeup
    6. Syntax
        - Syntax: Deep Sleep External Wakeup
    7. Example
        - Example: Deep Sleep External Wakeup
    8. Example
        - Example: Deep Sleep External Wakeup
    9. Pitfall
        - Pitfall: Deep Sleep External Wakeup
    10. Pitfall
        - Pitfall: Deep Sleep External Wakeup
    11. Q & A
        - Q & A: Deep Sleep External Wakeup
    12. Q & A
        - Q & A: Deep Sleep External Wakeup
4. **ULP Co-Processor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ULP Co-Processor
    2. Overview
        - Overview: ULP Co-Processor
    3. Core Concept
        - Core Concept: ULP Co-Processor
    4. Core Concept
        - Core Concept: ULP Co-Processor
    5. Syntax
        - Syntax: ULP Co-Processor
    6. Syntax
        - Syntax: ULP Co-Processor
    7. Example
        - Example: ULP Co-Processor
    8. Example
        - Example: ULP Co-Processor
    9. Pitfall
        - Pitfall: ULP Co-Processor
    10. Pitfall
        - Pitfall: ULP Co-Processor
    11. Q & A
        - Q & A: ULP Co-Processor
    12. Q & A
        - Q & A: ULP Co-Processor
5. **Battery Powered IoT Node**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Battery Powered IoT Node
    2. Overview
        - Overview: Battery Powered IoT Node
    3. Core Concept
        - Core Concept: Battery Powered IoT Node
    4. Core Concept
        - Core Concept: Battery Powered IoT Node
    5. Syntax
        - Syntax: Battery Powered IoT Node
    6. Syntax
        - Syntax: Battery Powered IoT Node
    7. Example
        - Example: Battery Powered IoT Node
    8. Example
        - Example: Battery Powered IoT Node
    9. Pitfall
        - Pitfall: Battery Powered IoT Node
    10. Pitfall
        - Pitfall: Battery Powered IoT Node
    11. Q & A
        - Q & A: Battery Powered IoT Node
    12. Q & A
        - Q & A: Battery Powered IoT Node

#### 1.7.9. Module 9 — OTA Updates

1. **OTA Concept**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: OTA Concept
    2. Overview
        - Overview: OTA Concept
    3. Core Concept
        - Core Concept: OTA Concept
    4. Core Concept
        - Core Concept: OTA Concept
    5. Syntax
        - Syntax: OTA Concept
    6. Syntax
        - Syntax: OTA Concept
    7. Example
        - Example: OTA Concept
    8. Example
        - Example: OTA Concept
    9. Pitfall
        - Pitfall: OTA Concept
    10. Pitfall
        - Pitfall: OTA Concept
    11. Q & A
        - Q & A: OTA Concept
    12. Q & A
        - Q & A: OTA Concept
2. **Arduino OTA**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino OTA
    2. Overview
        - Overview: Arduino OTA
    3. Core Concept
        - Core Concept: Arduino OTA
    4. Core Concept
        - Core Concept: Arduino OTA
    5. Syntax
        - Syntax: Arduino OTA
    6. Syntax
        - Syntax: Arduino OTA
    7. Example
        - Example: Arduino OTA
    8. Example
        - Example: Arduino OTA
    9. Pitfall
        - Pitfall: Arduino OTA
    10. Pitfall
        - Pitfall: Arduino OTA
    11. Q & A
        - Q & A: Arduino OTA
    12. Q & A
        - Q & A: Arduino OTA
3. **HTTP OTA Update**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: HTTP OTA Update
    2. Overview
        - Overview: HTTP OTA Update
    3. Core Concept
        - Core Concept: HTTP OTA Update
    4. Core Concept
        - Core Concept: HTTP OTA Update
    5. Syntax
        - Syntax: HTTP OTA Update
    6. Syntax
        - Syntax: HTTP OTA Update
    7. Example
        - Example: HTTP OTA Update
    8. Example
        - Example: HTTP OTA Update
    9. Pitfall
        - Pitfall: HTTP OTA Update
    10. Pitfall
        - Pitfall: HTTP OTA Update
    11. Q & A
        - Q & A: HTTP OTA Update
    12. Q & A
        - Q & A: HTTP OTA Update
4. **Secure OTA**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Secure OTA
    2. Overview
        - Overview: Secure OTA
    3. Core Concept
        - Core Concept: Secure OTA
    4. Core Concept
        - Core Concept: Secure OTA
    5. Syntax
        - Syntax: Secure OTA
    6. Syntax
        - Syntax: Secure OTA
    7. Example
        - Example: Secure OTA
    8. Example
        - Example: Secure OTA
    9. Pitfall
        - Pitfall: Secure OTA
    10. Pitfall
        - Pitfall: Secure OTA
    11. Q & A
        - Q & A: Secure OTA
    12. Q & A
        - Q & A: Secure OTA
5. **Rollback and Verification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Rollback and Verification
    2. Overview
        - Overview: Rollback and Verification
    3. Core Concept
        - Core Concept: Rollback and Verification
    4. Core Concept
        - Core Concept: Rollback and Verification
    5. Syntax
        - Syntax: Rollback and Verification
    6. Syntax
        - Syntax: Rollback and Verification
    7. Example
        - Example: Rollback and Verification
    8. Example
        - Example: Rollback and Verification
    9. Pitfall
        - Pitfall: Rollback and Verification
    10. Pitfall
        - Pitfall: Rollback and Verification
    11. Q & A
        - Q & A: Rollback and Verification
    12. Q & A
        - Q & A: Rollback and Verification

#### 1.7.10. Module 10 — FreeRTOS on ESP32

1. **FreeRTOS Tasks on ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: FreeRTOS Tasks on ESP32
    2. Overview
        - Overview: FreeRTOS Tasks on ESP32
    3. Core Concept
        - Core Concept: FreeRTOS Tasks on ESP32
    4. Core Concept
        - Core Concept: FreeRTOS Tasks on ESP32
    5. Syntax
        - Syntax: FreeRTOS Tasks on ESP32
    6. Syntax
        - Syntax: FreeRTOS Tasks on ESP32
    7. Example
        - Example: FreeRTOS Tasks on ESP32
    8. Example
        - Example: FreeRTOS Tasks on ESP32
    9. Pitfall
        - Pitfall: FreeRTOS Tasks on ESP32
    10. Pitfall
        - Pitfall: FreeRTOS Tasks on ESP32
    11. Q & A
        - Q & A: FreeRTOS Tasks on ESP32
    12. Q & A
        - Q & A: FreeRTOS Tasks on ESP32
2. **Task Priorities**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Task Priorities
    2. Overview
        - Overview: Task Priorities
    3. Core Concept
        - Core Concept: Task Priorities
    4. Core Concept
        - Core Concept: Task Priorities
    5. Syntax
        - Syntax: Task Priorities
    6. Syntax
        - Syntax: Task Priorities
    7. Example
        - Example: Task Priorities
    8. Example
        - Example: Task Priorities
    9. Pitfall
        - Pitfall: Task Priorities
    10. Pitfall
        - Pitfall: Task Priorities
    11. Q & A
        - Q & A: Task Priorities
    12. Q & A
        - Q & A: Task Priorities
3. **Queues for Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Queues for Communication
    2. Overview
        - Overview: Queues for Communication
    3. Core Concept
        - Core Concept: Queues for Communication
    4. Core Concept
        - Core Concept: Queues for Communication
    5. Syntax
        - Syntax: Queues for Communication
    6. Syntax
        - Syntax: Queues for Communication
    7. Example
        - Example: Queues for Communication
    8. Example
        - Example: Queues for Communication
    9. Pitfall
        - Pitfall: Queues for Communication
    10. Pitfall
        - Pitfall: Queues for Communication
    11. Q & A
        - Q & A: Queues for Communication
    12. Q & A
        - Q & A: Queues for Communication
4. **Semaphores and Mutexes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Semaphores and Mutexes
    2. Overview
        - Overview: Semaphores and Mutexes
    3. Core Concept
        - Core Concept: Semaphores and Mutexes
    4. Core Concept
        - Core Concept: Semaphores and Mutexes
    5. Syntax
        - Syntax: Semaphores and Mutexes
    6. Syntax
        - Syntax: Semaphores and Mutexes
    7. Example
        - Example: Semaphores and Mutexes
    8. Example
        - Example: Semaphores and Mutexes
    9. Pitfall
        - Pitfall: Semaphores and Mutexes
    10. Pitfall
        - Pitfall: Semaphores and Mutexes
    11. Q & A
        - Q & A: Semaphores and Mutexes
    12. Q & A
        - Q & A: Semaphores and Mutexes
5. **Dual Core Programming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Dual Core Programming
    2. Overview
        - Overview: Dual Core Programming
    3. Core Concept
        - Core Concept: Dual Core Programming
    4. Core Concept
        - Core Concept: Dual Core Programming
    5. Syntax
        - Syntax: Dual Core Programming
    6. Syntax
        - Syntax: Dual Core Programming
    7. Example
        - Example: Dual Core Programming
    8. Example
        - Example: Dual Core Programming
    9. Pitfall
        - Pitfall: Dual Core Programming
    10. Pitfall
        - Pitfall: Dual Core Programming
    11. Q & A
        - Q & A: Dual Core Programming
    12. Q & A
        - Q & A: Dual Core Programming

#### 1.7.11. Module 11 — ESP32 Projects

1. **WiFi Sensor Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: WiFi Sensor Dashboard
    2. Overview
        - Overview: WiFi Sensor Dashboard
    3. Core Concept
        - Core Concept: WiFi Sensor Dashboard
    4. Core Concept
        - Core Concept: WiFi Sensor Dashboard
    5. Syntax
        - Syntax: WiFi Sensor Dashboard
    6. Syntax
        - Syntax: WiFi Sensor Dashboard
    7. Example
        - Example: WiFi Sensor Dashboard
    8. Example
        - Example: WiFi Sensor Dashboard
    9. Pitfall
        - Pitfall: WiFi Sensor Dashboard
    10. Pitfall
        - Pitfall: WiFi Sensor Dashboard
    11. Q & A
        - Q & A: WiFi Sensor Dashboard
    12. Q & A
        - Q & A: WiFi Sensor Dashboard
2. **MQTT Home Automation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT Home Automation
    2. Overview
        - Overview: MQTT Home Automation
    3. Core Concept
        - Core Concept: MQTT Home Automation
    4. Core Concept
        - Core Concept: MQTT Home Automation
    5. Syntax
        - Syntax: MQTT Home Automation
    6. Syntax
        - Syntax: MQTT Home Automation
    7. Example
        - Example: MQTT Home Automation
    8. Example
        - Example: MQTT Home Automation
    9. Pitfall
        - Pitfall: MQTT Home Automation
    10. Pitfall
        - Pitfall: MQTT Home Automation
    11. Q & A
        - Q & A: MQTT Home Automation
    12. Q & A
        - Q & A: MQTT Home Automation
3. **BLE Sensor Monitor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: BLE Sensor Monitor
    2. Overview
        - Overview: BLE Sensor Monitor
    3. Core Concept
        - Core Concept: BLE Sensor Monitor
    4. Core Concept
        - Core Concept: BLE Sensor Monitor
    5. Syntax
        - Syntax: BLE Sensor Monitor
    6. Syntax
        - Syntax: BLE Sensor Monitor
    7. Example
        - Example: BLE Sensor Monitor
    8. Example
        - Example: BLE Sensor Monitor
    9. Pitfall
        - Pitfall: BLE Sensor Monitor
    10. Pitfall
        - Pitfall: BLE Sensor Monitor
    11. Q & A
        - Q & A: BLE Sensor Monitor
    12. Q & A
        - Q & A: BLE Sensor Monitor
4. **OTA Updatable Device**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: OTA Updatable Device
    2. Overview
        - Overview: OTA Updatable Device
    3. Core Concept
        - Core Concept: OTA Updatable Device
    4. Core Concept
        - Core Concept: OTA Updatable Device
    5. Syntax
        - Syntax: OTA Updatable Device
    6. Syntax
        - Syntax: OTA Updatable Device
    7. Example
        - Example: OTA Updatable Device
    8. Example
        - Example: OTA Updatable Device
    9. Pitfall
        - Pitfall: OTA Updatable Device
    10. Pitfall
        - Pitfall: OTA Updatable Device
    11. Q & A
        - Q & A: OTA Updatable Device
    12. Q & A
        - Q & A: OTA Updatable Device
5. **Battery IoT Node**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Battery IoT Node
    2. Overview
        - Overview: Battery IoT Node
    3. Core Concept
        - Core Concept: Battery IoT Node
    4. Core Concept
        - Core Concept: Battery IoT Node
    5. Syntax
        - Syntax: Battery IoT Node
    6. Syntax
        - Syntax: Battery IoT Node
    7. Example
        - Example: Battery IoT Node
    8. Example
        - Example: Battery IoT Node
    9. Pitfall
        - Pitfall: Battery IoT Node
    10. Pitfall
        - Pitfall: Battery IoT Node
    11. Q & A
        - Q & A: Battery IoT Node
    12. Q & A
        - Q & A: Battery IoT Node

### 1.8. Raspberry Pi

#### 1.8.1. Module 1 — Raspberry Pi Fundamentals

1. **Raspberry Pi Hardware Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Inspecting Raspberry Pi System Specs via Terminal
    5. Pitfall
    6. Q & A
2. **Raspberry Pi OS Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Raspberry Pi OS Setup Example
    5. Pitfall
    6. Q & A
3. **Linux Command Line on Pi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Linux Command Line on Pi Example
    5. Pitfall
    6. Q & A
4. **GPIO Control with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi GPIO Control with Python Example
    5. Pitfall
    6. Q & A
5. **Pi Camera Module Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Pi Camera Module Setup Example
    5. Pitfall
    6. Q & A

#### 1.8.2. Module 2 — Interfacing and Sensors

1. **I2C and SPI on Raspberry Pi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi I2C and SPI on Raspberry Pi Example
    5. Pitfall
    6. Q & A
2. **Reading Analog Sensors via MCP3008 ADC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Reading Analog Sensors via MCP3008 ADC Example
    5. Pitfall
    6. Q & A
3. **UART Serial Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi UART Serial Communication Example
    5. Pitfall
    6. Q & A
4. **PWM and Servo Motor Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi PWM and Servo Motor Control Example
    5. Pitfall
    6. Q & A
5. **OLED Display Interfacing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi OLED Display Interfacing Example
    5. Pitfall
    6. Q & A

#### 1.8.3. Module 3 — IoT Edge Gateway and Server

1. **Mosquitto MQTT Broker on Pi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Mosquitto MQTT Broker on Pi Example
    5. Pitfall
    6. Q & A
2. **Node-RED Visual IoT Workflow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Node-RED Visual IoT Workflow Example
    5. Pitfall
    6. Q & A
3. **Flask Web Server for GPIO Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Flask Web Server for GPIO Control Example
    5. Pitfall
    6. Q & A
4. **Database Storage with SQLite & InfluxDB**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Database Storage with SQLite & InfluxDB Example
    5. Pitfall
    6. Q & A
5. **Deploying IoT Gateway in Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Deploying IoT Gateway in Docker Example
    5. Pitfall
    6. Q & A

### 1.9. IoT Hardware

#### 1.9.1. Module 1 — ESP32 Microcontroller Architecture & Environment Setup

1. **Lesson 1.1 ESP32 Hardware Architecture & Dual-Core Xtensa/RISC-V**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 System-on-Chip (SoC) Architecture
        - Critical GPIO Pin Classification
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are ESP32 Strapping Pins and why must engineers exercise caution when connecting external hardware components to them?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 Toolchain Setup (PlatformIO, ESP-IDF, & C++ Environment)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded Development Frameworks
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `platformio.ini` (PlatformIO Configuration File)
        - File: `src/main.cpp` (Embedded Entrypoint)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is PlatformIO preferred over Arduino IDE for professional embedded engineering?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.2. Module 2 — Peripherals, GPIO, & Communication Protocols

1. **Lesson 2.1 GPIO Digital Input/Output & Interrupt Service Routines (ISR)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Polling vs Hardware Interrupts
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must ESP32 Interrupt Service Routine (ISR) functions be declared with the `IRAM_ATTR` attribute?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 Analog-to-Digital Conversion (ADC) & Pulse Width Modulation (PWM)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 12-Bit Analog-to-Digital Conversion (ADC)
        - Hardware PWM via LEDC Peripheral
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should embedded engineers avoid connecting analog sensors to ADC2 pins on the ESP32 in connected IoT applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 2.3 Serial Communication Protocols (I2C, SPI, & UART)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serial Protocol Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `main.cpp` (I2C Bus Address Scanner & Dual Hardware UART)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare I2C and SPI protocols. When would you choose SPI over I2C in an embedded system design?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.3. Module 3 — Embedded Hardware & Peripherals

1. **23 Core Electrical Physics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 23 Core Electrical Physics
        - Core Embedded Hardware Concepts
    2. Lab Exercise
2. **24 Circuit Analysis Laws**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 24 Circuit Analysis Laws
        - Core Embedded Hardware Concepts
    2. Lab Exercise
3. **25 Diagnostic Measurement Instrumentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 25 Diagnostic Measurement Instrumentation
        - Core Embedded Hardware Concepts
    2. Lab Exercise
4. **26 Passive Components**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 26 Passive Components
        - Core Embedded Hardware Concepts
    2. Lab Exercise
5. **27 Semiconductor Diodes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 27 Semiconductor Diodes
        - Core Embedded Hardware Concepts
    2. Lab Exercise
6. **28 Bipolar Junction Transistors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 28 Bipolar Junction Transistors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
7. **29 Field Effect Transistors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 29 Field Effect Transistors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
8. **30 Operational Amplifiers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 30 Operational Amplifiers
        - Core Embedded Hardware Concepts
    2. Lab Exercise
9. **31 Power Supplies And Linear Regulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 31 Power Supplies And Linear Regulation
        - Core Embedded Hardware Concepts
    2. Lab Exercise
10. **32 Switched Mode Power Supplies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 32 Switched Mode Power Supplies
        - Core Embedded Hardware Concepts
    2. Lab Exercise
11. **33 Microcontroller Core Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 33 Microcontroller Core Architecture
        - Core Embedded Hardware Concepts
    2. Lab Exercise
12. **34 Clock Generation And Timing Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 34 Clock Generation And Timing Systems
        - Core Embedded Hardware Concepts
    2. Lab Exercise
13. **35 Gpio Electrical Characteristics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 35 Gpio Electrical Characteristics
        - Core Embedded Hardware Concepts
    2. Lab Exercise
14. **36 Interrupt Controllers And Nvic**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 36 Interrupt Controllers And Nvic
        - Core Embedded Hardware Concepts
    2. Lab Exercise
15. **37 Analog To Digital Converters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 37 Analog To Digital Converters
        - Core Embedded Hardware Concepts
    2. Lab Exercise
16. **38 Digital To Analog Converters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 38 Digital To Analog Converters
        - Core Embedded Hardware Concepts
    2. Lab Exercise
17. **39 Dma Controllers And Memory Transfer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 39 Dma Controllers And Memory Transfer
        - Core Embedded Hardware Concepts
    2. Lab Exercise
18. **40 Pulse Width Modulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 40 Pulse Width Modulation
        - Core Embedded Hardware Concepts
    2. Lab Exercise
19. **41 Uart Usart Serial Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 41 Uart Usart Serial Communication
        - Core Embedded Hardware Concepts
    2. Lab Exercise
20. **42 Spi Bus Protocol**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 42 Spi Bus Protocol
        - Core Embedded Hardware Concepts
    2. Lab Exercise
21. **43 I2C Bus Protocol**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 43 I2C Bus Protocol
        - Core Embedded Hardware Concepts
    2. Lab Exercise
22. **44 Can Bus Protocol**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 44 Can Bus Protocol
        - Core Embedded Hardware Concepts
    2. Lab Exercise
23. **45 Temperature And Humidity Sensors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 45 Temperature And Humidity Sensors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
24. **46 Motion And Inertial Measurement**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 46 Motion And Inertial Measurement
        - Core Embedded Hardware Concepts
    2. Lab Exercise
25. **47 Optical And Ranging Sensors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 47 Optical And Ranging Sensors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
26. **48 Environmental Gas Pressure Sensors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 48 Environmental Gas Pressure Sensors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
27. **49 Dc Motor Control H Bridges**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 49 Dc Motor Control H Bridges
        - Core Embedded Hardware Concepts
    2. Lab Exercise
28. **50 Stepper Motor Driving Microstepping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 50 Stepper Motor Driving Microstepping
        - Core Embedded Hardware Concepts
    2. Lab Exercise
29. **51 Servo Motor Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 51 Servo Motor Control
        - Core Embedded Hardware Concepts
    2. Lab Exercise
30. **52 Solenoids Relays Power Switching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 52 Solenoids Relays Power Switching
        - Core Embedded Hardware Concepts
    2. Lab Exercise
31. **53 Wifi Networking Esp Supplicant**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 53 Wifi Networking Esp Supplicant
        - Core Embedded Hardware Concepts
    2. Lab Exercise
32. **54 Ble Gap Gatt Profile Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 54 Ble Gap Gatt Profile Architecture
        - Core Embedded Hardware Concepts
    2. Lab Exercise
33. **55 Ieee 802 15 4 Zigbee Thread**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 55 Ieee 802 15 4 Zigbee Thread
        - Core Embedded Hardware Concepts
    2. Lab Exercise
34. **56 Lora And Lorawan Mac Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 56 Lora And Lorawan Mac Architecture
        - Core Embedded Hardware Concepts
    2. Lab Exercise
35. **57 Cellular Iot Nb Iot Cat M1**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 57 Cellular Iot Nb Iot Cat M1
        - Core Embedded Hardware Concepts
    2. Lab Exercise
36. **58 Battery Chemistry Cell Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 58 Battery Chemistry Cell Selection
        - Core Embedded Hardware Concepts
    2. Lab Exercise
37. **59 Battery Management Systems Bms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 59 Battery Management Systems Bms
        - Core Embedded Hardware Concepts
    2. Lab Exercise
38. **60 Energy Harvesting Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 60 Energy Harvesting Techniques
        - Core Embedded Hardware Concepts
    2. Lab Exercise
39. **61 Low Power Sleep Modes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 61 Low Power Sleep Modes
        - Core Embedded Hardware Concepts
    2. Lab Exercise
40. **62 Hardware Root Of Trust Secure Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 62 Hardware Root Of Trust Secure Elements
        - Core Embedded Hardware Concepts
    2. Lab Exercise
41. **63 Cryptographic Hardware Accelerators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 63 Cryptographic Hardware Accelerators
        - Core Embedded Hardware Concepts
    2. Lab Exercise
42. **64 Secure Boot And Flash Encryption**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 64 Secure Boot And Flash Encryption
        - Core Embedded Hardware Concepts
    2. Lab Exercise
43. **65 Jtag Swd On Chip Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 65 Jtag Swd On Chip Debugging
        - Core Embedded Hardware Concepts
    2. Lab Exercise
44. **66 Logic Analysers Protocol Decoding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 66 Logic Analysers Protocol Decoding
        - Core Embedded Hardware Concepts
    2. Lab Exercise
45. **67 Oscilloscope Signal Integrity**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 67 Oscilloscope Signal Integrity
        - Core Embedded Hardware Concepts
    2. Lab Exercise
46. **68 Hardware In Loop Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 68 Hardware In Loop Testing
        - Core Embedded Hardware Concepts
    2. Lab Exercise

#### 1.9.4. Module 4 — Real-Time Operating System (FreeRTOS Core Mechanics)

1. **Lesson 3.1 FreeRTOS Task Creation, Multi-Threading, & Core Pinning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS on ESP32?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `xTaskCreate()` and `xTaskCreatePinnedToCore()` in ESP32 FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 3.2 Task Priorities, Delays, & Stack Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pre-emptive Priority Scheduling
        - `vTaskDelay()` vs `vTaskDelayUntil()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `vTaskDelay()` and `vTaskDelayUntil()` in FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.5. Module 5 — FreeRTOS Inter-Task Communication & Synchronization

1. **Lesson 4.1 FreeRTOS Queues & Inter-Task Messaging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS Queues?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do FreeRTOS Queues achieve thread safety when sharing data between tasks running on different CPU cores?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Semaphores, Mutexes, & Concurrency Locks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Binary Semaphores vs Mutexes
        - What is Priority Inversion?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Priority Inversion and how do FreeRTOS Mutexes resolve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.6. Module 6 — Wi-Fi Networking & Wireless Connectivity

1. **Lesson 5.1 Wi-Fi Station (STA) Mode & Access Point (AP) Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 Wi-Fi Operating Modes
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Station (STA) Mode and Access Point (AP) Mode on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Non-Blocking Auto-Reconnect & Wi-Fi Event Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Asynchronous System Wi-Fi Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for IoT Wi-Fi reconnect logic?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.7. Module 7 — IoT Network Protocols: MQTT, HTTP REST, & WebSockets

1. **Lesson 6.1 HTTP REST Client Requests from ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded HTTP Client Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `http.end()` mandatory after executing an HTTP request with `HTTPClient` on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 MQTT Protocol & PubSubClient Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is MQTT?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare MQTT and HTTP protocols for resource-constrained IoT devices.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 ESP32 WebSocket Client for Real-Time Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why WebSockets for Microcontroller Telemetry?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should an embedded engineer choose WebSockets over MQTT for an IoT system architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.8. Module 8 — Low Power Modes & Deep Sleep Architecture

1. **Lesson 7.1 Deep Sleep Modes & RTC Memory Retention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Power Consumption Modes Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens to standard C++ global variables versus `RTC_DATA_ATTR` variables when the ESP32 enters Deep Sleep?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 Timer, Ext0/Ext1 GPIO, & Touch Wake-Up Triggers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Deep Sleep Wake-Up Sources Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Ext0 and Ext1 wake-up sources on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.9. Module 9 — Over-The-Air (OTA) Firmware Updates & Security

1. **Lesson 8.1 Over-The-Air (OTA) Firmware Updates**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Dual-Bank OTA Partition Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the ESP32 dual-bank partition table prevent device bricking during Over-The-Air (OTA) updates?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 8.2 Secure Boot, Flash Encryption, & Partition Tables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom Partition Tables
        - Hardware Security Primitives
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `partitions_custom.csv` (Custom 4MB Dual-OTA Partition Table)
        - File: `platformio.ini` (Configuring Custom Partition Table)
        - File: `main.cpp` (Querying Partition & Security Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Explain how Secure Boot V2 and Flash Encryption combine to secure ESP32 hardware in the field.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.10. Module 10 — Embedded Asynchronous Web Servers & Filesystems

1. **Lesson 9.1 Embedded Filesystems (SPIFFS / LittleFS) & Static File Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SPIFFS vs LittleFS
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `data/index.html` (Static Web Asset in PlatformIO `data/` Directory)
        - File: `src/main.cpp` (Mounting LittleFS & File I/O)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is LittleFS preferred over SPIFFS for modern ESP32 embedded applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 Asynchronous Embedded Web Servers & REST Control Endpoints**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Web Servers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `ESPAsyncWebServer` superior to the standard synchronous `WebServer.h` library for ESP32 applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.9.11. Module 11 — Full-Stack End-to-End IoT Capstone Architecture

1. **Lesson 10.1 Full-Stack IoT System Architecture & Protocol Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - End-to-End Full-Stack IoT Data Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `backend_bridge.py` (FastAPI + MQTT Ingestion Bridge)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is an MQTT message broker placed between embedded ESP32 devices and backend FastAPI microservices in full-stack IoT architectures?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 10.2 Course 6 Capstone Project - Production End-to-End IoT Gateway & Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Architecture Blueprint
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - ESP32 Production FreeRTOS Firmware (`src/main.cpp`)
        - FastAPI Ingestion & WebSockets Backend (`server.py`)
    6. Guided Step-by-Step Hands-On Exercise
    7. Industry Interview Q&A
        - Q1: How does this capstone architecture ensure high reliability and zero telemetry loss across network drops?
    8. Self-Assessment Quiz
    9. Summary & Cheat Sheet

### 1.10. Python

#### 1.10.1. Module 1 — Setup and Overview

1. **Python Overview and Philosophy**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Python?
    2. Python's Design Philosophy
    3. Python Versions
    4. Where Python is Used
    5. Python Interpreter Types
    6. Lab Exercise
2. **Environment Setup and Tooling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Installing Python
    2. Virtual Environments
    3. Package Management with pip
    4. Modern Tooling — uv (recommended 2024+)
    5. pyproject.toml
    6. Code Quality Tools
    7. REPL and Interactive Tools
    8. Lab Exercise
3. **CPython Architecture and Execution Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. How Python Code Executes
    2. Inspecting Bytecode
    3. The GIL (Global Interpreter Lock)
    4. Memory Management
        - Reference Counting
        - Garbage Collector (for cycles)
        - Object Interning
    5. `__pycache__` and .pyc Files
    6. Lab Exercise

#### 1.10.2. Module 2 — Core Fundamentals & Control Flow

1. **Lesson 1.5 Structural Pattern Matching (match/case)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `match/case` vs Legacy `if-elif-else`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes structural pattern matching different from C/Java `switch` statements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks

#### 1.10.3. Module 3 — Variables and Types

1. **Variables and Dynamic Typing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Variables in Python
    2. Dynamic vs Static Typing
    3. Type Annotations (Optional Static Hints)
    4. Duck Typing
    5. Identity vs Equality
    6. Lab Exercise
2. **Built-in Primitive Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Numeric Types
    2. Strings
    3. NoneType
    4. Type Conversion
    5. isinstance and type
    6. Lab Exercise
3. **Syntax Rules and Code Style**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Syntax Fundamentals
        - Indentation (Significant Whitespace)
        - Statements and Line Continuation
        - Comments
        - Docstrings
    2. PEP 8 Style Guide
    3. Naming Conventions Summary
    4. Lab Exercise

#### 1.10.4. Module 4 — Control Flow

1. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Operators Reference
        - Arithmetic Operators
        - Comparison Operators
        - Logical Operators (Short-Circuit)
        - Bitwise Operators
        - Identity and Membership
        - Walrus Operator `:=` (Python 3.8+)
        - Operator Precedence (high → low)
    2. Lab Exercise
2. **Conditional Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. if / elif / else
    2. Ternary (Conditional Expression)
    3. Truthy and Falsy Values
    4. Structural Pattern Matching — match/case (3.10+)
        - Matching Sequences and Structures
        - Matching Data Classes
    5. Lab Exercise
3. **Iteration and Loop Structures**
    - **Course Coverage:** 🟢 Covered in Class
    1. for Loops
    2. while Loops
    3. break, continue, else
    4. Advanced Iteration Patterns
    5. Lab Exercise

#### 1.10.5. Module 5 — Collections

1. **Lists and Sequence Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lists
    2. Modifying Lists
    3. Sorting
    4. List Comprehensions
    5. Copying Lists
    6. Lab Exercise
2. **Tuples and Immutable Sequences**
    - **Course Coverage:** 🟢 Covered in Class
    1. Tuples
    2. Why Tuples?
    3. Named Tuples
    4. typing.NamedTuple (Modern)
    5. Tuple vs List Decision
    6. Lab Exercise
3. **Dictionaries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dictionaries
    2. CRUD Operations
    3. Iterating Dictionaries
    4. Dictionary Comprehensions
    5. Advanced Dict Types
    6. Merging Dicts (3.9+)
    7. Lab Exercise
4. **Sets and Frozensets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sets
    2. Set Operations
    3. Modifying Sets
    4. Set Comprehensions
    5. Frozenset (Immutable Set)
    6. Practical Use Cases
    7. Lab Exercise
5. **Strings and Text Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. String Fundamentals
    2. String Formatting
    3. Essential String Methods
    4. Multi-line and Raw Strings
    5. String Encoding
    6. textwrap for Formatting
    7. Lab Exercise
6. **Advanced Collections Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. collections.Counter
    2. collections.deque (Double-Ended Queue)
    3. heapq — Priority Queue
    4. UserDict and UserList
    5. Lab Exercise

#### 1.10.6. Module 6 — Async Concurrency & Type Hinting

1. **Lesson 5.1 Static Type Hinting & Mypy Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Gradual Typing in Python
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Do Python type hints affect runtime execution speed?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks
2. **Lesson 5.2 Asyncio Event Loop & async/await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Execution
        - Python 3.11+ `TaskGroup` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is Asyncio multi-threaded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks
3. **Lesson 5.3 Modern Python Packaging (pyproject.toml & uv)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy `setup.py` vs Modern `pyproject.toml`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Modern `pyproject.toml` Manifest Specification
        - High-Speed `uv` CLI Commands
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `pyproject.toml` and why is it preferred over `requirements.txt`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks

#### 1.10.7. Module 7 — Functions

1. **Functions and Arguments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining Functions
    2. Parameter Types
    3. *args and **kwargs
    4. Default Argument Gotcha
    5. Return Values
    6. Higher-Order Functions
    7. Lab Exercise
2. **Functional Programming in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lambda Functions
    2. map, filter, reduce
    3. functools.partial
    4. functools.lru_cache (Memoization)
    5. operator module
    6. Immutability and Pure Functions
    7. Lab Exercise
3. **List Dict Set Comprehensions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Comprehension Syntax
    2. List Comprehensions
    3. Dict Comprehensions
    4. Set Comprehensions
    5. Generator Expressions
    6. Performance and Readability
    7. When NOT to Use Comprehensions
    8. Lab Exercise

#### 1.10.8. Module 8 — Advanced Python

1. **Closures and Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Closures
    2. The `nonlocal` Keyword
    3. Decorators
    4. Parametrized Decorators
    5. Stacked Decorators
    6. Practical Decorators
    7. Class-Based Decorators
    8. Lab Exercise
2. **Generators and Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Iterator Protocol
    2. Generator Functions
    3. Generator Expressions
    4. yield with send() and throw()
    5. itertools — Powerful Combinators
    6. Memory Comparison
    7. Lab Exercise

#### 1.10.9. Module 9 — Object-Oriented Programming

1. **Classes and Instance Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining a Class
    2. Properties
    3. `__slots__` — Memory Optimization
    4. Lab Exercise
2. **Inheritance and Polymorphism**
    - **Course Coverage:** 🟢 Covered in Class
    1. Single Inheritance
    2. `super()` and `__init__`
    3. Abstract Base Classes
    4. Method Resolution Order (MRO)
    5. Mixins
    6. Lab Exercise
3. **Magic Dunder Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Essential Dunder Methods
    2. Container Protocol
    3. Context Manager Protocol
    4. Callable Objects `__call__`
    5. Lab Exercise
4. **Dataclasses and Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. @dataclass
    2. Advanced dataclass Options
    3. TypedDict
    4. Protocol (Structural Subtyping)
    5. attrs Library
    6. Lab Exercise

#### 1.10.10. Module 10 — Exceptions and File I/O

1. **Exception Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Exception Hierarchy
    2. try / except / else / finally
    3. Exception Information
    4. Raising Exceptions
    5. Custom Exceptions
    6. contextlib.suppress
    7. ExceptionGroup (Python 3.11+)
    8. Lab Exercise
2. **Context Managers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Context Manager Protocol
    2. contextlib.contextmanager
    3. Practical Examples
    4. contextlib.ExitStack
    5. Async Context Managers
    6. Lab Exercise
3. **Logging Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Logging Overview
    2. Log Levels
    3. Production Logger Setup
    4. Logging Exceptions
    5. Structured Logging with structlog
    6. Lab Exercise

#### 1.10.11. Module 11 — File I/O and Serialisation

1. **File I/O and Paths**
    - **Course Coverage:** 🟢 Covered in Class
    1. File Operations
    2. File Modes
    3. pathlib — Modern Path Handling
    4. CSV and JSON Files
    5. Lab Exercise
2. **Data Serialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. JSON
    2. pickle — Python Object Serialization
    3. YAML (requires PyYAML)
    4. TOML (Python 3.11+ built-in)
    5. Pydantic Serialization
    6. orjson — Fast JSON
    7. Lab Exercise

#### 1.10.12. Module 12 — Regular Expressions

1. **Regular Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. re Module Basics
    2. Regex Syntax Reference
    3. Groups and Named Groups
    4. sub and subn
    5. Compiled Patterns
    6. Lookahead and Lookbehind
    7. Lab Exercise

#### 1.10.13. Module 13 — s and Packages

1. **Modules and Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Importing Modules
    2. Module Attributes
    3. Package Structure
    4. Relative Imports
    5. sys.path and Import Resolution
    6. importlib — Dynamic Imports
    7. Lab Exercise

#### 1.10.14. Module 14 — Concurrency

1. **Asyncio and Async/Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Async/Await Fundamentals
    2. Tasks — Fire and Forget
    3. Async HTTP with aiohttp
    4. asyncio Primitives
    5. Async Context Managers and Generators
    6. Lab Exercise
2. **Threading and Multiprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Threading
    2. Thread Synchronization
    3. concurrent.futures — High-Level Interface
    4. multiprocessing — True Parallelism
    5. When to Use What
    6. Lab Exercise

#### 1.10.15. Module 15 — Scientific Python

1. **NumPy Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. NumPy Basics
    2. Indexing and Slicing
    3. Vectorized Operations (No Loops!)
    4. Broadcasting
    5. Matrix Operations
    6. Lab Exercise
2. **Pandas Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pandas Basics
    2. Selection and Filtering
    3. Essential Operations
    4. GroupBy
    5. Merge and Join
    6. Lab Exercise
3. **Matplotlib and Visualization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Matplotlib Basics
    2. Common Plot Types
    3. Subplots
    4. Seaborn — Statistical Plots
    5. Lab Exercise
4. **Hardware Interfacing with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Raspberry Pi GPIO
    2. gpiozero — Higher Level
    3. PySerial — UART Communication
    4. smbus2 — I2C Communication
    5. MicroPython
    6. Lab Exercise

#### 1.10.16. Module 16 — Debugging and Testing

1. **Debugging and Profiling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Debugger (pdb)
        - pdb Commands
    2. Profiling with cProfile
    3. timeit — Micro-Benchmarking
    4. Memory Profiling
    5. Line Profiler
    6. Lab Exercise
2. **Testing with Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pytest Basics
    2. Fixtures
    3. Parametrize
    4. Mocking
    5. Coverage
    6. Property-Based Testing with Hypothesis
    7. Lab Exercise

### 1.11. HTML5

#### 1.11.1. Module 1 — Web & Browser Architecture Fundamentals

1. **Lesson 1.1 Web Architecture & Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client-Server Architecture
        - The Request-Response Cycle
        - HTTP vs HTTPS Protocols
        - HTTP Request Methods (Verbs)
        - HTTP Status Codes Classification
        - Web Servers vs Application Servers
        - Identifiers: URI, URL, and URN
        - Domain Name System (DNS) Resolution Tracing
    4. Architecture & Diagram Visualizations
        - DNS Resolution & HTTP Request Sequence
    5. Code & Hardware Implementation
        - Deconstructing Raw HTTP/1.1 Request and Response Payload
        - Command Line Inspection with cURL
    6. Enterprise Real-World Applications
        - Case Study: High-Throughput IoT Gateway Architecture
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Web Request Lifecycle using Chrome DevTools & Python
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens under the hood when you type `https://example.com` into a browser address bar and press Enter?
        - Q2: What is the technical difference between HTTP `POST`, `PUT`, and `PATCH` methods?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Code
        - Success Criteria
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax & Command Cheat Sheet
        - Official References
2. **Lesson 1.2 Browser Rendering Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anatomy of a Modern Web Browser
        - Major Browser Engines
        - The 5 Stages of the Rendering Pipeline
        - Reflow vs Repaint Trigger Comparison
    4. Architecture & Diagram Visualizations
        - Critical Rendering Path Architecture
    5. Code & Hardware Implementation
        - Script Execution Blocking Modes (`async` vs `defer`)
    6. Enterprise Real-World Applications
        - Critical CSS Inline Pattern for Enterprise E-Commerce
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Profile Reflow & Layout Thrashing in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Reflow and Repaint, and how do you minimize them?
        - Q2: How does the browser construct the Render Tree, and why are `display: none` elements excluded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Requirements
        - Starter Code Snippet
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Cheat Sheet
        - Official References
3. **Lesson 1.3 HTML Standards & Document Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of HTML Standards
        - The DOCTYPE Declaration & Rendering Modes
        - Root Element (`<html>`) & Language Attribute
        - Character Encodings (ASCII vs UTF-8)
        - Viewport Configuration for Mobile Responsiveness
        - Metadata & Social Media Protocol (Open Graph)
    4. Architecture & Diagram Visualizations
        - Complete HTML5 Document Architecture Tree
    5. Code & Hardware Implementation
        - Production-Ready HTML5 Boilerplate Template
    6. Enterprise Real-World Applications
        - Open Graph Debugging & Rich Social Cards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build & Validate an Enterprise Boilerplate
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Standards Mode and Quirks Mode in modern browsers?
        - Q2: Why is the WHATWG specification referred to as a "Living Standard"?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References

#### 1.11.2. Module 2 — HTML Syntax, Text Formatting, & Hyperlinks

1. **Lesson 2.1 Syntax Rules & Element Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Tag Syntax & Element Composition
        - Standard Elements vs Void (Self-Closing) Elements
        - Attribute Categories
        - Block-Level vs Inline-Level vs Inline-Block
        - Element Nesting Rules & DOM Tree Integrity
        - HTML Entity Encoding & Escaping
    4. Architecture & Diagram Visualizations
        - Block vs Inline Box Model Layout Geometry
    5. Code & Hardware Implementation
        - Demonstrating Block, Inline, and Data Attributes
    6. Enterprise Real-World Applications
        - Data Attributes in Modern Web Frameworks & IoT Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspecting Box Geometry & Dataset Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact visual difference between Block-level, Inline-level, and Inline-Block elements?
        - Q2: What are HTML Void Elements, and how do they differ from standard elements in DOM parsing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
2. **Lesson 2.2 Text Content & Formatting Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Heading Hierarchy (`<h1>` through `<h6>`)
        - Semantic vs Presentational Text Formatting
        - Computer Code & Technical Documentation Elements
        - Quotations, Citations, & Abbreviations
        - Bidirectional Text Formatting (`<bdo>` & `<bdi>`)
    4. Architecture & Diagram Visualizations
        - Accessible Heading Tree Outline
    5. Code & Hardware Implementation
        - Technical Documentation Markup Example
    6. Enterprise Real-World Applications
        - Accessible Developer Portals & CLI Documentation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Technical Quick Reference Sheet
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the semantic difference between `<strong>` and `<b>`, and `<em>` and `<i>`?
        - Q2: How do `<bdo>` and `<bdi>` differ when handling internationalized text?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
3. **Lesson 2.3 Hyperlinks & Anchor Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anchor Element Architecture
        - URL Types & Path Resolution Rules
        - Fragment Identifiers & In-Page Jumping
        - Link Targets & Vulnerability Hardening (`tabnabbing`)
        - Non-HTML Protocols & Devices Integration
        - Download Attribute & Resource Hints
    4. Architecture & Diagram Visualizations
        - Reverse Tabnabbing Attack vs Hardened Fix
    5. Code & Hardware Implementation
        - Comprehensive Navigation Portal (`navigation_demo.html`)
    6. Enterprise Real-World Applications
        - Multi-Tenant SaaS & IoT Gateway Navigation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Reverse Tabnabbing Security in Browser Console
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What security risk is introduced by `target="_blank"`, and how does `rel="noopener"` fix it?
        - Q2: What is the difference between `<link rel="prefetch">` and `<link rel="preload">`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References

#### 1.11.3. Module 3 — Semantic HTML5 & Document Layout Architecture

1. **Lesson 3.1 Structural Semantic Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Semantic Web Philosophy
        - Structural Landmark Elements
        - Content Sectioning Elements
        - Interactive Native Components
        - Figures, Captions & Machine-Readable Time
    4. Architecture & Diagram Visualizations
        - Complete Semantic HTML5 Web Page Layout
    5. Code & Hardware Implementation
        - Semantic Web Page Implementation (`semantic_layout.html`)
    6. Enterprise Real-World Applications
        - Native Dialog Modals vs Heavy JS Libraries
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Native Dialog & Details Accordion
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact semantic distinction between an `<article>` and a `<section>`?
        - Q2: How does the native HTML5 `<dialog>` element improve accessibility over custom `<div>` modals?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
2. **Lesson 3.2 Document Outline & Accessibility Tree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Accessibility Tree (AOM) Architecture
        - HTML5 Semantic Elements vs ARIA Landmark Roles
        - Core ARIA Attributes & Properties
        - Keyboard Focus Management & `tabindex` Rules
    4. Architecture & Diagram Visualizations
        - DOM Tree vs Accessibility Tree Mapping
    5. Code & Hardware Implementation
        - Fully Accessible Component Suite (`accessible_suite.html`)
    6. Enterprise Real-World Applications
        - Automated Accessibility Testing in CI/CD Pipelines
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Audit Accessibility Tree Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `tabindex="0"`, `tabindex="-1"`, and `tabindex="1"`?
        - Q2: How does `aria-live="polite"` differ from `aria-live="assertive"`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References

#### 1.11.4. Module 4 — Data Organization: Lists & Tables

1. **Lesson 4.1 List Elements & Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unordered Lists (`<ul>`) & Ordered Lists (`<ol>`)
        - Description Lists (`<dl>`, `<dt>`, `<dd>`)
        - Nesting Rules for Lists
    4. Architecture & Diagram Visualizations
        - List Tree DOM Structure
    5. Code & Hardware Implementation
        - Semantic Navigation & Metadata Lists
    6. Enterprise Real-World Applications
        - Accessible Navigation Menus
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Nested IoT Setup Procedure List
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use a Description List (`<dl>`) instead of an Unordered List (`<ul>`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Tabular Data & Advanced Table Markup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic Table Architecture
        - Cell Spanning (`colspan` & `rowspan`)
        - Column Groups (`<colgroup>` & `<col>`)
        - Table Accessibility & Header Scoping
        - Responsive Mobile Table Patterns
    4. Architecture & Diagram Visualizations
        - Accessible Table DOM Hierarchy
    5. Code & Hardware Implementation
        - Complex Accessible Matrix Table (`matrix_table.html`)
    6. Enterprise Real-World Applications
        - Financial Reports & System Metrics Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Accessible Headers in DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of the `scope` attribute on `<th>` elements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.11.5. Module 5 — Forms, Inputs, & Client-Side Validation

1. **Lesson 5.1 Form Architecture & Submissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Form Architecture
        - Key `<form>` Attributes
        - HTTP Submission Methods: GET vs POST
        - Encoding Types (`enctype`)
    4. Architecture & Diagram Visualizations
        - Form Submission Payload Pipeline
    5. Code & Hardware Implementation
        - File Upload & Search Form Examples
    6. Enterprise Real-World Applications
        - Firmware Uploads & Cloud API Integration
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Payload Formats in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a developer omits `enctype="multipart/form-data"` on a form containing a file input?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Form Controls & Input Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Label Association (`<label>`)
        - Form Controls Classification Matrix
        - Form Grouping & Visual Metering
    4. Architecture & Diagram Visualizations
        - Accessible Form Fieldset Hierarchy
    5. Code & Hardware Implementation
        - IoT Device Configuration Form (`iot_config_form.html`)
    6. Enterprise Real-World Applications
        - Soft-Keyboards & Mobile Optimization
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<select>` dropdowns and `<datalist>` autocomplete inputs?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 5.3 Native Client-Side Form Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native Validation Attributes
        - CSS Validation Pseudo-Classes
        - The Constraint Validation API (JavaScript)
    4. Architecture & Diagram Visualizations
        - Constraint Validation Flow
    5. Code & Hardware Implementation
        - Custom Validation & RegEx Portal (`validation_portal.html`)
    6. Enterprise Real-World Applications
        - Client-Side Validation is NOT Security
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `ValidityState` in the HTML5 Constraint Validation API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.11.6. Module 6 — Multimedia, Embedded Content, & Graphics

1. **Lesson 6.1 Media Elements: Images, Audio, & Video**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Responsive Images (`srcset` & `sizes`)
        - Art Direction (`<picture>`)
        - Audio & Video Elements
    4. Architecture & Diagram Visualizations
        - Media Selection Pipeline
    5. Code & Hardware Implementation
        - Comprehensive Media Dashboard (`media_dashboard.html`)
    6. Enterprise Real-World Applications
        - AVIF & WebP Next-Gen Image Compression
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<img srcset>` and the `<picture>` tag?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 Embedded External Content**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Inline Frames (`<iframe>`)
        - Iframe Security Sandboxing (`sandbox` & `allow`)
    4. Architecture & Diagram Visualizations
        - Iframe Sandboxing Boundary
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
        - Embedded Grafana & OpenStreetMap Widgets
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does an empty `sandbox=""` attribute do on an iframe?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Vector Graphics & HTML5 Canvas**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SVG vs Canvas Comparison Matrix
        - SVG Primitives (`<svg>`)
        - HTML5 Canvas 2D API (`<canvas>`)
    4. Architecture & Diagram Visualizations
        - SVG (DOM Retained) vs Canvas (Pixel Immediate)
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main architectural difference between SVG and Canvas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.11.7. Module 7 — HTML5 Advanced APIs & Storage Mechanisms

1. **Lesson 7.2 Geolocation & Device APIs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Geolocation API
        - Position & Error Objects
    4. Architecture & Diagram Visualizations
        - Geolocation Permission Loop
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does Geolocation require HTTPS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.3 HTML5 Drag and Drop API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Drag and Drop Lifecycle
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `event.preventDefault()` required in the `dragover` handler?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 7.4 Web Workers & Multithreading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded JS & Web Workers Solution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Main Application Thread (`app.js`)
        - Background Worker Script (`worker.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Web Worker access `localStorage` or DOM elements directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.11.8. Module 8 — Web Components & Modern HTML Specifications

1. **Lesson 8.1 Shadow DOM & Custom Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Web Components Suite
        - Custom Element Lifecycle Callbacks
        - Shadow DOM Encapsulation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main purpose of the Shadow DOM in Web Components?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.11.9. Module 9 — Accessibility (a11y), SEO, & Performance Optimization

1. **Lesson 9.1 Web Content Accessibility Guidelines (WCAG)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The POUR Principles (WCAG 2.1 / 2.2)
        - Conformance Levels
        - Color Contrast Requirements (Level AA)
        - Skip Navigation Links
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the four WCAG POUR principles?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 Search Engine Optimization (SEO) & Microdata**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON-LD vs Microdata
        - JSON-LD Implementation Example
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is JSON-LD preferred over Microdata for SEO?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 9.3 Performance Optimization & Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Resource Hints Summary
        - Native Lazy Loading (`loading="lazy"`)
        - Obsolete & Deprecated HTML Tags
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `preload` and `prefetch`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 1.12. CSS3

#### 1.12.1. Module 1 — Core Fundamentals, Syntax, & Specificity Architecture

1. **Lesson 1.1 CSS Syntax & Inclusion Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Syntax Anatomy
        - Inclusion Methods Comparison
        - CSS At-Rules (`@`)
    4. Architecture & Diagram Visualizations
        - External CSS Loading vs `@import` Performance Waterfall
    5. Code & Hardware Implementation
        - External Stylesheet Architecture
    6. Enterprise Real-World Applications
        - Avoiding HTTP Request Waterfalls
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance disadvantages of using `@import` inside CSS files?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 Comprehensive Selector Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Attribute Selectors
        - Combinator Systems
        - Pseudo-Classes & Modern `:has()` Parent Selector
        - Pseudo-Elements (`::before` & `::after`)
    4. Architecture & Diagram Visualizations
        - Combinator Target Matching Tree
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `:nth-child()` and `:nth-of-type()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 1.3 Cascade, Specificity, & Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Cascade Algorithm
        - Specificity Calculation Vector Matrix `(A, B, C, D)`
        - Cascade Layers (`@layer`) Architecture
    4. Architecture & Diagram Visualizations
        - Cascade Layer Precedence Hierarchy
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do `@layer` declarations alter standard specificity calculations?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.2. Module 2 — The Box Model, Sizing, & Layout Fundamentals

1. **Lesson 2.1 The CSS Box Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Box Model Layers
        - `content-box` vs `border-box`
        - Margin Collapsing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `box-sizing: border-box` preferred over `content-box`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 Display Property & Visual Formatting Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Block Formatting Context (BFC) Triggers
        - `display: none` vs `visibility: hidden` vs `opacity: 0`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the modern standard property for creating a Block Formatting Context?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 2.3 Positioning Systems & Stacking Contexts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Position Modes Matrix
        - Stacking Contexts & $Z$-Index Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does a child with `z-index: 9999` fail to render above an element with `z-index: 2`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 2.4 Sizing Units & Intrinsic Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Categories Matrix
        - Intrinsic Sizing Keywords
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `1rem` and `1em`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.3. Module 3 — Modern Layout Engine: Flexbox & CSS Grid

1. **Lesson 3.1 Flexible Box Layout (Flexbox)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flexbox Axes System
        - Main Axis vs Cross Axis Alignment
        - Flex Item Sizing (`flex: grow shrink basis`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `flex: 1` expand to in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 3.2 CSS Grid Layout System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D Grid vs 1D Flexbox
        - Fractional Unit (`fr`) & `minmax()`
        - Named Grid Areas (`grid-template-areas`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `auto-fill` and `auto-fit` in CSS Grid?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.4. Module 4 — Typography, Colors, Backgrounds, & Visual Effects

1. **Lesson 4.1 Advanced Typography & Web Fonts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@font-face` Syntax & WOFF2
        - Micro-Typography & Line Clamping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `font-display: swap` in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Modern CSS Color Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of CSS Color Functions
        - The `color-mix()` Function
        - The `currentcolor` Keyword
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes `oklch()` superior to traditional `hsl()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 4.3 Backgrounds, Borders, & Shadows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Gradient Types
        - Box Shadow Layering (`box-shadow`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between blur-radius and spread-radius in a `box-shadow` property?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 4.4 Visual Effects, Filters, & Blending**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Glassmorphism & `backdrop-filter`
        - Clipping Paths (`clip-path`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `filter: blur()` differ from `backdrop-filter: blur()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.5. Module 5 — Transitions, 2D/3D Transforms, & Animations

1. **Lesson 5.1 CSS Transitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Transition Properties & Shorthand
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid animating `height` or `margin` properties?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 2D and 3D Transformations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D vs 3D Transform Functions
        - 3D Card Flipping Setup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `transform-style: preserve-3d` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 5.3 Keyframe Animations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@keyframes` Syntax & Shorthand
        - `animation-fill-mode`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `animation-fill-mode: forwards` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.6. Module 6 — Responsive Web Design, Media Queries, & Container Queries

1. **Lesson 6.1 Responsive Architecture Principles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mobile-First vs Desktop-First
        - The Viewport Meta Tag
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Mobile-First CSS architecture preferred over Desktop-First?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 Media Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Modern Range Syntax (Level 4)
        - User Preference Media Features
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `prefers-reduced-motion` and why is it important for accessibility?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Container Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Media Queries vs Container Queries
        - Setting Up Container Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main problem Container Queries solve that Media Queries could not?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 6.4 Fluid Layout Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Math Functions (`calc`, `min`, `max`, `clamp`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the three parameters passed to `clamp()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.7. Module 7 — Advanced CSS Architecture & Modern Specifications

1. **Lesson 7.1 CSS Custom Properties (Variables)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Syntax & Scoping
        - Typed Custom Properties (`@property`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Custom Properties differ from Sass/SCSS variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 Modern CSS Architecture & Methodologies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - BEM Naming Convention Syntax
        - ITCSS (Inverted Triangle CSS) Layers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does BEM stand for and what are its advantages?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 7.3 Native CSS Nesting & Logical Properties**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native CSS Nesting (`&`)
        - Physical vs Logical Properties Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the benefit of Logical Properties over Physical Properties in modern CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.12.8. Module 8 — CSS Frameworks Intro & Production Performance

1. **Lesson 8.1 Utility-First CSS & Tailwind Introduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic CSS vs Utility-First CSS
        - Component Extraction (`@apply`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main benefit of Utility-First CSS over traditional semantic CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 8.2 Component Frameworks & Component Styling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Modules Hashing Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Modules prevent global CSS class name collisions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 8.3 Production CSS Performance, Purging, & Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Critical CSS Extraction
        - GPU Layer Promotion (`will-change`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Critical CSS and why does inlining it improve performance?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 1.13. Bootstrap

#### 1.13.1. Module 1 — Grid System and Layout

1. **Bootstrap Grid System**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Bootstrap 12-Column Grid
        - Breakpoints
    2. Grid HTML Structure
    3. Equal Width vs Specific Widths
    4. Lab Exercise
2. **Responsive Utilities and Display**
    - **Course Coverage:** 🟢 Covered in Class
    1. Display Property Utilities
        - Classes Format
        - Common Display Values
    2. Responsive Hiding & Showing
    3. Lab Exercise
3. **Flexbox and Alignment Utilities**
    - **Course Coverage:** 🟢 Covered in Class
    1. Flexbox Utility Classes
    2. Lab Exercise
4. **Bootstrap Layout Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Common Bootstrap Layout Patterns
        - Holy Grail / Dashboard Layout
    2. Lab Exercise

#### 1.13.2. Module 2 — Typography and Utilities

1. **Typography System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Typography Helpers & Text Styling
    2. Lab Exercise
2. **Color Palette and Themes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Theme Colors
    2. Lab Exercise
3. **Spacing Utilities**
    - **Course Coverage:** 🟢 Covered in Class
    1. Spacing Notation
    2. Lab Exercise
4. **Borders Shadows and Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Borders, Radius, Shadows, and Sizing
    2. Lab Exercise

#### 1.13.3. Module 3 — Core Components

1. **Buttons and Button Groups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Buttons & Grouping
    2. Lab Exercise
2. **Cards and Accordions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Cards and Accordions
    2. Lab Exercise
3. **Navbars and Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Navbar Component
    2. Lab Exercise
4. **Forms and Input Groups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Form Controls and Input Groups
    2. Lab Exercise
5. **Modals and Tooltips**
    - **Course Coverage:** 🟢 Covered in Class
    1. Modals and Tooltips
    2. Lab Exercise

#### 1.13.4. Module 4 — Advanced Layout and Customization

1. **Flexbox Layout Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Deep Dive into Flexbox Helpers
    2. Lab Exercise
2. **CSS Grid in Bootstrap**
    - **Course Coverage:** 🟢 Covered in Class
    1. Opt-in CSS Grid System
    2. Lab Exercise
3. **Customizing Sass Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Customizing Bootstrap with SCSS
    2. Lab Exercise
4. **Utility API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Bootstrap Utility API
    2. Lab Exercise
5. **Capstone Portfolio Landing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Capstone Project: Developer Portfolio Landing Page
    2. Lab Exercise

### 1.14. JavaScript

#### 1.14.1. Module 1 — Language Architecture, Engine, & Execution Mechanics

1. **Lesson 1.1 History, Evolution, & ECMAScript Standards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - TC39 Proposal Process
        - Transpilers vs Polyfills
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Babel Configuration Setup (`babel.config.json`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between a Babel transpiler and a polyfill?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 JavaScript Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The V8 Engine Execution Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are Ignition and TurboFan in the Google Chrome V8 engine?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 1.3 Execution Context, Call Stack, & Memory Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Execution Context Lifecycle
        - Mark-and-Sweep Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Mark-and-Sweep Garbage Collection in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.2. Module 2 — Variables, Data Types, & Operators

1. **Lesson 2.1 Variable Declarations & Scoping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `var` vs `let` vs `const`
        - The Temporal Dead Zone (TDZ)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 Primitive & Reference Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Primitives vs Reference Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 7 primitive data types in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 2.3 Type Coercion & Comparison Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 8 Falsy Values in JavaScript
        - Abstract (`==`) vs Strict (`===`) Equality
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 8 falsy values in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 2.4 Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `||` vs `??` (Nullish Coalescing)
        - Optional Chaining (`?.`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Nullish Coalescing Operator (`??`) differ from the Logical OR Operator (`||`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.3. Module 3 — Control Flow, Loops, & Iteration Protocols

1. **Lesson 3.1 Conditional Logic & Guard Clauses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Guard Clauses vs Nested Arrow Code
        - Object Lookup Tables
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Guard Clause and why is it preferred over nested `if-else` blocks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 3.2 Loops & Iteration Constructs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `for...in` vs `for...of`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `for...in` and `for...of` in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 3.3 Iteration Protocols, Iterators, & Generators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Iterable & Iterator Protocols
        - Generator Functions (`function*`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does a Generator function differ from a regular function in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.4. Module 4 — Functions, Scope, & Closures

1. **Lesson 4.1 Function Declarations, Expressions, & Arrow Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Declarations vs Expressions vs Arrow Functions
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the `this` keyword behave differently in Arrow Functions compared to Regular Functions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Parameters, Arguments, & Return Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Rest Parameters (`...args`) vs `arguments` Object
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main advantage of Rest Parameters (`...args`) over the `arguments` object?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 4.3 Scope Chain & Closures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Lexical Scoping & Scope Chain
        - What is a Closure?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a JavaScript Closure and how does it retain memory?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 4.4 Functional Concepts & Higher-Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pure Functions vs Side Effects
        - Currying
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Currying in Functional JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.5. Module 5 — Objects, Arrays, & Data Structures

1. **Lesson 5.1 Object Literals, Descriptors, & Immutability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object Immutability Levels
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `Object.freeze()` and `Object.seal()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Arrays & Array Higher-Order Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mutating vs Non-Mutating Methods
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `.reduce()` work in JavaScript and what is the role of the initial value parameter?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 5.3 Destructuring Assignment & Spread/Rest Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unpacking Data Structures
        - Spread (`...`) for Immutable Merging
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you rename a variable during Object Destructuring in ES6?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 5.4 Keyed Collections: Map, Set, WeakMap, & WeakSet**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Plain Object vs `Map`
        - `WeakMap` & `WeakSet` Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why can you not iterate over a `WeakMap` or check its size?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.6. Module 6 — Asynchronous JavaScript, Promises, & Async/Await

1. **Lesson 6.1 Asynchronous Execution, Callbacks, & Event Queue**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Event Loop & Task Queue Priority
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Macrotask Queue and Microtask Queue in the JavaScript Event Loop?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 ES6 Promises Architecture, States, & Chaining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise States & Immutability
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a `.then()` callback returns a plain scalar value versus another Promise?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Async/Await & Asynchronous Iteration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Async/Await as Syntactic Sugar
        - Asynchronous Iteration (`for await...of`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when the `await` keyword is executed in an `async` function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 6.4 Promise Combinators (all, allSettled, race, any)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise Combinators Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between `Promise.all()` and `Promise.allSettled()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.7. Module 7 — Object-Oriented Programming, Classes, & Prototypes

1. **Lesson 7.1 Prototypes, Prototype Chain, & Prototypal Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Prototypal Inheritance vs Class-Based Inheritance
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when a property is accessed on a JavaScript object that does not exist on the instance itself?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 ES6 Class Syntax & Constructor Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Classes as Syntactic Sugar
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Are ES6 classes true classes like in Java or C++?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 7.3 Inheritance, Method Overriding, & Super Keyword**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Subclassing & Mandatory `super()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 7.4 Private Fields, Getters/Setters, & Static Members**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Hard Encapsulation (`#privateField`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do modern `#` private fields in JavaScript differ from the legacy `_` prefix convention?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.8. Module 8 — Document Object Model (DOM) Manipulation & Events

1. **Lesson 8.1 DOM Tree Navigation & Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `querySelectorAll` (NodeList) vs `getElementsByClassName` (HTMLCollection)
        - Upward Traversal with `.closest()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between a live `HTMLCollection` and a static `NodeList`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 8.2 Dynamic Element Creation, Modification, & Attributes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `appendChild()` vs `append()`
        - HTML5 `dataset` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the HTML5 `dataset` API in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 8.3 Event Handling, Propagation, Bubbling, & Capturing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 3 Event Propagation Phases
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `event.target` and `event.currentTarget`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 8.4 Event Delegation & Custom Event Dispatching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Event Delegation Architecture
        - Custom Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the primary benefits of using the Event Delegation Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.9. Module 9 — Web APIs, Client-Side Storage, & Network Requests

1. **Lesson 9.1 Fetch API & HTTP Network Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `fetch()` HTTP Status Code Trap
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does `fetch()` not reject when a server returns a 404 or 500 error code?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 Web Storage: Cookies, LocalStorage, & SessionStorage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main security risk of storing authentication tokens in LocalStorage compared to HttpOnly Cookies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 9.4 WebSockets & Real-Time Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for WebSocket reconnection strategies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.10. Module 10 — ES6+ Modules, Tooling, & Bundlers

1. **Lesson 10.1 ES6 Modules: Export & Import Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CommonJS (`require`) vs ES Modules (`import`)
        - Named vs Default Exports
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `mathUtils.js` (Module)
        - File 2: `main.js` (Consumer)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural advantage of ES Modules over CommonJS `require()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 10.2 Dynamic Imports & Top-Level Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Static Imports vs Dynamic `import()`
        - Top-Level Await
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Code Splitting and how do Dynamic Imports facilitate it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 10.3 Modern Build Tooling, Bundlers, & Tree Shaking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy Bundlers (Webpack) vs Modern Native ESM (Vite)
        - Tree Shaking Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Initializing a Lightning-Fast Vite Project
        - Production Build & Source Map Inspection
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Tree Shaking in modern JavaScript build tools and how does it work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.11. Module 11 — Browser Performance, Security, & Optimization

1. **Lesson 11.1 Critical Rendering Path & DOM Reflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Critical Rendering Path
        - Reflow vs Repaint vs Layout Thrashing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Layout Thrashing in JavaScript and how do you prevent it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 11.2 Core Web Vitals & Performance Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Google Core Web Vitals Metrics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Interaction to Next Paint (INP) and how does it differ from FID?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 11.3 Memory Management & Leak Prevention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mark-and-Sweep Garbage Collection
        - The 4 Common Memory Leak Patterns
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Detached DOM Node memory leak in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 11.4 Web Security: XSS, CSRF, & CSP Mitigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - XSS vs CSRF Vulnerability Matrix
        - Content Security Policy (CSP)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Content Security Policy (CSP) and how does it prevent XSS attacks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.14.12. Module 12 — Advanced Patterns, Meta-Programming, & Testing

1. **Lesson 12.1 Proxy & Reflect API Meta-Programming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Meta-Programming?
        - Proxy Traps & Reflect API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `Reflect` methods inside Proxy handler traps instead of accessing the target directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 12.2 Web Workers & Multithreaded JavaScript**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded Main Loop vs Worker Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `worker.js` (Background Thread)
        - File 2: `main.js` (UI Thread)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What capabilities and Web APIs are accessible inside a Web Worker?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 12.3 Service Workers & Offline PWA Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Service Worker Proxy Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `sw.js` (Service Worker Script)
        - File 2: `app.js` (Register Service Worker)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Stale-While-Revalidate caching strategy work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 12.4 JavaScript Unit Testing with Vitest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The AAA Unit Testing Pattern
        - `toBe` vs `toEqual`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Target Module: `math.js`
        - Vitest Test Suite: `math.test.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `toBe` and `toEqual` in Vitest/Jest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
5. **Lesson 12.5 Integration & E2E Testing with Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Testing vs End-to-End (E2E) Testing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Playwright Test Suite: `dashboard.spec.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Playwright preferred over older Selenium or Puppeteer testing frameworks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
6. **Lesson 12.6 Design Patterns: Singleton, Factory, & Observer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Design Patterns Categories
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between the Observer Pattern and the Publisher-Subscriber (PubSub) Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
7. **Lesson 12.7 Internationalization (Intl API)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Native ECMAScript `Intl` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance advantages of using the native `Intl` API over external libraries like Moment.js?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
8. **Lesson 12.8 Web Components & Shadow DOM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Web Components Technologies
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Usage in HTML:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Custom Element tag names contain a hyphen (`-`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
9. **Lesson 12.9 WebAssembly (Wasm) Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WebAssembly (Wasm)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is WebAssembly intended to replace JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
10. **Lesson 12.10 Debugging Techniques & Chrome DevTools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Advanced Breakpoint Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Logpoint in Chrome DevTools and how does it differ from a standard Breakpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
11. **Lesson 12.11 Capstone: Real-Time IoT Telemetry Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Enterprise Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Reactive State Store (`store.js`)
        - Capstone Dashboard Application (`app.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does this Vanilla JavaScript Capstone architecture achieve high performance without a frontend framework like React?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

## 2. Term 2

### 2.1. Advanced Components

#### 2.1.1. Module 1 — Power, Protection, and Signal Integrity

1. **Power Regulation and Distribution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Linear versus switching regulators
    2. Power budgets, efficiency, thermal limits, and decoupling
    3. Battery charging and protection fundamentals
2. **Circuit Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Reverse polarity, overcurrent, overvoltage, and ESD protection
    2. Fuses, TVS diodes, isolation, and grounding
    3. Design protection for field wiring and inductive loads
3. **Signal Integrity**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pull-ups, termination, impedance, crosstalk, and noise
    2. Level shifting and logic-voltage compatibility
    3. Lab: diagnose noisy digital and analog signals

#### 2.1.2. Module 2 — Precision Sensors and Analog Front Ends

1. **Sensor Interfaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Resistive, capacitive, current-loop, bridge, and frequency-output sensors
    2. Calibration, linearization, accuracy, precision, and uncertainty
    3. Environmental compensation and sensor placement
2. **Analog Front-End Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Operational amplifiers, instrumentation amplifiers, and filters
    2. ADC resolution, reference voltage, sampling, and aliasing
    3. Low-noise layout and grounding practices
3. **Measurement Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Read a low-level sensor through a conditioned ADC path
    2. Calibrate against a reference
    3. Document error budget and repeatability

#### 2.1.3. Module 3 — Drivers, Actuators, and Motion

1. **Power Switching**
    - **Course Coverage:** 🟢 Covered in Class
    1. BJT and MOSFET operation as switches
    2. Gate/base drive, flyback protection, and heat dissipation
    3. PWM control of LEDs, heaters, and DC loads
2. **Motor and Actuator Drivers**
    - **Course Coverage:** 🟢 Covered in Class
    1. DC, stepper, servo, relay, and solenoid interfaces
    2. H-bridges, current limiting, and motion feedback
    3. Safe startup, stop, stall, and fault behavior
3. **Control Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Build a closed-loop actuator subsystem
    2. Measure current, temperature, and response
    3. Implement hardware and firmware interlocks

#### 2.1.4. Module 4 — Industrial Interfaces and Timing

1. **Robust Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Differential signaling and RS-485 fundamentals
    2. CAN bus concepts, termination, arbitration, and diagnostics
    3. Isolation and surge protection for industrial buses
2. **Timing and Expansion**
    - **Course Coverage:** 🟢 Covered in Class
    1. RTC, watchdog, timers, counters, and clock sources
    2. GPIO expanders, multiplexers, and shift registers
    3. Interrupt design and deterministic event handling
3. **Interface Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Integrate multiple I2C/SPI peripherals
    2. Capture and decode bus traffic
    3. Handle address conflicts, timeouts, retries, and bus recovery

#### 2.1.5. Module 5 — Integration, Validation, and Capstone

1. **Component Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Datasheet limits, tolerances, derating, and lifecycle
    2. Package, availability, substitution, and cost
    3. Create a requirements-to-component decision matrix
2. **Prototype Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Bring-up checklist and test points
    2. Oscilloscope, logic analyzer, electronic load, and thermal inspection
    3. EMI/EMC awareness and pre-compliance checks
3. **Capstone: Rugged Sensor-Control Board**
    - **Course Coverage:** 🟢 Covered in Class
    1. Design power, sensing, communication, and actuator stages
    2. Validate normal, boundary, and fault conditions
    3. Produce schematic notes, BOM rationale, test report, and demo

### 2.2. PCB Design

#### 2.2.1. Module 1 — EDA & PCB Engineering

1. **01 Electronic Component Packaging Standards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 01 Electronic Component Packaging Standards
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
2. **01 Fundamentals For Pcb Layout Engineers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 01 Fundamentals For Pcb Layout Engineers
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
3. **01 Pcb Materials And Physical Layers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 01 Pcb Materials And Physical Layers
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
4. **02 Custom Schematic Symbol Creation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 02 Custom Schematic Symbol Creation
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
5. **02 Eda Software And Kicad Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 02 Eda Software And Kicad Fundamentals
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
6. **02 Schematic Capture Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 02 Schematic Capture Best Practices
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
7. **03 Component Placement Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 03 Component Placement Strategies
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
8. **03 Footprint Creation And Ipc 7351**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 03 Footprint Creation And Ipc 7351
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
9. **03 Pcb Stackup Design And Layer Assignment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 03 Pcb Stackup Design And Layer Assignment
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
10. **04 Differential Pair Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 04 Differential Pair Routing
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
11. **04 High Speed Routing And Controlled Impedance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 04 High Speed Routing And Controlled Impedance
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
12. **04 Trace Width Current Capacity And Clearance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 04 Trace Width Current Capacity And Clearance
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
13. **05 Decoupling Capacitor Placement And Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 05 Decoupling Capacitor Placement And Routing
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
14. **05 Ground Plane Design And Stitching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 05 Ground Plane Design And Stitching
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
15. **05 Pdn Power Distribution Network Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 05 Pdn Power Distribution Network Design
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
16. **06 Crosstalk Mitigation And Trace Spacing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 06 Crosstalk Mitigation And Trace Spacing
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
17. **06 Emi Emc Design Guidelines For Pcbs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 06 Emi Emc Design Guidelines For Pcbs
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
18. **06 Signal Integrity Fundamentals For Pcb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 06 Signal Integrity Fundamentals For Pcb
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
19. **07 Bom Bill Of Materials Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 07 Bom Bill Of Materials Generation
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
20. **07 Design Rule Checking Drc And Erc**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 07 Design Rule Checking Drc And Erc
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
21. **07 Gerber And Nc Drill File Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 07 Gerber And Nc Drill File Generation
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
22. **08 Assembly Drawings And Pick And Place**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 08 Assembly Drawings And Pick And Place
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
23. **08 Pcb Fabrication Processes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 08 Pcb Fabrication Processes
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
24. **08 Smt Reflow And Wave Soldering Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 08 Smt Reflow And Wave Soldering Design
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
25. **09 01 Flexible And Rigid Flex Pcb Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 09 01 Flexible And Rigid Flex Pcb Design
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
26. **09 02 Rf Pcb Design Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 09 02 Rf Pcb Design Fundamentals
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
27. **09 03 Thermal Management And Heat Sinks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 09 03 Thermal Management And Heat Sinks
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise
28. **09 04 Capstone Custom Esp32 Iot Board Pcb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 09 04 Capstone Custom Esp32 Iot Board Pcb
        - Key CAD/EDA Engineering Concepts
    2. Lab Exercise

### 2.3. STM32

#### 2.3.1. Module 1 — STM32 Introduction

1. **STM32 Family Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Python Script to Query STM32 Part Selection Matrix
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **STM32 Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Configuring Clock Tree (HSE 8MHz to 72MHz System Clock via PLL)
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **STM32CubeIDE Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Standard Structure of main.c in STM32CubeIDE
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **STM32CubeMX**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Configuring GPIO Output in CubeMX and Controlling via HAL Code
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **HAL Library Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - Polling vs Interrupt vs DMA HAL UART Transmission Pattern
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 2.3.2. Module 2 — STM32 Peripherals

1. **GPIO in STM32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 GPIO in STM32 Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **UART in STM32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 UART in STM32 Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **SPI in STM32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 SPI in STM32 Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **I2C in STM32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 I2C in STM32 Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **ADC in STM32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 ADC in STM32 Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 2.3.3. Module 3 — Timers and PWM

1. **Basic Timers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 Basic Timers Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **General Purpose Timers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 General Purpose Timers Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **PWM Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 PWM Generation Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Input Capture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 Input Capture Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **RTC Real-Time Clock**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 RTC Real-Time Clock Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 2.3.4. Module 4 — DMA and Low Power

1. **DMA Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 DMA Fundamentals Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **DMA with UART and SPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 DMA with UART and SPI Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **STM32 Low Power Modes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 STM32 Low Power Modes Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **RTC Wakeup from Stop Mode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 RTC Wakeup from Stop Mode Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Power Profiling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 Power Profiling Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 2.3.5. Module 5 — FreeRTOS on STM32

1. **FreeRTOS on STM32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 FreeRTOS on STM32 Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Task Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 Task Communication Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Memory Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 Memory Management Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **STM32 RTOS Project**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 STM32 RTOS Project Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **STM32 Production Checklist**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - STM32 STM32 Production Checklist Implementation Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

### 2.4. Basic MATLAB

#### 2.4.1. Module 1 — MATLAB Environment and Matrix Foundations

1. **Workspace and Tooling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Command Window, Editor, Workspace, and documentation
    2. Scripts, live scripts, variables, and path management
    3. Lab: create and run a reproducible analysis script
2. **Arrays and Matrices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Vectors, matrices, indexing, slicing, and concatenation
    2. Element-wise versus matrix operations
    3. Colon operator, logical indexing, and vectorization
3. **Data Types and Import**
    - **Course Coverage:** 🟢 Covered in Class
    1. Numeric, logical, string, categorical, table, and timetable data
    2. Import text, spreadsheet, and MAT files
    3. Inspect, clean, and export a small dataset

#### 2.4.2. Module 2 — Programming with MATLAB

1. **Control Flow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Conditional statements and switch
    2. for and while loops
    3. Preallocation and vectorized alternatives
2. **Functions and Code Organization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Function inputs, outputs, scope, and validation
    2. Local functions and reusable utilities
    3. Error handling and defensive programming
3. **Debugging and Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Breakpoints, stepping, and variable inspection
    2. Assertions and basic unit tests
    3. Lab: refactor and test a numerical program

#### 2.4.3. Module 3 — Data Analysis and Visualization

1. **Numerical and Statistical Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Descriptive statistics and missing data
    2. Interpolation, curve fitting, and numerical integration
    3. Solve linear systems and inspect conditioning
2. **Plotting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Line, scatter, bar, histogram, and surface plots
    2. Labels, legends, layouts, annotations, and export
    3. Create publication-ready and dashboard-style figures
3. **Analysis Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Import and clean experimental data
    2. Compute statistics and fit a model
    3. Communicate findings with annotated plots

#### 2.4.4. Module 4 — Signals, Systems, and Simulation Basics

1. **Signal Processing Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sampling, frequency, aliasing, and noise
    2. Filtering and moving-window operations
    3. FFT-based spectral inspection
2. **Dynamic Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Difference and differential equation concepts
    2. Transfer functions and state-space overview
    3. Step response and stability interpretation
3. **Simulation Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Generate and analyze a sampled signal
    2. Design and compare simple filters
    3. Simulate a first-order system response

#### 2.4.5. Module 5 — Engineering Workflow and Capstone

1. **Performance and Reproducibility**
    - **Course Coverage:** 🟢 Covered in Class
    1. Profiling, vectorization, and memory awareness
    2. Project folders, data provenance, and parameter files
    3. Reports and automated figure generation
2. **Hardware and External Data Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Serial communication and instrument data concepts
    2. Reading sensor logs and timestamped telemetry
    3. Preparing algorithms for embedded implementation
3. **Capstone: Sensor Data Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Acquire or import a multichannel dataset
    2. Clean, analyze, visualize, and model the data
    3. Deliver code, tests, figures, and an engineering report

### 2.5. Git Fundamentals

#### 2.5.1. Module 1 — Introduction

1. **Web Architecture And Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client-Server Architecture
        - The Request-Response Cycle
        - HTTP vs HTTPS Protocols
        - HTTP Request Methods (Verbs)
        - HTTP Status Codes Classification
        - Web Servers vs Application Servers
        - Identifiers: URI, URL, and URN
        - Domain Name System (DNS) Resolution Tracing
    4. Architecture & Diagram Visualizations
        - DNS Resolution & HTTP Request Sequence
    5. Code & Hardware Implementation
        - Deconstructing Raw HTTP/1.1 Request and Response Payload
        - Command Line Inspection with cURL
    6. Enterprise Real-World Applications
        - Case Study: High-Throughput IoT Gateway Architecture
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Web Request Lifecycle using Chrome DevTools & Python
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens under the hood when you type `https://example.com` into a browser address bar and press Enter?
        - Q2: What is the technical difference between HTTP `POST`, `PUT`, and `PATCH` methods?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Code
        - Success Criteria
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax & Command Cheat Sheet
        - Official References
2. **Browser Rendering Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anatomy of a Modern Web Browser
        - Major Browser Engines
        - The 5 Stages of the Rendering Pipeline
        - Reflow vs Repaint Trigger Comparison
    4. Architecture & Diagram Visualizations
        - Critical Rendering Path Architecture
    5. Code & Hardware Implementation
        - Script Execution Blocking Modes (`async` vs `defer`)
    6. Enterprise Real-World Applications
        - Critical CSS Inline Pattern for Enterprise E-Commerce
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Profile Reflow & Layout Thrashing in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Reflow and Repaint, and how do you minimize them?
        - Q2: How does the browser construct the Render Tree, and why are `display: none` elements excluded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Requirements
        - Starter Code Snippet
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Cheat Sheet
        - Official References
3. **Html Standards And Document Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of HTML Standards
        - The DOCTYPE Declaration & Rendering Modes
        - Root Element (`<html>`) & Language Attribute
        - Character Encodings (ASCII vs UTF-8)
        - Viewport Configuration for Mobile Responsiveness
        - Metadata & Social Media Protocol (Open Graph)
    4. Architecture & Diagram Visualizations
        - Complete HTML5 Document Architecture Tree
    5. Code & Hardware Implementation
        - Production-Ready HTML5 Boilerplate Template
    6. Enterprise Real-World Applications
        - Open Graph Debugging & Rich Social Cards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build & Validate an Enterprise Boilerplate
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Standards Mode and Quirks Mode in modern browsers?
        - Q2: Why is the WHATWG specification referred to as a "Living Standard"?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
4. **Html Syntax Rules And Element Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Tag Syntax & Element Composition
        - Standard Elements vs Void (Self-Closing) Elements
        - Attribute Categories
        - Block-Level vs Inline-Level vs Inline-Block
        - Element Nesting Rules & DOM Tree Integrity
        - HTML Entity Encoding & Escaping
    4. Architecture & Diagram Visualizations
        - Block vs Inline Box Model Layout Geometry
    5. Code & Hardware Implementation
        - Demonstrating Block, Inline, and Data Attributes
    6. Enterprise Real-World Applications
        - Data Attributes in Modern Web Frameworks & IoT Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspecting Box Geometry & Dataset Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact visual difference between Block-level, Inline-level, and Inline-Block elements?
        - Q2: What are HTML Void Elements, and how do they differ from standard elements in DOM parsing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
5. **Text Content And Formatting Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Heading Hierarchy (`<h1>` through `<h6>`)
        - Semantic vs Presentational Text Formatting
        - Computer Code & Technical Documentation Elements
        - Quotations, Citations, & Abbreviations
        - Bidirectional Text Formatting (`<bdo>` & `<bdi>`)
    4. Architecture & Diagram Visualizations
        - Accessible Heading Tree Outline
    5. Code & Hardware Implementation
        - Technical Documentation Markup Example
    6. Enterprise Real-World Applications
        - Accessible Developer Portals & CLI Documentation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Technical Quick Reference Sheet
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the semantic difference between `<strong>` and `<b>`, and `<em>` and `<i>`?
        - Q2: How do `<bdo>` and `<bdi>` differ when handling internationalized text?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
6. **Hyperlinks And Anchor Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anchor Element Architecture
        - URL Types & Path Resolution Rules
        - Fragment Identifiers & In-Page Jumping
        - Link Targets & Vulnerability Hardening (`tabnabbing`)
        - Non-HTML Protocols & Devices Integration
        - Download Attribute & Resource Hints
    4. Architecture & Diagram Visualizations
        - Reverse Tabnabbing Attack vs Hardened Fix
    5. Code & Hardware Implementation
        - Comprehensive Navigation Portal (`navigation_demo.html`)
    6. Enterprise Real-World Applications
        - Multi-Tenant SaaS & IoT Gateway Navigation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Reverse Tabnabbing Security in Browser Console
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What security risk is introduced by `target="_blank"`, and how does `rel="noopener"` fix it?
        - Q2: What is the difference between `<link rel="prefetch">` and `<link rel="preload">`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
7. **Structural Semantic Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Semantic Web Philosophy
        - Structural Landmark Elements
        - Content Sectioning Elements
        - Interactive Native Components
        - Figures, Captions & Machine-Readable Time
    4. Architecture & Diagram Visualizations
        - Complete Semantic HTML5 Web Page Layout
    5. Code & Hardware Implementation
        - Semantic Web Page Implementation (`semantic_layout.html`)
    6. Enterprise Real-World Applications
        - Native Dialog Modals vs Heavy JS Libraries
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Native Dialog & Details Accordion
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact semantic distinction between an `<article>` and a `<section>`?
        - Q2: How does the native HTML5 `<dialog>` element improve accessibility over custom `<div>` modals?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
8. **Document Outline And Accessibility Tree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Accessibility Tree (AOM) Architecture
        - HTML5 Semantic Elements vs ARIA Landmark Roles
        - Core ARIA Attributes & Properties
        - Keyboard Focus Management & `tabindex` Rules
    4. Architecture & Diagram Visualizations
        - DOM Tree vs Accessibility Tree Mapping
    5. Code & Hardware Implementation
        - Fully Accessible Component Suite (`accessible_suite.html`)
    6. Enterprise Real-World Applications
        - Automated Accessibility Testing in CI/CD Pipelines
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Audit Accessibility Tree Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `tabindex="0"`, `tabindex="-1"`, and `tabindex="1"`?
        - Q2: How does `aria-live="polite"` differ from `aria-live="assertive"`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
9. **List Elements And Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unordered Lists (`<ul>`) & Ordered Lists (`<ol>`)
        - Description Lists (`<dl>`, `<dt>`, `<dd>`)
        - Nesting Rules for Lists
    4. Architecture & Diagram Visualizations
        - List Tree DOM Structure
    5. Code & Hardware Implementation
        - Semantic Navigation & Metadata Lists
    6. Enterprise Real-World Applications
        - Accessible Navigation Menus
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Nested IoT Setup Procedure List
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use a Description List (`<dl>`) instead of an Unordered List (`<ul>`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
10. **Tabular Data And Advanced Table Markup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic Table Architecture
        - Cell Spanning (`colspan` & `rowspan`)
        - Column Groups (`<colgroup>` & `<col>`)
        - Table Accessibility & Header Scoping
        - Responsive Mobile Table Patterns
    4. Architecture & Diagram Visualizations
        - Accessible Table DOM Hierarchy
    5. Code & Hardware Implementation
        - Complex Accessible Matrix Table (`matrix_table.html`)
    6. Enterprise Real-World Applications
        - Financial Reports & System Metrics Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Accessible Headers in DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of the `scope` attribute on `<th>` elements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
11. **Form Architecture And Submissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Form Architecture
        - Key `<form>` Attributes
        - HTTP Submission Methods: GET vs POST
        - Encoding Types (`enctype`)
    4. Architecture & Diagram Visualizations
        - Form Submission Payload Pipeline
    5. Code & Hardware Implementation
        - File Upload & Search Form Examples
    6. Enterprise Real-World Applications
        - Firmware Uploads & Cloud API Integration
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Payload Formats in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a developer omits `enctype="multipart/form-data"` on a form containing a file input?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
12. **Form Controls And Input Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Label Association (`<label>`)
        - Form Controls Classification Matrix
        - Form Grouping & Visual Metering
    4. Architecture & Diagram Visualizations
        - Accessible Form Fieldset Hierarchy
    5. Code & Hardware Implementation
        - IoT Device Configuration Form (`iot_config_form.html`)
    6. Enterprise Real-World Applications
        - Soft-Keyboards & Mobile Optimization
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<select>` dropdowns and `<datalist>` autocomplete inputs?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
13. **Native Client Side Form Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native Validation Attributes
        - CSS Validation Pseudo-Classes
        - The Constraint Validation API (JavaScript)
    4. Architecture & Diagram Visualizations
        - Constraint Validation Flow
    5. Code & Hardware Implementation
        - Custom Validation & RegEx Portal (`validation_portal.html`)
    6. Enterprise Real-World Applications
        - Client-Side Validation is NOT Security
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `ValidityState` in the HTML5 Constraint Validation API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
14. **Media Elements Images Audio And Video**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Responsive Images (`srcset` & `sizes`)
        - Art Direction (`<picture>`)
        - Audio & Video Elements
    4. Architecture & Diagram Visualizations
        - Media Selection Pipeline
    5. Code & Hardware Implementation
        - Comprehensive Media Dashboard (`media_dashboard.html`)
    6. Enterprise Real-World Applications
        - AVIF & WebP Next-Gen Image Compression
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<img srcset>` and the `<picture>` tag?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
15. **Embedded External Content**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Inline Frames (`<iframe>`)
        - Iframe Security Sandboxing (`sandbox` & `allow`)
    4. Architecture & Diagram Visualizations
        - Iframe Sandboxing Boundary
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
        - Embedded Grafana & OpenStreetMap Widgets
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does an empty `sandbox=""` attribute do on an iframe?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
16. **Vector Graphics And Html5 Canvas**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SVG vs Canvas Comparison Matrix
        - SVG Primitives (`<svg>`)
        - HTML5 Canvas 2D API (`<canvas>`)
    4. Architecture & Diagram Visualizations
        - SVG (DOM Retained) vs Canvas (Pixel Immediate)
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main architectural difference between SVG and Canvas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
17. **Web Storage And Indexeddb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Matrix
        - LocalStorage & SessionStorage API
        - Storage Event Cross-Tab Sync
        - IndexedDB Architecture
    4. Architecture & Diagram Visualizations
        - IndexedDB Transaction Architecture
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is IndexedDB preferred over LocalStorage for offline-first web apps?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
18. **Geolocation And Device Apis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Geolocation API
        - Position & Error Objects
    4. Architecture & Diagram Visualizations
        - Geolocation Permission Loop
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does Geolocation require HTTPS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
19. **Html5 Drag And Drop Api**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Drag and Drop Lifecycle
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `event.preventDefault()` required in the `dragover` handler?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
20. **Web Workers And Multithreading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded JS & Web Workers Solution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Main Application Thread (`app.js`)
        - Background Worker Script (`worker.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Web Worker access `localStorage` or DOM elements directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
21. **Shadow Dom And Custom Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Web Components Suite
        - Custom Element Lifecycle Callbacks
        - Shadow DOM Encapsulation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main purpose of the Shadow DOM in Web Components?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
22. **Web Content Accessibility Guidelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The POUR Principles (WCAG 2.1 / 2.2)
        - Conformance Levels
        - Color Contrast Requirements (Level AA)
        - Skip Navigation Links
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the four WCAG POUR principles?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
23. **Search Engine Optimization And Microdata**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON-LD vs Microdata
        - JSON-LD Implementation Example
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is JSON-LD preferred over Microdata for SEO?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
24. **Performance Optimization And Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Resource Hints Summary
        - Native Lazy Loading (`loading="lazy"`)
        - Obsolete & Deprecated HTML Tags
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `preload` and `prefetch`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
25. **Css Syntax And Inclusion Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Syntax Anatomy
        - Inclusion Methods Comparison
        - CSS At-Rules (`@`)
    4. Architecture & Diagram Visualizations
        - External CSS Loading vs `@import` Performance Waterfall
    5. Code & Hardware Implementation
        - External Stylesheet Architecture
    6. Enterprise Real-World Applications
        - Avoiding HTTP Request Waterfalls
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance disadvantages of using `@import` inside CSS files?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
26. **Comprehensive Selector Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Attribute Selectors
        - Combinator Systems
        - Pseudo-Classes & Modern `:has()` Parent Selector
        - Pseudo-Elements (`::before` & `::after`)
    4. Architecture & Diagram Visualizations
        - Combinator Target Matching Tree
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `:nth-child()` and `:nth-of-type()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
27. **Cascade Specificity And Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Cascade Algorithm
        - Specificity Calculation Vector Matrix `(A, B, C, D)`
        - Cascade Layers (`@layer`) Architecture
    4. Architecture & Diagram Visualizations
        - Cascade Layer Precedence Hierarchy
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do `@layer` declarations alter standard specificity calculations?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
28. **The Css Box Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Box Model Layers
        - `content-box` vs `border-box`
        - Margin Collapsing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `box-sizing: border-box` preferred over `content-box`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
29. **Display Property And Visual Formatting Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Block Formatting Context (BFC) Triggers
        - `display: none` vs `visibility: hidden` vs `opacity: 0`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the modern standard property for creating a Block Formatting Context?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
30. **Positioning Systems And Stacking Contexts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Position Modes Matrix
        - Stacking Contexts & $Z$-Index Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does a child with `z-index: 9999` fail to render above an element with `z-index: 2`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
31. **Sizing Units And Intrinsic Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Categories Matrix
        - Intrinsic Sizing Keywords
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `1rem` and `1em`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
32. **Flexible Box Layout Flexbox**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flexbox Axes System
        - Main Axis vs Cross Axis Alignment
        - Flex Item Sizing (`flex: grow shrink basis`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `flex: 1` expand to in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
33. **Css Grid Layout System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D Grid vs 1D Flexbox
        - Fractional Unit (`fr`) & `minmax()`
        - Named Grid Areas (`grid-template-areas`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `auto-fill` and `auto-fit` in CSS Grid?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
34. **Advanced Typography And Web Fonts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@font-face` Syntax & WOFF2
        - Micro-Typography & Line Clamping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `font-display: swap` in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
35. **Modern Css Color Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of CSS Color Functions
        - The `color-mix()` Function
        - The `currentcolor` Keyword
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes `oklch()` superior to traditional `hsl()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
36. **Backgrounds Borders And Shadows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Gradient Types
        - Box Shadow Layering (`box-shadow`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between blur-radius and spread-radius in a `box-shadow` property?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
37. **Visual Effects Filters And Blending**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Glassmorphism & `backdrop-filter`
        - Clipping Paths (`clip-path`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `filter: blur()` differ from `backdrop-filter: blur()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
38. **Css Transitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Transition Properties & Shorthand
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid animating `height` or `margin` properties?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
39. **2D And 3D Transformations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D vs 3D Transform Functions
        - 3D Card Flipping Setup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `transform-style: preserve-3d` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
40. **Keyframe Animations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@keyframes` Syntax & Shorthand
        - `animation-fill-mode`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `animation-fill-mode: forwards` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
41. **Responsive Architecture Principles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mobile-First vs Desktop-First
        - The Viewport Meta Tag
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Mobile-First CSS architecture preferred over Desktop-First?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
42. **Media Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Modern Range Syntax (Level 4)
        - User Preference Media Features
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `prefers-reduced-motion` and why is it important for accessibility?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
43. **Container Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Media Queries vs Container Queries
        - Setting Up Container Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main problem Container Queries solve that Media Queries could not?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
44. **Fluid Layout Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Math Functions (`calc`, `min`, `max`, `clamp`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the three parameters passed to `clamp()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
45. **Css Custom Properties Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Syntax & Scoping
        - Typed Custom Properties (`@property`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Custom Properties differ from Sass/SCSS variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
46. **Modern Css Architecture And Methodologies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - BEM Naming Convention Syntax
        - ITCSS (Inverted Triangle CSS) Layers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does BEM stand for and what are its advantages?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
47. **Native Css Nesting And Logical Properties**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native CSS Nesting (`&`)
        - Physical vs Logical Properties Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the benefit of Logical Properties over Physical Properties in modern CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
48. **Utility First Css And Tailwind Introduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic CSS vs Utility-First CSS
        - Component Extraction (`@apply`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main benefit of Utility-First CSS over traditional semantic CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
49. **Component Frameworks And Component Styling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Modules Hashing Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Modules prevent global CSS class name collisions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
50. **Production Css Performance Purging And Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Critical CSS Extraction
        - GPU Layer Promotion (`will-change`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Critical CSS and why does inlining it improve performance?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
51. **History Evolution And Ecmascript Standards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - TC39 Proposal Process
        - Transpilers vs Polyfills
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Babel Configuration Setup (`babel.config.json`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between a Babel transpiler and a polyfill?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
52. **Javascript Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The V8 Engine Execution Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are Ignition and TurboFan in the Google Chrome V8 engine?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
53. **Execution Context Call Stack And Memory Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Execution Context Lifecycle
        - Mark-and-Sweep Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Mark-and-Sweep Garbage Collection in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
54. **Variable Declarations And Scoping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `var` vs `let` vs `const`
        - The Temporal Dead Zone (TDZ)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
55. **Primitive And Reference Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Primitives vs Reference Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 7 primitive data types in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
56. **Type Coercion And Comparison Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 8 Falsy Values in JavaScript
        - Abstract (`==`) vs Strict (`===`) Equality
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 8 falsy values in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
57. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `||` vs `??` (Nullish Coalescing)
        - Optional Chaining (`?.`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Nullish Coalescing Operator (`??`) differ from the Logical OR Operator (`||`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
58. **Vectors Matrices And Vector Spaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Vectors & The Dot Product
        - Matrix Multiplication Geometry
        - Linear Independence & Span
    4. Architecture & Diagram Visualizations
        - Matrix Multiplication Inner Dimension Match
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the geometric interpretation of the dot product between two normalized vectors?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
59. **Probability Fundamentals And Axioms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Kolmogorov Probability Axioms
        - Bayes' Theorem
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Prior Probability and Posterior Probability in Bayes' Theorem?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
60. **Parametric Hypothesis Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Error Matrix & Statistical Power
        - Two-Sample Independent $t$-Test
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a $p$-value in hypothesis testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
61. **Non Parametric Statistical Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parametric vs Non-Parametric Decision Matrix
        - Bootstrapping Resampling
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Bootstrapping and why is it useful in Data Science?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
62. **Python 312 Structural Pattern Matching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `match/case` vs Legacy `if-elif-else`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes structural pattern matching different from C/Java `switch` statements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
63. **Static Type Hinting And Mypy Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Gradual Typing in Python
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Do Python type hints affect runtime execution speed?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
64. **Asyncio Event Loop And Async Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Execution
        - Python 3.11+ `TaskGroup` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is Asyncio multi-threaded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
65. **Modern Python Packaging Pyproject And Uv**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy `setup.py` vs Modern `pyproject.toml`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Modern `pyproject.toml` Manifest Specification
        - High-Speed `uv` CLI Commands
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `pyproject.toml` and why is it preferred over `requirements.txt`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
66. **Java21 Record Classes And Dto Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Eliminating DTO Boilerplate
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Java Record Class extend another class or be extended?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
67. **Java21 Sealed Classes And Interfaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Controlled Class Hierarchies
        - Subclass Modifiers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does exhaustive pattern matching on a sealed class eliminate the need for a `default` case in switch expressions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
68. **Java21 Virtual Threads Project Loom**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Platform Threads vs Virtual Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Thread Pinning in Java 21 Virtual Threads and how do you avoid it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
69. **Java21 Sequenced Collections**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Missing Abstraction in Legacy Java Collections
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What problem do Sequenced Collections solve in Java 21?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
70. **Matrix Inversion Determinants And Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Determinants & Singular Matrices
        - Solving $A\mathbf{x} = \mathbf{b}$
        - Condition Number ($\kappa$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid explicitly computing $A^{-1}$ to solve $A\mathbf{x} = \mathbf{b}$?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
71. **Eigenvalues Eigenvectors And Decompositions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Eigenvalues & Eigenvectors
        - Singular Value Decomposition (SVD)
        - PCA & Covariance Matrix Connection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the relationship between SVD and PCA?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
72. **Multivariable Calculus And Gradient Vectors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Gradient Vector ($\nabla f$)
        - The Hessian Matrix ($H$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does the Gradient Vector $\nabla f$ represent geometrically?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
73. **Discrete And Continuous Probability Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - PMF, PDF, & CDF
        - Gaussian (Normal) Distribution $\mathcal{N}(\mu, \sigma^2)$
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between a PMF and a PDF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
74. **Joint Marginal And Conditional Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Joint & Marginal Distributions
        - Covariance & Pearson Correlation
        - The Central Limit Theorem (CLT)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does the Central Limit Theorem state and why is it crucial for statistics?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
75. **Selenium4 Relative Locators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Spatial Locating in Selenium 4
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Relative Locators in Selenium 4 calculate element positions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
76. **Estimation And Confidence Intervals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Point Estimation & MLE
        - Confidence Intervals (CI)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the correct interpretation of a 95% Confidence Interval?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
77. **Mysql8 Analytical Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `GROUP BY` vs Window Functions (`OVER`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `RANK()` and `DENSE_RANK()` in SQL?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
78. **Modern C23 Features Constexpr Typeof Auto**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The C23 Standard Evolution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `constexpr` in C23 improve performance over standard `const` variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
79. **Anova And Chi Square Tests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way ANOVA ($F$-Statistic)
        - Chi-Square Test of Independence ($\chi^2$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why use ANOVA instead of multiple individual $t$-tests when comparing 4 groups?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
80. **Cpp20 Smart Pointers And Memory Safety**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - RAII & Smart Pointers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `std::unique_ptr` and `std::shared_ptr`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
81. **Conditional Logic And Guard Clauses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Guard Clauses vs Nested Arrow Code
        - Object Lookup Tables
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Guard Clause and why is it preferred over nested `if-else` blocks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
82. **Loops And Iteration Constructs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `for...in` vs `for...of`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `for...in` and `for...of` in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
83. **Iteration Protocols Iterators And Generators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Iterable & Iterator Protocols
        - Generator Functions (`function*`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does a Generator function differ from a regular function in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
84. **Function Declarations Expressions And Arrow Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Declarations vs Expressions vs Arrow Functions
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the `this` keyword behave differently in Arrow Functions compared to Regular Functions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
85. **Parameters Arguments And Return Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Rest Parameters (`...args`) vs `arguments` Object
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main advantage of Rest Parameters (`...args`) over the `arguments` object?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
86. **Scope Chain And Closures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Lexical Scoping & Scope Chain
        - What is a Closure?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a JavaScript Closure and how does it retain memory?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
87. **Functional Concepts And Higher Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pure Functions vs Side Effects
        - Currying
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Currying in Functional JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
88. **Object Literals Descriptors And Immutability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object Immutability Levels
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `Object.freeze()` and `Object.seal()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
89. **Dense Sparse Arrays And Higher Order Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mutating vs Non-Mutating Methods
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `.reduce()` work in JavaScript and what is the role of the initial value parameter?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
90. **Destructuring Assignment And Spread Rest Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unpacking Data Structures
        - Spread (`...`) for Immutable Merging
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you rename a variable during Object Destructuring in ES6?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
91. **Keyed Collections Map Set Weakmap Weakset**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Plain Object vs `Map`
        - `WeakMap` & `WeakSet` Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why can you not iterate over a `WeakMap` or check its size?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
92. **Asynchronous Execution Callbacks Event Queue**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Event Loop & Task Queue Priority
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Macrotask Queue and Microtask Queue in the JavaScript Event Loop?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
93. **Es6 Promises Architecture States And Chaining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise States & Immutability
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a `.then()` callback returns a plain scalar value versus another Promise?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
94. **Async Await Syntactic Sugar And Async Iteration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Async/Await as Syntactic Sugar
        - Asynchronous Iteration (`for await...of`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when the `await` keyword is executed in an `async` function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
95. **Promise Combinators All Allsettled Race Any**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise Combinators Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between `Promise.all()` and `Promise.allSettled()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
96. **Prototypes Prototype Chain And Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Prototypal Inheritance vs Class-Based Inheritance
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when a property is accessed on a JavaScript object that does not exist on the instance itself?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
97. **Es6 Class Syntax And Constructors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Classes as Syntactic Sugar
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Are ES6 classes true classes like in Java or C++?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
98. **Inheritance Method Overriding And Super**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Subclassing & Mandatory `super()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
99. **Private Fields Getters Setters Static Members**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Hard Encapsulation (`#privateField`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do modern `#` private fields in JavaScript differ from the legacy `_` prefix convention?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
100. **Dom Tree Navigation And Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `querySelectorAll` (NodeList) vs `getElementsByClassName` (HTMLCollection)
        - Upward Traversal with `.closest()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between a live `HTMLCollection` and a static `NodeList`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
101. **Dynamic Element Creation And Modification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `appendChild()` vs `append()`
        - HTML5 `dataset` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the HTML5 `dataset` API in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
102. **Event Handling Propagation Bubbling Capturing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 3 Event Propagation Phases
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `event.target` and `event.currentTarget`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
103. **Event Delegation And Custom Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Event Delegation Architecture
        - Custom Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the primary benefits of using the Event Delegation Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
104. **Fetch Api And Http Network Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `fetch()` HTTP Status Code Trap
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does `fetch()` not reject when a server returns a 404 or 500 error code?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
105. **Web Storage Cookies Localstorage Sessionstorage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main security risk of storing authentication tokens in LocalStorage compared to HttpOnly Cookies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
106. **Client Side Storage With Indexeddb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why IndexedDB Over LocalStorage?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does IndexedDB differ from LocalStorage?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
107. **Websockets And Realtime Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for WebSocket reconnection strategies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
108. **Es6 Modules Export And Import Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CommonJS (`require`) vs ES Modules (`import`)
        - Named vs Default Exports
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `mathUtils.js` (Module)
        - File 2: `main.js` (Consumer)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural advantage of ES Modules over CommonJS `require()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
109. **Dynamic Imports And Toplevel Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Static Imports vs Dynamic `import()`
        - Top-Level Await
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Code Splitting and how do Dynamic Imports facilitate it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
110. **Modern Build Tooling Bundlers Tree Shaking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy Bundlers (Webpack) vs Modern Native ESM (Vite)
        - Tree Shaking Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Initializing a Lightning-Fast Vite Project
        - Production Build & Source Map Inspection
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Tree Shaking in modern JavaScript build tools and how does it work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
111. **Critical Rendering Path And Dom Reflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Critical Rendering Path
        - Reflow vs Repaint vs Layout Thrashing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Layout Thrashing in JavaScript and how do you prevent it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
112. **Core Web Vitals And Performance Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Google Core Web Vitals Metrics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Interaction to Next Paint (INP) and how does it differ from FID?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
113. **Memory Management And Leak Prevention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mark-and-Sweep Garbage Collection
        - The 4 Common Memory Leak Patterns
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Detached DOM Node memory leak in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
114. **Web Security Xss Csrf Csp Mitigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - XSS vs CSRF Vulnerability Matrix
        - Content Security Policy (CSP)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Content Security Policy (CSP) and how does it prevent XSS attacks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
115. **Proxy And Reflect Api Metaprogramming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Meta-Programming?
        - Proxy Traps & Reflect API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `Reflect` methods inside Proxy handler traps instead of accessing the target directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
116. **Web Workers And Multithreaded Javascript**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded Main Loop vs Worker Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `worker.js` (Background Thread)
        - File 2: `main.js` (UI Thread)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What capabilities and Web APIs are accessible inside a Web Worker?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
117. **Service Workers And Offline Pwa Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Service Worker Proxy Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `sw.js` (Service Worker Script)
        - File 2: `app.js` (Register Service Worker)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Stale-While-Revalidate caching strategy work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
118. **Javascript Unit Testing With Vitest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The AAA Unit Testing Pattern
        - `toBe` vs `toEqual`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Target Module: `math.js`
        - Vitest Test Suite: `math.test.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `toBe` and `toEqual` in Vitest/Jest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
119. **E2E Testing With Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Testing vs End-to-End (E2E) Testing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Playwright Test Suite: `dashboard.spec.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Playwright preferred over older Selenium or Puppeteer testing frameworks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
120. **Javascript Design Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Design Patterns Categories
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between the Observer Pattern and the Publisher-Subscriber (PubSub) Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
121. **Internationalization Intl Api**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Native ECMAScript `Intl` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance advantages of using the native `Intl` API over external libraries like Moment.js?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
122. **Web Components And Shadow Dom**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Web Components Technologies
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Usage in HTML:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Custom Element tag names contain a hyphen (`-`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
123. **Webassembly Integration Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WebAssembly (Wasm)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is WebAssembly intended to replace JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
124. **Advanced Debugging Chrome Devtools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Advanced Breakpoint Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Logpoint in Chrome DevTools and how does it differ from a standard Breakpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
125. **Capstone Realtime Iot Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Enterprise Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Reactive State Store (`store.js`)
        - Capstone Dashboard Application (`app.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does this Vanilla JavaScript Capstone architecture achieve high performance without a frontend framework like React?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
126. **Wsgi Architecture And Flask Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WSGI (PEP 3333)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is WSGI in Python web development and why is `Flask(__name__)` required?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
127. **Flask Application Factory Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why the Application Factory Pattern?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `config.py` (Environment Configurations)
        - File 2: `app/__init__.py` (Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Application Factory Pattern in Flask and why is it recommended for production applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
128. **Flask Routing And Url Converters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Built-in URL Converters
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `url_for()` instead of hardcoding URL strings in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
129. **Flask Request Response Objects**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Flask `request` Context Local
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Context Local in Flask and how does the `request` object work behind the scenes?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
130. **Jinja2 Syntax Control Flow And Macros**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Jinja2 Delimiter Syntax
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `templates/macros/card.html` (Jinja2 Reusable Macro)
        - File 2: `templates/dashboard.html` (Main Page)
        - File 3: `app.py` (Python View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Jinja2 prevent Cross-Site Scripting (XSS) attacks when rendering dynamic variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
131. **Flask Contexts Application And Request**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Application Context vs Request Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Application Context and Request Context in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
132. **Flask G Object And Request Scoped State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is the `g` Object?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `g` and `session` in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
133. **Flask Wtf Forms And Fields**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Processing Manual HTML Forms vs Flask-WTF
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (FlaskForm Class Definition)
        - File 2: `app.py` (Flask View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `form.validate_on_submit()` do in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
134. **Form Validation And Csrf Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom In-Class Field Validation
        - CSRF Protection Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (Form with Custom & Standard Validators)
        - File 2: `templates/register.html` (Rendering Inline Validation Errors)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you write a custom field validator in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
135. **Flask Sqlalchemy Extension Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object-Relational Mapping (ORM)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py` (Unbound Extension Instance)
        - File 2: `config.py`
        - File 3: `app/__init__.py` (Application Factory Integration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you initialize Flask-SQLAlchemy using `db = SQLAlchemy()` in an `extensions.py` module rather than `db = SQLAlchemy(app)`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
136. **Sqlalchemy Models Fields And Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy Model Mapping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `models.py` (SQLAlchemy Relational Schema)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `backref` and `back_populates` in SQLAlchemy relationships?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
137. **Sqlalchemy Crud Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit of Work Transaction Management
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `db.session.rollback()` in Flask-SQLAlchemy?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
138. **Schema Migrations With Flask Migrate**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `db.create_all()` Fails in Production
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py`
        - File 2: `app/__init__.py` (Factory Integration)
        - File 3: Command Line Execution Sequence
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask-Migrate detect changes made to SQLAlchemy models when generating migration scripts?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
139. **User Authentication With Flask Login**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask-Login Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (User Model with UserMixin)
        - File 2: `app.py` (Flask-Login Initialization & Auth Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `@login_manager.user_loader` in Flask-Login?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
140. **Password Hashing And Cookie Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way Password Hashing & Salting
        - Flask Session Cookie Security Configuration
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `security_demo.py` (Password Hashing & Cookie Security Config)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is storing plain MD5 or SHA-256 hashes of passwords insecure, and how does Werkzeug address this?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
141. **Flask Blueprint Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is a Flask Blueprint?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `app/api/routes.py` (Blueprint Module)
        - File 2: `app/__init__.py` (Registering Blueprints in Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Flask Blueprint and how does it improve code architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
142. **Restful Api Principles And Resource Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - REST Architectural Constraints
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is idempotency in RESTful APIs and which HTTP verbs are idempotent?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
143. **Api Serialization With Flask Marshmallow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serialization vs Deserialization
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `schemas.py` (Flask-Marshmallow Schemas)
        - File 2: `routes.py` (Using Schemas in API Views)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the primary role of Marshmallow schemas in a Flask REST API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
144. **Jwt Authentication With Flask Jwt Extended**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON Web Token (JWT) Structure
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural difference between session-based authentication and JWT authentication?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
145. **Application Caching With Flask Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Backend Caching?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@cache.cached()` and `@cache.memoize()` in Flask-Caching?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
146. **Asynchronous Background Tasks With Celery**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Asynchronous Background Tasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `celery_app.py` (Celery Integration Helper)
        - File 2: `tasks.py` (Celery Tasks)
        - File 3: `app.py` (Dispatching Tasks & Checking Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Celery used with Flask instead of Python's built-in `threading` module?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
147. **Email Delivery With Flask Mail**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SMTP Protocol & Synchronous vs Async Delivery
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is it crucial to send emails asynchronously in web applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
148. **Custom Error Pages And Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Exception Handling Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@errorhandler` and `@app_errorhandler` on a Flask Blueprint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
149. **Application Logging And Sentry**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Logging Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `RotatingFileHandler` critical for production Python applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
150. **Automated Testing With Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask `test_client()` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Shared Fixtures)
        - File 2: `test_api.py` (Pytest Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask's `app.test_client()` work and why is it preferred over HTTP requests library like `requests` during unit testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
151. **Production Deployment Gunicorn Nginx Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Deployment Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `wsgi.py` (Production Entrypoint)
        - File 2: `Dockerfile` (Production Multi-Stage Container)
        - File 3: `docker-compose.yml` (Multi-Container Orchestration)
        - File 4: `nginx.conf` (Nginx Reverse Proxy Configuration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Flask's built-in development server never be used in production environments, and what roles do Gunicorn and Nginx play?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
152. **Asgi Architecture Uvicorn And Fastapi Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - WSGI vs ASGI Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Running with Uvicorn Server:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if you call a synchronous blocking function inside an `async def` endpoint in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
153. **Fastapi App Instantiation Routing And Openapi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Zero-Configuration Automatic OpenAPI Generation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI generate Swagger UI documentation automatically without third-party plugins?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
154. **Path And Query Parameters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parameter Parsing & Automatic Type Conversion
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI differentiate between a Path Parameter and a Query Parameter in a route function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
155. **Pydantic V2 Models And Schema Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pydantic v2 Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the key improvements of Pydantic v2 over Pydantic v1 in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
156. **Dependency Injection Architecture And Depends**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Dependency Injection?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the main benefits of FastAPI's Dependency Injection system over traditional middleware?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
157. **Sub Dependencies Security And Yield Cleanups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Yield Dependencies & Context Cleanup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Mocking Dependencies in Unit Tests:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Yield Dependencies work in FastAPI and how do they prevent resource leaks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
158. **Sqlalchemy 20 Async Engine And Asyncpg**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Database Drivers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `database.py` (SQLAlchemy 2.0 Async Engine & Dependency)
        - File 2: `main.py` (Using AsyncSession in Route)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `asyncpg` significantly faster than `psycopg2` when used with FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
159. **Async Crud Operations And Asyncsession**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy 2.0 Async Query Style
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (Async SQLAlchemy Models)
        - File 2: `main.py` (Async CRUD Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is lazy loading problematic in asynchronous SQLAlchemy and how does `selectinload()` solve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
160. **Oauth2 Password Bearer And Hashing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - OAuth2 Password Bearer Flow
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `OAuth2PasswordBearer` do under the hood in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
161. **Jwt Authentication And Current User**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `get_current_user` Dependency Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI implement Role-Based Access Control (RBAC) cleanly using Dependency Injection?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
162. **Apirouter Architecture And Prefixes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is an APIRouter?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `routers/devices.py` (APIRouter Module)
        - File 2: `main.py` (Main FastAPI App Registering Router)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `APIRouter` in FastAPI differ from Flask's `Blueprint`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
163. **Modular Directory Structure And Big Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Directory Layout
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `src/app/core/config.py` (Pydantic-Settings Configuration)
        - File 2: `src/app/main.py` (Global Exception Handler & Main App)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `pydantic-settings` preferred over `os.environ.get()` in FastAPI production codebases?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
164. **Asynchronous Middleware And Cors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is FastAPI Middleware?
        - Cross-Origin Resource Sharing (CORS)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a CORS preflight request and how does FastAPI handle it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
165. **Request Timing Headers And Performance Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - High-Precision Latency Tracking
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `time.perf_counter()` preferred over `time.time()` for measuring code latency?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
166. **Fastapi Background Tasks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are FastAPI BackgroundTasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use FastAPI `BackgroundTasks` versus an external task queue like Celery?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
167. **Lifespan Event Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are Lifespan Events?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why did FastAPI deprecate `@app.on_event("startup")` in favor of the `lifespan` context manager?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
168. **Websockets Protocol And Endpoint Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs Full-Duplex WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `await websocket.accept()` in a FastAPI WebSocket endpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
169. **Realtime Connection Manager And Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Connection Manager Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you scale WebSocket broadcasting across multiple Uvicorn worker processes or servers?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
170. **Async Testing With Pytest And Httpx**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `httpx.AsyncClient` over Starlette `TestClient`?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Async Fixtures)
        - File 2: `test_main.py` (Async Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `httpx.AsyncClient` preferred over `TestClient` when testing async FastAPI applications with Pytest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
171. **Production Deployment Gunicorn Uvicorn Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Process Management: Gunicorn + Uvicorn
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `gunicorn_conf.py` (Gunicorn Configuration)
        - File 2: `Dockerfile` (Production Container Definition)
        - File 3: `docker-compose.yml` (Multi-Container Deployment)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why do we use Gunicorn together with Uvicorn in production rather than running Uvicorn alone?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
172. **Esp32 Architecture And Pinout**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 System-on-Chip (SoC) Architecture
        - Critical GPIO Pin Classification
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are ESP32 Strapping Pins and why must engineers exercise caution when connecting external hardware components to them?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
173. **Platformio Espidf Toolchain Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded Development Frameworks
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `platformio.ini` (PlatformIO Configuration File)
        - File: `src/main.cpp` (Embedded Entrypoint)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is PlatformIO preferred over Arduino IDE for professional embedded engineering?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
174. **Gpio Digital Io And Interrupts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Polling vs Hardware Interrupts
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must ESP32 Interrupt Service Routine (ISR) functions be declared with the `IRAM_ATTR` attribute?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
175. **Adc Dac And Pwm Timer Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 12-Bit Analog-to-Digital Conversion (ADC)
        - Hardware PWM via LEDC Peripheral
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should embedded engineers avoid connecting analog sensors to ADC2 pins on the ESP32 in connected IoT applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
176. **I2C Spi And Uart Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serial Protocol Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `main.cpp` (I2C Bus Address Scanner & Dual Hardware UART)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare I2C and SPI protocols. When would you choose SPI over I2C in an embedded system design?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
177. **Freertos Task Creation And Core Pinning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS on ESP32?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `xTaskCreate()` and `xTaskCreatePinnedToCore()` in ESP32 FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
178. **Freertos Task Priorities Delays And Stack**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pre-emptive Priority Scheduling
        - `vTaskDelay()` vs `vTaskDelayUntil()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `vTaskDelay()` and `vTaskDelayUntil()` in FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
179. **Freertos Queues And Inter Task Messaging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS Queues?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do FreeRTOS Queues achieve thread safety when sharing data between tasks running on different CPU cores?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
180. **Freertos Semaphores Mutexes And Locks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Binary Semaphores vs Mutexes
        - What is Priority Inversion?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Priority Inversion and how do FreeRTOS Mutexes resolve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
181. **Wifi Station And Access Point Modes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 Wi-Fi Operating Modes
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Station (STA) Mode and Access Point (AP) Mode on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
182. **Non Blocking Wifi Reconnect And Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Asynchronous System Wi-Fi Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for IoT Wi-Fi reconnect logic?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
183. **Http Rest Client Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded HTTP Client Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `http.end()` mandatory after executing an HTTP request with `HTTPClient` on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
184. **Mqtt Protocol And Pubsubclient**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is MQTT?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare MQTT and HTTP protocols for resource-constrained IoT devices.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
185. **Esp32 Websocket Client Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why WebSockets for Microcontroller Telemetry?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should an embedded engineer choose WebSockets over MQTT for an IoT system architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
186. **Deep Sleep Modes And Rtc Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Power Consumption Modes Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens to standard C++ global variables versus `RTC_DATA_ATTR` variables when the ESP32 enters Deep Sleep?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
187. **Deep Sleep Wakeup Sources**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Deep Sleep Wake-Up Sources Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Ext0 and Ext1 wake-up sources on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
188. **Over The Air Ota Firmware Updates**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Dual-Bank OTA Partition Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the ESP32 dual-bank partition table prevent device bricking during Over-The-Air (OTA) updates?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
189. **Secure Boot Flash Encryption Partitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom Partition Tables
        - Hardware Security Primitives
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `partitions_custom.csv` (Custom 4MB Dual-OTA Partition Table)
        - File: `platformio.ini` (Configuring Custom Partition Table)
        - File: `main.cpp` (Querying Partition & Security Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Explain how Secure Boot V2 and Flash Encryption combine to secure ESP32 hardware in the field.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
190. **Spiffs Littlefs And Static File Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SPIFFS vs LittleFS
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `data/index.html` (Static Web Asset in PlatformIO `data/` Directory)
        - File: `src/main.cpp` (Mounting LittleFS & File I/O)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is LittleFS preferred over SPIFFS for modern ESP32 embedded applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
191. **Espasyncwebserver And Rest Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Web Servers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `ESPAsyncWebServer` superior to the standard synchronous `WebServer.h` library for ESP32 applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
192. **Fullstack Iot System Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - End-to-End Full-Stack IoT Data Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `backend_bridge.py` (FastAPI + MQTT Ingestion Bridge)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is an MQTT message broker placed between embedded ESP32 devices and backend FastAPI microservices in full-stack IoT architectures?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
193. **Capstone Production Iot Gateway**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Architecture Blueprint
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - ESP32 Production FreeRTOS Firmware (`src/main.cpp`)
        - FastAPI Ingestion & WebSockets Backend (`server.py`)
    6. Guided Step-by-Step Hands-On Exercise
    7. Industry Interview Q&A
        - Q1: How does this capstone architecture ensure high reliability and zero telemetry loss across network drops?
    8. Self-Assessment Quiz
    9. Summary & Cheat Sheet
194. **Numpy Core Architecture And Ndarray**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Python Lists vs NumPy `ndarray`
        - Array Strides
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why are NumPy `ndarray` operations significantly faster than standard Python list comprehensions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
195. **Vectorization Slicing And Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - NumPy Broadcasting Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the two conditions under which two array dimensions are compatible for NumPy broadcasting?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
196. **Pandas Dataframes Series And Ingestion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pandas Data Structures Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does converting string columns with low cardinality to the `category` dtype in Pandas significantly reduce memory usage?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
197. **Pandas Indexing Filtering And Imputation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `loc` vs `iloc` Indexing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the crucial difference between `df.loc[0:2]` and `df.iloc[0:2]` in Pandas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
198. **Pandas Groupby Pivoting And Merging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Split-Apply-Combine Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `transform()` and `agg()` when performing a `groupby()` in Pandas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.5.2. Module 2 — Remote Collaboration

1. **Remote Repositories & Origin Config**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual Architecture Diagram
        - What is a Remote?
        - Git vs. Hosting Platforms
        - Clone vs. Fork
        - origin vs. upstream
        - Remote-Tracking Branches
        - HTTPS vs. SSH
    3. Practical Code Examples
        - Remote Command Cheat Sheet
        - Example A: Managing Multiple Remotes in Enterprise Environment
        - Example B: Renaming and Inspecting Remotes
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - E2E Remote Association Workflow
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Syncing Data: Fetch, Pull & Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Fetch vs. Pull Architecture Diagram
        - Fetch vs. Pull Comparison
        - git pull: Merge vs. Rebase
        - Ahead and Behind Tracking States
    3. Practical Code Examples
        - Syncing Commands Cheat Sheet
        - Example A: Pulling with Rebase
        - Example B: Pushing and linking branch
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Rejected Push
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Forking & Upstream Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Forking Workflow Diagram
        - Fork vs. Clone vs. Branch
        - origin vs. upstream
        - Pull Requests (PR) vs. Merge Requests (MR)
        - Merge vs. Rebase in Workflows
    3. Practical Code Examples
        - Remote Fork Commands Cheat Sheet
        - Example A: Full Open-Source Contribution Workflow
        - Example B: Syncing your Local Fork
        - Example C: Rebasing feature branches
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - GitHub Feature Lifecycle Flow
    5. Workout Answers & Solutions
        - Pull Request Best Practices
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.5.3. Module 3 — Branching & Merging

1. **Branching Basics & Conflict Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branch Visualization Diagrams
        - Merging Strategies (FF vs. 3-Way)
        - Why Merge Conflicts Occur
        - Tagging Releases (Lightweight vs. Annotated)
    3. Practical Code Examples
        - Branch Command Cheat Sheet
        - Merge Command Cheat Sheet
        - Example A: Resolving Conflicts with git status Checks
        - Example B: Tagging and Remote Operations
        - Example C: Realistic Feature Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Standard Branch Naming Conventions
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Merge Conflict Handling in Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Conflict Visualization Diagram
        - Conflict Resolution Workflow
        - Merge vs. Rebase Conflicts
        - Conflict Markers Decoded
        - HEAD vs. Theirs Pointer Reference Map
        - Conflict Types
    3. Practical Code Examples
        - Conflict Commands Cheat Sheet
        - Example A: Managing conflict status
        - Example B: Visual merge tools setup
        - Example C: Practical Team Resolution Workflow
        - Advanced Tip: `git rerere`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge: Resolving Worksheets
        - Conflict Prevention Workflow Diagram
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.5.4. Module 4 — Troubleshooting

1. **Diagnostic & Troubleshooting Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Common Git Troubleshooting Scenarios
        - Scenario 1: Detached HEAD State
        - Scenario 2: Recovering Lost Commits (Reflog)
        - Scenario 3: Committed on the Wrong Branch
        - Scenario 4: Stuck Merge or Rebase
        - Scenario 5: Force Push Recovery
    3. Practical Code Examples
        - Diagnostic Commands Cheat Sheet
        - Example A: Finding lost commits using `git fsck`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Wrong branch commit
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.5.5. Module 5 — Automation & Security

1. **Git Customization: Hooks & Aliases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Hook Lifecycle Diagrams
        - Client-side vs. Server-side Hooks
        - Why Hooks Exist
        - Git Hook Trigger Reference
        - Modern SaaS Hosting Realities
    3. Practical Code Examples
        - Hook & Alias Cheat Sheet
        - Common Git Aliases
        - Example A: Enterprise Pre-commit Pipeline
        - Example B: Portable pre-commit hook (POSIX sh)
        - Example C: Robust commit-msg message parsing (Bash)
    4. Hands-on Workouts
        - MCQ
        - Hook Distribution Strategies
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Credential Management & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - HTTPS vs. SSH Authentication
        - Credential Helpers
        - SSH Key Setup Overview
    3. Practical Code Examples
        - Credential Config Cheat Sheet
        - Example A: Setting Up SSH Authentication
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Token Expiration
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.5.6. Module 6 — Advanced Workflows

1. **Rewriting History: Amend, Rebase & Squash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - History Rewriting Diagram
        - Decision Guide
        - History Rewriting Command Comparisons
        - Visualizing Interactive Rebase & Squashing
        - reflog Recovery Mechanics
    3. Practical Code Examples
        - Interactive Rebase Command Reference
        - Example A: Interactive Rebase Setup
        - Example B: Safe Force-Pushing
        - Example C: Complete Cleanup Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Undoing an amend
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Workspace Helpers: Stash, Bisect & Worktree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Workspace Helper Decision Guide
    2. Part 1: Git Stash
        - Stash Workflow
        - Stash Internals
        - Stash Commands Cheat Sheet
        - Enterprise Scenario: Stashing
    3. Part 2: Git Bisect
        - Bisect Visualization
        - Automated Bisect
        - Bisect Commands Cheat Sheet
        - Enterprise Scenario: Bisecting
    4. Part 3: Git Worktree
        - Worktree Visualization
        - Worktree vs. Clone
        - Worktree Commands Cheat Sheet
        - Enterprise Scenario: Worktrees
    5. Hands-on Workouts
        - MCQ
        - Coding Challenge
    6. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Cherry-picking & Backporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Cherry-picking Visual Diagram
        - What is Backporting?
        - Cherry-pick vs. Merge vs. Rebase
    3. Practical Code Examples
        - Cherry-pick Command Cheat Sheet
        - Example A: Cherry-picking a Hotfix
        - Example B: Handling Cherry-pick Conflicts
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Hotfixing
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
4. **Tags & Release Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Tag Types Comparison
        - Semantic Versioning (SemVer)
        - Tags vs. Releases
    3. Practical Code Examples
        - Tag Command Cheat Sheet
        - Example A: Creating and Pushing an Annotated Release Tag
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Security verification
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
5. **Branching Strategies for Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branching Strategies Comparison
        - Git Flow Branch Layout
        - Trunk-Based Development (TBD)
    3. Practical Code Examples
        - Example A: Git Flow feature release sequence
        - Example B: Git Flow hotfix release sequence
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Choosing a strategy
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.5.7. Module 7 — Git Internals

1. **Git Internals: Blobs, Trees & Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Object Relationship Diagram
        - Object Hierarchy Flow
        - Inside the `.git` Directory
        - SHA-1 vs. SHA-256 Hashes
        - Content-Addressable Storage & Deduplication
        - Sample Commit Object Layout
        - Porcelain vs. Plumbing
    3. Practical Code Examples
        - Internal Investigation Command Reference
        - Example A: Inspecting Objects E2E
        - Example B: Tag objects vs References
        - Example C: Pack files optimization
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.5.8. Module 8 — Git Foundations

1. **Git Architecture & Three States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git File States & Environments
        - The Lifecycle of a File
        - The State Transition Flow Connected to `git status`
        - Repository Creation Workflows
    3. Practical Code Examples
        - Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
        - Step-by-Step Lab 2: Initializing and First Staging
        - Step-by-Step Lab 3: Creating Your First Commit
    4. Hands-on Workouts
        - Checkpoint Questions
        - Try It Yourself Exercise: Selective Staging
    5. Workout Answers & Solutions
        - Checkpoint Answers
        - Solution to Try It Yourself Exercise
        - Common Beginner Mistakes
2. **Local Workflow: Init, Stage & Commit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Configuration Scopes & Precedence
        - git init vs. git clone
        - Short Status Output (`git status -s`)
        - Git Ignore Filters (`.gitignore`)
    3. Practical Code Examples
        - Before You Start
        - Step-by-Step Lab 1: Configuration Scopes
        - Step-by-Step Lab 2: Cloning an Existing Repository
        - Step-by-Step Lab 3: Ignoring Cache & Temp Files
    4. Hands-on Workouts
        - Workout Exercises
    5. Workout Answers & Solutions
        - Checkpoint Questions
        - Workout Solutions
        - Summary of New Concepts
        - Next Lesson Preview
3. **Version Control History & Evolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Problem: Coding Without Version Control
        - Version Control System (VCS) Evolution Timeline
        - VCS Comparison Chart
        - Why Git Was Created
        - Git vs. GitHub
        - Why Git is Fast
    3. Practical Code Examples
        - Example A: Basic Environment Checks
        - Example B: Help Document Lookup
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Collaboration without Git
    5. Workout Answers & Solutions
        - Common Problems Solved by Git
        - Why Git Won the Industry
        - Key Takeaways

#### 2.5.9. Module 9 — History Management

1. **Inspecting History: Log & Diff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual History Diagram
        - git diff State Comparisons
        - git log Cheat Sheet
        - git diff Comparison Chart
        - Understanding Diff Output Markers
        - git show
        - Commit Hash Mechanics
    3. Practical Code Examples
        - Example A: Basic log filtering
        - Example B: Snoop searching with `git log -S`
        - Example C: Practical Investigation Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Who updated the file lines?
        - Common Investigation Commands
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Interactive Staging: Patch Mode & Partial Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - What is Interactive Staging?
        - Patch Mode Options Decoded
    3. Practical Code Examples
        - Interactive Staging Cheat Sheet
        - Example A: Running an Interactive Staging Session
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Unrelated modifications
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Undoing Changes: Reset, Restore & Revert**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Undo Action Decision Flow
    2. Definitions & Core Concepts
        - Command Comparisons
        - Visual Explanation of `git reset` Modes
        - Detached HEAD
        - git log vs. git reflog
    3. Practical Code Examples
        - Example A: git restore Variations
        - Example B: Detached HEAD branch creation
        - Example C: Realistic Recovery Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - When Should I Use... Reference Box
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
### 2.6. Git

#### 2.6.1. Module 1 — Core Concepts and Workflows

1. **Git Architecture & Three States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git File States & Environments
        - The Lifecycle of a File
        - The State Transition Flow Connected to `git status`
        - Repository Creation Workflows
    3. Practical Code Examples
        - Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
        - Step-by-Step Lab 2: Initializing and First Staging
        - Step-by-Step Lab 3: Creating Your First Commit
    4. Hands-on Workouts
        - Checkpoint Questions
        - Try It Yourself Exercise: Selective Staging
    5. Workout Answers & Solutions
        - Checkpoint Answers
        - Solution to Try It Yourself Exercise
        - Common Beginner Mistakes
2. **Local Workflow: Init, Stage & Commit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Configuration Scopes & Precedence
        - git init vs. git clone
        - Short Status Output (`git status -s`)
        - Git Ignore Filters (`.gitignore`)
    3. Practical Code Examples
        - Before You Start
        - Step-by-Step Lab 1: Configuration Scopes
        - Step-by-Step Lab 2: Cloning an Existing Repository
        - Step-by-Step Lab 3: Ignoring Cache & Temp Files
    4. Hands-on Workouts
        - Workout Exercises
    5. Workout Answers & Solutions
        - Checkpoint Questions
        - Workout Solutions
        - Summary of New Concepts
        - Next Lesson Preview
3. **Inspecting History: Log & Diff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual History Diagram
        - git diff State Comparisons
        - git log Cheat Sheet
        - git diff Comparison Chart
        - Understanding Diff Output Markers
        - git show
        - Commit Hash Mechanics
    3. Practical Code Examples
        - Example A: Basic log filtering
        - Example B: Snoop searching with `git log -S`
        - Example C: Practical Investigation Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Who updated the file lines?
        - Common Investigation Commands
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
4. **Version Control History & Evolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Problem: Coding Without Version Control
        - Version Control System (VCS) Evolution Timeline
        - VCS Comparison Chart
        - Why Git Was Created
        - Git vs. GitHub
        - Why Git is Fast
    3. Practical Code Examples
        - Example A: Basic Environment Checks
        - Example B: Help Document Lookup
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Collaboration without Git
    5. Workout Answers & Solutions
        - Common Problems Solved by Git
        - Why Git Won the Industry
        - Key Takeaways
5. **Interactive Staging: Patch Mode & Partial Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - What is Interactive Staging?
        - Patch Mode Options Decoded
    3. Practical Code Examples
        - Interactive Staging Cheat Sheet
        - Example A: Running an Interactive Staging Session
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Unrelated modifications
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
6. **Undoing Changes: Reset, Restore & Revert**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Undo Action Decision Flow
    2. Definitions & Core Concepts
        - Command Comparisons
        - Visual Explanation of `git reset` Modes
        - Detached HEAD
        - git log vs. git reflog
    3. Practical Code Examples
        - Example A: git restore Variations
        - Example B: Detached HEAD branch creation
        - Example C: Realistic Recovery Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - When Should I Use... Reference Box
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
7. **Branching Basics & Conflict Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branch Visualization Diagrams
        - Merging Strategies (FF vs. 3-Way)
        - Why Merge Conflicts Occur
        - Tagging Releases (Lightweight vs. Annotated)
    3. Practical Code Examples
        - Branch Command Cheat Sheet
        - Merge Command Cheat Sheet
        - Example A: Resolving Conflicts with git status Checks
        - Example B: Tagging and Remote Operations
        - Example C: Realistic Feature Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Standard Branch Naming Conventions
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
8. **Remote Repositories & Origin Config**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual Architecture Diagram
        - What is a Remote?
        - Git vs. Hosting Platforms
        - Clone vs. Fork
        - origin vs. upstream
        - Remote-Tracking Branches
        - HTTPS vs. SSH
    3. Practical Code Examples
        - Remote Command Cheat Sheet
        - Example A: Managing Multiple Remotes in Enterprise Environment
        - Example B: Renaming and Inspecting Remotes
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - E2E Remote Association Workflow
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
9. **Syncing Data: Fetch, Pull & Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Fetch vs. Pull Architecture Diagram
        - Fetch vs. Pull Comparison
        - git pull: Merge vs. Rebase
        - Ahead and Behind Tracking States
    3. Practical Code Examples
        - Syncing Commands Cheat Sheet
        - Example A: Pulling with Rebase
        - Example B: Pushing and linking branch
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Rejected Push
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
10. **Merge Conflict Handling in Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Conflict Visualization Diagram
        - Conflict Resolution Workflow
        - Merge vs. Rebase Conflicts
        - Conflict Markers Decoded
        - HEAD vs. Theirs Pointer Reference Map
        - Conflict Types
    3. Practical Code Examples
        - Conflict Commands Cheat Sheet
        - Example A: Managing conflict status
        - Example B: Visual merge tools setup
        - Example C: Practical Team Resolution Workflow
        - Advanced Tip: `git rerere`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge: Resolving Worksheets
        - Conflict Prevention Workflow Diagram
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
11. **Forking & Upstream Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Forking Workflow Diagram
        - Fork vs. Clone vs. Branch
        - origin vs. upstream
        - Pull Requests (PR) vs. Merge Requests (MR)
        - Merge vs. Rebase in Workflows
    3. Practical Code Examples
        - Remote Fork Commands Cheat Sheet
        - Example A: Full Open-Source Contribution Workflow
        - Example B: Syncing your Local Fork
        - Example C: Rebasing feature branches
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - GitHub Feature Lifecycle Flow
    5. Workout Answers & Solutions
        - Pull Request Best Practices
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
12. **Git Internals: Blobs, Trees & Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Object Relationship Diagram
        - Object Hierarchy Flow
        - Inside the `.git` Directory
        - SHA-1 vs. SHA-256 Hashes
        - Content-Addressable Storage & Deduplication
        - Sample Commit Object Layout
        - Porcelain vs. Plumbing
    3. Practical Code Examples
        - Internal Investigation Command Reference
        - Example A: Inspecting Objects E2E
        - Example B: Tag objects vs References
        - Example C: Pack files optimization
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
13. **Rewriting History: Amend, Rebase & Squash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - History Rewriting Diagram
        - Decision Guide
        - History Rewriting Command Comparisons
        - Visualizing Interactive Rebase & Squashing
        - reflog Recovery Mechanics
    3. Practical Code Examples
        - Interactive Rebase Command Reference
        - Example A: Interactive Rebase Setup
        - Example B: Safe Force-Pushing
        - Example C: Complete Cleanup Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Undoing an amend
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
14. **Workspace Helpers: Stash, Bisect & Worktree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Workspace Helper Decision Guide
    2. Part 1: Git Stash
        - Stash Workflow
        - Stash Internals
        - Stash Commands Cheat Sheet
        - Enterprise Scenario: Stashing
    3. Part 2: Git Bisect
        - Bisect Visualization
        - Automated Bisect
        - Bisect Commands Cheat Sheet
        - Enterprise Scenario: Bisecting
    4. Part 3: Git Worktree
        - Worktree Visualization
        - Worktree vs. Clone
        - Worktree Commands Cheat Sheet
        - Enterprise Scenario: Worktrees
    5. Hands-on Workouts
        - MCQ
        - Coding Challenge
    6. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
15. **Git Customization: Hooks & Aliases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Hook Lifecycle Diagrams
        - Client-side vs. Server-side Hooks
        - Why Hooks Exist
        - Git Hook Trigger Reference
        - Modern SaaS Hosting Realities
    3. Practical Code Examples
        - Hook & Alias Cheat Sheet
        - Common Git Aliases
        - Example A: Enterprise Pre-commit Pipeline
        - Example B: Portable pre-commit hook (POSIX sh)
        - Example C: Robust commit-msg message parsing (Bash)
    4. Hands-on Workouts
        - MCQ
        - Hook Distribution Strategies
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
16. **Cherry-picking & Backporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Cherry-picking Visual Diagram
        - What is Backporting?
        - Cherry-pick vs. Merge vs. Rebase
    3. Practical Code Examples
        - Cherry-pick Command Cheat Sheet
        - Example A: Cherry-picking a Hotfix
        - Example B: Handling Cherry-pick Conflicts
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Hotfixing
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
17. **Tags & Release Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Tag Types Comparison
        - Semantic Versioning (SemVer)
        - Tags vs. Releases
    3. Practical Code Examples
        - Tag Command Cheat Sheet
        - Example A: Creating and Pushing an Annotated Release Tag
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Security verification
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
18. **Branching Strategies for Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branching Strategies Comparison
        - Git Flow Branch Layout
        - Trunk-Based Development (TBD)
    3. Practical Code Examples
        - Example A: Git Flow feature release sequence
        - Example B: Git Flow hotfix release sequence
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Choosing a strategy
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
19. **Credential Management & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - HTTPS vs. SSH Authentication
        - Credential Helpers
        - SSH Key Setup Overview
    3. Practical Code Examples
        - Credential Config Cheat Sheet
        - Example A: Setting Up SSH Authentication
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Token Expiration
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
20. **Diagnostic & Troubleshooting Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Common Git Troubleshooting Scenarios
        - Scenario 1: Detached HEAD State
        - Scenario 2: Recovering Lost Commits (Reflog)
        - Scenario 3: Committed on the Wrong Branch
        - Scenario 4: Stuck Merge or Rebase
        - Scenario 5: Force Push Recovery
    3. Practical Code Examples
        - Diagnostic Commands Cheat Sheet
        - Example A: Finding lost commits using `git fsck`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Wrong branch commit
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

### 2.7. MySQL

#### 2.7.1. Module 1 — MySQL Foundations

1. **Database Architecture and Relational Concepts**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a Relational Database?
        - Key Concepts
    2. MySQL Architecture
        - Storage Engines Comparison
    3. ACID Properties
    4. SQL Categories
    5. Connecting to MySQL
    6. Lab Exercise
2. **Database Design ER Modeling and Normalization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Entity-Relationship Modeling
        - ER to Schema Mapping
        - Normal Forms
        - Normalization Example
    2. Lab

#### 2.7.2. Module 2 — SQL Fundamentals

1. **DDL and Integrity Constraints**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - CREATE TABLE
        - ALTER TABLE
        - ON DELETE / ON UPDATE Actions
        - Indexes Created Automatically
    2. Lab
2. **DML and Basic Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - INSERT
        - UPDATE
        - DELETE
        - SELECT with Filtering
    2. Lab
3. **Aggregation Grouping and Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Aggregate Functions
        - WITH ROLLUP
        - String Functions
        - Date Functions
        - CASE Expression
    2. Lab
4. **Relational Joins and Set Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - JOIN Types
        - Multi-Table Join
        - Set Operations
    2. Lab

#### 2.7.3. Module 3 — Modern Analytical SQL & Window Functions

1. **Lesson 3.1 MySQL 8.4 Analytical Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `GROUP BY` vs Window Functions (`OVER`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `RANK()` and `DENSE_RANK()` in SQL?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing SQL Reference Files

#### 2.7.4. Module 4 — Advanced SQL

1. **Subqueries CTEs and Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Subqueries
        - Common Table Expressions (CTEs)
        - Recursive CTE — Org Chart
        - Window Functions
    2. Lab

#### 2.7.5. Module 5 — Programmability

1. **Stored Procedures Functions Triggers and Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Stored Procedures
        - User-Defined Functions
        - Triggers
        - Events (Scheduled Jobs)
    2. Lab
2. **Transactions Concurrency and Locking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Transactions
        - ACID Properties
        - Isolation Levels
        - Lock Types
    2. Lab

#### 2.7.6. Module 6 — Administration

1. **Database Security Administration and Replication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - User Management
        - MySQL Roles (8.0+)
        - Backup and Restore
        - Replication Overview
    2. Lab
2. **MySQL Integration with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - mysql-connector-python
        - Connection Pooling
        - SQLAlchemy ORM (MySQL)
        - Async MySQL (aiomysql)
    2. Lab

### 2.8. Flask

#### 2.8.1. Module 1 — WSGI Architecture & Flask Core Basics

1. **Lesson 1.1 Web Server Gateway Interface (WSGI) Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WSGI (PEP 3333)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is WSGI in Python web development and why is `Flask(__name__)` required?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 Flask Application Factory Pattern & Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why the Application Factory Pattern?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `config.py` (Environment Configurations)
        - File 2: `app/__init__.py` (Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Application Factory Pattern in Flask and why is it recommended for production applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.2. Module 2 — Routing, Request Handling, & Responses

1. **Lesson 2.1 Routing System, Dynamic URL Parameters, & Converter Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Built-in URL Converters
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `url_for()` instead of hardcoding URL strings in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 HTTP Methods, Request Object Inspection, & Response Formatting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Flask `request` Context Local
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Context Local in Flask and how does the `request` object work behind the scenes?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.3. Module 3 — Jinja2 Templating Engine

1. **Lesson 3.1 Jinja2 Syntax, Variables, Control Flow, & Macros**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Jinja2 Delimiter Syntax
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `templates/macros/card.html` (Jinja2 Reusable Macro)
        - File 2: `templates/dashboard.html` (Main Page)
        - File 3: `app.py` (Python View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Jinja2 prevent Cross-Site Scripting (XSS) attacks when rendering dynamic variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.4. Module 4 — Flask Application Contexts & Globals

1. **Lesson 4.1 Application Context & Request Context Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Application Context vs Request Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Application Context and Request Context in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 The g Global Object & Request-Scoped State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is the `g` Object?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `g` and `session` in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.5. Module 5 — Advanced Flask Patterns

1. **Flask Response Objects and Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Response Object Basics
        - Streaming Responses
        - Server-Sent Events (SSE)
        - File Streaming
        - JSON Responses
    2. Lab Exercise
2. **Advanced Form Validation and File Uploads**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - WTForms File Field
        - Secure File Handling
        - MIME Type Validation
        - Multiple File Uploads
        - Custom Validators
    2. Lab Exercise
3. **SQLAlchemy Relationship Types and Lazy Loading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - One-to-Many Relationship
        - Many-to-Many with Association Table
        - Lazy Loading Strategies
        - Association Object Pattern (with extra fields)
    2. Lab Exercise
4. **Access Control and Role Authorization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Role-Based Access Control (RBAC) Pattern
        - Role-Required Decorator
        - Permission-Based Access (Fine-Grained)
        - Flask-Principal Integration
    2. Lab Exercise

#### 2.8.6. Module 6 — Web Forms & Input Validation (Flask-WTF)

1. **Lesson 5.1 WTForms & Flask-WTF Extension**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Processing Manual HTML Forms vs Flask-WTF
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (FlaskForm Class Definition)
        - File 2: `app.py` (Flask View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `form.validate_on_submit()` do in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Form Validation & Automatic CSRF Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom In-Class Field Validation
        - CSRF Protection Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (Form with Custom & Standard Validators)
        - File 2: `templates/register.html` (Rendering Inline Validation Errors)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you write a custom field validator in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.7. Module 7 — Production Deployment

1. **Reverse Proxy and Nginx Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Nginx as Reverse Proxy for Flask
        - Gunicorn Configuration
        - SSL/HTTPS with Let's Encrypt
        - Flask ProxyFix Middleware
        - Systemd Service
    2. Lab Exercise
2. **Containerization with Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Flask Dockerfile
        - Docker Compose (Flask + MySQL + Redis)
        - Environment Management
        - Build and Run Commands
        - Health Check and Restart Policy
    2. Lab Exercise

#### 2.8.8. Module 8 — Relational Databases & ORM (Flask-SQLAlchemy)

1. **Lesson 6.1 Flask-SQLAlchemy Extension Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object-Relational Mapping (ORM)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py` (Unbound Extension Instance)
        - File 2: `config.py`
        - File 3: `app/__init__.py` (Application Factory Integration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you initialize Flask-SQLAlchemy using `db = SQLAlchemy()` in an `extensions.py` module rather than `db = SQLAlchemy(app)`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 Defining SQLAlchemy Models, Fields, & Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy Model Mapping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `models.py` (SQLAlchemy Relational Schema)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `backref` and `back_populates` in SQLAlchemy relationships?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Executing Database CRUD Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit of Work Transaction Management
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `db.session.rollback()` in Flask-SQLAlchemy?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 6.4 Schema Migrations with Flask-Migrate & Alembic**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `db.create_all()` Fails in Production
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py`
        - File 2: `app/__init__.py` (Factory Integration)
        - File 3: Command Line Execution Sequence
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask-Migrate detect changes made to SQLAlchemy models when generating migration scripts?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.9. Module 9 — Session Management, Cookies, & Authentication

1. **Lesson 7.1 User Authentication with Flask-Login**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask-Login Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (User Model with UserMixin)
        - File 2: `app.py` (Flask-Login Initialization & Auth Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `@login_manager.user_loader` in Flask-Login?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 Password Hashing & Cookie Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way Password Hashing & Salting
        - Flask Session Cookie Security Configuration
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `security_demo.py` (Password Hashing & Cookie Security Config)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is storing plain MD5 or SHA-256 hashes of passwords insecure, and how does Werkzeug address this?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.10. Module 10 — Application Structuring with Blueprints

1. **Lesson 8.1 Flask Blueprint Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is a Flask Blueprint?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `app/api/routes.py` (Blueprint Module)
        - File 2: `app/__init__.py` (Registering Blueprints in Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Flask Blueprint and how does it improve code architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.11. Module 11 — REST API Development & Serialization

1. **Lesson 9.1 RESTful API Principles & Resource Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - REST Architectural Constraints
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is idempotency in RESTful APIs and which HTTP verbs are idempotent?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 API Serialization with Flask-Marshmallow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serialization vs Deserialization
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `schemas.py` (Flask-Marshmallow Schemas)
        - File 2: `routes.py` (Using Schemas in API Views)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the primary role of Marshmallow schemas in a Flask REST API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 9.3 JWT Authentication with Flask-JWT-Extended**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON Web Token (JWT) Structure
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural difference between session-based authentication and JWT authentication?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.12. Module 12 — Advanced Flask Extensions & Background Tasks

1. **Lesson 10.1 Application Caching with Flask-Caching & Redis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Backend Caching?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@cache.cached()` and `@cache.memoize()` in Flask-Caching?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 10.2 Asynchronous Background Tasks with Celery & Redis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Asynchronous Background Tasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `celery_app.py` (Celery Integration Helper)
        - File 2: `tasks.py` (Celery Tasks)
        - File 3: `app.py` (Dispatching Tasks & Checking Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Celery used with Flask instead of Python's built-in `threading` module?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 10.3 Email Delivery with Flask-Mail**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SMTP Protocol & Synchronous vs Async Delivery
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is it crucial to send emails asynchronously in web applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.13. Module 13 — Error Handling, Logging, & Testing

1. **Lesson 11.1 Custom Error Pages & Error Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Exception Handling Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@errorhandler` and `@app_errorhandler` on a Flask Blueprint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 11.2 Application Logging & Sentry Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Logging Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `RotatingFileHandler` critical for production Python applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.8.14. Module 14 — Testing & Production Deployment

1. **Lesson 12.1 Automated Testing with Pytest & Test Client**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask `test_client()` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Shared Fixtures)
        - File 2: `test_api.py` (Pytest Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask's `app.test_client()` work and why is it preferred over HTTP requests library like `requests` during unit testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 12.2 Production Deployment with Gunicorn, Nginx, & Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Deployment Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `wsgi.py` (Production Entrypoint)
        - File 2: `Dockerfile` (Production Multi-Stage Container)
        - File 3: `docker-compose.yml` (Multi-Container Orchestration)
        - File 4: `nginx.conf` (Nginx Reverse Proxy Configuration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Flask's built-in development server never be used in production environments, and what roles do Gunicorn and Nginx play?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 2.9. MQTT Protocol

#### 2.9.1. Module 1 — MQTT Fundamentals

1. **What Is MQTT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: What Is MQTT
    2. Core Concept
        - Core Concept: What Is MQTT
    3. Syntax
        - Syntax: What Is MQTT
    4. Example
        - Example: What Is MQTT
    5. Pitfall
        - Pitfall: What Is MQTT
    6. Q & A
        - Q & A: What Is MQTT
2. **Publish Subscribe Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Publish Subscribe Model
    2. Core Concept
        - Core Concept: Publish Subscribe Model
    3. Syntax
        - Syntax: Publish Subscribe Model
    4. Example
        - Example: Publish Subscribe Model
    5. Pitfall
        - Pitfall: Publish Subscribe Model
    6. Q & A
        - Q & A: Publish Subscribe Model
3. **Topics and Wildcards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Topics and Wildcards
    2. Core Concept
        - Core Concept: Topics and Wildcards
    3. Syntax
        - Syntax: Topics and Wildcards
    4. Example
        - Example: Topics and Wildcards
    5. Pitfall
        - Pitfall: Topics and Wildcards
    6. Q & A
        - Q & A: Topics and Wildcards
4. **QoS Levels 0 1 2**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: QoS Levels 0 1 2
    2. Core Concept
        - Core Concept: QoS Levels 0 1 2
    3. Syntax
        - Syntax: QoS Levels 0 1 2
    4. Example
        - Example: QoS Levels 0 1 2
    5. Pitfall
        - Pitfall: QoS Levels 0 1 2
    6. Q & A
        - Q & A: QoS Levels 0 1 2
5. **Retained Messages and LWT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Retained Messages and LWT
    2. Core Concept
        - Core Concept: Retained Messages and LWT
    3. Syntax
        - Syntax: Retained Messages and LWT
    4. Example
        - Example: Retained Messages and LWT
    5. Pitfall
        - Pitfall: Retained Messages and LWT
    6. Q & A
        - Q & A: Retained Messages and LWT

#### 2.9.2. Module 2 — MQTT Broker Setup

1. **Mosquitto Installation on Linux**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Mosquitto Installation on Linux
    2. Core Concept
        - Core Concept: Mosquitto Installation on Linux
    3. Syntax
        - Syntax: Mosquitto Installation on Linux
    4. Example
        - Example: Mosquitto Installation on Linux
    5. Pitfall
        - Pitfall: Mosquitto Installation on Linux
    6. Q & A
        - Q & A: Mosquitto Installation on Linux
2. **Mosquitto on Raspberry Pi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Mosquitto on Raspberry Pi
    2. Core Concept
        - Core Concept: Mosquitto on Raspberry Pi
    3. Syntax
        - Syntax: Mosquitto on Raspberry Pi
    4. Example
        - Example: Mosquitto on Raspberry Pi
    5. Pitfall
        - Pitfall: Mosquitto on Raspberry Pi
    6. Q & A
        - Q & A: Mosquitto on Raspberry Pi
3. **Cloud Brokers HiveMQ EMQX**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Cloud Brokers HiveMQ EMQX
    2. Core Concept
        - Core Concept: Cloud Brokers HiveMQ EMQX
    3. Syntax
        - Syntax: Cloud Brokers HiveMQ EMQX
    4. Example
        - Example: Cloud Brokers HiveMQ EMQX
    5. Pitfall
        - Pitfall: Cloud Brokers HiveMQ EMQX
    6. Q & A
        - Q & A: Cloud Brokers HiveMQ EMQX
4. **Broker Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Broker Configuration
    2. Core Concept
        - Core Concept: Broker Configuration
    3. Syntax
        - Syntax: Broker Configuration
    4. Example
        - Example: Broker Configuration
    5. Pitfall
        - Pitfall: Broker Configuration
    6. Q & A
        - Q & A: Broker Configuration
5. **Testing with MQTT Explorer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Testing with MQTT Explorer
    2. Core Concept
        - Core Concept: Testing with MQTT Explorer
    3. Syntax
        - Syntax: Testing with MQTT Explorer
    4. Example
        - Example: Testing with MQTT Explorer
    5. Pitfall
        - Pitfall: Testing with MQTT Explorer
    6. Q & A
        - Q & A: Testing with MQTT Explorer

#### 2.9.3. Module 3 — MQTT with Python

1. **Paho MQTT Library**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Paho MQTT Library
    2. Core Concept
        - Core Concept: Paho MQTT Library
    3. Syntax
        - Syntax: Paho MQTT Library
    4. Example
        - Example: Paho MQTT Library
    5. Pitfall
        - Pitfall: Paho MQTT Library
    6. Q & A
        - Q & A: Paho MQTT Library
2. **Publisher Client**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Publisher Client
    2. Core Concept
        - Core Concept: Publisher Client
    3. Syntax
        - Syntax: Publisher Client
    4. Example
        - Example: Publisher Client
    5. Pitfall
        - Pitfall: Publisher Client
    6. Q & A
        - Q & A: Publisher Client
3. **Subscriber Client**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Subscriber Client
    2. Core Concept
        - Core Concept: Subscriber Client
    3. Syntax
        - Syntax: Subscriber Client
    4. Example
        - Example: Subscriber Client
    5. Pitfall
        - Pitfall: Subscriber Client
    6. Q & A
        - Q & A: Subscriber Client
4. **Sensor Data Publishing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Sensor Data Publishing
    2. Core Concept
        - Core Concept: Sensor Data Publishing
    3. Syntax
        - Syntax: Sensor Data Publishing
    4. Example
        - Example: Sensor Data Publishing
    5. Pitfall
        - Pitfall: Sensor Data Publishing
    6. Q & A
        - Q & A: Sensor Data Publishing
5. **MQTT Dashboard with Flask**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT Dashboard with Flask
    2. Core Concept
        - Core Concept: MQTT Dashboard with Flask
    3. Syntax
        - Syntax: MQTT Dashboard with Flask
    4. Example
        - Example: MQTT Dashboard with Flask
    5. Pitfall
        - Pitfall: MQTT Dashboard with Flask
    6. Q & A
        - Q & A: MQTT Dashboard with Flask

#### 2.9.4. Module 4 — MQTT with ESP32

1. **Arduino MQTT Library Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Arduino MQTT Library Setup
    2. Core Concept
        - Core Concept: Arduino MQTT Library Setup
    3. Syntax
        - Syntax: Arduino MQTT Library Setup
    4. Example
        - Example: Arduino MQTT Library Setup
    5. Pitfall
        - Pitfall: Arduino MQTT Library Setup
    6. Q & A
        - Q & A: Arduino MQTT Library Setup
2. **ESP32 Publisher**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 Publisher
    2. Core Concept
        - Core Concept: ESP32 Publisher
    3. Syntax
        - Syntax: ESP32 Publisher
    4. Example
        - Example: ESP32 Publisher
    5. Pitfall
        - Pitfall: ESP32 Publisher
    6. Q & A
        - Q & A: ESP32 Publisher
3. **ESP32 Subscriber**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ESP32 Subscriber
    2. Core Concept
        - Core Concept: ESP32 Subscriber
    3. Syntax
        - Syntax: ESP32 Subscriber
    4. Example
        - Example: ESP32 Subscriber
    5. Pitfall
        - Pitfall: ESP32 Subscriber
    6. Q & A
        - Q & A: ESP32 Subscriber
4. **JSON Payload over MQTT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: JSON Payload over MQTT
    2. Core Concept
        - Core Concept: JSON Payload over MQTT
    3. Syntax
        - Syntax: JSON Payload over MQTT
    4. Example
        - Example: JSON Payload over MQTT
    5. Pitfall
        - Pitfall: JSON Payload over MQTT
    6. Q & A
        - Q & A: JSON Payload over MQTT
5. **MQTT over TLS with ESP32**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT over TLS with ESP32
    2. Core Concept
        - Core Concept: MQTT over TLS with ESP32
    3. Syntax
        - Syntax: MQTT over TLS with ESP32
    4. Example
        - Example: MQTT over TLS with ESP32
    5. Pitfall
        - Pitfall: MQTT over TLS with ESP32
    6. Q & A
        - Q & A: MQTT over TLS with ESP32

#### 2.9.5. Module 5 — MQTT Security

1. **Username and Password Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Username and Password Authentication
    2. Core Concept
        - Core Concept: Username and Password Authentication
    3. Syntax
        - Syntax: Username and Password Authentication
    4. Example
        - Example: Username and Password Authentication
    5. Pitfall
        - Pitfall: Username and Password Authentication
    6. Q & A
        - Q & A: Username and Password Authentication
2. **TLS SSL for MQTT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: TLS SSL for MQTT
    2. Core Concept
        - Core Concept: TLS SSL for MQTT
    3. Syntax
        - Syntax: TLS SSL for MQTT
    4. Example
        - Example: TLS SSL for MQTT
    5. Pitfall
        - Pitfall: TLS SSL for MQTT
    6. Q & A
        - Q & A: TLS SSL for MQTT
3. **ACL Access Control Lists**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ACL Access Control Lists
    2. Core Concept
        - Core Concept: ACL Access Control Lists
    3. Syntax
        - Syntax: ACL Access Control Lists
    4. Example
        - Example: ACL Access Control Lists
    5. Pitfall
        - Pitfall: ACL Access Control Lists
    6. Q & A
        - Q & A: ACL Access Control Lists
4. **Certificate-Based Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Certificate-Based Authentication
    2. Core Concept
        - Core Concept: Certificate-Based Authentication
    3. Syntax
        - Syntax: Certificate-Based Authentication
    4. Example
        - Example: Certificate-Based Authentication
    5. Pitfall
        - Pitfall: Certificate-Based Authentication
    6. Q & A
        - Q & A: Certificate-Based Authentication
5. **MQTT Security Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT Security Best Practices
    2. Core Concept
        - Core Concept: MQTT Security Best Practices
    3. Syntax
        - Syntax: MQTT Security Best Practices
    4. Example
        - Example: MQTT Security Best Practices
    5. Pitfall
        - Pitfall: MQTT Security Best Practices
    6. Q & A
        - Q & A: MQTT Security Best Practices

#### 2.9.6. Module 6 — MQTT Integrations

1. **MQTT to Node-RED**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT to Node-RED
    2. Core Concept
        - Core Concept: MQTT to Node-RED
    3. Syntax
        - Syntax: MQTT to Node-RED
    4. Example
        - Example: MQTT to Node-RED
    5. Pitfall
        - Pitfall: MQTT to Node-RED
    6. Q & A
        - Q & A: MQTT to Node-RED
2. **MQTT to InfluxDB**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT to InfluxDB
    2. Core Concept
        - Core Concept: MQTT to InfluxDB
    3. Syntax
        - Syntax: MQTT to InfluxDB
    4. Example
        - Example: MQTT to InfluxDB
    5. Pitfall
        - Pitfall: MQTT to InfluxDB
    6. Q & A
        - Q & A: MQTT to InfluxDB
3. **MQTT to Grafana**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT to Grafana
    2. Core Concept
        - Core Concept: MQTT to Grafana
    3. Syntax
        - Syntax: MQTT to Grafana
    4. Example
        - Example: MQTT to Grafana
    5. Pitfall
        - Pitfall: MQTT to Grafana
    6. Q & A
        - Q & A: MQTT to Grafana
4. **MQTT to AWS IoT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT to AWS IoT
    2. Core Concept
        - Core Concept: MQTT to AWS IoT
    3. Syntax
        - Syntax: MQTT to AWS IoT
    4. Example
        - Example: MQTT to AWS IoT
    5. Pitfall
        - Pitfall: MQTT to AWS IoT
    6. Q & A
        - Q & A: MQTT to AWS IoT
5. **MQTT to WebSocket Bridge**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: MQTT to WebSocket Bridge
    2. Core Concept
        - Core Concept: MQTT to WebSocket Bridge
    3. Syntax
        - Syntax: MQTT to WebSocket Bridge
    4. Example
        - Example: MQTT to WebSocket Bridge
    5. Pitfall
        - Pitfall: MQTT to WebSocket Bridge
    6. Q & A
        - Q & A: MQTT to WebSocket Bridge

### 2.10. IoT Cloud

#### 2.10.1. Module 1 — Cloud IoT Architecture and Device Identity

1. **End-to-End Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Devices, gateways, brokers, ingestion, processing, storage, and applications
    2. Telemetry, commands, events, and digital state
    3. Cloud, edge, and hybrid responsibility boundaries
2. **Protocols and Message Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. MQTT and HTTP trade-offs
    2. Topic hierarchy, payload schema, QoS, idempotency, and timestamps
    3. Connection lifecycle, retries, backoff, and offline buffering
3. **Device Identity**
    - **Course Coverage:** 🟢 Covered in Class
    1. Unique identities, credentials, and provisioning
    2. Certificate-based authentication concepts
    3. Lab: securely connect a simulated device to a broker

#### 2.10.2. Module 2 — Ingestion and Fleet Management

1. **Scalable Ingestion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Broker and gateway roles
    2. Routing, filtering, throttling, and dead-letter handling
    3. Design for intermittent connectivity and duplicate messages
2. **Device Registry and Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Metadata, capabilities, tags, and groups
    2. Desired versus reported state and device shadows/twins
    3. Remote configuration with validation and rollback
3. **Provisioning and Updates**
    - **Course Coverage:** 🟢 Covered in Class
    1. Claim-based and factory provisioning patterns
    2. OTA firmware workflow and staged rollout
    3. Lab: register, group, configure, and update a test fleet

#### 2.10.3. Module 3 — Data Processing and Storage

1. **Stream Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Rules, windows, aggregation, enrichment, and anomaly triggers
    2. Event-time versus processing-time concepts
    3. Serverless and managed-stream processing patterns
2. **Storage Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Time-series, relational, object, and document storage
    2. Hot, warm, and cold retention tiers
    3. Partitioning, indexing, lifecycle, and cost considerations
3. **Data Pipeline Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Route telemetry into appropriate stores
    2. Compute rolling metrics and alerts
    3. Query device history and export an analytics dataset

#### 2.10.4. Module 4 — Applications, APIs, and Automation

1. **Dashboards and Alerts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Operational dashboards and device drill-down
    2. Threshold, rate-of-change, and absence-of-data alerts
    3. Notification routing, acknowledgement, and escalation
2. **Command and Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Cloud-to-device commands and acknowledgements
    2. Safe command authorization, expiry, and deduplication
    3. Audit trails for remote actions
3. **Integration Lab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Expose data through a secured REST API
    2. Trigger an automation workflow from a device event
    3. Build a dashboard with live and historical views

#### 2.10.5. Module 5 — Security, Observability, Cost, and Capstone

1. **Security Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Least privilege, encryption, key rotation, and secrets
    2. Tenant and fleet isolation
    3. Threat modeling and incident response for IoT
2. **Reliability and Cost**
    - **Course Coverage:** 🟢 Covered in Class
    1. Logs, metrics, traces, device health, and SLOs
    2. Load testing, quotas, backpressure, and disaster recovery
    3. Estimate and optimize messaging, compute, and storage cost
3. **Capstone: Managed IoT Fleet**
    - **Course Coverage:** 🟢 Covered in Class
    1. Provision simulated or physical devices
    2. Implement ingestion, storage, dashboard, alerts, and commands
    3. Demonstrate security, failure recovery, observability, and cost estimate

### 2.11. Basic ML for IoT

#### 2.11.1. Module 1 — Machine Learning and Edge AI Foundations

1. **ML Concepts for IoT Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Learning types: supervised, unsupervised, and anomaly detection
    2. Features, labels, training, inference, and model lifecycle
    3. Cloud inference versus edge inference trade-offs
2. **IoT Data and Use-Case Framing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Telemetry, time-series, audio, image, and event data
    2. Define measurable objectives, constraints, and success metrics
    3. Select classification, regression, forecasting, or anomaly detection
3. **Development Environment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python, notebooks, NumPy, pandas, and scikit-learn
    2. Dataset versioning and reproducible experiments
    3. Lab: train and inspect a first sensor classifier

#### 2.11.2. Module 2 — Sensor Data Preparation and Feature Engineering

1. **Data Acquisition and Labeling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sampling rate, resolution, calibration, and timestamping
    2. Windowing continuous sensor streams
    3. Label quality, class balance, and data leakage prevention
2. **Cleaning and Transformation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Missing values, noise filtering, smoothing, and outlier handling
    2. Normalization, standardization, and categorical encoding
    3. Train, validation, and test splits for time-dependent data
3. **Feature Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Time-domain statistical features
    2. Frequency-domain features using FFT
    3. Lab: build a reusable sensor preprocessing pipeline

#### 2.11.3. Module 3 — Model Development and Evaluation

1. **Classification and Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Linear and logistic models
    2. Decision trees, random forests, and gradient boosting
    3. Model selection using baselines and cross-validation
2. **Anomaly Detection and Forecasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Threshold and statistical baselines
    2. Isolation Forest and one-class approaches
    3. Short-horizon forecasting for telemetry
3. **Evaluation for IoT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Precision, recall, F1, ROC-AUC, MAE, and RMSE
    2. Latency, memory, energy, and false-alarm costs
    3. Lab: compare models using accuracy and device constraints

#### 2.11.4. Module 4 — Tiny Models and Edge Deployment

1. **Model Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Feature reduction and compact model selection
    2. Quantization, pruning, and knowledge distillation concepts
    3. Accuracy-size-latency benchmarking
2. **Deployment Workflow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Export formats and inference runtimes
    2. Input/output preprocessing parity
    3. Deploy to a gateway or microcontroller-class target
3. **On-Device Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Memory budgeting and timing measurements
    2. Offline behavior and fallback rules
    3. Lab: run and profile streaming inference

#### 2.11.5. Module 5 — Operations, Safety, and Capstone

1. **Production Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Data drift, concept drift, and sensor degradation
    2. Model telemetry and alert thresholds
    3. Versioning, rollback, and controlled updates
2. **Responsible Edge AI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Privacy-preserving local inference
    2. Bias, explainability, safety boundaries, and human override
    3. Threats involving poisoned data and model extraction
3. **Capstone: Predictive IoT Node**
    - **Course Coverage:** 🟢 Covered in Class
    1. Collect and label a real sensor dataset
    2. Train, optimize, and deploy a model
    3. Document metrics, architecture, limitations, and demo results

### 2.12. Computer Vision for IoT

#### 2.12.1. Module 1 — Edge Vision Foundations

1. **Image and Camera Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pixels, color spaces, resolution, frame rate, and dynamic range
    2. Lenses, focus, exposure, lighting, and field of view
    3. Camera interfaces and bandwidth constraints
2. **Edge Vision Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Camera, processor, inference runtime, and communication path
    2. Edge, gateway, and cloud processing trade-offs
    3. Latency, privacy, power, memory, and thermal budgets
3. **Environment and First Capture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python and OpenCV setup
    2. Capture images and video from a camera or file
    3. Lab: measure frame rate and image quality under varied lighting

#### 2.12.2. Module 2 — Image Processing and Data Pipelines

1. **Core Image Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Resize, crop, normalize, blur, threshold, and morphology
    2. Contours, edges, geometric transforms, and regions of interest
    3. Build a deterministic preprocessing pipeline
2. **Dataset Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Image collection, annotation, and class definitions
    2. Augmentation and train-validation-test splits
    3. Prevent leakage, imbalance, and environmental bias
3. **Classical Vision**
    - **Course Coverage:** 🟢 Covered in Class
    1. Motion detection and background subtraction
    2. Feature matching and simple tracking
    3. Lab: implement an event-triggered camera pipeline

#### 2.12.3. Module 3 — Vision Models for Constrained Devices

1. **Classification and Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. CNN and transfer-learning concepts
    2. Object detection outputs, anchors, confidence, and NMS
    3. Select a model based on accuracy and resource limits
2. **Segmentation, Tracking, and OCR**
    - **Course Coverage:** 🟢 Covered in Class
    1. Semantic segmentation and mask processing
    2. Multi-frame tracking and identity continuity
    3. OCR pipelines for labels, meters, and displays
3. **Optimization and Conversion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Quantization and input-shape trade-offs
    2. ONNX, TensorFlow Lite, and hardware-specific runtimes
    3. Lab: benchmark model size, latency, and accuracy

#### 2.12.4. Module 4 — Device Integration and Event Delivery

1. **Embedded and Gateway Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Raspberry Pi and accelerator-assisted inference
    2. ESP32-class camera use cases and limitations
    3. Startup services, watchdogs, and offline buffering
2. **IoT Messaging and APIs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Publish detections through MQTT
    2. REST endpoints for configuration and snapshots
    3. Event schemas, timestamps, device identity, and deduplication
3. **Storage and Dashboards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Store metadata separately from image evidence
    2. Retention, compression, and upload policies
    3. Lab: build a live detection dashboard

#### 2.12.5. Module 5 — Security, Reliability, and Capstone

1. **Security and Privacy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Camera credentials, encryption, and signed updates
    2. Privacy masking, access control, and retention policy
    3. Adversarial inputs and tamper detection concepts
2. **Field Reliability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lighting drift, lens obstruction, and camera movement
    2. Confidence calibration, health checks, and alert suppression
    3. Remote logs, metrics, rollback, and fleet updates
3. **Capstone: Smart Vision Node**
    - **Course Coverage:** 🟢 Covered in Class
    1. Choose inspection, safety, occupancy, or agriculture use case
    2. Deploy real-time inference with MQTT/API integration
    3. Validate accuracy, latency, power, privacy, and failure recovery

### 2.13. IoT Projects

#### 2.13.1. Module 1 — End-to-End IoT Systems

1. **01 01 Web Based Environmental Data Logger**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 01 01 Web Based Environmental Data Logger
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
2. **01 02 Smart Appliance Relay Switch**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 01 02 Smart Appliance Relay Switch
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
3. **01 03 Rfid Attendance Door Access**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 01 03 Rfid Attendance Door Access
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
4. **02 01 Mqtt Industrial Tank Pump Controller**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 02 01 Mqtt Industrial Tank Pump Controller
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
5. **02 02 Cellular Gps Fleet Tracker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 02 02 Cellular Gps Fleet Tracker
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
6. **02 03 Lorawan Soil Moisture Agricultural Node**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 02 03 Lorawan Soil Moisture Agricultural Node
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
7. **03 01 Ble Beacon Indoor Asset Tracker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 03 01 Ble Beacon Indoor Asset Tracker
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
8. **03 02 Thread Matter Smart Home Mesh Light**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 03 02 Thread Matter Smart Home Mesh Light
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
9. **04 01 Tiny Ml Vibration Anomaly Detector**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 04 01 Tiny Ml Vibration Anomaly Detector
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
10. **04 02 Edge Ai Camera Person Counter**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 04 02 Edge Ai Camera Person Counter
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
11. **05 01 Ota Firmware Update Server Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 05 01 Ota Firmware Update Server Pipeline
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
12. **05 02 Industrial Modbus Rtu To Cloud Gateway**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of 05 02 Industrial Modbus Rtu To Cloud Gateway
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
