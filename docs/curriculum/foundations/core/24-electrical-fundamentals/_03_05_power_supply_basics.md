# Power Supply Basics

> **Course**: Electrical Fundamentals | **Module**: Practical Electrical Skills | **Difficulty**: beginner

---

Power supply design ensures stable, noise-free voltage rails (5V, 3.3V, 1.8V) for microcontrollers, sensors, and wireless transceivers.

---



---

Power supplies convert unregulated raw DC or AC input into clean, tightly regulated DC output. Linear Regulators (LDOs) use active feedback to burn excess voltage as heat, offering ripple-free output. Switching Regulators (Buck/Boost) rapidly switch inductors/capacitors to efficiently step voltage up or down with minimal heat.

---

Linear Regulator Power Dissipation:
P_loss = (V_in - V_out) * I_load

Switching Regulator Efficiency:
Efficiency (η) = P_out / P_in = (V_out * I_out) / (V_in * I_in)  (Typically 85% - 95%)

Regulator Types:
LDO (Low Dropout)  : Dropping small ΔV (e.g. 5V -> 3.3V) with clean low noise.
Buck Converter     : Efficient Step-Down (12V -> 3.3V @ high current).
Boost Converter    : Efficient Step-Up (3.7V Li-ion -> 5V USB output).
Buck-Boost         : Can step up or down depending on battery state.

---

### Thermal Calculation for AMS1117-3.3 LDO Regulator

Input = 12V DC Adapter, Output = 3.3V to ESP32 drawing 200mA average.

```python
v_in = 12.0
v_out = 3.3
i_load = 0.200 # 200 mA

# Power Dissipated as Heat
p_heat = (v_in - v_out) * i_load # (12.0 - 3.3) * 0.2 = 1.74 Watts!

# Thermal Resistance SOT-223 package: R_thja = 90 °C/W
temp_rise = p_heat * 90.0
ambient_temp = 25.0
junction_temp = ambient_temp + temp_rise

print(f'Power Heat Loss: {p_heat:.2f} W')
print(f'Junction Temp: {junction_temp:.1f} °C')
# Junction temp = 181.6°C -> EXCEEDS 125°C max limit! Regulator will thermal shut down!
```

Solution: Replace LDO with a DC-DC Buck Converter module (90% efficiency, minimal heat).

---

1. **Powering High-Current Loads via LDO from High Input Voltage**: Burning large ΔV at high currents causes thermal shutdown.
2. **Omitting Regulator Input/Output Capacitors**: LDOs oscillate without manufacturer-recommended ceramic input and output capacitors.
3. **Dropout Voltage Neglect**: Supplying 3.5V to a non-LDO 3.3V regulator that requires 2.0V dropout (V_in >= 5.3V) causes output voltage to drop below 3.3V.

---

**Q1: What is Dropout Voltage in LDOs?**
A: Minimum difference between V_in and V_out required for the regulator to maintain output regulation.

**Q2: When should you prefer an LDO over a Buck Converter?**
A: For low-current noise-sensitive analog applications (like precision ADCs, audio, RF receivers) where ΔV is small.

**Q3: What is Power Ripple?**
A: Small residual periodic AC variation in DC output voltage resulting from switching or AC rectification.

**Q4: How does a Buck converter achieve >90% efficiency?**
A: By rapidly switching a transistor fully ON and fully OFF (minimizing resistive loss) and using an inductor/capacitor filter to store energy.

---

**Q1: What is Dropout Voltage in LDOs?**
A: Minimum difference between V_in and V_out required for the regulator to maintain output regulation.

**Q2: When should you prefer an LDO over a Buck Converter?**
A: For low-current noise-sensitive analog applications (like precision ADCs, audio, RF receivers) where ΔV is small.

**Q3: What is Power Ripple?**
A: Small residual periodic AC variation in DC output voltage resulting from switching or AC rectification.

**Q4: How does a Buck converter achieve >90% efficiency?**
A: By rapidly switching a transistor fully ON and fully OFF (minimizing resistive loss) and using an inductor/capacitor filter to store energy.

---



---



---



---



---
