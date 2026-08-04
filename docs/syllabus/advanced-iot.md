# Advanced IoT — Syllabus

## Study Flow

### 1. IoT Hardware

#### 1.1. Module 1 — ESP32 Microcontroller Architecture & Environment Setup

1. **Lesson 1.1 ESP32 Hardware Architecture & Dual-Core Xtensa/RISC-V**
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

#### 1.2. Module 2 — Peripherals, GPIO, & Communication Protocols

1. **Lesson 2.1 GPIO Digital Input/Output & Interrupt Service Routines (ISR)**
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

#### 1.3. Module 3 — Embedded Hardware & Peripherals

1. **23 Core Electrical Physics**
    1. Overview of 23 Core Electrical Physics
        - Core Embedded Hardware Concepts
    2. Lab Exercise
2. **24 Circuit Analysis Laws**
    1. Overview of 24 Circuit Analysis Laws
        - Core Embedded Hardware Concepts
    2. Lab Exercise
3. **25 Diagnostic Measurement Instrumentation**
    1. Overview of 25 Diagnostic Measurement Instrumentation
        - Core Embedded Hardware Concepts
    2. Lab Exercise
4. **26 Passive Components**
    1. Overview of 26 Passive Components
        - Core Embedded Hardware Concepts
    2. Lab Exercise
5. **27 Semiconductor Diodes**
    1. Overview of 27 Semiconductor Diodes
        - Core Embedded Hardware Concepts
    2. Lab Exercise
6. **28 Bipolar Junction Transistors**
    1. Overview of 28 Bipolar Junction Transistors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
7. **29 Field Effect Transistors**
    1. Overview of 29 Field Effect Transistors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
8. **30 Operational Amplifiers**
    1. Overview of 30 Operational Amplifiers
        - Core Embedded Hardware Concepts
    2. Lab Exercise
9. **31 Power Supplies And Linear Regulation**
    1. Overview of 31 Power Supplies And Linear Regulation
        - Core Embedded Hardware Concepts
    2. Lab Exercise
10. **32 Switched Mode Power Supplies**
    1. Overview of 32 Switched Mode Power Supplies
        - Core Embedded Hardware Concepts
    2. Lab Exercise
11. **33 Microcontroller Core Architecture**
    1. Overview of 33 Microcontroller Core Architecture
        - Core Embedded Hardware Concepts
    2. Lab Exercise
12. **34 Clock Generation And Timing Systems**
    1. Overview of 34 Clock Generation And Timing Systems
        - Core Embedded Hardware Concepts
    2. Lab Exercise
13. **35 Gpio Electrical Characteristics**
    1. Overview of 35 Gpio Electrical Characteristics
        - Core Embedded Hardware Concepts
    2. Lab Exercise
14. **36 Interrupt Controllers And Nvic**
    1. Overview of 36 Interrupt Controllers And Nvic
        - Core Embedded Hardware Concepts
    2. Lab Exercise
15. **37 Analog To Digital Converters**
    1. Overview of 37 Analog To Digital Converters
        - Core Embedded Hardware Concepts
    2. Lab Exercise
16. **38 Digital To Analog Converters**
    1. Overview of 38 Digital To Analog Converters
        - Core Embedded Hardware Concepts
    2. Lab Exercise
17. **39 Dma Controllers And Memory Transfer**
    1. Overview of 39 Dma Controllers And Memory Transfer
        - Core Embedded Hardware Concepts
    2. Lab Exercise
18. **40 Pulse Width Modulation**
    1. Overview of 40 Pulse Width Modulation
        - Core Embedded Hardware Concepts
    2. Lab Exercise
19. **41 Uart Usart Serial Communication**
    1. Overview of 41 Uart Usart Serial Communication
        - Core Embedded Hardware Concepts
    2. Lab Exercise
20. **42 Spi Bus Protocol**
    1. Overview of 42 Spi Bus Protocol
        - Core Embedded Hardware Concepts
    2. Lab Exercise
