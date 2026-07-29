"""
seed_iot_structure.py
=====================
Learning OS — IoT Course Structure Seeder (Placeholders Only)

Workflow:
  STEP 1 — Audit existing course
  STEP 2 — Generate missing Modules
  STEP 3 — Generate missing Lessons (status=pending)
  STEP 4 — Generate placeholder LessonSection stubs
  STEP 5 — Print course metadata summary
  STEP 6 — STOP  (no notes, no quizzes, no labs)

Content is generated separately when explicitly requested.

Usage:
  python scripts/seed_iot_structure.py                   # all 5 priority courses
  python scripts/seed_iot_structure.py --course embedded-c
  python scripts/seed_iot_structure.py --audit-only      # just show what exists
"""
import sys, re, argparse
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

# ─── Placeholder section stubs (empty content, status pending) ───────────────
PLACEHOLDER_SECTIONS = [
    ("overview",    "Overview",             1),
    ("objectives",  "Learning Objectives",  2),
    ("concept",     "Theory / Concept",     3),
    ("syntax",      "Syntax & API",         4),
    ("example",     "Worked Example",       5),
    ("pitfall",     "Common Mistakes",      6),
    ("exercise",    "Exercise",             7),
    ("quiz",        "Quiz",                 8),
    ("summary",     "Summary & Cheat Sheet",9),
    ("references",  "References",          10),
]

# ─── Full Curriculum Spec ─────────────────────────────────────────────────────
# Format per module: (title, slug, [(lesson_title, est_minutes, description)])

