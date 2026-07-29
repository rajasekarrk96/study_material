"""
generate_iot_content.py
=======================
Learning OS — Batch IoT Curriculum Content Generator

Reads the curriculum spec, seeds Module + Lesson rows, then calls the
AI provider (Ollama / OpenAI / Gemini) to generate LessonSection content
for every lesson in Priority-1 IoT courses.

Usage:
  python scripts/generate_iot_content.py                  # all priority-1 courses
  python scripts/generate_iot_content.py --course embedded-c
  python scripts/generate_iot_content.py --course arduino
  python scripts/generate_iot_content.py --course sensors-actuators
  python scripts/generate_iot_content.py --course esp32
  python scripts/generate_iot_content.py --course mqtt
  python scripts/generate_iot_content.py --seed-only      # create rows, skip AI
  python scripts/generate_iot_content.py --ai-only        # run AI for existing lessons

Features:
  - Idempotent: skips modules/lessons that already exist
  - Resumable: skips lessons that already have AI-generated sections
  - Progress logging with ETA
  - Saves markdown to DB as LessonSection rows
"""
import sys, os, re, time, argparse
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection
from app.providers.registry import get_provider
from app.providers.prompts import get_prompt

app = create_app()

# ─── Section types per lesson ────────────────────────────────────────────────
SECTION_TYPES = [
    ("overview",  "Overview",        1),
    ("concept",   "Core Concept",    2),
    ("syntax",    "Syntax & API",    3),
    ("example",   "Practical Example", 4),
    ("pitfall",   "Common Pitfalls", 5),
    ("qa",        "Q & A",           6),
]

# ─── Curriculum Spec ─────────────────────────────────────────────────────────
# Format: { course_slug: { title, domain, difficulty, modules: [ (title, slug, [lessons]) ] } }

