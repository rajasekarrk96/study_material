# Safety and ESD

> **Course**: Electrical Fundamentals | **Module**: Practical Electrical Skills | **Difficulty**: beginner

---

Electrostatic Discharge (ESD) and high voltage safety procedures prevent destructive silicon damage and protect engineers against electrical hazards.

---



---

**Electrostatic Discharge (ESD)**: Sudden transfer of static charge accumulated on human skin (up to 15,000V) to delicate microchips, rupturing microscopic MOSFET gate oxides.

**Electrical Safety**: High voltage (>50V DC / 30V AC) can overcome human skin resistance and cause fatal electric shock or ventricular fibrillation.

---

ESD Protection Controls:
- Anti-Static Wrist Strap : 1MΩ series resistor to Earth Ground
- ESD Mat                 : Static dissipative surface (10^6 - 10^9 Ω/sq)
- ESD Packaging           : Shielding bags (Faraday cage effect) for MOSFETs/ICs

Voltage Safety Limits:
Safe Low Voltage (SELV)  : < 50V AC RMS, < 120V Ripple-Free DC
Hazardous Voltage        : > 50V AC / 120V DC (Requires insulation, barriers, fused probes)

---

### Setting Up an ESD-Safe Workstation

1. Spread a dissipative ESD mat over the workbench.
2. Attach the ESD mat grounding cord to mains Earth Ground or dedicated bench ground point.
3. Wear a conductive wrist strap connected via a **1MΩ safety resistor** to the mat ground.
4. Store sensitive microcontrollers (ESP32, STM32, CMOS sensors) inside metallic ESD shielding bags when not in use.

---

1. **Direct Grounding Wrist Straps Without a 1MΩ Resistor**: Creates a dangerous direct path to ground if the engineer touches a live wire!
2. **Latent ESD Damage**: Sub-lethal ESD zaps weaken gate oxide without immediate failure, causing unexplainable crashes weeks later in production.
3. **Working on Mains AC Power with Both Hands**: Current can flow through one arm across the heart to the other arm.

---

**Q1: Why is there a 1MΩ resistor inside anti-static wrist straps?**
A: It slowly bleeds off static charges safely while protecting the human from high-current shock if they accidentally touch a live voltage source.

**Q2: What is Latent ESD Defect?**
A: Damage where a component functions initial factory testing but fails prematurely during field operation due to static stress.

**Q3: Which electronic components are most sensitive to ESD?**
A: MOSFETs, CMOS microcontrollers, high-speed RAM, and RF amplifiers.

**Q4: What is the 'One-Hand Rule' in high voltage work?**
A: Keep one hand in your pocket when testing live high-voltage circuits to prevent current passing through your chest between both arms.

---

**Q1: Why is there a 1MΩ resistor inside anti-static wrist straps?**
A: It slowly bleeds off static charges safely while protecting the human from high-current shock if they accidentally touch a live voltage source.

**Q2: What is Latent ESD Defect?**
A: Damage where a component functions initial factory testing but fails prematurely during field operation due to static stress.

**Q3: Which electronic components are most sensitive to ESD?**
A: MOSFETs, CMOS microcontrollers, high-speed RAM, and RF amplifiers.

**Q4: What is the 'One-Hand Rule' in high voltage work?**
A: Keep one hand in your pocket when testing live high-voltage circuits to prevent current passing through your chest between both arms.

---



---



---



---



---
