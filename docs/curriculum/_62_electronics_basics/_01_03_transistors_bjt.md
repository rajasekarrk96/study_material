# Transistors BJT

> **Course**: Electronics Basics | **Module**: Semiconductor Devices | **Difficulty**: beginner

---

Bipolar Junction Transistors (BJTs) are current-controlled semiconductor amplifiers and switches used to drive relays, LEDs, motors, and buzzers from low-power MCU GPIO pins.

---



---

A BJT has three terminals: Base (B), Collector (C), and Emitter (E). A small current entering the Base ($I_B$) controls a much larger current flowing between Collector and Emitter ($I_C = \beta \times I_B$). In Switching Applications, the BJT operates in Saturation (Fully ON, $V_{CE} \approx 0.2V$) or Cutoff (Fully OFF, $I_C = 0$).

---

BJT Key Equations:
I_C = β * I_B           (Active Amplification Region)
I_E = I_C + I_B
V_BE ≈ 0.7V             (Forward Biased Base-Emitter Junction)

Saturation Rule of Thumb for Switching:
Target I_B = I_C / 10   (Forced beta of 10 to ensure deep saturation)
R_base = (V_gpio - V_BE) / I_B

---

### Designing an NPN BJT (2N2222) Relay Driver Circuit

Drive a 5V relay coil requiring 80mA using a 3.3V ESP32 GPIO pin.

```python
v_gpio = 3.3    # ESP32 High voltage
v_be = 0.7      # Base-emitter drop
i_collector = 0.080 # 80 mA relay current

# Saturation overdrive factor (forced beta = 10)
i_base = i_collector / 10.0 # 8 mA Base current

r_base = (v_gpio - v_be) / i_base
print(f'Calculated Base Resistor: {r_base:.1f} Ω')
# Pick standard resistor R_base = 330 Ω
```

---

1. **Connecting Base Directly to MCU GPIO Without Resistor**: Destroys the MCU pin and Base-Emitter junction due to unlimited forward current.
2. **Operating BJT in Linear Region When Switching**: Causes excessive $V_{CE}$ drop, causing high power dissipation ($P = V_{CE} \times I_C$) and overheating.
3. **Forgetting Flyback Diode Across Relays**: Inductive kickback destroys Collector-Emitter junction on turn-off.

---

**Q1: What is the difference between NPN and PNP BJTs?**
A: NPN turns ON when Base voltage is pulled above Emitter (+0.7V); PNP turns ON when Base is pulled below Emitter (-0.7V).

**Q2: What is Beta (hFE)?**
A: DC Current Gain ratio ($I_C / I_B$), typically ranging between 50 and 300.

**Q3: What is VCE(sat)?**
A: Collector-Emitter Saturation Voltage (~0.1V - 0.3V) when transistor is fully turned ON as a switch.

**Q4: Which BJT terminal is connected to Ground in low-side NPN switching?**
A: Emitter terminal.

---



---



---



---



---