CURRICULUM = {

    # ── EMBEDDED C ────────────────────────────────────────────────────────────
    "embedded-c": {
        "title": "Embedded C", "domain": "Embedded Systems", "difficulty": "Intermediate",
        "modules": [
            ("Introduction to Embedded Systems", "introduction-to-embedded-systems", [
                "What Is an Embedded System",
                "Embedded vs Desktop Programming",
                "Cross-Compilation Toolchain",
                "Hex File Flashing Process",
                "Bare-Metal Programming Concept",
            ]),
            ("Memory Architecture", "memory-architecture", [
                "Harvard vs Von Neumann Architecture",
                "Flash SRAM EEPROM and Registers",
                "Memory-Mapped I/O",
                "Stack and Heap in Embedded Systems",
                "Volatile and Const Qualifiers",
            ]),
            ("Bit Manipulation", "bit-manipulation", [
                "Bitwise Operators Review",
                "Setting Clearing and Toggling Bits",
                "Bit Masking Techniques",
                "Register-Level Programming",
                "Practical Bit Manipulation Exercises",
            ]),
            ("GPIO Programming", "gpio-programming", [
                "GPIO Concept and Registers",
                "Input and Output Configuration",
                "Pull-Up and Pull-Down Resistors",
                "LED and Button Interfacing",
                "GPIO Debouncing",
            ]),
            ("Interrupts", "interrupts", [
                "Interrupt Concept and ISR",
                "Interrupt Vector Table",
                "External Interrupts",
                "Interrupt Priority and Nesting",
                "Interrupt-Driven Design",
            ]),
            ("Timers and Counters", "timers-and-counters", [
                "Timer Fundamentals",
                "Timer Modes Normal CTC PWM",
                "Delay Generation Using Timers",
                "Event Counting",
                "Watchdog Timer",
            ]),
            ("PWM", "pwm", [
                "PWM Concept and Duty Cycle",
                "Hardware PWM Generation",
                "Software PWM",
                "Motor Speed Control with PWM",
                "LED Dimming with PWM",
            ]),
            ("Communication Protocols", "communication-protocols-embedded", [
                "UART Protocol in Embedded C",
                "SPI Protocol in Embedded C",
                "I2C Protocol in Embedded C",
                "Protocol Comparison",
                "Debugging with UART Serial",
            ]),
            ("ADC and DAC", "adc-dac", [
                "ADC Fundamentals Resolution and Sampling",
                "Reading Analog Sensors with ADC",
                "DAC Fundamentals",
                "ADC and DAC in Embedded C",
                "Signal Conditioning",
            ]),
            ("Embedded C Patterns", "embedded-c-patterns", [
                "State Machines in Embedded C",
                "Circular Buffers and Ring Buffers",
                "Callback Functions in C",
                "Driver Abstraction Layers",
                "HAL Hardware Abstraction Layer",
            ]),
            ("Real-Time Concepts", "real-time-concepts", [
                "What Is an RTOS",
                "Tasks Scheduling and Priority",
                "Semaphores and Mutexes",
                "Queues and Event Groups",
                "FreeRTOS Introduction",
            ]),
            ("Embedded C Projects", "embedded-c-projects", [
                "Digital Clock Project",
                "Temperature Display System",
                "Motor Control System",
                "UART Command Interface",
                "Sensor Data Logger",
            ]),
        ],
    },

    # ── ARDUINO ───────────────────────────────────────────────────────────────
    "arduino": {
        "title": "Arduino", "domain": "Embedded Systems / IoT", "difficulty": "Beginner",
        "modules": [
            ("Arduino Introduction", "arduino-introduction", [
                "What Is Arduino",
                "Arduino Boards Uno Nano Mega Micro",
                "Arduino IDE Setup",
                "First Sketch Blink",
                "Arduino Pin Diagram",
            ]),
            ("Digital I/O", "digital-io", [
                "Digital Read and Write",
                "LED Control",
                "Button Input",
                "Debouncing",
                "Multiple LEDs Pattern",
            ]),
            ("Analog I/O", "analog-io", [
                "analogRead and Potentiometer",
                "analogWrite PWM",
                "LED Dimming",
                "LDR Light Sensor",
                "Analog Signal Mapping",
            ]),
            ("Serial Communication", "serial-communication", [
                "Serial Monitor Basics",
                "Printing Sensor Values",
                "Reading Serial Input",
                "Serial Communication Two Arduinos",
                "Serial Debugging Tips",
            ]),
            ("Sensors with Arduino", "sensors-with-arduino", [
                "DHT11 Temperature and Humidity",
                "Ultrasonic Sensor HC-SR04",
                "PIR Motion Sensor",
                "LDR and Soil Moisture",
                "Gas Sensor MQ-2",
            ]),
            ("Actuators with Arduino", "actuators-with-arduino", [
                "Servo Motor Control",
                "DC Motor with L298N",
                "Stepper Motor",
                "Relay Module",
                "Buzzer Control",
            ]),
            ("Displays", "displays-arduino", [
                "16x2 LCD with Arduino",
                "OLED Display SSD1306",
                "7-Segment Display",
                "NeoPixel LED Strip",
                "Displaying Sensor Data",
            ]),
            ("Communication Protocols", "communication-protocols-arduino", [
                "I2C with Arduino",
                "SPI with Arduino",
                "UART Serial Communication",
                "NRF24L01 Wireless",
                "IR Remote Control",
            ]),
            ("Arduino Projects", "arduino-projects", [
                "Temperature Monitoring System",
                "Automatic Street Light",
                "Water Level Indicator",
                "Home Automation Relay",
                "Obstacle Avoiding Robot",
            ]),
            ("Advanced Arduino", "advanced-arduino", [
                "Arduino Interrupts",
                "Timer Libraries",
                "EEPROM Storage",
                "Arduino with SD Card",
                "Low Power Arduino",
            ]),
        ],
    },

    # ── SENSORS & ACTUATORS ───────────────────────────────────────────────────
    "sensors-actuators": {
        "title": "Sensors and Actuators", "domain": "IoT Hardware", "difficulty": "Beginner",
        "modules": [
            ("Sensor Fundamentals", "sensor-fundamentals", [
                "What Is a Sensor",
                "Sensor Parameters Range Resolution Accuracy",
                "Analog vs Digital Sensors",
                "Sensor Interfacing Methods",
                "Sensor Selection Guide",
            ]),
            ("Environmental Sensors", "environmental-sensors", [
                "DHT11 DHT22 Temperature and Humidity",
                "BME280 Pressure Humidity Temperature",
                "DS18B20 Waterproof Temperature Sensor",
                "LDR Light Sensor",
                "MQ Series Gas Sensors",
            ]),
            ("Motion Sensors", "motion-sensors", [
                "PIR Motion Sensor",
                "Ultrasonic HC-SR04",
                "IR Sensor",
                "MPU6050 Accelerometer and Gyroscope",
                "Vibration Sensor SW-420",
            ]),
            ("Industrial and Special Sensors", "industrial-sensors", [
                "Flow Sensor",
                "Pressure Sensor",
                "Current Sensor ACS712",
                "Hall Effect Sensor",
                "Load Cell and HX711",
            ]),
            ("Connectivity Modules", "connectivity-modules", [
                "GPS Module NEO-6M",
                "GSM Module SIM800L",
                "RFID RC522",
                "NFC Module",
                "Fingerprint Sensor",
            ]),
            ("Actuators", "actuators", [
                "Relay Module",
                "Servo Motor",
                "Stepper Motor A4988",
                "DC Motor L298N",
                "Solenoid Valve",
            ]),
            ("Display and Output", "display-and-output", [
                "16x2 LCD I2C Interface",
                "OLED SSD1306",
                "NeoPixel WS2812B",
                "Buzzer and Audio Output",
                "7-Segment and Matrix Display",
            ]),
        ],
    },

    # ── ESP32 ─────────────────────────────────────────────────────────────────
    "esp32": {
        "title": "ESP32", "domain": "IoT / Embedded Systems", "difficulty": "Intermediate",
        "modules": [
            ("ESP32 Introduction", "esp32-introduction", [
                "ESP32 vs ESP8266 vs Arduino",
                "ESP32 Architecture Dual Core",
                "Development Boards DevKit WROOM S3",
                "ESP-IDF vs Arduino Framework",
                "Pinout and Hardware Overview",
            ]),
            ("ESP32 GPIO", "esp32-gpio", [
                "Digital I/O on ESP32",
                "Analog ADC Channels",
                "DAC Output",
                "Touch Sensors",
                "GPIO Interrupt on ESP32",
            ]),
            ("WiFi", "wifi-esp32", [
                "WiFi Station Mode",
                "WiFi Access Point Mode",
                "Connecting to Router",
                "HTTP Client GET and POST",
                "HTTPS SSL TLS on ESP32",
            ]),
            ("Bluetooth and BLE", "bluetooth-ble-esp32", [
                "Classic Bluetooth Basics",
                "BLE Fundamentals",
                "BLE Server and Client",
                "BLE Sensor Broadcasting",
                "BLE with Mobile App",
            ]),
            ("MQTT with ESP32", "mqtt-with-esp32", [
                "MQTT Setup on ESP32",
                "Publishing Sensor Data",
                "Subscribing for Commands",
                "QoS Levels",
                "MQTT over TLS",
            ]),
            ("HTTP and REST API", "http-rest-esp32", [
                "ESP32 HTTP Client",
                "Posting to Flask API",
                "JSON Parsing on ESP32",
                "ESP32 Web Server",
                "REST API Command and Control",
            ]),
            ("ESP32 Sensors", "esp32-sensors", [
                "DHT22 Temperature and Humidity",
                "BME280 Environment Sensor",
                "MPU6050 IMU Sensor",
                "Hall Effect Sensor",
                "Capacitive Touch Sensor",
            ]),
            ("Deep Sleep and Power Management", "deep-sleep-power", [
                "ESP32 Power Modes",
                "Deep Sleep Timer Wakeup",
                "Deep Sleep External Wakeup",
                "ULP Co-Processor",
                "Battery Powered IoT Node",
            ]),
            ("OTA Updates", "ota-updates-esp32", [
                "OTA Concept",
                "Arduino OTA",
                "HTTP OTA Update",
                "Secure OTA",
                "Rollback and Verification",
            ]),
            ("FreeRTOS on ESP32", "freertos-esp32", [
                "FreeRTOS Tasks on ESP32",
                "Task Priorities",
                "Queues for Communication",
                "Semaphores and Mutexes",
                "Dual Core Programming",
            ]),
            ("ESP32 Projects", "esp32-projects", [
                "WiFi Sensor Dashboard",
                "MQTT Home Automation",
                "BLE Sensor Monitor",
                "OTA Updatable Device",
                "Battery IoT Node",
            ]),
        ],
    },

    # ── MQTT ─────────────────────────────────────────────────────────────────
    "mqtt": {
        "title": "MQTT Protocol", "domain": "IoT Networking", "difficulty": "Intermediate",
        "modules": [
            ("MQTT Fundamentals", "mqtt-fundamentals", [
                "What Is MQTT",
                "Publish Subscribe Model",
                "Topics and Wildcards",
                "QoS Levels 0 1 2",
                "Retained Messages and LWT",
            ]),
            ("MQTT Broker Setup", "mqtt-broker-setup", [
                "Mosquitto Installation on Linux",
                "Mosquitto on Raspberry Pi",
                "Cloud Brokers HiveMQ EMQX",
                "Broker Configuration",
                "Testing with MQTT Explorer",
            ]),
            ("MQTT with Python", "mqtt-with-python", [
                "Paho MQTT Library",
                "Publisher Client",
                "Subscriber Client",
                "Sensor Data Publishing",
                "MQTT Dashboard with Flask",
            ]),
            ("MQTT with ESP32", "mqtt-with-esp32-course", [
                "Arduino MQTT Library Setup",
                "ESP32 Publisher",
                "ESP32 Subscriber",
                "JSON Payload over MQTT",
                "MQTT over TLS with ESP32",
            ]),
            ("MQTT Security", "mqtt-security", [
                "Username and Password Authentication",
                "TLS SSL for MQTT",
                "ACL Access Control Lists",
                "Certificate-Based Authentication",
                "MQTT Security Best Practices",
            ]),
            ("MQTT Integrations", "mqtt-integrations", [
                "MQTT to Node-RED",
                "MQTT to InfluxDB",
                "MQTT to Grafana",
                "MQTT to AWS IoT",
                "MQTT to WebSocket Bridge",
            ]),
        ],
    },
}


