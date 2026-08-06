# Series and Parallel Circuits

> **Course**: Electrical Fundamentals | **Module**: Circuit Components | **Difficulty**: beginner

---

Analyzing series and parallel configurations allows engineers to determine equivalent impedance, branch currents, and node voltages across complex hardware systems.

---



---

**Series Circuits**: Components are connected end-to-end in a single path. The identical current flows through every component (I_total = I1 = I2). Voltages add up (V_total = V1 + V2).

**Parallel Circuits**: Components share common top and bottom nodes. The identical voltage exists across every parallel branch (V_total = V1 = V2). Currents add up (I_total = I1 + I2).

---

Series Rules:
R_total = R1 + R2 + R3 + ... + Rn
C_total = 1 / (1/C1 + 1/C2 + ... + 1/Cn)
L_total = L1 + L2 + L3 + ... + Ln

Parallel Rules:
R_total = 1 / (1/R1 + 1/R2 + ... + 1/Rn)
C_total = C1 + C2 + C3 + ... + Cn
L_total = 1 / (1/L1 + 1/L2 + ... + 1/Ln)

Two Parallel Resistors Shortcut:
R_eq = (R1 * R2) / (R1 + R2)

---

### Python Solver for Equivalent Series-Parallel Networks

```python
def parallel(r1, r2):
    return (r1 * r2) / (r1 + r2)

# Circuit: R1 (100Ω) in series with parallel pair [R2(200Ω) || R3(200Ω)]
r1 = 100.0
r2 = 200.0
r3 = 200.0

r_p = parallel(r2, r3)     # 200 || 200 = 100Ω
r_eq = r1 + r_p            # 100 + 100 = 200Ω

print(f'Parallel Pair R2||R3: {r_p:.1f} Ω')
print(f'Total Equivalent Resistance: {r_eq:.1f} Ω')
```

---

1. **Connecting Batteries of Different Voltages in Parallel**: Causes massive recirculating current between cells, leading to thermal runaway or fire.
2. **Series Component Failure Impact**: An open failure in a series branch halts the entire circuit; in parallel, remaining branches stay powered.
3. **Assuming Equal Current in Parallel LEDs**: Variations in LED forward voltages cause current hogging in the lowest Vf LED.

---

**Q1: If four 100Ω resistors are connected in parallel, what is the total equivalent resistance?**
A: R_eq = 100 / 4 = 25Ω.

**Q2: What happens if one light bulb fails open in a series Christmas light string?**
A: All lights turn off because the current path is broken.

**Q3: Are home electrical outlets wired in series or parallel?**
A: Parallel, so each appliance receives full 120V/230V mains voltage independently.

**Q4: How do you double battery voltage while keeping capacity the same?**
A: Connect two identical batteries in series.

---

**Q1: If four 100Ω resistors are connected in parallel, what is the total equivalent resistance?**
A: R_eq = 100 / 4 = 25Ω.

**Q2: What happens if one light bulb fails open in a series Christmas light string?**
A: All lights turn off because the current path is broken.

**Q3: Are home electrical outlets wired in series or parallel?**
A: Parallel, so each appliance receives full 120V/230V mains voltage independently.

**Q4: How do you double battery voltage while keeping capacity the same?**
A: Connect two identical batteries in series.

---



---



---



---



---
