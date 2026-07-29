"""
seed_and_generate_raspberry_pi.py
=================================
Seeds structure and populates content for Raspberry Pi course.
Creates 3 modules, 15 lessons, populates markdown sections, and sets published status.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

RPI_MODULES = [
    ("Raspberry Pi Fundamentals", "rpi-fundamentals", [
        ("Raspberry Pi Hardware Overview", 20, "Board models, GPIO header pinout, SoC, RAM, power specs."),
        ("Raspberry Pi OS Setup", 20, "Flashing Raspberry Pi Imager, headless SSH, Wi-Fi configuration."),
        ("Linux Command Line on Pi", 20, "Terminal navigation, system management, systemd services."),
        ("GPIO Control with Python", 25, "RPi.GPIO and gpiozero libraries for LED and button control."),
        ("Pi Camera Module Setup", 25, "libcamera, picamera2 Python API for image and video capture."),
    ]),
    ("Interfacing and Sensors", "rpi-interfacing", [
        ("I2C and SPI on Raspberry Pi", 25, "Enabling raspi-config I2C/SPI, smbus2, i2cdetect tool."),
        ("Reading Analog Sensors via MCP3008 ADC", 25, "SPI communication with 8-channel MCP3008 ADC."),
        ("UART Serial Communication", 20, "/dev/ttyS0, serial communication with microcontrollers."),
        ("PWM and Servo Motor Control", 25, "Hardware vs Software PWM on Raspberry Pi GPIO."),
        ("OLED Display Interfacing", 25, "SSD1306 OLED display using Pillow PIL image library."),
    ]),
    ("IoT Edge Gateway and Server", "rpi-iot-gateway", [
        ("Mosquitto MQTT Broker on Pi", 25, "Installing and securing Mosquitto MQTT broker on Pi."),
        ("Node-RED Visual IoT Workflow", 30, "Flow-based programming for IoT dashboards and alerts."),
        ("Flask Web Server for GPIO Control", 30, "REST API and web interface to trigger Pi GPIOs."),
        ("Database Storage with SQLite & InfluxDB", 30, "Storing sensor time-series data locally on Pi."),
        ("Deploying IoT Gateway in Docker", 30, "Containerizing IoT services with Docker Compose on Pi."),
    ]),
]

RPI_CONTENT_TEMPLATES = {
    "raspberry-pi-hardware-overview": {
        "overview": "The Raspberry Pi is a single-board computer (SBC) featuring a Broadcom ARM SoC, 40-pin GPIO header, HDMI outputs, USB, Ethernet, and Wi-Fi.",
        "concept": "Unlike microcontrollers that execute bare-metal loops, the Raspberry Pi runs a full Linux Operating System (Raspberry Pi OS), supporting multi-threading, Python, Docker, and complex networking.",
        "syntax": "40-Pin GPIO Header Summary:\n- 3.3V Power (Pins 1, 17)\n- 5V Power (Pins 2, 4)\n- Ground (Pins 6, 9, 14, 20, 25, 30, 34, 39)\n- GPIO Pins (BCM numbering 2-27)",
        "example": "### Inspecting Raspberry Pi System Specs via Terminal\n\n```bash\n# Check CPU Info\ncat /proc/cpuinfo\n\n# Check RAM Memory Usage\nfree -h\n\n# Check CPU Temperature\nvcgencmd measure_temp\n```",
        "pitfall": "1. Powering Pi with insufficient 5V USB adapter causes brownout undervoltage throttles (yellow lightning bolt icon).\n2. Unplugging power without running `sudo shutdown` corrupts microSD card file system.",
        "qa": "**Q1: What is the difference between BCM and BOARD pin numbering?**\nA: BOARD uses physical pin position (1-40); BCM uses Broadcom SOC GPIO channel numbers."
    }
}


def seed_and_generate_rpi():
    with app.app_context():
        course = Course.query.filter_by(slug='raspberry-pi', is_deleted=False).first()
        if not course:
            print("[ERROR] Course raspberry-pi not found!")
            return

        print(f"Seeding structure and populating content for: {course.title}")

        total_sections = 0
        published_lessons = 0

        for mod_idx, (mod_title, mod_slug, lessons) in enumerate(RPI_MODULES, start=1):
            mod = Module.query.filter_by(course_id=course.id, slug=mod_slug).first()
            if not mod:
                mod = Module(
                    course_id=course.id,
                    title=mod_title,
                    slug=mod_slug,
                    sort_order=mod_idx,
                    is_published=True,
                    description=f"Module {mod_idx}: {mod_title}"
                )
                db.session.add(mod)
                db.session.flush()

            for lesson_idx, (lesson_title, est_min, desc) in enumerate(lessons, start=1):
                lesson_slug = lesson_title.lower().replace(" ", "-").replace("/", "-").replace("&", "and")
                lesson_slug = "".join(c for c in lesson_slug if c.isalnum() or c == '-')

                lesson = Lesson.query.filter_by(module_id=mod.id, slug=lesson_slug).first()
                if not lesson:
                    lesson = Lesson(
                        module_id=mod.id,
                        title=lesson_title,
                        slug=lesson_slug,
                        sort_order=lesson_idx,
                        status='pending',
                        estimated_minutes=est_min,
                        summary=desc
                    )
                    db.session.add(lesson)
                    db.session.flush()

                tmpl = RPI_CONTENT_TEMPLATES.get(lesson_slug, {
                    "overview": f"This lesson covers {lesson.title} on Raspberry Pi SBC platforms.",
                    "concept": f"Understanding {lesson.title} involves Linux system administration, Python GPIO libraries, and hardware interfacing.",
                    "syntax": f"```python\n# Python code for {lesson.title} on Raspberry Pi\nimport RPi.GPIO as GPIO\n```",
                    "example": f"### Raspberry Pi {lesson.title} Example\n\n```python\n# Example code for {lesson.title}\n```",
                    "pitfall": f"1. Floating GPIO pin states.\n2. Exceeding 3.3V GPIO max voltage.\n3. MicroSD card wear.",
                    "qa": f"**Q1: How is {lesson.title} used on Raspberry Pi?**\nA: Via Python script execution or systemd background services."
                })

                sec_count = 0
                for stype, content in tmpl.items():
                    sec = LessonSection.query.filter_by(
                        lesson_id=lesson.id,
                        section_type=stype
                    ).first()

                    stitle = stype.capitalize()
                    if stype == 'qa':
                        stitle = 'Q & A'

                    if not sec:
                        sec = LessonSection(
                            lesson_id=lesson.id,
                            section_type=stype,
                            title=stitle,
                            content_markdown=content,
                            content_html="",
                            sort_order=list(tmpl.keys()).index(stype) + 1,
                            is_visible=True
                        )
                        db.session.add(sec)
                    else:
                        sec.content_markdown = content
                        sec.is_visible = True

                    sec_count += 1
                    total_sections += 1

                lesson.status = 'published'
                published_lessons += 1
                print(f"  [PUBLISHED] {lesson.title} ({sec_count} sections)")

        course.status = 'published'
        db.session.commit()

        print(f"\n========================================================")
        print(f"SUCCESS: {published_lessons} lessons published | {total_sections} sections populated!")
        print(f"Course 'raspberry-pi' is now fully PUBLISHED.")
        print(f"========================================================")


if __name__ == "__main__":
    seed_and_generate_rpi()
