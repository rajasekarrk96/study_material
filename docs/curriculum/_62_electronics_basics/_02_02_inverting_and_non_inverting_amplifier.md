# Inverting and Non-Inverting Amplifier

> **Course**: Electronics Basics | **Module**: Operational Amplifiers | **Difficulty**: beginner

---

Inverting and Non-Inverting amplifiers are the two fundamental closed-loop gain configurations used to scale weak sensor signals to microcontroller levels.

---



---

**Inverting Amplifier**: Input is applied through $R_{\text{in}}$ to the inverting terminal ($V_-$). The output is inverted (180° phase shift) with Closed-Loop Gain $A_v = -R_f / R_{\text{in}}$.

**Non-Inverting Amplifier**: Input is applied directly to non-inverting terminal ($V_+$). The output maintains input phase with Closed-Loop Gain $A_v = 1 + (R_f / R_1)$ and ultra-high input impedance.

---

Inverting Gain Formula:
V_out = - (R_f / R_in) * V_in
Input Impedance = R_in

Non-Inverting Gain Formula:
V_out = (1 + (R_f / R1)) * V_in
Input Impedance = Extremely High (Giga-ohms)

---

### Designing Non-Inverting Amplifier for 0-100mV Strain Gauge Sensor

Amplify 0-100mV sensor output up to 0-3.3V for ESP32 ADC ($A_v = 33$).

```python
v_in_max = 0.100  # 100 mV
v_out_max = 3.30  # 3.3V ADC Max

gain = v_out_max / v_in_max # Gain = 33.0

# Pick R1 = 1 kΩ
r1 = 1000.0
r_f = r1 * (gain - 1.0) # 1000 * 32 = 32 kΩ

print(f'Required Feedback Resistor Rf: {r_f/1000:.1f} kΩ')
```

---

1. **Saturation at Power Rails**: Attempting to amplify input such that calculated $V_{\text{out}}$ exceeds supply rail clips the waveform.
2. **Low Input Impedance of Inverting Amplifier**: Inverting configuration input impedance equals $R_{\text{in}}$, which can load weak high-resistance sensors.
3. **Using High-Value Resistors (>1MΩ)**: Creates noise and thermal offset errors from input bias currents.

---

**Q1: Which configuration offers higher input impedance: Inverting or Non-Inverting?**
A: Non-Inverting, because input goes directly to the insulated Op-Amp gate/base.

**Q2: How do you achieve a gain of less than 1 (attenuation) with an Op-Amp?**
A: Use an Inverting Amplifier with $R_f < R_{\text{in}}$.

**Q3: Can a single-supply op-amp produce a negative output voltage?**
A: No, single-supply op-amps powered from 0V and 5V cannot swing below Ground (0V).

**Q4: What is Virtual Ground in an inverting amplifier?**
A: The inverting node ($V_-$) is held at 0V potential by feedback matching $V_+ = 0V$, though not physically grounded.

---



---



---



---



---