21. **43 I2C Bus Protocol**
    1. Overview of 43 I2C Bus Protocol
        - Core Embedded Hardware Concepts
    2. Lab Exercise
22. **44 Can Bus Protocol**
    1. Overview of 44 Can Bus Protocol
        - Core Embedded Hardware Concepts
    2. Lab Exercise
23. **45 Temperature And Humidity Sensors**
    1. Overview of 45 Temperature And Humidity Sensors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
24. **46 Motion And Inertial Measurement**
    1. Overview of 46 Motion And Inertial Measurement
        - Core Embedded Hardware Concepts
    2. Lab Exercise
25. **47 Optical And Ranging Sensors**
    1. Overview of 47 Optical And Ranging Sensors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
26. **48 Environmental Gas Pressure Sensors**
    1. Overview of 48 Environmental Gas Pressure Sensors
        - Core Embedded Hardware Concepts
    2. Lab Exercise
27. **49 Dc Motor Control H Bridges**
    1. Overview of 49 Dc Motor Control H Bridges
        - Core Embedded Hardware Concepts
    2. Lab Exercise
28. **50 Stepper Motor Driving Microstepping**
    1. Overview of 50 Stepper Motor Driving Microstepping
        - Core Embedded Hardware Concepts
    2. Lab Exercise
29. **51 Servo Motor Control**
    1. Overview of 51 Servo Motor Control
        - Core Embedded Hardware Concepts
    2. Lab Exercise
30. **52 Solenoids Relays Power Switching**
    1. Overview of 52 Solenoids Relays Power Switching
        - Core Embedded Hardware Concepts
    2. Lab Exercise
31. **53 Wifi Networking Esp Supplicant**
    1. Overview of 53 Wifi Networking Esp Supplicant
        - Core Embedded Hardware Concepts
    2. Lab Exercise
32. **54 Ble Gap Gatt Profile Architecture**
    1. Overview of 54 Ble Gap Gatt Profile Architecture
        - Core Embedded Hardware Concepts
    2. Lab Exercise
33. **55 Ieee 802 15 4 Zigbee Thread**
    1. Overview of 55 Ieee 802 15 4 Zigbee Thread
        - Core Embedded Hardware Concepts
    2. Lab Exercise
34. **56 Lora And Lorawan Mac Architecture**
    1. Overview of 56 Lora And Lorawan Mac Architecture
        - Core Embedded Hardware Concepts
    2. Lab Exercise
35. **57 Cellular Iot Nb Iot Cat M1**
    1. Overview of 57 Cellular Iot Nb Iot Cat M1
        - Core Embedded Hardware Concepts
    2. Lab Exercise
36. **58 Battery Chemistry Cell Selection**
    1. Overview of 58 Battery Chemistry Cell Selection
        - Core Embedded Hardware Concepts
    2. Lab Exercise
37. **59 Battery Management Systems Bms**
    1. Overview of 59 Battery Management Systems Bms
        - Core Embedded Hardware Concepts
    2. Lab Exercise
38. **60 Energy Harvesting Techniques**
    1. Overview of 60 Energy Harvesting Techniques
        - Core Embedded Hardware Concepts
    2. Lab Exercise
39. **61 Low Power Sleep Modes**
    1. Overview of 61 Low Power Sleep Modes
        - Core Embedded Hardware Concepts
    2. Lab Exercise
40. **62 Hardware Root Of Trust Secure Elements**
    1. Overview of 62 Hardware Root Of Trust Secure Elements
        - Core Embedded Hardware Concepts
    2. Lab Exercise
41. **63 Cryptographic Hardware Accelerators**
    1. Overview of 63 Cryptographic Hardware Accelerators
        - Core Embedded Hardware Concepts
    2. Lab Exercise
42. **64 Secure Boot And Flash Encryption**
    1. Overview of 64 Secure Boot And Flash Encryption
        - Core Embedded Hardware Concepts
    2. Lab Exercise