CURRICULUM = {

    "embedded-c": {
        "title": "Embedded C",
        "description": "Master C programming for microcontrollers — memory, registers, GPIO, interrupts, timers, PWM, ADC, communication protocols, and RTOS fundamentals.",
        "target_role": "Embedded Systems Engineer",
        "difficulty": "Intermediate",
        "estimated_hours": 35,
        "prerequisites": ["C Programming"],
        "skills": ["Register-level programming", "ISR design", "GPIO", "UART/SPI/I2C", "PWM", "ADC", "FreeRTOS basics", "HAL design"],
        "career": ["Embedded Systems Engineer", "Firmware Engineer", "IoT Hardware Engineer"],
        "software": ["AVR-GCC", "STM32CubeIDE", "PlatformIO", "VS Code", "Wokwi"],
        "modules": [
            ("Introduction to Embedded Systems", "introduction-to-embedded-systems", [
                ("What Is an Embedded System", 20, "Definition, characteristics, and real-world examples of embedded systems."),
                ("Embedded vs Desktop Programming", 20, "Key differences: memory, OS, peripherals, and development flow."),
                ("Cross-Compilation Toolchain", 25, "Build process: compiler, linker, hex files, and flashing."),
                ("Hex File and Flashing Process", 20, "Understanding .hex/.elf files and how they are written to flash memory."),
                ("Bare-Metal Programming Concept", 20, "Programming without OS — direct hardware access."),
            ]),
            ("Memory Architecture", "memory-architecture", [
                ("Harvard vs Von Neumann Architecture", 20, "Two memory bus architectures and their impact on embedded design."),
                ("Flash SRAM EEPROM and Registers", 25, "Types of memory in microcontrollers and their use cases."),
                ("Memory-Mapped I/O", 20, "How peripherals are accessed via memory addresses."),
                ("Stack and Heap in Embedded Systems", 25, "Memory layout: stack, heap, BSS, data segments."),
                ("Volatile and Const Qualifiers", 20, "Why volatile is critical in embedded C and interrupt handlers."),
            ]),
            ("Bit Manipulation", "bit-manipulation", [
                ("Bitwise Operators Review", 20, "AND, OR, XOR, NOT, shift operators in C."),
                ("Setting Clearing and Toggling Bits", 20, "Standard idioms for bit-level register control."),
                ("Bit Masking Techniques", 20, "Reading and writing specific bits without affecting others."),
                ("Register-Level Programming", 25, "Writing directly to hardware registers using bit operations."),
                ("Practical Bit Manipulation Exercises", 30, "Hands-on practice with GPIO registers."),
            ]),
            ("GPIO Programming", "gpio-programming", [
                ("GPIO Concept and Registers", 20, "What GPIO is, DDR/PORT/PIN registers."),
                ("Input and Output Configuration", 20, "Configuring pins as input or output."),
                ("Pull-Up and Pull-Down Resistors", 20, "Preventing floating inputs — hardware and software pull-ups."),
                ("LED and Button Interfacing", 25, "Basic input/output: LED blink, button read."),
                ("GPIO Debouncing", 20, "Software and hardware debouncing techniques."),
            ]),
            ("Interrupts", "interrupts", [
                ("Interrupt Concept and ISR", 20, "What interrupts are, ISR function signature."),
                ("Interrupt Vector Table", 20, "IVT layout and how the CPU finds ISRs."),
                ("External Interrupts", 25, "Rising/falling edge triggered interrupts."),
                ("Interrupt Priority and Nesting", 20, "Handling multiple interrupt sources."),
                ("Interrupt-Driven Design", 25, "Replacing polling loops with ISRs."),
            ]),
            ("Timers and Counters", "timers-and-counters", [
                ("Timer Fundamentals", 20, "Timer hardware, prescalers, overflow."),
                ("Timer Modes Normal CTC PWM", 25, "Three key timer operating modes."),
                ("Delay Generation Using Timers", 20, "Hardware delay without blocking delay() calls."),
                ("Event Counting", 20, "Using timer in counter mode."),
                ("Watchdog Timer", 20, "Resetting stuck firmware with WDT."),
            ]),
            ("PWM", "pwm", [
                ("PWM Concept and Duty Cycle", 20, "What PWM is and how duty cycle controls power."),
                ("Hardware PWM Generation", 25, "Configuring timer for PWM output."),
                ("Software PWM", 20, "Bit-banging PWM when hardware channels are limited."),
                ("Motor Speed Control with PWM", 25, "Driving DC motors with PWM + H-bridge."),
                ("LED Dimming with PWM", 20, "Brightness control using duty cycle."),
            ]),
            ("Communication Protocols", "communication-protocols-embedded", [
                ("UART Protocol in Embedded C", 25, "Async serial: baud rate, frame format, ISR receive."),
                ("SPI Protocol in Embedded C", 25, "Synchronous serial: master/slave, CPOL/CPHA."),
                ("I2C Protocol in Embedded C", 25, "Two-wire bus: address, ACK, multi-device."),
                ("Protocol Comparison", 15, "When to use UART vs SPI vs I2C."),
                ("Debugging with UART Serial", 20, "Using printf over UART as a debug channel."),
            ]),
            ("ADC and DAC", "adc-dac", [
                ("ADC Fundamentals Resolution and Sampling", 20, "Conversion process, resolution, sampling rate."),
                ("Reading Analog Sensors with ADC", 25, "Connecting and reading sensor voltage."),
                ("DAC Fundamentals", 20, "Converting digital values to analog voltage."),
                ("ADC and DAC in Embedded C", 25, "Code-level ADC/DAC configuration."),
                ("Signal Conditioning", 20, "Op-amps and filters for sensor signals."),
            ]),
            ("Embedded C Patterns", "embedded-c-patterns", [
                ("State Machines in Embedded C", 25, "FSM design pattern for embedded software."),
                ("Circular Buffers and Ring Buffers", 20, "FIFO buffer for UART and sensor data."),
                ("Callback Functions in C", 20, "Function pointers as callbacks."),
                ("Driver Abstraction Layers", 25, "Writing portable, hardware-independent drivers."),
                ("HAL Hardware Abstraction Layer", 25, "HAL design and implementation."),
            ]),
            ("Real-Time Concepts", "real-time-concepts", [
                ("What Is an RTOS", 20, "Real-time OS concepts, determinism, scheduling."),
                ("Tasks Scheduling and Priority", 25, "Preemptive scheduling, task creation."),
                ("Semaphores and Mutexes", 20, "Resource protection and synchronization."),
                ("Queues and Event Groups", 20, "Inter-task communication."),
                ("FreeRTOS Introduction", 30, "FreeRTOS API, tasks, queues on Arduino/ESP32."),
            ]),
            ("Embedded C Projects", "embedded-c-projects", [
                ("Digital Clock Project", 40, "Build a digital clock using timer interrupts."),
                ("Temperature Display System", 35, "Read sensor, display on LCD."),
                ("Motor Control System", 35, "PWM-based DC motor speed control."),
                ("UART Command Interface", 35, "Control hardware via serial commands."),
                ("Sensor Data Logger", 40, "Log sensor readings to EEPROM."),
            ]),
        ],
    },

    "arduino": {
        "title": "Arduino",
        "description": "Learn embedded prototyping with Arduino — GPIO, sensors, actuators, displays, communication protocols, and real-world IoT projects.",
        "target_role": "IoT Prototype Engineer",
        "difficulty": "Beginner",
        "estimated_hours": 30,
        "prerequisites": ["C Programming (basic)"],
        "skills": ["Arduino IDE", "GPIO", "Sensor interfacing", "Actuator control", "I2C/SPI/UART", "PWM", "Interrupt handling"],
        "career": ["IoT Engineer", "Embedded Prototype Engineer", "Robotics Engineer"],
        "software": ["Arduino IDE", "VS Code + PlatformIO", "Wokwi", "Fritzing"],
        "modules": [
            ("Arduino Introduction", "arduino-introduction", [
                ("What Is Arduino", 20, "History, ecosystem, and why Arduino is the best prototyping platform."),
                ("Arduino Boards Uno Nano Mega Micro", 20, "Comparing popular Arduino variants and when to use each."),
                ("Arduino IDE Setup", 25, "Installing IDE, boards manager, and first connection."),
                ("First Sketch Blink", 20, "The Hello World of embedded: blinking an LED."),
                ("Arduino Pin Diagram", 15, "Digital, analog, PWM, power pins and their functions."),
            ]),
            ("Digital I/O", "digital-io", [
                ("Digital Read and Write", 20, "pinMode, digitalWrite, digitalRead functions."),
                ("LED Control", 20, "Controlling multiple LEDs with loops."),
                ("Button Input", 20, "Reading button state and acting on it."),
                ("Debouncing", 20, "Software debouncing with millis()."),
                ("Multiple LEDs Pattern", 25, "Chasing, blinking patterns with arrays."),
            ]),
            ("Analog I/O", "analog-io", [
                ("analogRead and Potentiometer", 20, "10-bit ADC, 0-1023 range, potentiometer mapping."),
                ("analogWrite PWM", 20, "8-bit PWM output on PWM-capable pins."),
                ("LED Dimming", 15, "Controlling brightness with analogWrite."),
                ("LDR Light Sensor", 20, "Light-dependent resistor voltage divider circuit."),
                ("Analog Signal Mapping", 20, "map() function for sensor value scaling."),
            ]),
            ("Serial Communication", "serial-communication", [
                ("Serial Monitor Basics", 15, "Serial.begin(), Serial.print(), Serial.println()."),
                ("Printing Sensor Values", 15, "Real-time sensor output to serial monitor."),
                ("Reading Serial Input", 20, "Serial.read(), Serial.available() for input."),
                ("Serial Communication Two Arduinos", 25, "Hardware serial wiring between two boards."),
                ("Serial Debugging Tips", 15, "Using serial as a debugging tool."),
            ]),
            ("Sensors with Arduino", "sensors-with-arduino", [
                ("DHT11 Temperature and Humidity", 25, "DHT library, reading temp and humidity values."),
                ("Ultrasonic Sensor HC-SR04", 25, "Distance measurement with trigger/echo timing."),
                ("PIR Motion Sensor", 20, "Passive infrared motion detection output."),
                ("LDR and Soil Moisture", 20, "Analog sensor reading for environment/agriculture."),
                ("Gas Sensor MQ-2", 25, "Smoke and LPG detection with analog output."),
            ]),
            ("Actuators with Arduino", "actuators-with-arduino", [
                ("Servo Motor Control", 25, "Servo library, angle control 0-180 degrees."),
                ("DC Motor with L298N", 25, "Motor driver H-bridge, speed and direction."),
                ("Stepper Motor", 25, "Stepper library, steps per revolution, speed."),
                ("Relay Module", 20, "Switching AC/high-voltage loads safely."),
                ("Buzzer Control", 15, "tone(), noTone() for sound generation."),
            ]),
            ("Displays", "displays-arduino", [
                ("16x2 LCD with Arduino", 25, "LiquidCrystal library, 4-bit and I2C mode."),
                ("OLED Display SSD1306", 25, "Adafruit library, graphics on 128x64 OLED."),
                ("7-Segment Display", 20, "Digit encoding, multiplexing."),
                ("NeoPixel LED Strip", 25, "WS2812B addressing, color control."),
                ("Displaying Sensor Data", 20, "Combining sensors and displays in one sketch."),
            ]),
            ("Communication Protocols", "communication-protocols-arduino", [
                ("I2C with Arduino", 25, "Wire library, scanner sketch, multi-device bus."),
                ("SPI with Arduino", 25, "SPI library, chip select, modes."),
                ("UART Serial Communication", 20, "SoftwareSerial for additional UART ports."),
                ("NRF24L01 Wireless", 30, "2.4GHz wireless with RF24 library."),
                ("IR Remote Control", 20, "IRremote library, decoding remote signals."),
            ]),
            ("Arduino Projects", "arduino-projects", [
                ("Temperature Monitoring System", 40, "DHT + LCD + serial plotter project."),
                ("Automatic Street Light", 35, "LDR + relay auto on/off project."),
                ("Water Level Indicator", 35, "Float sensor + LED bar graph."),
                ("Home Automation Relay", 40, "Serial command controlled relay bank."),
                ("Obstacle Avoiding Robot", 45, "Ultrasonic + motor driver robot."),
            ]),
            ("Advanced Arduino", "advanced-arduino", [
                ("Arduino Interrupts", 25, "attachInterrupt(), ISR, CHANGE/RISING/FALLING."),
                ("Timer Libraries", 20, "TimerOne, MsTimer2 for periodic tasks."),
                ("EEPROM Storage", 20, "Persistent data storage across power cycles."),
                ("Arduino with SD Card", 25, "SD library, CSV logging to SD card."),
                ("Low Power Arduino", 25, "Sleep modes, power reduction techniques."),
            ]),
        ],
    },

    "sensors-actuators": {
        "title": "Sensors and Actuators",
        "description": "Interface real-world sensors and actuators with microcontrollers — environmental, motion, industrial sensors, GPS, GSM, RFID, motors, displays.",
        "target_role": "IoT Hardware Engineer",
        "difficulty": "Beginner",
        "estimated_hours": 25,
        "prerequisites": ["Arduino"],
        "skills": ["Sensor interfacing", "Actuator control", "Analog/digital signals", "GPS", "GSM", "RFID", "Motor drivers"],
        "career": ["IoT Engineer", "Automation Engineer", "Hardware Prototyper"],
        "software": ["Arduino IDE", "PlatformIO", "Wokwi", "Fritzing"],
        "modules": [
            ("Sensor Fundamentals", "sensor-fundamentals", [
                ("What Is a Sensor", 15, "Definition, types, and role in IoT systems."),
                ("Sensor Parameters Range Resolution Accuracy", 20, "Understanding spec sheet parameters."),
                ("Analog vs Digital Sensors", 20, "Output types, interfacing differences."),
                ("Sensor Interfacing Methods", 20, "GPIO, ADC, I2C, SPI, UART sensor interfaces."),
                ("Sensor Selection Guide", 15, "Choosing the right sensor for your application."),
            ]),
            ("Environmental Sensors", "environmental-sensors", [
                ("DHT11 DHT22 Temperature and Humidity", 25, "Single-wire protocol, library usage, accuracy differences."),
                ("BME280 Pressure Humidity Temperature", 25, "I2C sensor with pressure reading, Bosch library."),
                ("DS18B20 Waterproof Temperature Sensor", 25, "1-Wire protocol, multiple sensors on one bus."),
                ("LDR Light Sensor", 20, "Voltage divider, lux calculation."),
                ("MQ Series Gas Sensors", 25, "MQ-2 MQ-135 MQ-7 calibration and reading."),
            ]),
            ("Motion Sensors", "motion-sensors", [
                ("PIR Motion Sensor", 20, "Detection range, sensitivity adjustment, output."),
                ("Ultrasonic HC-SR04", 25, "Echo pulse timing, distance formula."),
                ("IR Sensor", 20, "Obstacle detection, line following."),
                ("MPU6050 Accelerometer and Gyroscope", 30, "I2C 6-DOF IMU, DMP, pitch/roll/yaw."),
                ("Vibration Sensor SW-420", 20, "Digital vibration detection output."),
            ]),
            ("Industrial and Special Sensors", "industrial-sensors", [
                ("Flow Sensor", 25, "Pulse counting, flow rate calculation."),
                ("Pressure Sensor", 20, "Analog/I2C pressure sensors for fluid systems."),
                ("Current Sensor ACS712", 25, "Hall effect current sensing, AC/DC measurement."),
                ("Hall Effect Sensor", 20, "Magnetic field detection, RPM sensing."),
                ("Load Cell and HX711", 30, "Weight measurement, HX711 24-bit ADC."),
            ]),
            ("Connectivity Modules", "connectivity-modules", [
                ("GPS Module NEO-6M", 30, "NMEA sentences, parsing latitude/longitude."),
                ("GSM Module SIM800L", 30, "AT commands, SMS, GPRS data."),
                ("RFID RC522", 25, "SPI RFID reader, tag UID reading."),
                ("NFC Module", 20, "NFC tag reading and writing."),
                ("Fingerprint Sensor", 25, "UART fingerprint enrollment and verification."),
            ]),
            ("Actuators", "actuators", [
                ("Relay Module", 20, "NC/NO contacts, coil voltage, safe switching."),
                ("Servo Motor", 25, "PWM control, angle precision, torque."),
                ("Stepper Motor A4988", 30, "Step/direction control, microstepping."),
                ("DC Motor L298N", 25, "H-bridge direction and speed control."),
                ("Solenoid Valve", 20, "Electromagnetic valve for fluid control."),
            ]),
            ("Display and Output", "display-and-output", [
                ("16x2 LCD I2C Interface", 20, "I2C backpack, PCF8574 address, library."),
                ("OLED SSD1306", 25, "I2C OLED, graphics library, text and shapes."),
                ("NeoPixel WS2812B", 25, "Addressable RGB LEDs, color animations."),
                ("Buzzer and Audio Output", 15, "Passive buzzer tones, active buzzer."),
                ("7-Segment and Matrix Display", 25, "Multiplexing digits, MAX7219 matrix."),
            ]),
        ],
    },

    "esp32": {
        "title": "ESP32",
        "description": "Build WiFi and BLE IoT devices with ESP32 — GPIO, WiFi, Bluetooth, MQTT, REST APIs, deep sleep, OTA updates, and FreeRTOS multitasking.",
        "target_role": "IoT Firmware Engineer",
        "difficulty": "Intermediate",
        "estimated_hours": 35,
        "prerequisites": ["Arduino", "C Programming (basic)", "Networking basics"],
        "skills": ["ESP32 WiFi", "BLE", "MQTT", "REST API", "Deep Sleep", "OTA", "FreeRTOS", "Dual core"],
        "career": ["IoT Firmware Engineer", "Embedded WiFi Engineer", "Smart Device Developer"],
        "software": ["Arduino IDE", "VS Code + PlatformIO", "MQTT Explorer", "Postman", "Wokwi"],
        "modules": [
            ("ESP32 Introduction", "esp32-introduction", [
                ("ESP32 vs ESP8266 vs Arduino", 20, "Feature comparison: CPU, RAM, WiFi, BLE, ADC."),
                ("ESP32 Architecture Dual Core", 20, "Xtensa LX6 cores, peripheral bus, memory map."),
                ("Development Boards DevKit WROOM S3", 15, "Popular ESP32 boards and pinout differences."),
                ("ESP-IDF vs Arduino Framework", 20, "Choosing the right framework for your project."),
                ("Pinout and Hardware Overview", 15, "ESP32 pins: GPIO, ADC, DAC, touch, strapping."),
            ]),
            ("ESP32 GPIO", "esp32-gpio", [
                ("Digital I/O on ESP32", 20, "pinMode, digitalWrite, digitalRead — ESP32 specifics."),
                ("Analog ADC Channels", 25, "12-bit ADC, channels, attenuation, accuracy."),
                ("DAC Output", 20, "8-bit DAC on GPIO 25/26 for analog voltage."),
                ("Touch Sensors", 20, "Capacitive touch on GPIO 2/4/12-15/27/32/33."),
                ("GPIO Interrupt on ESP32", 25, "attachInterrupt with IRAM_ATTR for ISR."),
            ]),
            ("WiFi", "wifi-esp32", [
                ("WiFi Station Mode", 25, "Connecting to router, IP address, reconnection."),
                ("WiFi Access Point Mode", 20, "Creating a hotspot for direct connection."),
                ("Connecting to Router", 15, "WiFiMulti, stored credentials."),
                ("HTTP Client GET and POST", 25, "HTTPClient library, JSON requests."),
                ("HTTPS SSL TLS on ESP32", 25, "WiFiClientSecure, root CA certificate."),
            ]),
            ("Bluetooth and BLE", "bluetooth-ble-esp32", [
                ("Classic Bluetooth Basics", 20, "BluetoothSerial library, pairing."),
                ("BLE Fundamentals", 20, "GATT, services, characteristics, UUID."),
                ("BLE Server and Client", 30, "Creating and connecting BLE devices."),
                ("BLE Sensor Broadcasting", 25, "Advertising sensor data as BLE beacon."),
                ("BLE with Mobile App", 25, "nRF Connect, custom app interaction."),
            ]),
            ("MQTT with ESP32", "mqtt-with-esp32", [
                ("MQTT Setup on ESP32", 20, "PubSubClient library, broker connection."),
                ("Publishing Sensor Data", 25, "JSON payload, topic design."),
                ("Subscribing for Commands", 25, "Callback function, topic subscription."),
                ("QoS Levels", 15, "QoS 0/1/2 on ESP32."),
                ("MQTT over TLS", 25, "Secure MQTT with root CA certificate."),
            ]),
            ("HTTP and REST API", "http-rest-esp32", [
                ("ESP32 HTTP Client", 25, "GET, POST, headers, timeout."),
                ("Posting to Flask API", 25, "Sending sensor JSON to Flask backend."),
                ("JSON Parsing on ESP32", 25, "ArduinoJson library, nested objects."),
                ("ESP32 Web Server", 30, "WebServer library, HTML page, REST endpoints."),
                ("REST API Command and Control", 25, "Receiving commands via HTTP endpoints."),
            ]),
            ("ESP32 Sensors", "esp32-sensors", [
                ("DHT22 Temperature and Humidity", 20, "Higher accuracy DHT on ESP32."),
                ("BME280 Environment Sensor", 25, "I2C BME280 — temp, humidity, pressure."),
                ("MPU6050 IMU Sensor", 30, "6-DOF motion sensing with DMP."),
                ("Hall Effect Sensor", 15, "Built-in hall sensor in ESP32 chip."),
                ("Capacitive Touch Sensor", 20, "touchRead() for touch-based input."),
            ]),
            ("Deep Sleep and Power Management", "deep-sleep-power", [
                ("ESP32 Power Modes", 20, "Active, modem sleep, light sleep, deep sleep."),
                ("Deep Sleep Timer Wakeup", 25, "esp_sleep_enable_timer_wakeup()."),
                ("Deep Sleep External Wakeup", 25, "GPIO wakeup on button press."),
                ("ULP Co-Processor", 25, "Ultra-low power co-processor for sensor polling."),
                ("Battery Powered IoT Node", 30, "Battery circuit, charging, power budget design."),
            ]),
            ("OTA Updates", "ota-updates-esp32", [
                ("OTA Concept", 15, "Why OTA, use cases, risks."),
                ("Arduino OTA", 25, "ArduinoOTA library, WiFi over-the-air upload."),
                ("HTTP OTA Update", 25, "httpUpdate library, update server."),
                ("Secure OTA", 25, "HTTPS OTA with certificate."),
                ("Rollback and Verification", 20, "Partition scheme, rollback on failure."),
            ]),
            ("FreeRTOS on ESP32", "freertos-esp32", [
                ("FreeRTOS Tasks on ESP32", 25, "xTaskCreate, task parameters, handles."),
                ("Task Priorities", 20, "Priority levels, preemption, starvation."),
                ("Queues for Communication", 25, "xQueueCreate, send/receive between tasks."),
                ("Semaphores and Mutexes", 25, "Protecting shared resources."),
                ("Dual Core Programming", 30, "Pinning tasks to Core 0 and Core 1."),
            ]),
            ("ESP32 Projects", "esp32-projects", [
                ("WiFi Sensor Dashboard", 45, "ESP32 + Flask + MQTT + chart.js dashboard."),
                ("MQTT Home Automation", 45, "Node-RED + ESP32 + relay control."),
                ("BLE Sensor Monitor", 40, "BLE advertising + mobile app display."),
                ("OTA Updatable Device", 35, "Production-ready OTA update workflow."),
                ("Battery IoT Node", 40, "Deep sleep sensor node with 6-month battery life."),
            ]),
        ],
    },

    "mqtt": {
        "title": "MQTT Protocol",
        "description": "Master MQTT — the lightweight IoT messaging protocol. Broker setup, publish/subscribe, QoS, security, Python/ESP32 clients, and cloud integrations.",
        "target_role": "IoT Backend / Protocol Engineer",
        "difficulty": "Intermediate",
        "estimated_hours": 20,
        "prerequisites": ["Python (basic)", "Networking basics"],
        "skills": ["MQTT publish/subscribe", "Mosquitto broker", "Paho Python", "QoS", "TLS security", "Node-RED", "InfluxDB", "Grafana"],
        "career": ["IoT Engineer", "Backend Engineer", "Industrial Automation Engineer"],
        "software": ["Mosquitto", "MQTT Explorer", "Node-RED", "Python", "InfluxDB", "Grafana"],
        "modules": [
            ("MQTT Fundamentals", "mqtt-fundamentals", [
                ("What Is MQTT", 20, "Protocol history, use cases, why it dominates IoT."),
                ("Publish Subscribe Model", 20, "Decoupled messaging: publishers, subscribers, broker."),
                ("Topics and Wildcards", 20, "Topic hierarchy, + single-level, # multi-level wildcards."),
                ("QoS Levels 0 1 2", 25, "At-most-once, at-least-once, exactly-once semantics."),
                ("Retained Messages and LWT", 20, "Persistent last message and Last Will and Testament."),
            ]),
            ("MQTT Broker Setup", "mqtt-broker-setup", [
                ("Mosquitto Installation on Linux", 25, "apt install mosquitto, config file, starting service."),
                ("Mosquitto on Raspberry Pi", 25, "Pi as local IoT MQTT broker."),
                ("Cloud Brokers HiveMQ EMQX", 20, "Free cloud brokers for development."),
                ("Broker Configuration", 20, "mosquitto.conf: listeners, persistence, logging."),
                ("Testing with MQTT Explorer", 15, "GUI client for topic inspection."),
            ]),
            ("MQTT with Python", "mqtt-with-python", [
                ("Paho MQTT Library", 20, "pip install paho-mqtt, client setup."),
                ("Publisher Client", 20, "client.publish(), loop, connection."),
                ("Subscriber Client", 20, "client.subscribe(), on_message() callback."),
                ("Sensor Data Publishing", 25, "JSON payloads, topic naming convention."),
                ("MQTT Dashboard with Flask", 30, "Real-time web dashboard with MQTT + Flask + SocketIO."),
            ]),
            ("MQTT with ESP32", "mqtt-with-esp32-course", [
                ("Arduino MQTT Library Setup", 20, "PubSubClient library install and configuration."),
                ("ESP32 Publisher", 20, "Connecting and publishing from firmware."),
                ("ESP32 Subscriber", 20, "Receiving commands from broker."),
                ("JSON Payload over MQTT", 25, "ArduinoJson + MQTT message formatting."),
                ("MQTT over TLS with ESP32", 25, "Root CA setup for secure connection."),
            ]),
            ("MQTT Security", "mqtt-security", [
                ("Username and Password Authentication", 20, "mosquitto_passwd, auth config."),
                ("TLS SSL for MQTT", 25, "Self-signed certificates, port 8883."),
                ("ACL Access Control Lists", 20, "Topic-level read/write permissions."),
                ("Certificate-Based Authentication", 25, "Mutual TLS with client certificates."),
                ("MQTT Security Best Practices", 15, "Checklist for production IoT deployments."),
            ]),
            ("MQTT Integrations", "mqtt-integrations", [
                ("MQTT to Node-RED", 25, "Flow-based visual programming for MQTT."),
                ("MQTT to InfluxDB", 25, "Time-series data storage from MQTT."),
                ("MQTT to Grafana", 25, "Real-time dashboard from InfluxDB + MQTT."),
                ("MQTT to AWS IoT", 25, "Connecting local broker to AWS IoT Core."),
                ("MQTT to WebSocket Bridge", 25, "Real-time browser updates via MQTT over WebSocket."),
            ]),
        ],
    },
}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def audit_course(course_slug: str):
    """STEP 1: Audit existing course structure."""
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        print(f"  [NOT FOUND] {course_slug}")
        return 0, 0
    mods = course.modules.all()
    total_lessons = sum(m.lessons.filter_by(is_deleted=False).count() for m in mods)
    total_sections = sum(
        LessonSection.query.filter_by(lesson_id=l.id).count()
        for m in mods
        for l in m.lessons.filter_by(is_deleted=False).all()
    )
    print(f"  Existing: {len(mods)} modules | {total_lessons} lessons | {total_sections} sections")
    return len(mods), total_lessons


