# Voltage Dividers

> **Course**: Electrical Fundamentals | **Module**: Circuit Components | **Difficulty**: beginner

---

Voltage dividers scale high analog voltages down to safe microcontroller ADC input levels (e.g. 0-3.3V) and provide bias networks for resistive sensors.

---



---

A voltage divider consists of two resistors (R1 and R2) connected in series across an input voltage V_in. The output voltage V_out tapped from the junction between R1 and R2 is a linear fraction of V_in, proportional to R2 / (R1 + R2).

---

Voltage Divider Equation:
V_out = V_in * ( R2 / (R1 + R2) )

Solving for R1 given V_in, V_out, R2:
R1 = R2 * ( (V_in / V_out) - 1 )

Loaded Voltage Divider Equation (with Load R_L connected to V_out):
R2_eff = (R2 * R_L) / (R2 + R_L)
V_out_loaded = V_in * ( R2_eff / (R1 + R2_eff) )

---

### Designing a Battery Voltage Monitor Divider for ESP32 (3.3V ADC)

Scale a 12.6V fully-charged 3S LiPo battery down to max 3.0V for safe ESP32 ADC measurement.

```python
v_in_max = 12.6   # Max Battery Voltage
v_out_target = 3.0 # Target ADC Voltage
r2 = 10000.0      # Pick R2 = 10 kΩ

# Calculate required R1
r1 = r2 * ((v_in_max / v_out_target) - 1)

print(f'Calculated R1: {r1/1000:.2f} kΩ')
# Pick standard E24 resistor value R1 = 32 kΩ

r1_actual = 32000.0
v_out_actual = v_in_max * (r2 / (r1_actual + r2))
print(f'Actual Max ADC Voltage: {v_out_actual:.2f} V')
```

---

1. **Loading Effect Errors**: Connecting a low-impedance input to a high-resistance voltage divider pulls down V_out significantly.
2. **Using Voltage Dividers as Power Supplies**: Voltage dividers are extremely inefficient for powering active loads (V_out drops when load current is drawn).
3. **Using Ultra-High Resistance Values with MCU ADCs**: Resistances above 100kΩ fail to sample accurately because ADC sampling capacitors cannot charge fast enough.

---

**Q1: Can a voltage divider be used to step down 12V to power a 5V 1A Raspberry Pi?**
A: NO! A voltage divider has high output impedance and cannot supply current without output voltage collapsing. Use a Buck Switching Converter.

**Q2: What is the rule of thumb for load impedance on a voltage divider?**
A: The load resistance R_L should be at least 10x (preferably 100x) larger than R2 to prevent voltage sag.

**Q3: How do LDR (Light Dependent Resistor) sensors measure light using a voltage divider?**
A: The LDR replaces R1 or R2. As light changes LDR resistance, V_out fluctuates proportionally for the ADC pin to read.

**Q4: If R1 = R2, what is V_out?**
A: V_out = 0.5 * V_in (exactly half).

---

**Q1: Can a voltage divider be used to step down 12V to power a 5V 1A Raspberry Pi?**
A: NO! A voltage divider has high output impedance and cannot supply current without output voltage collapsing. Use a Buck Switching Converter.

**Q2: What is the rule of thumb for load impedance on a voltage divider?**
A: The load resistance R_L should be at least 10x (preferably 100x) larger than R2 to prevent voltage sag.

**Q3: How do LDR (Light Dependent Resistor) sensors measure light using a voltage divider?**
A: The LDR replaces R1 or R2. As light changes LDR resistance, V_out fluctuates proportionally for the ADC pin to read.

**Q4: If R1 = R2, what is V_out?**
A: V_out = 0.5 * V_in (exactly half).

---



---



---



---



---
