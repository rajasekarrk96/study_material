# Sequential Circuits

> **Course**: Electronics Basics | **Module**: Digital Electronics | **Difficulty**: beginner

---

Sequential logic incorporates memory elements (Flip-Flops, Latches) where outputs depend on current inputs and past state history, driven by clock pulses.

---



---

Unlike combinational logic, sequential circuits store state using memory elements. Flip-Flops (D-Type, JK, T) update output state on clock edges (Rising/Falling). Registers, Counters, and Shift Registers (74HC595) are fundamental sequential blocks.

---

D Flip-Flop Characteristic:
Q(next) = D  (sampled on Clock Edge)

T Flip-Flop (Toggle / Frequency Divider):
Q(next) = Q' if T=1 on Clock Edge (Divides frequency by 2)

74HC595 Shift Register Pins:
DS    : Serial Data Input
SHCP  : Shift Register Clock
STCP  : Storage Latch Clock
Q0-Q7 : 8 Parallel Outputs

---

### Bit-Banging 8-Bit Data to 74HC595 Shift Register

```python
# Python simulation of 74HC595 Shift Register
def shift_out(data_byte):
    parallel_pins = [0] * 8
    for bit in range(8):
        # Extract MSB first
        bit_val = (data_byte >> (7 - bit)) & 1
        parallel_pins[bit] = bit_val
    return parallel_pins

pins = shift_out(0b10110001)
print(f'Parallel Outputs Q7..Q0: {pins}')
```

---

1. **Violating Setup and Hold Times**: Changing D input too close to clock edge causes **Metastability** (unpredictable floating state).
2. **Clock Jitter / Bouncing Clocks**: Mechanical switch noise on clock pins causes multiple unwanted flip-flop triggers.
3. **Asynchronous Reset Hazards**: Glitches on asynchronous Clear/Reset lines unintentionally wipe registers.

---

**Q1: What is the difference between a Latch and a Flip-Flop?**
A: A Latch is level-triggered (transparent when EN is high); a Flip-Flop is edge-triggered (samples on clock transition).

**Q2: What is Metastability?**
A: Hazardous state where flip-flop output hovers in an invalid intermediate voltage between 0 and 1 when setup/hold time is violated.

**Q3: How does a 74HC595 shift register expand MCU GPIO pins?**
A: Uses 3 MCU pins (Data, Clock, Latch) to drive 8 or more parallel outputs.

**Q4: How do you construct a divide-by-2 frequency counter?**
A: Connect Q-bar back to D input on a D Flip-Flop.

---



---



---



---



---
