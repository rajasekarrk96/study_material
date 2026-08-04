# Ohms Law

> **Course**: Electrical Fundamentals | **Module**: Basic Electrical Theory | **Difficulty**: beginner

---

Ohm's Law is the fundamental equation linking voltage, current, and resistance (V = I * R). It is used continuously when calculating resistor values, sensor biasing, power dissipation, and current draw in hardware engineering.

---



---

Discovered by Georg Simon Ohm in 1827, Ohm's Law states that the current flowing through a linear conductor between two points is directly proportional to the voltage across the two points and inversely proportional to the resistance between them. If you double the voltage across a fixed resistor, the current doubles. If you double the resistance while keeping voltage constant, the current drops in half.

---

Ohm's Law Equations & Variants:

Primary Formula : V = I * R    [Voltage = Current x Resistance]
Current Formula : I = V / R    [Current = Voltage / Resistance]
Resistance Form : R = V / I    [Resistance = Voltage / Current]

Power Triad (Joules Heating):
P = V * I                      [Power (Watts) = Voltage x Current]
P = I^2 * R                    [Power = Current squared x Resistance]
P = V^2 / R                    [Power = Voltage squared / Resistance]

---

### Designing a Pull-Up Resistor for a Digital Sensor Button

To prevent a floating input on a 5V microcontroller input pin, we install a pull-up resistor connected to 5V. When the button is pressed, it shorts the pin directly to Ground (0V).

```python
# Calculate power dissipation when button is pressed with a 10k ohm pull-up
v_cc = 5.0          # Operating Voltage (Volts)
r_pullup = 10000.0  # 10 kΩ Resistor

# Current when button is shorted to GND
i_pressed = v_cc / r_pullup  # 5.0 / 10000 = 0.0005 A (0.5 mA)

# Power dissipated by resistor as heat
p_resistor = (v_cc ** 2) / r_pullup # 25 / 10000 = 0.0025 W (2.5 mW)

print(f'Current during press: {i_pressed * 1000:.2f} mA')
print(f'Power dissipated: {p_resistor * 1000:.2f} mW')
```

A standard 1/4-Watt (250 mW) resistor dissipates 2.5 mW easily without overheating.

---

1. **Ignoring Resistor Power Ratings**: Using a 1/4W resistor in a circuit that dissipates 1W will cause the resistor to burn and potentially ignite.
2. **Assuming Non-linear Devices Obey Ohm's Law Directly**: Diodes, LEDs, and transistors are non-ohmic components; their dynamic resistance changes non-linearly with applied voltage.
3. **Temperature Coefficient Neglect**: High current causes heating, which increases conductor resistance and alters operating parameters.

---

**Q1: If a 1kΩ resistor has 10V across it, how much current flows?**
A: Using I = V / R, I = 10V / 1000Ω = 0.01A = 10mA.

**Q2: What happens to power dissipation if you double the current through a resistor?**
A: Because P = I^2 * R, doubling the current quadruples (4x) the thermal power dissipation.

**Q3: Are all materials subject to Ohm's Law?**
A: No. Metals and carbon resistors are ohmic. Semiconductor junctions (diodes, transistors, gas discharge tubes) are non-ohmic.

**Q4: How do you pick the power rating for a resistor?**
A: Calculate calculated dissipation (P = I^2 * R) and select a resistor rated for at least twice that value for safety derating.

---



---



---



---



---