43. **65 Jtag Swd On Chip Debugging**
    1. Overview of 65 Jtag Swd On Chip Debugging
        - Core Embedded Hardware Concepts
    2. Lab Exercise
44. **66 Logic Analysers Protocol Decoding**
    1. Overview of 66 Logic Analysers Protocol Decoding
        - Core Embedded Hardware Concepts
    2. Lab Exercise
45. **67 Oscilloscope Signal Integrity**
    1. Overview of 67 Oscilloscope Signal Integrity
        - Core Embedded Hardware Concepts
    2. Lab Exercise
46. **68 Hardware In Loop Testing**
    1. Overview of 68 Hardware In Loop Testing
        - Core Embedded Hardware Concepts
    2. Lab Exercise

#### 1.4. Module 4 — Real-Time Operating System (FreeRTOS Core Mechanics)

1. **Lesson 3.1 FreeRTOS Task Creation, Multi-Threading, & Core Pinning**
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

#### 1.5. Module 5 — FreeRTOS Inter-Task Communication & Synchronization

1. **Lesson 4.1 FreeRTOS Queues & Inter-Task Messaging**
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

#### 1.6. Module 6 — Wi-Fi Networking & Wireless Connectivity

1. **Lesson 5.1 Wi-Fi Station (STA) Mode & Access Point (AP) Configuration**
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

#### 1.7. Module 7 — IoT Network Protocols: MQTT, HTTP REST, & WebSockets

1. **Lesson 6.1 HTTP REST Client Requests from ESP32**
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

#### 1.8. Module 8 — Low Power Modes & Deep Sleep Architecture

1. **Lesson 7.1 Deep Sleep Modes & RTC Memory Retention**
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

#### 1.9. Module 9 — Over-The-Air (OTA) Firmware Updates & Security

1. **Lesson 8.1 Over-The-Air (OTA) Firmware Updates**
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

#### 1.10. Module 10 — Embedded Asynchronous Web Servers & Filesystems

1. **Lesson 9.1 Embedded Filesystems (SPIFFS / LittleFS) & Static File Serving**
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

#### 1.11. Module 11 — Full-Stack End-to-End IoT Capstone Architecture

1. **Lesson 10.1 Full-Stack IoT System Architecture & Protocol Integration**
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

### 2. Arduino

#### 2.1. Module 1 — Arduino Introduction

1. **What Is Arduino**
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

#### 2.2. Module 2 — Digital I/O

1. **Digital Read and Write**
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

#### 2.3. Module 3 — Analog I/O

1. **analogRead and Potentiometer**
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

#### 2.4. Module 4 — Serial Communication

1. **Serial Monitor Basics**
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

#### 2.5. Module 5 — Sensors with Arduino

1. **DHT11 Temperature and Humidity**
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

#### 2.6. Module 6 — Actuators with Arduino

1. **Servo Motor Control**
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

#### 2.7. Module 7 — Displays

1. **16x2 LCD with Arduino**
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

#### 2.8. Module 8 — Communication Protocols

1. **I2C with Arduino**
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

#### 2.9. Module 9 — Arduino Projects

1. **Temperature Monitoring System**
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

#### 2.10. Module 10 — Advanced Arduino

1. **Arduino Interrupts**
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

### 3. ESP32

#### 3.1. Module 1 — ESP32 Introduction

1. **ESP32 vs ESP8266 vs Arduino**
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

#### 3.2. Module 2 — ESP32 GPIO

1. **Digital I/O on ESP32**
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

#### 3.3. Module 3 — WiFi

1. **WiFi Station Mode**
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

#### 3.4. Module 4 — Bluetooth and BLE

1. **Classic Bluetooth Basics**
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

#### 3.5. Module 5 — MQTT with ESP32

1. **MQTT Setup on ESP32**
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

#### 3.6. Module 6 — HTTP and REST API

1. **ESP32 HTTP Client**
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

#### 3.7. Module 7 — ESP32 Sensors

