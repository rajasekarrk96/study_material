# Kirchhoffs Laws

> **Course**: Electrical Fundamentals | **Module**: Basic Electrical Theory | **Difficulty**: beginner

---

Kirchhoff's Current Law (KCL) and Kirchhoff's Voltage Law (KVL) allow complete mathematical analysis of complex electrical circuits with multiple branches, loops, and power sources.

---



---

**Kirchhoff's Current Law (KCL)**: Based on the Conservation of Charge, KCL states that the algebraic sum of currents entering any circuit node (junction) must equal zero. Total Current In = Total Current Out.

**Kirchhoff's Voltage Law (KVL)**: Based on the Conservation of Energy, KVL states that the directed sum of electrical potential differences (voltages) around any closed loop in a circuit must equal zero. Sum of Voltage Rises = Sum of Voltage Drops.

---

KCL Math Expression:
∑ I_in = ∑ I_out     or     ∑ I_k = 0 at any node

KVL Math Expression:
∑ V_source = ∑ V_drop  or   ∑ V_k = 0 around any closed loop

Loop Rule Signs:
- Moving from (-) to (+) through a source = Voltage Rise (+V)
- Moving in the direction of current through a resistor = Voltage Drop (-I*R)

---

### Solving a Dual-Resistor Branch with KCL & KVL

Consider a 12V DC source connected to two parallel branches (R1 = 100Ω, R2 = 200Ω).

```python
# KCL Parallel Calculation
v_source = 12.0
r1 = 100.0
r2 = 200.0

# Current through Branch 1 (KVL on Loop 1)
i1 = v_source / r1  # 12 / 100 = 0.12 A

# Current through Branch 2 (KVL on Loop 2)
i2 = v_source / r2  # 12 / 200 = 0.06 A

# KCL at main node: Total Current = I1 + I2
i_total = i1 + i2

print(f'Branch 1 Current: {i1*1000:.1f} mA')
print(f'Branch 2 Current: {i2*1000:.1f} mA')
print(f'Total Source Current (KCL): {i_total*1000:.1f} mA')
```

---

1. **Incorrect Sign Conventions in KVL Loops**: Assigning wrong polarities to voltage drops during loop equations leads to incorrect sign results.
2. **Applying KCL at Non-Independent Nodes**: Writing KCL equations at reference (ground) nodes duplicates existing equations without adding new information.
3. **Ignoring Internal Resistance of Sources**: Real power supplies drop voltage under load due to internal impedance.

---

**Q1: What fundamental law of physics is KCL based on?**
A: KCL is based on the Law of Conservation of Electric Charge.

**Q2: What physical law forms the basis of KVL?**
A: KVL is based on the Law of Conservation of Energy.

**Q3: How many independent KVL equations can be written in a circuit with B branches and N nodes?**
A: Number of independent loops = B - N + 1.

**Q4: Can KCL be applied to high-frequency AC circuits?**
A: At extremely high frequencies where component sizes approach signal wavelengths, parasitic capacitance requires localized field calculations, but lump-element KCL applies across standard PCB design frequencies.

---



---



---



---



---
