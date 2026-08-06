# Comparator

> **Course**: Electronics Basics | **Module**: Operational Amplifiers | **Difficulty**: beginner

---

Comparators compare two analog voltages and output a crisp HIGH or LOW digital signal indicating which input voltage is higher.

---



---

A comparator operates in open-loop mode (no negative feedback). If $V_+ > V_-$, Output goes saturation HIGH ($V_{CC}$). If $V_+ < V_-$, Output goes saturation LOW ($GND$). Hysteresis (positive feedback) is added to prevent output chatter caused by noise near the threshold.

---

Basic Comparator Rule:
V_out = HIGH (VCC) if V_+ > V_-
V_out = LOW  (GND) if V_+ < V_-

Hysteresis Thresholds (Schmitt Trigger):
V_TH_high = Threshold for switching LOW -> HIGH
V_TL_low  = Threshold for switching HIGH -> LOW
V_hysteresis = V_TH_high - V_TL_low

---

### Over-Temperature Threshold Detector using LM393 Comparator

Trigger alarm pin HIGH when NTC thermistor node drops below 1.65V (Reference = 1.65V).

```python
v_ref = 1.65    # Set reference voltage on V_-
v_sensor = 1.40 # Temperature spiked, V_+ drops to 1.40V

if v_sensor > v_ref:
    state = 'NORMAL (0V)'
else:
    state = 'ALARM OVERTEMP (5V)'

print(f'Comparator Output: {state}')
```

---

1. **Omitting Hysteresis on Noisy Signals**: Causes rapid output oscillation ('chattering') when input is near threshold level.
2. **Omitting Pull-Up Resistors on Open-Collector Comparators (LM393)**: Open-collector outputs cannot drive HIGH without an external pull-up resistor to VCC.
3. **Using Slow Standard Op-Amps as Fast Comparators**: Standard op-amps have long saturation recovery times when driven into rails.

---

**Q1: What is a Schmitt Trigger?**
A: A comparator configuration incorporating positive feedback to create hysteresis band for noise immunity.

**Q2: What is an Open-Collector / Open-Drain Comparator Output?**
A: Output stage consisting of an uncommitted internal transistor collector that requires an external pull-up resistor to define the HIGH voltage.

**Q3: What is the main difference between an Op-Amp and a dedicated Comparator IC?**
A: Comparators are optimized for ultra-fast open-loop switching and saturation recovery; op-amps are optimized for linear closed-loop amplification.

**Q4: How do you adjust hysteresis width?**
A: By changing the ratio of the positive feedback resistor to the input resistor.

---



---



---



---



---