1. **DHT22 Temperature and Humidity**
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

#### 3.8. Module 8 — Deep Sleep and Power Management

1. **ESP32 Power Modes**
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

#### 3.9. Module 9 — OTA Updates

1. **OTA Concept**
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

#### 3.10. Module 10 — FreeRTOS on ESP32

1. **FreeRTOS Tasks on ESP32**
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

#### 3.11. Module 11 — ESP32 Projects

1. **WiFi Sensor Dashboard**
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

### 4. Raspberry Pi

#### 4.1. Module 1 — Raspberry Pi Fundamentals

1. **Raspberry Pi Hardware Overview**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Inspecting Raspberry Pi System Specs via Terminal
    5. Pitfall
    6. Q & A
2. **Raspberry Pi OS Setup**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Raspberry Pi OS Setup Example
    5. Pitfall
    6. Q & A
3. **Linux Command Line on Pi**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Linux Command Line on Pi Example
    5. Pitfall
    6. Q & A
4. **GPIO Control with Python**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi GPIO Control with Python Example
    5. Pitfall
    6. Q & A
5. **Pi Camera Module Setup**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Pi Camera Module Setup Example
    5. Pitfall
    6. Q & A

#### 4.2. Module 2 — Interfacing and Sensors

1. **I2C and SPI on Raspberry Pi**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi I2C and SPI on Raspberry Pi Example
    5. Pitfall
    6. Q & A
2. **Reading Analog Sensors via MCP3008 ADC**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Reading Analog Sensors via MCP3008 ADC Example
    5. Pitfall
    6. Q & A
3. **UART Serial Communication**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi UART Serial Communication Example
    5. Pitfall
    6. Q & A
4. **PWM and Servo Motor Control**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi PWM and Servo Motor Control Example
    5. Pitfall
    6. Q & A
5. **OLED Display Interfacing**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi OLED Display Interfacing Example
    5. Pitfall
    6. Q & A

#### 4.3. Module 3 — IoT Edge Gateway and Server

1. **Mosquitto MQTT Broker on Pi**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Mosquitto MQTT Broker on Pi Example
    5. Pitfall
    6. Q & A
2. **Node-RED Visual IoT Workflow**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Node-RED Visual IoT Workflow Example
    5. Pitfall
    6. Q & A
3. **Flask Web Server for GPIO Control**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Flask Web Server for GPIO Control Example
    5. Pitfall
    6. Q & A
4. **Database Storage with SQLite & InfluxDB**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Database Storage with SQLite & InfluxDB Example
    5. Pitfall
    6. Q & A
5. **Deploying IoT Gateway in Docker**
    1. Overview
    2. Concept
    3. Syntax
    4. Example
        - Raspberry Pi Deploying IoT Gateway in Docker Example
    5. Pitfall
    6. Q & A

### 5. MQTT Protocol

#### 5.1. Module 1 — MQTT Fundamentals

1. **What Is MQTT**
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

#### 5.2. Module 2 — MQTT Broker Setup

1. **Mosquitto Installation on Linux**
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

#### 5.3. Module 3 — MQTT with Python

1. **Paho MQTT Library**
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

#### 5.4. Module 4 — MQTT with ESP32

1. **Arduino MQTT Library Setup**
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

#### 5.5. Module 5 — MQTT Security

1. **Username and Password Authentication**
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

#### 5.6. Module 6 — MQTT Integrations

1. **MQTT to Node-RED**
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

### 6. IoT Cloud

#### 6.1. Module 1 — Cloud IoT Architecture and Device Identity

1. **End-to-End Architecture**
    1. Devices, gateways, brokers, ingestion, processing, storage, and applications
    2. Telemetry, commands, events, and digital state
    3. Cloud, edge, and hybrid responsibility boundaries
2. **Protocols and Message Design**
    1. MQTT and HTTP trade-offs
    2. Topic hierarchy, payload schema, QoS, idempotency, and timestamps
    3. Connection lifecycle, retries, backoff, and offline buffering
