# Hardware Interfacing with Python

> **Course**: Core Python | **Module**: Scientific Python | **Difficulty**: intermediate

---

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)    # use BCM pin numbering
GPIO.setup(18, GPIO.OUT)  # pin 18 as output
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # pin 24 input

# Blink LED
try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()   # always clean up!
```

---

```python
from gpiozero import LED, Button, DistanceSensor
from time import sleep

led = LED(18)
button = Button(17)

# Event-driven
button.when_pressed = led.on
button.when_released = led.off

# Distance sensor (HC-SR04)
sensor = DistanceSensor(echo=24, trigger=23)
while True:
    print(f"Distance: {sensor.distance * 100:.1f} cm")
    sleep(0.1)
```

---

```python
import serial

# Connect to Arduino/ESP32
ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

# Send command
ser.write(b"READ_TEMP\n")

# Read response
line = ser.readline().decode("utf-8").strip()
print(f"Temperature: {line}")

ser.close()
```

---

```python
from smbus2 import SMBus

# Read from BME280 sensor at address 0x76
with SMBus(1) as bus:
    # Read 2 bytes from register 0xF3
    data = bus.read_i2c_block_data(0x76, 0xF3, 2)
    raw_temp = (data[0] << 8) | data[1]
```

---

```python
# On ESP32/Pico
from machine import Pin, ADC, PWM
import time

# LED blink
led = Pin(2, Pin.OUT)
while True:
    led.value(1); time.sleep(0.5)
    led.value(0); time.sleep(0.5)

# ADC reading
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V range
voltage = adc.read() * 3.3 / 4095

# PWM (servo control)
servo = PWM(Pin(5), freq=50)
servo.duty(77)   # ~0 degrees
```

---

1. Read temperature from DHT11 using `gpiozero` and log to CSV every 10 seconds
2. Send commands over serial to an Arduino to blink an LED at variable frequencies
3. Read ADC values from a potentiometer on ESP32 via MicroPython and print the voltage

---
