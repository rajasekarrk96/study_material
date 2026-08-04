# Op-Amp Basics

> **Course**: Electronics Basics | **Module**: Operational Amplifiers | **Difficulty**: beginner

---

Operational Amplifiers (Op-Amps) are versatile analog building blocks used for signal conditioning, filtering, amplification, and mathematical operations in sensor interfacing.

---



---

An Op-Amp is a high-gain DC-coupled differential amplifier with two inputs: Non-Inverting ($V_+$) and Inverting ($V_-$), and one output ($V_{\text{out}}$). Ideal Op-Amp Golden Rules:
1. **Infinite Input Impedance**: Zero current enters input terminals ($I_+ = I_- = 0$).
2. **Virtual Short**: When negative feedback is applied, the op-amp adjusts output to make $V_+ = V_-$.

---

Op-Amp Open Loop Equation:
V_out = A_OL * (V_+ - V_-)
A_OL = Open-loop gain (typically 100,000+ or 100dB)

Golden Rules for Negative Feedback:
Rule 1: I_+ = 0  and  I_- = 0
Rule 2: V_+ = V_-  (Virtual Short)

---

### Unity Gain Voltage Follower (Buffer) Circuit

Connect Output directly back to Inverting Input ($V_-$). Apply sensor voltage to $V_+$.

```python
# Voltage Follower Buffer Analysis
# V_out = V_+ (Gain = 1.0)
v_sensor = 2.45 # High impedance sensor output
v_out = v_sensor
print(f'Buffered Output Voltage: {v_out:.2f} V')
```

The Buffer provides high input impedance to the sensor and low output impedance to drive the ADC without loading error.

---

1. **Exceeding Op-Amp Input Common-Mode Range**: Operating non-rail-to-rail op-amps near supply rails causes phase reversal or distortion.
2. **Omitting Power Supply Decoupling Capacitors**: Causes parasitic high-frequency self-oscillation.
3. **Ignoring Slew Rate Limits**: High-frequency signals become distorted if required $dV/dt$ exceeds op-amp Slew Rate ($V/\mu s$).

---

**Q1: What is Negative Feedback?**
A: Feeding a portion of the output signal back to the inverting input ($V_-$) to stabilize gain, increase bandwidth, and reduce distortion.

**Q2: What is a Rail-to-Rail Op-Amp?**
A: An op-amp designed so input and output voltage swings can reach the positive and negative power supply rails.

**Q3: What is Gain-Bandwidth Product (GBW)?**
A: Constant product of amplifier gain and cutoff frequency (e.g. 1MHz GBW means Gain=100 has 10kHz bandwidth).

**Q4: What is Input Offset Voltage?**
A: Small differential voltage required between inputs to force output voltage to zero.

---



---



---



---



---
