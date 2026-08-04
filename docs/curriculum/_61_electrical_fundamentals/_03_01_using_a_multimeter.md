# Using a Multimeter

> **Course**: Electrical Fundamentals | **Module**: Practical Electrical Skills | **Difficulty**: beginner

---

Digital Multimeters (DMM) are the indispensable diagnostic instrument for verifying voltages, measuring currents, testing continuity, and debugging hardware defects.

---



---

A Digital Multimeter measures electrical parameters via internal precision analog-to-digital converters and shunt resistors. Proper terminal jack selection is critical: COM is always ground/black. Red probe connects to V/Ω for voltage/resistance and mA or 10A for current measurements.

---

Multimeter Dial Modes:
V~   : AC Voltage Measurement
V=   : DC Voltage Measurement (Battery, MCU rails)
mA/A : Current Measurement (MUST BE IN SERIES)
Ω    : Resistance Measurement (Circuit Powered OFF!)
->|- : Diode Test / Semiconductor Junction Drop
°))) : Continuity Buzzer (< 50Ω shorts beep)

---

### Standard Procedure for Measuring Microcontroller Current Draw

1. Turn OFF power to the circuit board.
2. Move the red DMM probe to the **mA** or **10A** jack (COM stays in COM).
3. Set dial to **DC mA** mode.
4. Break the positive power lead from the supply.
5. Connect the Red probe to the positive supply output, and Black probe to the MCU VCC pin.
6. Apply power and observe steady-state and peak current consumption.

---

1. **Measuring Voltage while Probes are in Current (A) Jacks**: Blows internal meter fuses or short-circuits power supplies with zero-resistance shunt.
2. **Measuring Resistance on Powered Circuits**: Destroys multimeter internals and yields false readings.
3. **Leaving Multimeter in Current Mode After Use**: Invites accidental short circuits on the next voltage test.

---

**Q1: What does the continuity buzzer test indicate?**
A: It beeps when resistance between probes is less than ~30-50Ω, indicating a low-resistance direct connection or short.

**Q2: What happens if a DMM internal fuse is blown?**
A: Current measurements will read 0.00A continuously, though voltage readings still function.

**Q3: Why must current be measured in series?**
A: All current flowing to the load must physically pass through the meter's internal low-resistance shunt resistor.

**Q4: What is Auto-Ranging?**
A: Feature where DMM automatically adjusts measurement scale for optimal resolution.

---

**Q1: What does the continuity buzzer test indicate?**
A: It beeps when resistance between probes is less than ~30-50Ω, indicating a low-resistance direct connection or short.

**Q2: What happens if a DMM internal fuse is blown?**
A: Current measurements will read 0.00A continuously, though voltage readings still function.

**Q3: Why must current be measured in series?**
A: All current flowing to the load must physically pass through the meter's internal low-resistance shunt resistor.

**Q4: What is Auto-Ranging?**
A: Feature where DMM automatically adjusts measurement scale for optimal resolution.

---



---



---



---



---