3. **Device Identity**
    1. Unique identities, credentials, and provisioning
    2. Certificate-based authentication concepts
    3. Lab: securely connect a simulated device to a broker

#### 6.2. Module 2 — Ingestion and Fleet Management

1. **Scalable Ingestion**
    1. Broker and gateway roles
    2. Routing, filtering, throttling, and dead-letter handling
    3. Design for intermittent connectivity and duplicate messages
2. **Device Registry and Configuration**
    1. Metadata, capabilities, tags, and groups
    2. Desired versus reported state and device shadows/twins
    3. Remote configuration with validation and rollback
3. **Provisioning and Updates**
    1. Claim-based and factory provisioning patterns
    2. OTA firmware workflow and staged rollout
    3. Lab: register, group, configure, and update a test fleet

#### 6.3. Module 3 — Data Processing and Storage

1. **Stream Processing**
    1. Rules, windows, aggregation, enrichment, and anomaly triggers
    2. Event-time versus processing-time concepts
    3. Serverless and managed-stream processing patterns
2. **Storage Design**
    1. Time-series, relational, object, and document storage
    2. Hot, warm, and cold retention tiers
    3. Partitioning, indexing, lifecycle, and cost considerations
3. **Data Pipeline Lab**
    1. Route telemetry into appropriate stores
    2. Compute rolling metrics and alerts
    3. Query device history and export an analytics dataset

#### 6.4. Module 4 — Applications, APIs, and Automation

1. **Dashboards and Alerts**
    1. Operational dashboards and device drill-down
    2. Threshold, rate-of-change, and absence-of-data alerts
    3. Notification routing, acknowledgement, and escalation
2. **Command and Control**
    1. Cloud-to-device commands and acknowledgements
    2. Safe command authorization, expiry, and deduplication
    3. Audit trails for remote actions
3. **Integration Lab**
    1. Expose data through a secured REST API
    2. Trigger an automation workflow from a device event
    3. Build a dashboard with live and historical views

#### 6.5. Module 5 — Security, Observability, Cost, and Capstone

1. **Security Operations**
    1. Least privilege, encryption, key rotation, and secrets
    2. Tenant and fleet isolation
    3. Threat modeling and incident response for IoT
2. **Reliability and Cost**
    1. Logs, metrics, traces, device health, and SLOs
    2. Load testing, quotas, backpressure, and disaster recovery
    3. Estimate and optimize messaging, compute, and storage cost
3. **Capstone: Managed IoT Fleet**
    1. Provision simulated or physical devices
    2. Implement ingestion, storage, dashboard, alerts, and commands
    3. Demonstrate security, failure recovery, observability, and cost estimate

### 7. Basic ML for IoT

#### 7.1. Module 1 — Machine Learning and Edge AI Foundations

1. **ML Concepts for IoT Systems**
    1. Learning types: supervised, unsupervised, and anomaly detection
    2. Features, labels, training, inference, and model lifecycle
    3. Cloud inference versus edge inference trade-offs
2. **IoT Data and Use-Case Framing**
    1. Telemetry, time-series, audio, image, and event data
    2. Define measurable objectives, constraints, and success metrics
    3. Select classification, regression, forecasting, or anomaly detection
3. **Development Environment**
    1. Python, notebooks, NumPy, pandas, and scikit-learn
    2. Dataset versioning and reproducible experiments
    3. Lab: train and inspect a first sensor classifier

#### 7.2. Module 2 — Sensor Data Preparation and Feature Engineering

1. **Data Acquisition and Labeling**
    1. Sampling rate, resolution, calibration, and timestamping
    2. Windowing continuous sensor streams
    3. Label quality, class balance, and data leakage prevention
2. **Cleaning and Transformation**
    1. Missing values, noise filtering, smoothing, and outlier handling
    2. Normalization, standardization, and categorical encoding
    3. Train, validation, and test splits for time-dependent data
