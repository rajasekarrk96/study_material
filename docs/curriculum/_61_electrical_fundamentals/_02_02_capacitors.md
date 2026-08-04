# Capacitors

> **Course**: Electrical Fundamentals | **Module**: Circuit Components | **Difficulty**: beginner

---

Capacitors store electrical energy in electrostatic fields. They filter power supply noise, block DC, smooth ripple, and provide timing circuits.

---



---

A capacitor consists of two conducting plates separated by an insulating dielectric material (ceramic, electrolytic, film, tantalum). When voltage is applied, positive and negative charges accumulate on opposing plates. Capacitors oppose rapid changes in voltage: I = C * (dV/dt). They act as open circuits to steady DC and low-impedance paths to high-frequency AC signals.

---

Capacitance Equation:
C = Q / V    [Farads (F) = Coulombs / Volt]

Capacitive Reactance (Impedance to AC):
X_c = 1 / (2 * π * f * C)  (Ohms)

Standard Unit Scale:
1 µF  = 10^-6 F   (Electrolytic decoupling caps 1µF - 1000µF)
1 nF  = 10^-9 F   (Noise filtering caps)
1 pF  = 10^-12 F  (Crystal oscillator load caps 12pF - 22pF)

---

### Calculating Decoupling Filter Cutoff Frequency

```python
import math

def lowpass_cutoff(r_ohms, c_farads):
    return 1.0 / (2 * math.pi * r_ohms * c_farads)

# RC Lowpass filter: 1kΩ and 100nF
r = 1000.0
c = 100e-9

f_c = lowpass_cutoff(r, c)
print(f'Cutoff Frequency (-3dB): {f_c:.1f} Hz')
# Output: Cutoff Frequency: 1591.5 Hz
```

---

1. **Reverse-Polarizing Electrolytic Capacitors**: Connecting an aluminum electrolytic cap backwards causes explosive failure.
2. **Ignoring DC Bias Characteristic of Ceramic Capacitors**: High-density X5R/X7R MLCC capacitors can lose over 60% capacitance at their rated DC voltage.
3. **Placing Decoupling Capacitors Far from Microcontroller Pins**: Long PCB traces introduce parasitic inductance that negates high-frequency noise filtering.

---

**Q1: Why are decoupling capacitors placed right next to MCU VCC pins?**
A: They act as local energy reservoirs supplying instantaneous current spikes when internal logic gates switch, suppressing voltage drops on the power rail.

**Q2: What is ESR?**
A: Equivalent Series Resistance — the internal electrical resistance of a real capacitor.

**Q3: How do capacitors combine in series and parallel?**
A: In parallel, capacitances add (C_T = C1 + C2). In series, total capacitance decreases (1/C_T = 1/C1 + 1/C2).

**Q4: What capacitor type is non-polarized?**
A: Ceramic, film, and mica capacitors are non-polarized.

---

**Q1: Why are decoupling capacitors placed right next to MCU VCC pins?**
A: They act as local energy reservoirs supplying instantaneous current spikes when internal logic gates switch, suppressing voltage drops on the power rail.

**Q2: What is ESR?**
A: Equivalent Series Resistance — the internal electrical resistance of a real capacitor.

**Q3: How do capacitors combine in series and parallel?**
A: In parallel, capacitances add (C_T = C1 + C2). In series, total capacitance decreases (1/C_T = 1/C1 + 1/C2).

**Q4: What capacitor type is non-polarized?**
A: Ceramic, film, and mica capacitors are non-polarized.

---



---



---



---



---