def seed_course(course_slug: str, spec: dict) -> dict:
    """STEPS 2-4: Seed modules, lessons, placeholder sections."""
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        print(f"  [ERROR] Course not found: {course_slug}")
        return {}

    stats = {"modules_created": 0, "lessons_created": 0, "sections_created": 0,
             "modules_existing": 0, "lessons_existing": 0}

    for mod_idx, (mod_title, mod_slug, lessons) in enumerate(spec["modules"], start=1):
        # STEP 2: Module
        mod = Module.query.filter_by(course_id=course.id, slug=mod_slug).first()
        if not mod:
            mod = Module(
                course_id=course.id, title=mod_title, slug=mod_slug,
                sort_order=mod_idx, is_published=True,
                description=f"Module {mod_idx} of {spec['title']} — {mod_title}",
            )
            db.session.add(mod)
            db.session.flush()
            stats["modules_created"] += 1
            print(f"  [MOD+] {mod_title}")
        else:
            stats["modules_existing"] += 1

        for lesson_idx, (lesson_title, est_minutes, lesson_desc) in enumerate(lessons, start=1):
            # STEP 3: Lesson
            lesson_slug = slugify(lesson_title)
            lesson = Lesson.query.filter_by(module_id=mod.id, slug=lesson_slug).first()
            if not lesson:
                lesson = Lesson(
                    module_id=mod.id, title=lesson_title, slug=lesson_slug,
                    sort_order=lesson_idx, status='pending',
                    is_deleted=False, estimated_minutes=est_minutes,
                    description=lesson_desc,
                )
                db.session.add(lesson)
                db.session.flush()
                stats["lessons_created"] += 1
                print(f"    [L+] {lesson_title} (~{est_minutes}min) — pending")
            else:
                stats["lessons_existing"] += 1

            # STEP 4: Placeholder sections (only if none exist)
            existing = LessonSection.query.filter_by(lesson_id=lesson.id).count()
            if existing == 0:
                for (stype, stitle, sort_order) in PLACEHOLDER_SECTIONS:
                    stub = LessonSection(
                        lesson_id=lesson.id, section_type=stype,
                        title=stitle, content_markdown="",
                        content_html="", sort_order=sort_order,
                        is_visible=False,  # hidden until content is generated
                    )
                    db.session.add(stub)
                    stats["sections_created"] += 1

    db.session.commit()
    return stats