3. **Feature Engineering**
    1. Time-domain statistical features
    2. Frequency-domain features using FFT
    3. Lab: build a reusable sensor preprocessing pipeline

#### 7.3. Module 3 — Model Development and Evaluation

1. **Classification and Regression**
    1. Linear and logistic models
    2. Decision trees, random forests, and gradient boosting
    3. Model selection using baselines and cross-validation
2. **Anomaly Detection and Forecasting**
    1. Threshold and statistical baselines
    2. Isolation Forest and one-class approaches
    3. Short-horizon forecasting for telemetry
3. **Evaluation for IoT**
    1. Precision, recall, F1, ROC-AUC, MAE, and RMSE
    2. Latency, memory, energy, and false-alarm costs
    3. Lab: compare models using accuracy and device constraints

#### 7.4. Module 4 — Tiny Models and Edge Deployment

1. **Model Optimization**
    1. Feature reduction and compact model selection
    2. Quantization, pruning, and knowledge distillation concepts
    3. Accuracy-size-latency benchmarking
2. **Deployment Workflow**
    1. Export formats and inference runtimes
    2. Input/output preprocessing parity
    3. Deploy to a gateway or microcontroller-class target
3. **On-Device Validation**
    1. Memory budgeting and timing measurements
    2. Offline behavior and fallback rules
    3. Lab: run and profile streaming inference

#### 7.5. Module 5 — Operations, Safety, and Capstone

1. **Production Monitoring**
    1. Data drift, concept drift, and sensor degradation
    2. Model telemetry and alert thresholds
    3. Versioning, rollback, and controlled updates
2. **Responsible Edge AI**
    1. Privacy-preserving local inference
    2. Bias, explainability, safety boundaries, and human override
    3. Threats involving poisoned data and model extraction
3. **Capstone: Predictive IoT Node**
    1. Collect and label a real sensor dataset
    2. Train, optimize, and deploy a model
    3. Document metrics, architecture, limitations, and demo results

### 8. Computer Vision for IoT

#### 8.1. Module 1 — Edge Vision Foundations

1. **Image and Camera Fundamentals**
    1. Pixels, color spaces, resolution, frame rate, and dynamic range
    2. Lenses, focus, exposure, lighting, and field of view
    3. Camera interfaces and bandwidth constraints
2. **Edge Vision Architecture**
    1. Camera, processor, inference runtime, and communication path
    2. Edge, gateway, and cloud processing trade-offs
    3. Latency, privacy, power, memory, and thermal budgets
3. **Environment and First Capture**
    1. Python and OpenCV setup
    2. Capture images and video from a camera or file
    3. Lab: measure frame rate and image quality under varied lighting

#### 8.2. Module 2 — Image Processing and Data Pipelines

1. **Core Image Operations**
    1. Resize, crop, normalize, blur, threshold, and morphology
    2. Contours, edges, geometric transforms, and regions of interest
    3. Build a deterministic preprocessing pipeline
2. **Dataset Engineering**
    1. Image collection, annotation, and class definitions
    2. Augmentation and train-validation-test splits
    3. Prevent leakage, imbalance, and environmental bias
3. **Classical Vision**
    1. Motion detection and background subtraction
    2. Feature matching and simple tracking
    3. Lab: implement an event-triggered camera pipeline

#### 8.3. Module 3 — Vision Models for Constrained Devices

1. **Classification and Detection**
    1. CNN and transfer-learning concepts
    2. Object detection outputs, anchors, confidence, and NMS
    3. Select a model based on accuracy and resource limits
2. **Segmentation, Tracking, and OCR**
    1. Semantic segmentation and mask processing
    2. Multi-frame tracking and identity continuity
    3. OCR pipelines for labels, meters, and displays
3. **Optimization and Conversion**
    1. Quantization and input-shape trade-offs
    2. ONNX, TensorFlow Lite, and hardware-specific runtimes
    3. Lab: benchmark model size, latency, and accuracy

