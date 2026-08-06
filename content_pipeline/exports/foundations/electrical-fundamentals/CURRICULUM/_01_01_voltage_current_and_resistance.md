# Voltage Current and Resistance

> **Course**: Electrical Fundamentals | **Module**: Basic Electrical Theory | **Difficulty**: beginner

---

Voltage, current, and resistance form the foundational trilogy of electrical engineering and embedded system design. Understanding these parameters is essential for power supply design, sensor reading, component selection, and debugging hardware circuits in IoT projects.

---



---

Think of electricity as water flowing through a pipe network. Voltage is equivalent to water pressure pushed by a pump — it represents the electrical potential difference between two points that forces charges to move. Current is the rate of flow of water (electric charge) passing a specific cross-section per second, measured in Amperes (A). Resistance is the constriction in the pipe restricting water flow, measured in Ohms (Ω). In electrical systems, electrons move through conductors (like copper wires) when a voltage potential exists across them. The magnitude of this electron flow is directly limited by the physical resistance of the material and components in the path.

---

Electrical Quantities & Standard Units:

Voltage (V or U)   : Measured in Volts (V)      [1 V = 1 Joule / Coulomb]
Current (I)        : Measured in Amperes (A)    [1 A = 1 Coulomb / second = 6.242 x 10^18 electrons/sec]
Resistance (R)     : Measured in Ohms (Ω)       [1 Ω = 1 Volt / Ampere]

Key Prefixes in Embedded Systems:
1 kV  = 1,000 V         (High voltage power grids)
1 mV  = 0.001 V         (Sensor analog outputs, e.g. thermocouples)
1 mA  = 0.001 A         (Microcontroller GPIO output current ~20mA max)
1 µA  = 0.000001 A      (ESP32 deep sleep current ~10µA)
1 kΩ  = 1,000 Ω         (Standard pull-up resistor value)
1 MΩ  = 1,000,000 Ω     (High-impedance ADC input rating)

---

### Calculating LED Current Draw on a 3.3V Microcontroller

Suppose an ESP32 GPIO pin provides 3.3V to illuminate a standard Red LED (forward voltage drop Vf = 2.0V) using a 220Ω current-limiting resistor.

```python
# Python calculation of LED Current
v_supply = 3.3   # Supply voltage from GPIO pin (Volts)
v_led = 2.0      # Red LED forward voltage drop (Volts)
r_resistor = 220 # Resistor value (Ohms)

# Voltage drop across the resistor
v_resistor = v_supply - v_led

# Calculate current using Ohm's Law: I = V / R
current_amps = v_resistor / r_resistor
current_ma = current_amps * 1000

print(f'Voltage across resistor: {v_resistor:.2f} V')
print(f'Current through LED: {current_ma:.2f} mA')
# Output: Voltage across resistor: 1.30 V, Current through LED: 5.91 mA
```

Since 5.91 mA is safely below the maximum rated GPIO sourcing limit of 12 mA for the ESP32, this design operates reliably.

---

1. **Omitting Current-Limiting Resistors on LEDs**: Connecting an LED directly across a voltage source causes near-zero resistance, drawing destructive current that immediately burns out the LED and GPIO pin.
2. **Confusing Voltage Drop with Supply Voltage**: Measuring voltage relative to the wrong reference point (not System Ground) gives misleading floating readings.
3. **Exceeding Microcontroller Pins Current Limits**: Drawing more than 12-20mA directly from a single MCU GPIO pin causes thermal degradation and silicon failure.

---

**Q1: What is the physical difference between Voltage and Current?**
A: Voltage is the potential energy per unit charge driving the movement, while current is the actual flow rate of charges moving through the circuit.

**Q2: Why does an open circuit have voltage but zero current?**
A: An open circuit has infinite air resistance between terminals. The electrical potential difference (voltage) remains present, but no charge can flow across the air gap.

**Q3: What current level is considered dangerous to humans?**
A: Currents as low as 10 mA AC can cause muscle contractions, and currents above 100 mA through the heart are potentially fatal.

**Q4: How do multimeter probes need to be connected to measure voltage vs current?**
A: Voltage is measured in PARALLEL across a component without breaking the circuit. Current must be measured in SERIES by breaking the circuit so all current passes through the meter.

---



---



---



---



---
