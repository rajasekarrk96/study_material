# 09 02 Rf Pcb Design Fundamentals

> **Course**: Pcb | **Module**: EDA & PCB Engineering | **Difficulty**: intermediate

---

In this lesson, you will master **09 02 Rf Pcb Design Fundamentals** in PCB Layout & Electronics Manufacturing.

### Key CAD/EDA Engineering Concepts

1. **Layer Stackup & Rules**: Defining trace clearance, via types (through-hole, blind, buried), copper weight (1 oz), and substrate materials (FR4, Rogers).
2. **Schematic to Layout Workflow**:
   - Component footprint association (IPC-7351B standards).
   - Placement optimization for short signal loops and thermal dissipation.
   - DRC (Design Rule Check) validation prior to Gerber export.

```text
IPC-7351 Component Footprint Designation Example:
RES_0603 (1608 Metric) -> L: 1.6mm, W: 0.8mm, Courtyard: +0.25mm
```

---

1. Open KiCad EDA, set up net classes for Power (24 mil trace) and Signal (8 mil trace), and run a complete DRC check on a 2-layer board layout.

---
