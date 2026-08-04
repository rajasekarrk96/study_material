# Logic Gates

> **Course**: Electronics Basics | **Module**: Digital Electronics | **Difficulty**: beginner

---

Logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR) are the primitive digital building blocks executing Boolean logic in silicon.

---



---

Logic gates process high (1 / VCC) and low (0 / GND) voltage states. NAND and NOR are Universal Gates because any arbitrary Boolean logic function can be constructed using exclusively NAND or NOR gates.

---

Truth Tables Summary:
AND  : Y = A • B       (HIGH only if A=1 AND B=1)
OR   : Y = A + B       (HIGH if A=1 OR B=1)
NOT  : Y = Ā           (Inverts input)
NAND : Y = NOT(A • B)  (LOW only if A=1 AND B=1)
NOR  : Y = NOT(A + B)  (HIGH only if A=0 AND B=0)
XOR  : Y = A ⊕ B       (HIGH if inputs are DIFFERENT)
XNOR : Y = NOT(A ⊕ B)  (HIGH if inputs are IDENTICAL)

---

### Python Bitwise Operations Equivalent to Logic Gates

```python
a = 0b1100
b = 0b1010

print(f'AND : {bin(a & b)}')  # 0b1000
print(f'OR  : {bin(a | b)}')  # 0b1110
print(f'XOR : {bin(a ^ b)}')  # 0b0110
print(f'NOT : {bin(~a & 0xF)}') # 0b0011
```

---

1. **Leaving CMOS Logic Gate Inputs Unconnected**: Unused CMOS gate inputs float, pick up EMI noise, and cause high shoot-through supply current.
2. **Confusing Bitwise (&, |) with Logical (&&, ||) Operators in C**: Bitwise evaluates bit-by-bit; logical evaluates truthiness of entire expression.
3. **Propagation Delay Accumulation**: Chaining many gate stages introduces propagation delay skew in high-speed clocks.

---

**Q1: Why are NAND gates called universal gates?**
A: Because AND, OR, NOT, and XOR functions can all be implemented using combinations of NAND gates.

**Q2: What is the XOR gate used for in digital arithmetic?**
A: XOR performs binary addition without carry (Sum output of Half Adder).

**Q3: What should you do with unused inputs on a 74HC00 NAND chip?**
A: Tie unused input pins to VCC or GND.

**Q4: What is De Morgan's Law?**
A: $\overline{A \cdot B} = \bar{A} + \bar{B}$ and $\overline{A + B} = \bar{A} \cdot \bar{B}$.

---



---



---



---



---
