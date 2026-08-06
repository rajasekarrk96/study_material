# Inductors and Coils

> **Course**: Electrical Fundamentals | **Module**: Circuit Components | **Difficulty**: beginner

---

Inductors store energy in magnetic fields. They are core components in DC-DC buck/boost converters, noise chokes, relays, motors, and wireless communication circuits.

---



---

An inductor is a coil of wire wrapped around a magnetic core (ferrite or air). When current flows through the coil, it creates a magnetic field. Inductors oppose changes in electric current: V = L * (dI/dt). When current suddenly changes, the collapsing magnetic field produces a high back-EMF voltage kick.

---

Inductance Equation:
V_induced = L * (dI / dt)

Inductive Reactance (AC Impedance):
X_L = 2 * π * f * L   (Ohms)

Standard Units:
1 H  = 1 Henry
1 mH = 10^-3 H   (Relay coils, power inductors)
1 µH = 10^-6 H   (Buck converter switching inductors 2.2µH - 47µH)

---

### Calculating Back-EMF Voltage from a De-energized Relay Coil

A 100mH relay coil carrying 100mA is switched off in 1 microsecond by a transistor without a flyback diode.

```python
l_henry = 0.100       # 100 mH
delta_i = 0.100       # 100 mA to 0 mA
delta_t = 1.0e-6      # 1 microsecond

# Induced Back-EMF Voltage
v_spike = l_henry * (delta_i / delta_t)

print(f'Inductive Voltage Spike: {v_spike:.1f} V')
# Output: 10,000 Volts!
```

This massive voltage spike will instantly destroy the switching transistor unless a Flyback Diode is connected across the coil.

---

1. **Omitting Flyback Diodes Across Inductive Loads**: Relays, solenoids, and motors generate inductive spikes that destroy switching MOSFETs/BJT drivers.
2. **Inductor Core Saturation**: Exceeding the rated saturation current causes inductance to collapse, causing overcurrent spikes.
3. **Magnetic Crosstalk on PCB**: Placing inductors close together without shielding causes unwanted EMI coupling between signals.

---

**Q1: What is a flyback diode?**
A: A diode placed across an inductive load in reverse bias to safely dissipate inductive back-EMF current when the switch turns off.

**Q2: How does an inductor behave at DC steady-state?**
A: At DC steady-state (dI/dt = 0), an ideal inductor behaves as a pure short circuit (zero voltage drop).

**Q3: What is the primary use of a ferrite bead?**
A: A ferrite bead is a specialized inductor that attenuates high-frequency noise on power supply traces by dissipating high-frequency AC as heat.

**Q4: What happens to inductive reactance as frequency increases?**
A: Inductive reactance (X_L = 2*π*f*L) increases linearly with frequency.

---

**Q1: What is a flyback diode?**
A: A diode placed across an inductive load in reverse bias to safely dissipate inductive back-EMF current when the switch turns off.

**Q2: How does an inductor behave at DC steady-state?**
A: At DC steady-state (dI/dt = 0), an ideal inductor behaves as a pure short circuit (zero voltage drop).

**Q3: What is the primary use of a ferrite bead?**
A: A ferrite bead is a specialized inductor that attenuates high-frequency noise on power supply traces by dissipating high-frequency AC as heat.

**Q4: What happens to inductive reactance as frequency increases?**
A: Inductive reactance (X_L = 2*π*f*L) increases linearly with frequency.

---



---



---



---



---