def print_structure(course_slug: str, spec: dict):
    """STEP 5: Print course metadata summary."""
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        return

    mods = course.modules.all()
    total_lessons = sum(m.lessons.filter_by(is_deleted=False).count() for m in mods)
    pending = sum(
        m.lessons.filter_by(is_deleted=False, status='pending').count() for m in mods
    )

    print(f"\n{'='*60}")
    print(f"COURSE STRUCTURE READY: {spec['title']}")
    print(f"{'='*60}")
    print(f"  Slug:         {course_slug}")
    print(f"  Difficulty:   {spec['difficulty']}")
    print(f"  Hours:        {spec['estimated_hours']}h")
    print(f"  Target Role:  {spec['target_role']}")
    print(f"  Prerequisites: {', '.join(spec['prerequisites'])}")
    print(f"  Modules:      {len(mods)}")
    print(f"  Lessons:      {total_lessons}  ({pending} pending)")
    print(f"  Status:       Structure Ready | Content Pending")
    print(f"\n  Skills: {', '.join(spec['skills'][:4])}...")
    print(f"  Career: {', '.join(spec['career'])}")
    print(f"  Software: {', '.join(spec['software'])}")
    print(f"\n  Modules:")
    for m in mods:
        lc = m.lessons.filter_by(is_deleted=False).count()
        print(f"    [{m.sort_order:2d}] {m.title} ({lc} lessons)")
    print(f"\n  STEP 6: STOP. Content generation is a separate step.")


