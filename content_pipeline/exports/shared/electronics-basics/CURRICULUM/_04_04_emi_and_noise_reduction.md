# EMI and Noise Reduction

> **Course**: Electronics Basics | **Module**: Practical Electronics | **Difficulty**: beginner

---

Electromagnetic Interference (EMI) and noise reduction techniques shield Sensitive IoT circuits from switching transients, RF interference, and ground loops.

---



---

Noise enters circuits via Conducted Emissions (power lines, shared ground traces) or Radiated Emissions (electromagnetic fields). Mitigation strategies:
1. Decoupling capacitors (0.1µF MLCC + 10µF Tantalum)
2. Solid Ground Planes (minimize ground loop area)
3. Shielded cables & Twisted pair wires (cancel differential noise)
4. Ferrite Beads on power entries

---

Differential Mode vs Common Mode Noise:
V_diff   = V_signal1 - V_signal2  (Desired Data)
V_common = (V_signal1 + V_signal2) / 2 (Corrupting Noise)

Twisted Pair Rejection:
Equal noise induced in both twisted wires cancels out in differential receiver

---

### PCB Layout Rules for Low-Noise Analog Design

1. **Star Grounding**: Separate Analog Ground (AGND) from Digital Ground (DGND), connecting them at a SINGLE star point under ADC IC.
2. **Continuous Ground Plane**: Never split ground planes under high-speed data traces.
3. **Bypass Capacitors**: Place 100nF ceramic cap within < 2mm of every IC power pin.
4. **Trace Angle**: Use 45° bends instead of 90° right angles on high-speed traces to minimize EMI reflection.

---

1. **Creating Ground Loops**: Connecting ground at multiple points creates a loop antenna picking up magnetic AC hum.
2. **Running High-Speed Digital Traces Parallel to Sensitive Analog Inputs**: Capacitive crosstalk corrupts sensor readings.
3. **Omitting Ferrite Beads on DC Power Entrances**: Allows switching noise from AC adapters to enter MCU board.

---

**Q1: What is a Ground Loop?**
A: Unwanted current path formed when two connected devices ground at different potential points, creating circulating noise currents.

**Q2: Why are differential signals (like RS485, CAN bus, USB) highly immune to noise?**
A: Because noise affects both twisted signal lines equally, and the receiver measures the difference ($V_+ - V_-$), cancelling out common noise.

**Q3: What is a Faraday Shield?**
A: Metal enclosure surrounding sensitive electronics grounded to block external RF fields.

**Q4: What capacitor value is standard for high-frequency MCU decoupling?**
A: 0.1 µF (100 nF) surface-mount ceramic capacitor.

---



---



---



---



---
