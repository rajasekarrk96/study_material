# Diodes

> **Course**: Electronics Basics | **Module**: Semiconductor Devices | **Difficulty**: beginner

---

Diodes are semiconductor one-way valves for electric current. They are essential for reverse polarity protection, rectification, signal clipping, and flyback protection in IoT hardware.

---



---

A semiconductor diode consists of a P-N junction formed by joining P-type (positive hole majority) and N-type (negative electron majority) silicon. In Forward Bias (Anode > Cathode by ~0.7V for silicon), the depletion region shrinks and current flows freely. In Reverse Bias (Cathode > Anode), the depletion region expands, blocking current flow until breakdown voltage is reached.

---

Diode Equation (Shockley Model):
I = I_s * (exp(V / (n * V_t)) - 1)

Key Specifications:
V_f  : Forward Voltage Drop (~0.7V Silicon, ~0.3V Schottky, 1.8-3.3V LED)
I_f  : Maximum Continuous Forward Current
PIV  : Peak Inverse Voltage (Max Reverse Voltage before breakdown)
t_rr : Reverse Recovery Time (High speed switching factor)

---

### Reverse Polarity Protection Circuit using Schottky Diode

Connect a 1N5819 Schottky Diode (Vf = 0.3V) in series with positive battery input to protect an ESP32 board.

```python
v_battery = 5.0    # Input battery voltage
v_f_schottky = 0.3 # Low forward drop Schottky
i_load = 0.250     # 250 mA MCU consumption

v_mcu_vcc = v_battery - v_f_schottky
p_diode_loss = v_f_schottky * i_load

print(f'MCU Operating VCC: {v_mcu_vcc:.2f} V')
print(f'Diode Power Dissipation: {p_diode_loss * 1000:.1f} mW')
# Output: VCC = 4.70V, Dissipation = 75.0 mW
```

---

1. **Using Standard 1N4007 Diodes in High-Speed Switching (PWM/DC-DC)**: Slow reverse recovery time (t_rr) causes high switching losses and overheating; use Schottky or Ultrafast diodes.
2. **Exceeding Diode Peak Inverse Voltage**: Exceeding PIV in AC rectifiers causes reverse avalanche breakdown.
3. **Ignoring Diode Thermal Voltage Drift**: Forward voltage Vf drops by ~2mV/°C as temperature rises, which can cause thermal runaway in parallel diodes.

---

**Q1: Why are Schottky diodes preferred in battery-powered IoT systems?**
A: They feature much lower forward voltage drops (0.2V - 0.4V vs 0.7V for silicon diodes), minimizing wasted power.

**Q2: What is the Anode and Cathode polarity?**
A: Anode is positive (+); Cathode is negative (-), marked with a silver/black line band on the physical diode package.

**Q3: Can diodes be placed in parallel to double current capacity?**
A: Not directly without current-sharing resistors, because the diode with slightly lower Vf will draw most current, overheat, and fail.

**Q4: What is Zener breakdown?**
A: Controlled reverse voltage breakdown engineered to maintain a constant voltage across the diode for voltage regulation.

---



---



---



---



---