def slugify(text: str) -> str:
    """Convert lesson title to URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def seed_structure(course_slug: str, spec: dict) -> list[dict]:
    """Create Module + Lesson rows. Returns list of lesson dicts to generate AI for."""
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        print(f"  [ERROR] Course not found: {course_slug}")
        return []

    lessons_to_generate = []

    for mod_idx, (mod_title, mod_slug, lesson_titles) in enumerate(spec["modules"], start=1):
        # Get or create Module
        mod = Module.query.filter_by(course_id=course.id, slug=mod_slug).first()
        if not mod:
            mod = Module(
                course_id=course.id,
                title=mod_title,
                slug=mod_slug,
                sort_order=mod_idx,
                is_published=True,
            )
            db.session.add(mod)
            db.session.flush()
            print(f"  [MOD+] {mod_title}")
        else:
            print(f"  [MOD=] {mod_title} (exists)")

        for lesson_idx, lesson_title in enumerate(lesson_titles, start=1):
            lesson_slug = slugify(lesson_title)
            lesson = Lesson.query.filter_by(module_id=mod.id, slug=lesson_slug).first()
            if not lesson:
                lesson = Lesson(
                    module_id=mod.id,
                    title=lesson_title,
                    slug=lesson_slug,
                    sort_order=lesson_idx,
                    status='published',
                    is_deleted=False,
                    estimated_minutes=30,
                )
                db.session.add(lesson)
                db.session.flush()
                print(f"    [L+] {lesson_title}")
            else:
                print(f"    [L=] {lesson_title} (exists)")

            # Check if AI sections already generated
            existing_sections = LessonSection.query.filter_by(lesson_id=lesson.id).count()
            if existing_sections == 0:
                lessons_to_generate.append({
                    "lesson_id": lesson.id,
                    "lesson_title": lesson_title,
                    "module_title": mod_title,
                    "course_title": spec["title"],
                    "domain": spec["domain"],
                    "difficulty": spec["difficulty"],
                })

    db.session.commit()
    return lessons_to_generate


def generate_ai_sections(lesson_info: dict, provider) -> int:
    """Generate all 6 LessonSection rows for one lesson via AI. Returns sections created."""
    created = 0
    for (stype, stitle, sort_order) in SECTION_TYPES:
        try:
            prompt = get_prompt(
                "generate_lesson_section",
                section_type=stype,
                course_title=lesson_info["course_title"],
                module_title=lesson_info["module_title"],
                lesson_title=lesson_info["lesson_title"],
                domain=lesson_info["domain"],
                difficulty=lesson_info["difficulty"],
            )
            content = provider.chat(prompt)

            section = LessonSection(
                lesson_id=lesson_info["lesson_id"],
                section_type=stype,
                title=stitle,
                content_markdown=content.strip(),
                content_html="",
                sort_order=sort_order,
                is_visible=True,
            )
            db.session.add(section)
            created += 1

        except Exception as e:
            print(f"      [ERR] {stype}: {str(e)[:80]}")

    db.session.commit()
    return created


def run(course_filter=None, seed_only=False, ai_only=False):
    courses = (
        {course_filter: CURRICULUM[course_filter]}
        if course_filter and course_filter in CURRICULUM
        else CURRICULUM
    )

    with app.app_context():
        provider = get_provider()
        print(f"\nAI Provider: {provider.__class__.__name__}")

        for course_slug, spec in courses.items():
            print(f"\n{'='*65}")
            print(f"COURSE: {spec['title']} ({course_slug})")
            print(f"{'='*65}")

            if not ai_only:
                print("\n[STEP 1] Seeding modules and lessons...")
                lessons_queue = seed_structure(course_slug, spec)
            else:
                # Build queue from existing DB lessons without sections
                course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
                lessons_queue = []
                if course:
                    for mod in course.modules.all():
                        for lesson in mod.lessons.filter_by(is_deleted=False).all():
                            if LessonSection.query.filter_by(lesson_id=lesson.id).count() == 0:
                                lessons_queue.append({
                                    "lesson_id": lesson.id,
                                    "lesson_title": lesson.title,
                                    "module_title": mod.title,
                                    "course_title": spec["title"],
                                    "domain": spec["domain"],
                                    "difficulty": spec["difficulty"],
                                })

            if seed_only:
                print(f"  Seed complete. {len(lessons_queue)} lessons awaiting AI generation.")
                continue

            if not lessons_queue:
                print("  All lessons already have AI sections. Nothing to generate.")
                continue

            total = len(lessons_queue)
            print(f"\n[STEP 2] Generating AI content for {total} lessons...")
            print(f"  Estimated time: ~{total * 3} minutes (6 sections x ~30s each)\n")

            start_time = time.time()
            for idx, lesson_info in enumerate(lessons_queue, start=1):
                elapsed = time.time() - start_time
                avg = elapsed / idx if idx > 1 else 0
                eta_min = int((total - idx) * avg / 60) if avg else "?"
                print(f"  [{idx:3d}/{total}] {lesson_info['lesson_title']} (ETA: ~{eta_min}min)")

                t0 = time.time()
                created = generate_ai_sections(lesson_info, provider)
                t1 = time.time()
                print(f"         {created} sections in {t1-t0:.1f}s")

            total_time = int((time.time() - start_time) / 60)
            print(f"\n  Done! {total} lessons generated in ~{total_time} minutes.")

        print("\n[COMPLETE] IoT Content Generation finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Learning OS IoT Content Generator")
    parser.add_argument("--course", help="Generate only this course slug")
    parser.add_argument("--seed-only", action="store_true", help="Only seed DB rows, skip AI")
    parser.add_argument("--ai-only", action="store_true", help="Only run AI for existing lessons")
    args = parser.parse_args()

    run(
        course_filter=args.course,
        seed_only=args.seed_only,
        ai_only=args.ai_only,
    )
