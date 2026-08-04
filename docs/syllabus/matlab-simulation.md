# MATLAB & Simulation — Syllabus

## Study Flow

### 1. Basic MATLAB

#### 1.1. Module 1 — MATLAB Environment and Matrix Foundations

1. **Workspace and Tooling**
    1. Command Window, Editor, Workspace, and documentation
    2. Scripts, live scripts, variables, and path management
    3. Lab: create and run a reproducible analysis script
2. **Arrays and Matrices**
    1. Vectors, matrices, indexing, slicing, and concatenation
    2. Element-wise versus matrix operations
    3. Colon operator, logical indexing, and vectorization
3. **Data Types and Import**
    1. Numeric, logical, string, categorical, table, and timetable data
    2. Import text, spreadsheet, and MAT files
    3. Inspect, clean, and export a small dataset

#### 1.2. Module 2 — Programming with MATLAB

1. **Control Flow**
    1. Conditional statements and switch
    2. for and while loops
    3. Preallocation and vectorized alternatives
2. **Functions and Code Organization**
    1. Function inputs, outputs, scope, and validation
    2. Local functions and reusable utilities
    3. Error handling and defensive programming
3. **Debugging and Testing**
    1. Breakpoints, stepping, and variable inspection
    2. Assertions and basic unit tests
    3. Lab: refactor and test a numerical program

#### 1.3. Module 3 — Data Analysis and Visualization

1. **Numerical and Statistical Analysis**
    1. Descriptive statistics and missing data
    2. Interpolation, curve fitting, and numerical integration
    3. Solve linear systems and inspect conditioning
2. **Plotting**
    1. Line, scatter, bar, histogram, and surface plots
    2. Labels, legends, layouts, annotations, and export
    3. Create publication-ready and dashboard-style figures
3. **Analysis Lab**
    1. Import and clean experimental data
    2. Compute statistics and fit a model
    3. Communicate findings with annotated plots

#### 1.4. Module 4 — Signals, Systems, and Simulation Basics

1. **Signal Processing Foundations**
    1. Sampling, frequency, aliasing, and noise
    2. Filtering and moving-window operations
    3. FFT-based spectral inspection
2. **Dynamic Systems**
    1. Difference and differential equation concepts
    2. Transfer functions and state-space overview
    3. Step response and stability interpretation
3. **Simulation Lab**
    1. Generate and analyze a sampled signal
    2. Design and compare simple filters
    3. Simulate a first-order system response

#### 1.5. Module 5 — Engineering Workflow and Capstone

1. **Performance and Reproducibility**
    1. Profiling, vectorization, and memory awareness
    2. Project folders, data provenance, and parameter files
    3. Reports and automated figure generation
2. **Hardware and External Data Overview**
    1. Serial communication and instrument data concepts
    2. Reading sensor logs and timestamped telemetry
    3. Preparing algorithms for embedded implementation
3. **Capstone: Sensor Data Analysis**
    1. Acquire or import a multichannel dataset
    2. Clean, analyze, visualize, and model the data
    3. Deliver code, tests, figures, and an engineering report

### 2. Simulation (Proteus / Wokwi)

#### 2.1. Module 1 — Simulation Workflow Foundations

1. **Purpose and Limitations**
    1. Simulation versus breadboard and production hardware
    2. Models, assumptions, tolerances, and idealized behavior
    3. Select Proteus or Wokwi based on circuit and firmware needs
2. **Project Setup**
    1. Create a schematic or virtual wiring project
    2. Select boards, components, libraries, and power rails
    3. Build, load, and execute firmware
3. **Measurement Tools**
    1. Virtual oscilloscope, logic analyzer, serial monitor, and probes
    2. Voltage, current, timing, and protocol observation
    3. Lab: verify a digital-output and serial program

#### 2.2. Module 2 — Digital and Analog Circuit Simulation

1. **Digital Inputs and Outputs**
    1. Buttons, pull resistors, debouncing, LEDs, and logic levels
    2. Interrupt-driven input
    3. Faults caused by floating or conflicting signals
2. **Analog Inputs and PWM**
    1. Potentiometers and analog sensors
    2. ADC scaling, reference voltage, and quantization
    3. PWM-based brightness and speed control
3. **Circuit Lab**
    1. Simulate a sensor-controlled output
    2. Measure response and timing
    3. Inject wiring and component faults and diagnose them

#### 2.3. Module 3 — Microcontrollers, Sensors, and Actuators

1. **Controller Platforms**
    1. Arduino-class and ESP32-class board simulation
    2. GPIO capabilities, pin constraints, and peripheral mapping
    3. Timers, interrupts, and serial logging
2. **Sensor Integration**
    1. Temperature, humidity, distance, light, and motion sensors
    2. Digital and analog interface patterns
    3. Create realistic test inputs and boundary cases
3. **Actuator Integration**
    1. Relays, buzzers, displays, servos, and motors
    2. Driver and flyback-protection concepts
    3. Lab: simulate an automated monitoring-and-control node

#### 2.4. Module 4 — Communication Protocols and Debugging

1. **Serial Protocols**
    1. UART, I2C, and SPI wiring and timing
    2. Addressing, chip select, baud rate, and bus contention
    3. Decode frames with virtual instruments
2. **Networked Simulation**
    1. Wi-Fi setup in Wokwi-supported boards
    2. HTTP and MQTT test workflows
    3. Connect simulated firmware to a local or test service
3. **Systematic Debugging**
    1. Compile, startup, wiring, timing, and logic failures
    2. Break problems into power, signal, firmware, and protocol layers
    3. Lab: diagnose a deliberately broken multi-device project

#### 2.5. Module 5 — Validation and Capstone

1. **Test Planning**
    1. Nominal, boundary, fault, and recovery cases
    2. Expected results and pass/fail criteria
    3. Automate repeatable input scenarios where supported
2. **From Simulation to Hardware**
    1. Check voltage, current, pin, timing, and library assumptions
    2. Identify components that require physical validation
    3. Prepare schematic, wiring, BOM, and bring-up checklist
3. **Capstone: Simulated IoT Controller**
    1. Integrate sensors, display or actuator, and communication
    2. Demonstrate telemetry, commands, alarms, and fault recovery
    3. Submit project files, firmware, test evidence, and limitations