#### 8.4. Module 4 — Device Integration and Event Delivery

1. **Embedded and Gateway Deployment**
    1. Raspberry Pi and accelerator-assisted inference
    2. ESP32-class camera use cases and limitations
    3. Startup services, watchdogs, and offline buffering
2. **IoT Messaging and APIs**
    1. Publish detections through MQTT
    2. REST endpoints for configuration and snapshots
    3. Event schemas, timestamps, device identity, and deduplication
3. **Storage and Dashboards**
    1. Store metadata separately from image evidence
    2. Retention, compression, and upload policies
    3. Lab: build a live detection dashboard

#### 8.5. Module 5 — Security, Reliability, and Capstone

1. **Security and Privacy**
    1. Camera credentials, encryption, and signed updates
    2. Privacy masking, access control, and retention policy
    3. Adversarial inputs and tamper detection concepts
2. **Field Reliability**
    1. Lighting drift, lens obstruction, and camera movement
    2. Confidence calibration, health checks, and alert suppression
    3. Remote logs, metrics, rollback, and fleet updates
3. **Capstone: Smart Vision Node**
    1. Choose inspection, safety, occupancy, or agriculture use case
    2. Deploy real-time inference with MQTT/API integration
    3. Validate accuracy, latency, power, privacy, and failure recovery

### 9. Advanced Components

#### 9.1. Module 1 — Power, Protection, and Signal Integrity

1. **Power Regulation and Distribution**
    1. Linear versus switching regulators
    2. Power budgets, efficiency, thermal limits, and decoupling
    3. Battery charging and protection fundamentals
2. **Circuit Protection**
    1. Reverse polarity, overcurrent, overvoltage, and ESD protection
    2. Fuses, TVS diodes, isolation, and grounding
    3. Design protection for field wiring and inductive loads
3. **Signal Integrity**
    1. Pull-ups, termination, impedance, crosstalk, and noise
    2. Level shifting and logic-voltage compatibility
    3. Lab: diagnose noisy digital and analog signals

#### 9.2. Module 2 — Precision Sensors and Analog Front Ends

1. **Sensor Interfaces**
    1. Resistive, capacitive, current-loop, bridge, and frequency-output sensors
    2. Calibration, linearization, accuracy, precision, and uncertainty
    3. Environmental compensation and sensor placement
2. **Analog Front-End Design**
    1. Operational amplifiers, instrumentation amplifiers, and filters
    2. ADC resolution, reference voltage, sampling, and aliasing
    3. Low-noise layout and grounding practices
3. **Measurement Lab**
    1. Read a low-level sensor through a conditioned ADC path
    2. Calibrate against a reference
    3. Document error budget and repeatability

#### 9.3. Module 3 — Drivers, Actuators, and Motion

1. **Power Switching**
    1. BJT and MOSFET operation as switches
    2. Gate/base drive, flyback protection, and heat dissipation
    3. PWM control of LEDs, heaters, and DC loads
2. **Motor and Actuator Drivers**
    1. DC, stepper, servo, relay, and solenoid interfaces
    2. H-bridges, current limiting, and motion feedback
    3. Safe startup, stop, stall, and fault behavior
3. **Control Lab**
    1. Build a closed-loop actuator subsystem
    2. Measure current, temperature, and response
    3. Implement hardware and firmware interlocks

#### 9.4. Module 4 — Industrial Interfaces and Timing

1. **Robust Communication**
    1. Differential signaling and RS-485 fundamentals
    2. CAN bus concepts, termination, arbitration, and diagnostics
    3. Isolation and surge protection for industrial buses
2. **Timing and Expansion**
    1. RTC, watchdog, timers, counters, and clock sources
    2. GPIO expanders, multiplexers, and shift registers
    3. Interrupt design and deterministic event handling
3. **Interface Lab**
    1. Integrate multiple I2C/SPI peripherals
    2. Capture and decode bus traffic
    3. Handle address conflicts, timeouts, retries, and bus recovery

