# Rectifiers

> **Course**: Electronics Basics | **Module**: Semiconductor Devices | **Difficulty**: beginner

---

Rectifiers convert alternating current (AC) into pulsating direct current (DC). They are the foundational front-end of all mains-powered DC supply adapters.

---



---

Rectification utilizes diode directional conduction to allow only positive half-cycles of AC through. Half-Wave Rectifiers use 1 diode (50% efficiency). Full-Wave Bridge Rectifiers use 4 diodes arranged in a diamond bridge to invert negative half-cycles into positive pulses, maximizing output power and doubling ripple frequency for easier smoothing.

---

Full-Wave Bridge Rectifier Equations:
V_dc_avg = (2 * V_peak) / π ≈ 0.636 * V_peak
V_dc_peak = V_ac_peak - (2 * V_f_diode)

Filter Capacitor Ripple Voltage Equation:
V_ripple = I_load / (f_ripple * C_filter)
Note: f_ripple = 2 * f_ac (100Hz for 50Hz mains, 120Hz for 60Hz mains)

---

### Sizing Filter Capacitor for 12V DC 1A Power Supply

Design a 12V 1A DC supply with max 1.0V AC ripple from a 50Hz AC Transformer.

```python
i_load = 1.0        # 1 Ampere
f_mains = 50.0      # 50 Hz AC
f_ripple = 2 * f_mains # 100 Hz full-wave
v_ripple_max = 1.0  # 1V max peak-to-peak ripple

# Calculate required smoothing capacitance: C = I / (f * V_ripple)
c_farads = i_load / (f_ripple * v_ripple_max)
c_uf = c_farads * 1e6

print(f'Minimum Filter Capacitance: {c_uf:.0f} µF')
# Output: 10,000 µF
```

---

1. **Forgetting 2x Diode Drops in Bridge Rectifiers**: Total voltage drop is 2 * Vf (~1.4V for silicon diodes), reducing peak DC voltage.
2. **Selecting Inadequate Capacitor Ripple Current Rating**: High load current causes smoothing caps to heat up and dry out if ripple current rating is exceeded.
3. **Inadequate PIV Rating**: Bridge diodes experience Peak Inverse Voltage equal to peak AC voltage.

---

**Q1: What is the main advantage of a full-wave bridge rectifier over a half-wave rectifier?**
A: Full-wave rectifies both AC half-cycles, producing double the average DC voltage and twice the ripple frequency (making filtering much easier).

**Q2: Why is a filter capacitor placed across the rectifier output?**
A: It charges up during voltage peaks and discharges into the load during voltage troughs, smoothing pulsating DC into steady DC.

**Q3: What is Diode PIV in a bridge rectifier?**
A: Peak Inverse Voltage = V_peak.

**Q4: What is ripple voltage?**
A: Residual AC fluctuations remaining on a DC voltage line after rectification and filtering.

---



---



---



---



---
