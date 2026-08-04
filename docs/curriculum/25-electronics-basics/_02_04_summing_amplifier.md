# Summing Amplifier

> **Course**: Electronics Basics | **Module**: Operational Amplifiers | **Difficulty**: beginner

---

Summing Amplifiers combine multiple analog input voltages into a single weighted composite output, commonly used in audio mixing and DAC signal reconstruction.

---



---

A Summing Amplifier is an inverting op-amp variant with multiple input resistors ($R_1, R_2, R_3$) connected to the virtual ground node ($V_-$). Because no current enters $V_-$, the currents from all input branches sum together into the single feedback resistor $R_f$.

---

Summing Amplifier Output Equation:
V_out = - R_f * ( (V1 / R1) + (V2 / R2) + (V3 / R3) )

If R1 = R2 = R3 = R:
V_out = - (R_f / R) * (V1 + V2 + V3)

---

### 3-Bit R-2R Ladder DAC Summing Stage

Sum 3 digital signals (V1=3.3V, V2=0V, V3=3.3V) with equal 10kΩ resistors and Rf = 10kΩ.

```python
v1, v2, v3 = 3.3, 0.0, 3.3
r1 = r2 = r3 = 10000.0
r_f = 10000.0

v_out = - r_f * ((v1/r1) + (v2/r2) + (v3/r3))
print(f'Summed Inverted Output: {v_out:.2f} V')
# Followed by Inverting Buffer (Gain=-1) -> +6.60V (scaled down by attenuator)
```

---

1. **Exceeding Output Rails when Summing Multiple Signals**: Summing multiple positive signals can easily drive output to negative rail limit.
2. **Channel Crosstalk**: Unequal input source impedances alter weighting coefficients.
3. **Phase Inversion**: Remembering output is inverted relative to input sum unless followed by an inverting stage.

---

**Q1: How do you create an averaging amplifier?**
A: Set $R_f = R / N$, where $N$ is the number of inputs, making $V_{\text{out}} = -\frac{V_1 + V_2 + ... + V_N}{N}$.

**Q2: Why do input signals not interfere with each other in a summing amplifier?**
A: Because they all connect to the Virtual Ground node ($0V$), providing complete isolation between input channels.

**Q3: Can DC offset voltages be added to AC signals using a summing amplifier?**
A: Yes, apply AC signal to $V_1$ and DC offset voltage to $V_2$.

**Q4: What is an audio mixer circuit?**
A: A summing amplifier using potentiometers for each input resistor to adjust channel volume levels.

---



---



---



---



---
