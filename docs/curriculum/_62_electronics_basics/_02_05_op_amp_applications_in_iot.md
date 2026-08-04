# Op-Amp Applications in IoT

> **Course**: Electronics Basics | **Module**: Operational Amplifiers | **Difficulty**: beginner

---

Op-amps are critical interface bridges in IoT nodes for active filtering, instrumentation amplification, current sensing, and photodiode signal conditioning.

---



---

Real-world IoT sensors produce weak, noisy, high-impedance signals (microvolts to millivolts). Op-amps condition these raw signals through: Instrumentation Amplifiers (differential sensor bridges), Transimpedance Amplifiers (photodiode light sensors), Active Low-Pass Filters (anti-aliasing for ADC), and High-Side Current Shunt Sensing.

---

Instrumentation Amplifier Gain Formula:
Gain = 1 + (2 * R1 / R_gain)

Transimpedance Amplifier (TIA Light Sensor):
V_out = I_photodiode * R_feedback

Active Sallen-Key 2nd Order Low-Pass Cutoff:
f_c = 1 / (2 * π * sqrt(R1 * R2 * C1 * C2))

---

### Transimpedance Amplifier (TIA) Photodiode Sensor Interface

Convert 0-10µA photodiode current into 0-3.3V for ESP32 ADC.

```python
i_photo_max = 10.0e-6  # 10 µA max
v_adc_max = 3.3        # 3.3V

# Calculate TIA Feedback Resistor: Rf = V_out / I_in
r_f = v_adc_max / i_photo_max
print(f'TIA Feedback Resistor: {r_f/1000:.0f} kΩ')
# Output: 330 kΩ
```

---

1. **Aliasing Distortion without Active Anti-Aliasing Filter**: ADC sampling higher frequencies than Nyquist rate distorts readings.
2. **High-Side Current Sensing Common-Mode Range**: Standard op-amps fail when sensing current on 12V rails; use dedicated Current Sense Amplifiers (INA180).
3. **Photodiode Parasitic Capacitance Instability**: Requires small feedback capacitor across $R_f$ to prevent TIA oscillation.

---

**Q1: What is an Instrumentation Amplifier (InAmp)?**
A: An integrated 3-op-amp precision differential amplifier providing high Common-Mode Rejection Ratio (CMRR) and high input impedance for Wheatstone bridges.

**Q2: What is CMRR?**
A: Common-Mode Rejection Ratio — ability of an amplifier to reject identical noise present on both differential inputs.

**Q3: Why is an active filter better than a passive RC filter?**
A: Active filters provide gain, sharper cutoff roll-off slopes (-40dB/dec), and eliminate loading impedance issues.

**Q4: What is Nyquist theorem?**
A: Sampling frequency must be at least 2x the highest signal frequency to prevent aliasing.

---



---



---



---



---
