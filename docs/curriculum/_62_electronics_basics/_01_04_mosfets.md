# MOSFETs

> **Course**: Electronics Basics | **Module**: Semiconductor Devices | **Difficulty**: beginner

---

Metal-Oxide-Semiconductor Field-Effect Transistors (MOSFETs) are voltage-controlled switches offering near-zero gate current, extremely low ON-resistance ($R_{DS(on)}$), and high switching speeds.

---



---

A MOSFET has three terminals: Gate (G), Drain (D), and Source (S). An electric field applied to the insulated Gate voltage controls charge carrier channel formation between Drain and Source. Unlike BJTs, MOSFETs draw zero continuous Gate DC current ($I_G = 0$), making them ideal for driving heavy loads (motors, solenoids, high-power LEDs) directly from microcontrollers.

---

MOSFET Key Parameters:
V_GS(th) : Gate-Source Threshold Voltage (Voltage where channel begins conducting)
R_DS(on) : Drain-Source On-Resistance when fully turned ON (e.g. 5mΩ - 50mΩ)
V_GS_max : Absolute maximum Gate-Source voltage (typically ±20V)
I_D_max  : Maximum continuous Drain Current

Power Loss in ON State:
P_conduction = I_D^2 * R_DS(on)

---

### High-Side PWM Motor Control with N-Channel Logic-Level MOSFET (IRLZ44N)

Drive a 12V 5A DC Motor using a 3.3V GPIO pin running PWM.

```python
i_drain = 5.0        # 5 Amps Motor Current
r_dson = 0.022       # 22 mΩ ON-Resistance at VGS = 3.3V

# Conduction Power Dissipation
p_loss = (i_drain ** 2) * r_dson

print(f'MOSFET Heat Loss: {p_loss:.2f} Watts')
# Output: 0.55 Watts (Minimal heating, no large heatsink required)
```

---

1. **Using Standard MOSFETs instead of Logic-Level MOSFETs at 3.3V**: Standard MOSFETs require $V_{GS} = 10V$ to turn fully ON; driving them at 3.3V causes high $R_{DS(on)}$ and catastrophic thermal destruction.
2. **Leaving the Gate Floating**: Floating Gate accumulates static charge causing erratic partial ON switching; always add a 10kΩ Gate pull-down resistor to Ground.
3. **Ignoring Gate Capacitance ($C_{iss}$) in High-Speed PWM**: High gate charge requires high peak driver current during fast PWM switching.

---

**Q1: What is a Logic-Level MOSFET?**
A: A MOSFET engineered with a low threshold voltage ($V_{GS(th)} < 2.0V$) to turn fully ON ($R_{DS(on)}$ specified) at 3.3V or 5V logic levels.

**Q2: What is the purpose of a Gate resistor?**
A: A small series Gate resistor (22Ω - 100Ω) limits current ringing spikes charging the internal MOSFET Gate capacitance during switching.

**Q3: How does N-Channel differ from P-Channel MOSFET?**
A: N-Channel is used for Low-Side switching (placed between load and GND, turned ON with +VGS); P-Channel is used for High-Side switching (between VCC and load, turned ON by pulling Gate LOW).

**Q4: What is the Body Diode?**
A: An intrinsic internal diode formed between Source and Drain in power MOSFETs.

---



---



---



---



---
