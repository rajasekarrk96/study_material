# AC vs DC

> **Course**: Electrical Fundamentals | **Module**: Basic Electrical Theory | **Difficulty**: beginner

---

Direct Current (DC) flows in one unidirectional path, while Alternating Current (AC) periodically reverses direction. Microcontrollers run on DC, while mains power grids deliver AC.

---



---

Direct Current (DC) maintains a constant voltage polarity over time (e.g. 5V USB, 3.3V battery power). Electrons travel continuously from the negative terminal to the positive terminal. Alternating Current (AC) voltage oscillates sinusoidally, reversing direction at a frequency f (50Hz or 60Hz in power mains). AC is ideal for long-distance grid transmission using step-up/step-down transformers.

---

Sinusoidal AC Waveform Parameters:
v(t) = V_peak * sin(2 * π * f * t)

Root Mean Square (RMS) Voltage:
V_rms = V_peak / sqrt(2) ≈ 0.707 * V_peak
V_peak = V_rms * sqrt(2) ≈ 1.414 * V_rms

Frequency & Period:
f = 1 / T    [Frequency (Hz) = 1 / Period (seconds)]
Mains Standards: 120V RMS @ 60Hz (North America), 230V RMS @ 50Hz (Europe/Asia)

---

### Calculating Peak Voltage for 230V AC Mains Transformer Conversion

```python
import math

v_rms = 230.0  # Standard AC Mains voltage
freq = 50.0    # 50 Hz

# Peak AC Voltage
v_peak = v_rms * math.sqrt(2)

# Peak-to-Peak Voltage
v_pp = 2 * v_peak

print(f'AC RMS Voltage: {v_rms:.1f} V')
print(f'AC Peak Voltage: {v_peak:.1f} V')
print(f'AC Peak-to-Peak: {v_pp:.1f} V')
# Peak Voltage is ~325.3V!
```

When selecting AC-DC power converters or relay isolation, components must withstand the 325V peak, not just the 230V RMS value.

---

1. **Connecting AC Mains Directly to DC Microcontrollers**: Instantly destroys low-voltage DC electronics and creates lethal shock hazards.
2. **Selecting Rectifier Diodes Based Only on RMS Voltage**: Diodes in rectifiers experience Peak Inverse Voltage (PIV >= V_peak), needing ratings higher than RMS.
3. **Confusing Frequency Standards**: Operating 60Hz magnetic transformers on 50Hz AC causes core saturation and overheating.

---

**Q1: Why is AC used for electrical power transmission instead of DC?**
A: AC voltage can be easily stepped up to ultra-high voltages (e.g. 400kV) using transformers to minimize I^2R power line losses over long distances, then stepped down safely.

**Q2: What is RMS voltage?**
A: Root Mean Square (RMS) is the equivalent DC voltage value that produces the identical heating power in a resistor as the AC wave.

**Q3: What component converts AC to pulsating DC?**
A: A Diode Bridge Rectifier.

**Q4: Do microcontrollers require AC or DC power?**
A: Microcontrollers require clean, regulated DC voltage (typically 3.3V or 5V).

---

**Q1: Why is AC used for electrical power transmission instead of DC?**
A: AC voltage can be easily stepped up to ultra-high voltages (e.g. 400kV) using transformers to minimize I^2R power line losses over long distances, then stepped down safely.

**Q2: What is RMS voltage?**
A: Root Mean Square (RMS) is the equivalent DC voltage value that produces the identical heating power in a resistor as the AC wave.

**Q3: What component converts AC to pulsating DC?**
A: A Diode Bridge Rectifier.

**Q4: Do microcontrollers require AC or DC power?**
A: Microcontrollers require clean, regulated DC voltage (typically 3.3V or 5V).

---



---



---



---



---
