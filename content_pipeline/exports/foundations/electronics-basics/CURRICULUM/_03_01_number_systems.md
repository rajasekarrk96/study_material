# Number Systems

> **Course**: Electronics Basics | **Module**: Digital Electronics | **Difficulty**: beginner

---

Binary (Base-2), Hexadecimal (Base-16), and Decimal (Base-10) are the core numerical representations used in microcontrollers, memory addresses, and bitwise operations.

---



---

Computers operate exclusively on Binary digits (Bits: 0 and 1) representing low and high voltages. Hexadecimal groups 4 binary bits (a Nibble) into a single compact character (0-9, A-F), simplifying memory address reading and register configuration.

---

Base Systems:
Binary (0b)       : Base 2  [Digits: 0, 1]
Decimal           : Base 10 [Digits: 0-9]
Hexadecimal (0x)   : Base 16 [Digits: 0-9, A, B, C, D, E, F]

Byte & Bit Sizes:
1 Bit = 0 or 1
1 Nibble = 4 Bits  (e.g. 0b1010 = 0xA)
1 Byte = 8 Bits    (Range: 0 - 255 Unsigned / -128 to +127 Signed 2's Comp)
1 Word = 16 Bits or 32 Bits (MCU Architecture dependent)

---

### Python Number Base Conversions & Bitwise Operations

```python
value = 0x3A # Hexadecimal 0x3A

dec_val = int(value)
bin_val = bin(value)
hex_val = hex(value)

print(f'Decimal: {dec_val}')     # 58
print(f'Binary: {bin_val}')       # 0b111010
print(f'Hex: {hex_val}')         # 0x3a
```

---

1. **Signed Integer Overflow in 2's Complement**: Incrementing +127 in signed 8-bit int flips bit 7, yielding -128.
2. **Endianness Confusion**: Little-Endian (ARM Cortex-M) stores least-significant byte first in memory; Big-Endian stores most-significant byte first.
3. **Off-by-One Bit Shifts**: Shifting bits beyond data type width causes silent truncation.

---

**Q1: How do you represent negative numbers in binary?**
A: Using Two's Complement: Invert all bits (1's complement) and add 1.

**Q2: What is 0xFF in decimal?**
A: 255 (Max unsigned 8-bit value).

**Q3: How many hex digits represent a 32-bit register?**
A: 8 hex digits (e.g. `0x40021000`).

**Q4: What is ASCII?**
A: 7-bit/8-bit binary code mapping numbers 0-127 to printable characters.

---



---



---



---



---
