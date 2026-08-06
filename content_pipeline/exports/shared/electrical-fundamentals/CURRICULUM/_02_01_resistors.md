# Resistors

> **Course**: Electrical Fundamentals | **Module**: Circuit Components | **Difficulty**: beginner

---

Resistors limit current flow, divide voltages, and establish bias levels across electronic circuits. They are the most common passive component in IoT hardware.

---



---

A resistor is a two-terminal passive component engineered to provide a specific electrical resistance. Resistors convert unwanted electrical energy into heat. Resistors are classified by value (Ω), tolerance (%), and power rating (W). Standard resistor color codes utilize 4 or 5 bands to indicate nominal value and precision.

---

4-Band Resistor Color Code:
Band 1: 1st Digit
Band 2: 2nd Digit
Band 3: Multiplier (10^n)
Band 4: Tolerance (Gold=5%, Silver=10%, Brown=1%)

Color Values:
Black=0, Brown=1, Red=2, Orange=3, Yellow=4,
Green=5, Blue=6, Violet=7, Grey=8, White=9

Example: Yellow - Violet - Red - Gold
Digit 1 = 4, Digit 2 = 7, Multiplier = 10^2 (100), Tolerance = ±5%
Value = 47 x 100 = 4700 Ω = 4.7 kΩ ± 5%

---

### Python Resistor Color Code Decoder

```python
COLOR_CODES = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

def decode_4band(b1, b2, b3_mult):
    d1 = COLOR_CODES[b1.lower()]
    d2 = COLOR_CODES[b2.lower()]
    mult = 10 ** COLOR_CODES[b3_mult.lower()]
    value = (d1 * 10 + d2) * mult
    return value

value_ohms = decode_4band('yellow', 'violet', 'red')
print(f'Resistor Value: {value_ohms/1000:.1f} kΩ')
# Output: 4.7 kΩ
```

---

1. **Using Standard Carbon Resistors in Precision Analog Circuits**: Carbon film resistors have higher thermal drift than Metal Film resistors.
2. **Exceeding Voltage Rating**: Small SMD 0603 resistors have maximum working voltage limits (e.g. 50V) regardless of power calculations.
3. **Assuming Nominal Resistance is Exact**: Standard 5% tolerance means a 100kΩ resistor can range between 95kΩ and 105kΩ.

---

**Q1: What does pull-up and pull-down mean?**
A: Pull-up resistors connect a signal line to VCC to keep it HIGH when idle; pull-down resistors connect it to GND to keep it LOW when idle.

**Q2: What is SMD resistor 103 rating?**
A: 10 x 10^3 Ω = 10,000 Ω = 10 kΩ.

**Q3: What happens when resistors are connected in series vs parallel?**
A: In series, resistances add (R_T = R1 + R2). In parallel, equivalent resistance drops (1/R_T = 1/R1 + 1/R2).

**Q4: What is a potentiometer?**
A: A 3-terminal manually adjustable variable resistor functioning as a voltage divider.

---

**Q1: What does pull-up and pull-down mean?**
A: Pull-up resistors connect a signal line to VCC to keep it HIGH when idle; pull-down resistors connect it to GND to keep it LOW when idle.

**Q2: What is SMD resistor 103 rating?**
A: 10 x 10^3 Ω = 10,000 Ω = 10 kΩ.

**Q3: What happens when resistors are connected in series vs parallel?**
A: In series, resistances add (R_T = R1 + R2). In parallel, equivalent resistance drops (1/R_T = 1/R1 + 1/R2).

**Q4: What is a potentiometer?**
A: A 3-terminal manually adjustable variable resistor functioning as a voltage divider.

---



---



---



---



---
