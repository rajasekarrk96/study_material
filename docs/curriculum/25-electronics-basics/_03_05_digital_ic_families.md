# Digital IC Families

> **Course**: Electronics Basics | **Module**: Digital Electronics | **Difficulty**: beginner

---

Digital IC Families (TTL vs CMOS: 74HC, 74HCT, 74LVC) define voltage thresholds, switching speed, power consumption, and logic level compatibility.

---



---

**TTL (Transistor-Transistor Logic)**: Uses BJTs (5V supply). $V_{IH} = 2.0V$, $V_{IL} = 0.8V$. Higher static power consumption.

**CMOS (Complementary MOS)**: Uses PMOS+NMOS pairs (1.8V-5V). Low static power, high input impedance. Thresholds scale as percentage of VCC ($V_{IH} = 0.7V_{CC}$).

---

Logic Threshold Voltage Comparison:
5V TTL     : V_IL = 0.8V, V_IH = 2.0V
5V CMOS    : V_IL = 1.5V, V_IH = 3.5V
3.3V LVCMOS: V_IL = 0.8V, V_IH = 2.0V

Compatibility Issue:
3.3V Output (VOH = 3.0V) -> Drives 5V TTL (VIH = 2.0V)  -> OK!
3.3V Output (VOH = 3.0V) -> Drives 5V CMOS (VIH = 3.5V) -> FAILS! Requires Level Shifter!

---

### Logic Level Shifting between 5V Sensor and 3.3V ESP32

```python
# Bidirectional MOSFET Level Shifter Simulation
v_hv = 5.0  # 5V Sensor side
v_lv = 3.3  # 3.3V ESP32 side

# 5V TX to 3.3V RX via Voltage Divider (1k / 2k)
r1, r2 = 1000.0, 2000.0
v_esp_rx = v_hv * (r2 / (r1 + r2))
print(f'Scaled 5V Signal to ESP32 RX: {v_esp_rx:.2f} V')
# Output: 3.33V (Safe for 3.3V MCU)
```

---

1. **Connecting 5V Logic Directly to Non-5V-Tolerant 3.3V MCU Pins**: Overvoltage destroys internal ESD protection diodes and GPIO silicon.
2. **Assuming 74HC Inputs Work with 3.3V Logic on 5V VCC**: 74HC requires $V_{IH} = 3.5V$ at 5V VCC; 3.3V signal is ignored! Use **74HCT** (TTL thresholds at 5V VCC).
3. **Floating CMOS Inputs**: Unused CMOS inputs oscillate between rails, causing excessive power draw.

---

**Q1: What does the 'T' in 74HCT stand for?**
A: TTL-compatible inputs (allows 3.3V/5V TTL signals to drive the 5V CMOS IC).

**Q2: What is Noise Margin?**
A: Difference between worst-case output voltage ($V_{OH}/V_{OL}$) and input threshold voltage ($V_{IH}/V_{IL}$) providing immunity against noise spikes.

**Q3: Are ESP32 GPIO pins 5V tolerant?**
A: Official datasheet specifies ESP32 pins are NOT 5V tolerant (Max 3.6V).

**Q4: What is Fan-Out?**
A: Maximum number of digital gate inputs a single digital output can drive without signal degradation.

---



---



---



---



---