def run(course_filter=None, audit_only=False):
    courses = (
        {course_filter: CURRICULUM[course_filter]}
        if course_filter and course_filter in CURRICULUM
        else CURRICULUM
    )

    with app.app_context():
        for course_slug, spec in courses.items():
            print(f"\n{'#'*65}")
            print(f"# {spec['title'].upper()} ({course_slug})")
            print(f"{'#'*65}")

            # STEP 1: Audit
            print("\n[STEP 1] Auditing existing course...")
            existing_mods, existing_lessons = audit_course(course_slug)

            if audit_only:
                continue

            # STEPS 2-4: Seed
            print("\n[STEP 2-4] Seeding modules, lessons, placeholder sections...")
            stats = seed_course(course_slug, spec)

            print(f"\n  Summary:")
            print(f"    Modules created: {stats.get('modules_created', 0)}")
            print(f"    Modules existing: {stats.get('modules_existing', 0)}")
            print(f"    Lessons created: {stats.get('lessons_created', 0)}")
            print(f"    Lessons existing: {stats.get('lessons_existing', 0)}")
            print(f"    Placeholder sections created: {stats.get('sections_created', 0)}")

            # STEP 5: Print metadata
            print_structure(course_slug, spec)

        print(f"\n{'='*65}")
        print("WORKFLOW COMPLETE.")
        print("  All courses: Structure Ready | Content: Pending")
        print("  To generate content: request per lesson or per module.")
        print(f"{'='*65}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Learning OS IoT Structure Seeder")
    parser.add_argument("--course", help="Seed only this course slug")
    parser.add_argument("--audit-only", action="store_true", help="Only audit, no seeding")
    args = parser.parse_args()
    run(course_filter=args.course, audit_only=args.audit_only)
