---
id: "09_21"
title: "07 Gerber And Nc Drill File Generation"
course: "PCB Design"
module: 1
module_title: "EDA & PCB Engineering"
lesson: 21
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pcb", "kicad", "eda", "hardware"]
prerequisites: []
lab_required: true
---

# 07 Gerber And Nc Drill File Generation

## Overview of 07 Gerber And Nc Drill File Generation

In this lesson, you will master **07 Gerber And Nc Drill File Generation** in PCB Layout & Electronics Manufacturing.

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

## Lab Exercise
1. Open KiCad EDA, set up net classes for Power (24 mil trace) and Signal (8 mil trace), and run a complete DRC check on a 2-layer board layout.