#### 9.5. Module 5 — Integration, Validation, and Capstone

1. **Component Selection**
    1. Datasheet limits, tolerances, derating, and lifecycle
    2. Package, availability, substitution, and cost
    3. Create a requirements-to-component decision matrix
2. **Prototype Validation**
    1. Bring-up checklist and test points
    2. Oscilloscope, logic analyzer, electronic load, and thermal inspection
    3. EMI/EMC awareness and pre-compliance checks
3. **Capstone: Rugged Sensor-Control Board**
    1. Design power, sensing, communication, and actuator stages
    2. Validate normal, boundary, and fault conditions
    3. Produce schematic notes, BOM rationale, test report, and demo

### 10. TinyML

#### 10.1. Module 1 — TinyML Introduction

1. **What Is TinyML**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML What Is TinyML Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **TinyML vs Cloud AI**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML TinyML vs Cloud AI Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Hardware for TinyML**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Hardware for TinyML Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **TensorFlow Lite Overview**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML TensorFlow Lite Overview Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Edge Impulse Platform**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Edge Impulse Platform Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 10.2. Module 2 — Model Training and Optimization

1. **Training a Simple Classifier**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Training a Simple Classifier Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **Model Quantization**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Model Quantization Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Model Pruning**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Model Pruning Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **TFLite Model Conversion**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML TFLite Model Conversion Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **Evaluating Quantized Models**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Evaluating Quantized Models Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References

#### 10.3. Module 3 — Deployment on Microcontrollers

1. **TFLite Micro on Arduino**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML TFLite Micro on Arduino Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
2. **TFLite Micro on ESP32**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML TFLite Micro on ESP32 Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
3. **Keyword Spotting**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Keyword Spotting Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
4. **Gesture Recognition**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML Gesture Recognition Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
5. **TinyML in Production**
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
        - TinyML TinyML in Production Example
    6. Common Mistakes
    7. Q & A
    8. Exercise
    9. Quiz
    10. Summary & Cheat Sheet
    11. References
### 11. IoT Projects

#### 11.1. Module 1 — End-to-End IoT Systems

1. **01 01 Web Based Environmental Data Logger**
    1. Overview of 01 01 Web Based Environmental Data Logger
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
2. **01 02 Smart Appliance Relay Switch**
    1. Overview of 01 02 Smart Appliance Relay Switch
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
3. **01 03 Rfid Attendance Door Access**
    1. Overview of 01 03 Rfid Attendance Door Access
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
4. **02 01 Mqtt Industrial Tank Pump Controller**
    1. Overview of 02 01 Mqtt Industrial Tank Pump Controller
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
5. **02 02 Cellular Gps Fleet Tracker**
    1. Overview of 02 02 Cellular Gps Fleet Tracker
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
6. **02 03 Lorawan Soil Moisture Agricultural Node**
    1. Overview of 02 03 Lorawan Soil Moisture Agricultural Node
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
7. **03 01 Ble Beacon Indoor Asset Tracker**
    1. Overview of 03 01 Ble Beacon Indoor Asset Tracker
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
8. **03 02 Thread Matter Smart Home Mesh Light**
    1. Overview of 03 02 Thread Matter Smart Home Mesh Light
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
9. **04 01 Tiny Ml Vibration Anomaly Detector**
    1. Overview of 04 01 Tiny Ml Vibration Anomaly Detector
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
10. **04 02 Edge Ai Camera Person Counter**
    1. Overview of 04 02 Edge Ai Camera Person Counter
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
11. **05 01 Ota Firmware Update Server Pipeline**
    1. Overview of 05 01 Ota Firmware Update Server Pipeline
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
12. **05 02 Industrial Modbus Rtu To Cloud Gateway**
    1. Overview of 05 02 Industrial Modbus Rtu To Cloud Gateway
        - End-to-End System Architecture
        - Complete Firmware Implementation
    2. Lab Exercise
