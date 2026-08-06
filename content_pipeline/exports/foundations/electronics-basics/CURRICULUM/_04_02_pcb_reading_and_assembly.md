# PCB Reading and Assembly

> **Course**: Electronics Basics | **Module**: Practical Electronics | **Difficulty**: beginner

---

Printed Circuit Board (PCB) assembly converts schematics into physical hardware products using copper traces, surface-mount (SMD), and through-hole (THD) components.

---



---

A PCB consists of FR4 fiberglass substrate layered with copper traces (typically 1 oz/sq.ft = 35µm thickness). Silkscreen prints component reference designators and pin 1 indicators. Solder mask covers non-soldered copper to prevent short circuits.

---

PCB Layer Breakdown:
Copper Layers     : Top / Bottom / Inner (Signal, Power, GND Planes)
Solder Mask       : Protective green/black/blue polymer coating
Silkscreen        : White text layer (R1, C1, U1, pin numbers, logos)
Vias              : Plated holes connecting traces across different layers
Component Types   : THD (Through-Hole Device) vs SMD/SMT (Surface Mount)

---

### Assembly Order Checklist for Populating PCBA

1. Inspection: Verify PCB for shorts/opens using schematic netlist.
2. Lowest Height Components First: Solder SMD resistors, capacitors, and diodes.
3. Medium Components: Solder ICs, transistors, and small modules.
4. Tallest Components Last: Solder electrolytic caps, connectors, terminal blocks, headers.
5. Post-Assembly Cleanup & Visual Inspection under microscope.

---

1. **Reverse IC Orientation**: Aligning Pin 1 dot/notch incorrectly damages IC upon power-up.
2. **Tombstoning in SMD Reflow**: Unequal thermal mass or solder paste application causes SMD chip resistor to lift vertically on one pad.
3. **Insufficient Thermal Relief Nets on Ground Plane**: Soldering pads connected to large ground planes without thermal relief spokes dissipates heat into board faster than iron can supply.

---

**Q1: How is Pin 1 identified on an IC chip?**
A: Identified by a small circular dot mark near Pin 1 or a U-shaped notch at top of IC package.

**Q2: What is a Via?**
A: A copper-plated hole drilled through PCB layers to electrically route signals between layers.

**Q3: What is thermal relief on PCB pads?**
A: Pattern connecting a pad to a copper plane using narrow spokes to prevent heat sinking during soldering.

**Q4: What is FR4?**
A: Standard flame-retardant glass-reinforced epoxy laminate material used as PCB substrate.

---



---



---



---



---
