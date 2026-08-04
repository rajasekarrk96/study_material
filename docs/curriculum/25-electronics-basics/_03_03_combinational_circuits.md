# Combinational Circuits

> **Course**: Electronics Basics | **Module**: Digital Electronics | **Difficulty**: beginner

---

Combinational logic circuits compute outputs based purely on current inputs without memory (e.g. Multiplexers, Decoders, Adders).

---



---

In combinational logic, output state depends strictly on instant input combinations. Key ICs:
- **Multiplexer (MUX)**: Selects 1 of $N$ input channels to route to a single output using $S$ select lines.
- **Decoder / Demultiplexer**: Converts binary code into single active output line.
- **Adder**: Performs binary addition (Half Adder & Full Adder).

---

Multiplexer 4-to-1 Equation:
Y = (I0 • S1' • S0') + (I1 • S1' • S0) + (I2 • S1 • S0') + (I3 • S1 • S0)

Full Adder Equations:
Sum   = A ⊕ B ⊕ C_in
C_out = (A • B) + (C_in • (A ⊕ B))

---

### Expanding Microcontroller Analog Inputs using CD74HC4067 16-Channel Analog MUX

```python
# Select Analog Channel 9 (Binary 1001) using 4 GPIO Select Pins (S0-S3)
channel = 9
s0 = (channel >> 0) & 1 # 1
s1 = (channel >> 1) & 1 # 0
s2 = (channel >> 2) & 1 # 0
s3 = (channel >> 3) & 1 # 1

print(f'Select Pins [S3 S2 S1 S0] = [{s3} {s2} {s1} {s0}]')
# Set MCU GPIOs to 1, 0, 0, 1 to read Channel 9 on single ADC pin
```

---

1. **Glitching (Glitches/Race Conditions)**: Temporary incorrect output spikes occurring when inputs transition due to unequal gate delays.
2. **Analog MUX On-Resistance ($R_{on}$)**: Analog multiplexers introduce internal resistance (~70Ω) affecting analog readings.
3. **Exceeding MUX Voltage Range**: Passing negative or overvoltage signals through 74HC4067 MUX clamps/distorts signals.

---

**Q1: What is the difference between a Multiplexer and Demultiplexer?**
A: MUX routes multiple inputs to 1 output; DEMUX routes 1 input to multiple outputs.

**Q2: How many select lines does an 8-to-1 MUX require?**
A: 3 select lines ($2^3 = 8$).

**Q3: What is a Priority Encoder?**
A: Encoder that outputs binary code of highest-priority active input line.

**Q4: What is a BCD to 7-Segment Decoder?**
A: IC (e.g. 74HC4511) converting 4-bit binary coded decimal into 7 segment outputs for LED displays.

---



---



---



---



---
