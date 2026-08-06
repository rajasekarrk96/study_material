# Signal Conditioning

> **Course**: Electronics Basics | **Module**: Practical Electronics | **Difficulty**: beginner

---

Signal conditioning modifies raw sensor signals through filtering, amplification, attenuation, and isolation to match microcontroller ADC sampling requirements.

---



---

Real-world sensor signals are often noisy, weak, offset from 0V, or contain unwanted high-frequency interference. Signal conditioning stages:
1. Attenuation / Level Shifting
2. Low-Pass RC / Active Filtering
3. Amplification (Op-Amp)
4. Galvanic Isolation (Optocoupler)

---

RC Passive Low-Pass Filter:
f_cutoff = 1 / (2 * π * R * C)
Attenuation at f > f_c = -20 dB/decade

Optocoupler Galvanic Isolation:
Input : LED (Current limited by R_in)
Output: Phototransistor (Completely electrically isolated from input)

---

### Python Simulation of RC Low-Pass Filter on Noisy ADC Data

```python
# Exponential Moving Average (Digital Software RC Filter)
def rc_filter(new_sample, prev_output, alpha=0.1):
    return (alpha * new_sample) + ((1.0 - alpha) * prev_output)

filtered_val = 0.0
raw_samples = [1.2, 3.5, 1.3, 1.4, 1.2, 4.0, 1.3] # Spikes at index 1 and 5

for sample in raw_samples:
    filtered_val = rc_filter(sample, filtered_val)
    print(f'Raw: {sample:.1f}V -> Filtered: {filtered_val:.2f}V')
```

---

1. **Impedance Mismatching Between Filter and ADC**: Low ADC input resistance shifts passive RC filter cutoff frequency.
2. **Omitting Anti-Aliasing Filter Before ADC**: High frequency noise folds back into measurement band as false low-frequency signals.
3. **Ignoring Optocoupler CTR (Current Transfer Ratio)**: CTR drops over age and temperature, causing incomplete switching.

---

**Q1: What is Galvanic Isolation?**
A: Complete electrical separation between two circuits (no shared ground/DC path), preventing high-voltage ground loops and safety hazards.

**Q2: What is an Optocoupler (Optoisolator)?**
A: Component using light (internal LED and phototransistor) to transfer signals across an isolation barrier.

**Q3: What is the purpose of an anti-aliasing filter?**
A: Low-pass filter removing frequencies above half the ADC sampling rate (Nyquist frequency).

**Q4: How do you convert a 4-20mA industrial current loop sensor to 0-3.3V for MCU ADC?**
A: Pass 4-20mA current through a precision 165Ω resistor ($V = 0.020A \times 165\Omega = 3.3V$ max).

---



---



---



---



---
