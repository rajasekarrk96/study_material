"""
generate_electrical_content_direct.py
======================================
Direct content generator for Electrical Fundamentals course.
Populates high-quality technical markdown content across all 15 lessons and published status.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

ELECTRICAL_LESSON_CONTENT = {

    # ── MODULE 1: Basic Electrical Theory ──────────────────────────────────────
    "voltage-current-and-resistance": {
        "overview": (
            "Voltage, current, and resistance form the foundational trilogy of electrical engineering and embedded system design. "
            "Understanding these parameters is essential for power supply design, sensor reading, component selection, and debugging hardware circuits in IoT projects."
        ),
        "concept": (
            "Think of electricity as water flowing through a pipe network. Voltage is equivalent to water pressure pushed by a pump — it represents the electrical potential difference between two points that forces charges to move. "
            "Current is the rate of flow of water (electric charge) passing a specific cross-section per second, measured in Amperes (A). "
            "Resistance is the constriction in the pipe restricting water flow, measured in Ohms (Ω). "
            "In electrical systems, electrons move through conductors (like copper wires) when a voltage potential exists across them. The magnitude of this electron flow is directly limited by the physical resistance of the material and components in the path."
        ),
        "syntax": (
            "Electrical Quantities & Standard Units:\n\n"
            "Voltage (V or U)   : Measured in Volts (V)      [1 V = 1 Joule / Coulomb]\n"
            "Current (I)        : Measured in Amperes (A)    [1 A = 1 Coulomb / second = 6.242 x 10^18 electrons/sec]\n"
            "Resistance (R)     : Measured in Ohms (Ω)       [1 Ω = 1 Volt / Ampere]\n\n"
            "Key Prefixes in Embedded Systems:\n"
            "1 kV  = 1,000 V         (High voltage power grids)\n"
            "1 mV  = 0.001 V         (Sensor analog outputs, e.g. thermocouples)\n"
            "1 mA  = 0.001 A         (Microcontroller GPIO output current ~20mA max)\n"
            "1 µA  = 0.000001 A      (ESP32 deep sleep current ~10µA)\n"
            "1 kΩ  = 1,000 Ω         (Standard pull-up resistor value)\n"
            "1 MΩ  = 1,000,000 Ω     (High-impedance ADC input rating)"
        ),
        "example": (
            "### Calculating LED Current Draw on a 3.3V Microcontroller\n\n"
            "Suppose an ESP32 GPIO pin provides 3.3V to illuminate a standard Red LED (forward voltage drop Vf = 2.0V) using a 220Ω current-limiting resistor.\n\n"
            "```python\n"
            "# Python calculation of LED Current\n"
            "v_supply = 3.3   # Supply voltage from GPIO pin (Volts)\n"
            "v_led = 2.0      # Red LED forward voltage drop (Volts)\n"
            "r_resistor = 220 # Resistor value (Ohms)\n\n"
            "# Voltage drop across the resistor\n"
            "v_resistor = v_supply - v_led\n\n"
            "# Calculate current using Ohm's Law: I = V / R\n"
            "current_amps = v_resistor / r_resistor\n"
            "current_ma = current_amps * 1000\n\n"
            "print(f'Voltage across resistor: {v_resistor:.2f} V')\n"
            "print(f'Current through LED: {current_ma:.2f} mA')\n"
            "# Output: Voltage across resistor: 1.30 V, Current through LED: 5.91 mA\n"
            "```\n\n"
            "Since 5.91 mA is safely below the maximum rated GPIO sourcing limit of 12 mA for the ESP32, this design operates reliably."
        ),
        "pitfall": (
            "1. **Omitting Current-Limiting Resistors on LEDs**: Connecting an LED directly across a voltage source causes near-zero resistance, drawing destructive current that immediately burns out the LED and GPIO pin.\n"
            "2. **Confusing Voltage Drop with Supply Voltage**: Measuring voltage relative to the wrong reference point (not System Ground) gives misleading floating readings.\n"
            "3. **Exceeding Microcontroller Pins Current Limits**: Drawing more than 12-20mA directly from a single MCU GPIO pin causes thermal degradation and silicon failure."
        ),
        "qa": (
            "**Q1: What is the physical difference between Voltage and Current?**\n"
            "A: Voltage is the potential energy per unit charge driving the movement, while current is the actual flow rate of charges moving through the circuit.\n\n"
            "**Q2: Why does an open circuit have voltage but zero current?**\n"
            "A: An open circuit has infinite air resistance between terminals. The electrical potential difference (voltage) remains present, but no charge can flow across the air gap.\n\n"
            "**Q3: What current level is considered dangerous to humans?**\n"
            "A: Currents as low as 10 mA AC can cause muscle contractions, and currents above 100 mA through the heart are potentially fatal.\n\n"
            "**Q4: How do multimeter probes need to be connected to measure voltage vs current?**\n"
            "A: Voltage is measured in PARALLEL across a component without breaking the circuit. Current must be measured in SERIES by breaking the circuit so all current passes through the meter."
        )
    },

    "ohms-law": {
        "overview": (
            "Ohm's Law is the fundamental equation linking voltage, current, and resistance (V = I * R). "
            "It is used continuously when calculating resistor values, sensor biasing, power dissipation, and current draw in hardware engineering."
        ),
        "concept": (
            "Discovered by Georg Simon Ohm in 1827, Ohm's Law states that the current flowing through a linear conductor between two points is directly proportional to the voltage across the two points and inversely proportional to the resistance between them. "
            "If you double the voltage across a fixed resistor, the current doubles. If you double the resistance while keeping voltage constant, the current drops in half."
        ),
        "syntax": (
            "Ohm's Law Equations & Variants:\n\n"
            "Primary Formula : V = I * R    [Voltage = Current x Resistance]\n"
            "Current Formula : I = V / R    [Current = Voltage / Resistance]\n"
            "Resistance Form : R = V / I    [Resistance = Voltage / Current]\n\n"
            "Power Triad (Joules Heating):\n"
            "P = V * I                      [Power (Watts) = Voltage x Current]\n"
            "P = I^2 * R                    [Power = Current squared x Resistance]\n"
            "P = V^2 / R                    [Power = Voltage squared / Resistance]"
        ),
        "example": (
            "### Designing a Pull-Up Resistor for a Digital Sensor Button\n\n"
            "To prevent a floating input on a 5V microcontroller input pin, we install a pull-up resistor connected to 5V. When the button is pressed, it shorts the pin directly to Ground (0V).\n\n"
            "```python\n"
            "# Calculate power dissipation when button is pressed with a 10k ohm pull-up\n"
            "v_cc = 5.0          # Operating Voltage (Volts)\n"
            "r_pullup = 10000.0  # 10 kΩ Resistor\n\n"
            "# Current when button is shorted to GND\n"
            "i_pressed = v_cc / r_pullup  # 5.0 / 10000 = 0.0005 A (0.5 mA)\n\n"
            "# Power dissipated by resistor as heat\n"
            "p_resistor = (v_cc ** 2) / r_pullup # 25 / 10000 = 0.0025 W (2.5 mW)\n\n"
            "print(f'Current during press: {i_pressed * 1000:.2f} mA')\n"
            "print(f'Power dissipated: {p_resistor * 1000:.2f} mW')\n"
            "```\n\n"
            "A standard 1/4-Watt (250 mW) resistor dissipates 2.5 mW easily without overheating."
        ),
        "pitfall": (
            "1. **Ignoring Resistor Power Ratings**: Using a 1/4W resistor in a circuit that dissipates 1W will cause the resistor to burn and potentially ignite.\n"
            "2. **Assuming Non-linear Devices Obey Ohm's Law Directly**: Diodes, LEDs, and transistors are non-ohmic components; their dynamic resistance changes non-linearly with applied voltage.\n"
            "3. **Temperature Coefficient Neglect**: High current causes heating, which increases conductor resistance and alters operating parameters."
        ),
        "qa": (
            "**Q1: If a 1kΩ resistor has 10V across it, how much current flows?**\n"
            "A: Using I = V / R, I = 10V / 1000Ω = 0.01A = 10mA.\n\n"
            "**Q2: What happens to power dissipation if you double the current through a resistor?**\n"
            "A: Because P = I^2 * R, doubling the current quadruples (4x) the thermal power dissipation.\n\n"
            "**Q3: Are all materials subject to Ohm's Law?**\n"
            "A: No. Metals and carbon resistors are ohmic. Semiconductor junctions (diodes, transistors, gas discharge tubes) are non-ohmic.\n\n"
            "**Q4: How do you pick the power rating for a resistor?**\n"
            "A: Calculate calculated dissipation (P = I^2 * R) and select a resistor rated for at least twice that value for safety derating."
        )
    },

    "kirchhoffs-laws": {
        "overview": (
            "Kirchhoff's Current Law (KCL) and Kirchhoff's Voltage Law (KVL) allow complete mathematical analysis of complex electrical circuits with multiple branches, loops, and power sources."
        ),
        "concept": (
            "**Kirchhoff's Current Law (KCL)**: Based on the Conservation of Charge, KCL states that the algebraic sum of currents entering any circuit node (junction) must equal zero. Total Current In = Total Current Out.\n\n"
            "**Kirchhoff's Voltage Law (KVL)**: Based on the Conservation of Energy, KVL states that the directed sum of electrical potential differences (voltages) around any closed loop in a circuit must equal zero. Sum of Voltage Rises = Sum of Voltage Drops."
        ),
        "syntax": (
            "KCL Math Expression:\n"
            "∑ I_in = ∑ I_out     or     ∑ I_k = 0 at any node\n\n"
            "KVL Math Expression:\n"
            "∑ V_source = ∑ V_drop  or   ∑ V_k = 0 around any closed loop\n\n"
            "Loop Rule Signs:\n"
            "- Moving from (-) to (+) through a source = Voltage Rise (+V)\n"
            "- Moving in the direction of current through a resistor = Voltage Drop (-I*R)"
        ),
        "example": (
            "### Solving a Dual-Resistor Branch with KCL & KVL\n\n"
            "Consider a 12V DC source connected to two parallel branches (R1 = 100Ω, R2 = 200Ω).\n\n"
            "```python\n"
            "# KCL Parallel Calculation\n"
            "v_source = 12.0\n"
            "r1 = 100.0\n"
            "r2 = 200.0\n\n"
            "# Current through Branch 1 (KVL on Loop 1)\n"
            "i1 = v_source / r1  # 12 / 100 = 0.12 A\n\n"
            "# Current through Branch 2 (KVL on Loop 2)\n"
            "i2 = v_source / r2  # 12 / 200 = 0.06 A\n\n"
            "# KCL at main node: Total Current = I1 + I2\n"
            "i_total = i1 + i2\n\n"
            "print(f'Branch 1 Current: {i1*1000:.1f} mA')\n"
            "print(f'Branch 2 Current: {i2*1000:.1f} mA')\n"
            "print(f'Total Source Current (KCL): {i_total*1000:.1f} mA')\n"
            "```"
        ),
        "pitfall": (
            "1. **Incorrect Sign Conventions in KVL Loops**: Assigning wrong polarities to voltage drops during loop equations leads to incorrect sign results.\n"
            "2. **Applying KCL at Non-Independent Nodes**: Writing KCL equations at reference (ground) nodes duplicates existing equations without adding new information.\n"
            "3. **Ignoring Internal Resistance of Sources**: Real power supplies drop voltage under load due to internal impedance."
        ),
        "qa": (
            "**Q1: What fundamental law of physics is KCL based on?**\n"
            "A: KCL is based on the Law of Conservation of Electric Charge.\n\n"
            "**Q2: What physical law forms the basis of KVL?**\n"
            "A: KVL is based on the Law of Conservation of Energy.\n\n"
            "**Q3: How many independent KVL equations can be written in a circuit with B branches and N nodes?**\n"
            "A: Number of independent loops = B - N + 1.\n\n"
            "**Q4: Can KCL be applied to high-frequency AC circuits?**\n"
            "A: At extremely high frequencies where component sizes approach signal wavelengths, parasitic capacitance requires localized field calculations, but lump-element KCL applies across standard PCB design frequencies."
        )
    },

    "power-and-energy": {
        "overview": (
            "Power determines heat generation and energy consumption in IoT devices. Calculating power dissipation is critical for thermal management and battery life estimation."
        ),
        "concept": (
            "Electrical Power (P) is the rate at which electrical energy is converted into another energy form (such as heat, light, or mechanical motion), measured in Watts (W = J/s). "
            "Electrical Energy (E) is the total power consumed over time (E = P * t), typically measured in Joules (J) or Watt-hours (Wh) / milliamp-hours (mAh) for battery-operated IoT sensors."
        ),
        "syntax": (
            "Power Equations:\n"
            "P = V * I             (Watts)\n"
            "P = I^2 * R           (Resistive heat loss)\n"
            "P = V^2 / R           (Voltage-driven power)\n\n"
            "Energy Equations:\n"
            "E = P * t             (Joules when t in seconds, Wh when t in hours)\n"
            "Battery Capacity (Wh) = Nominal Voltage (V) * Battery Capacity (Ah)\n"
            "Battery Life (hours)  = Battery Capacity (mAh) / Average Current Draw (mA)"
        ),
        "example": (
            "### Calculating ESP32 Battery Life on a 2500 mAh LiPo Cell\n\n"
            "An IoT sensor wakes up for 2 seconds every 60 seconds. Active current = 120 mA, Deep Sleep current = 15 µA (0.015 mA).\n\n"
            "```python\n"
            "# Battery Life Estimation Script\n"
            "battery_capacity_mah = 2500.0\n\n"
            "active_current_ma = 120.0\n"
            "active_time_sec = 2.0\n\n"
            "sleep_current_ma = 0.015\n"
            "sleep_time_sec = 58.0\n\n"
            "total_cycle_sec = active_time_sec + sleep_time_sec\n\n"
            "# Average Current Draw over 1 cycle\n"
            "avg_current_ma = ((active_current_ma * active_time_sec) + (sleep_current_ma * sleep_time_sec)) / total_cycle_sec\n\n"
            "# Battery Runtime in Hours and Days\n"
            "runtime_hours = battery_capacity_mah / avg_current_ma\n"
            "runtime_days = runtime_hours / 24.0\n\n"
            "print(f'Average Current: {avg_current_ma:.3f} mA')\n"
            "print(f'Estimated Runtime: {runtime_days:.1f} days ({runtime_days/365:.2f} years)')\n"
            "```"
        ),
        "pitfall": (
            "1. **Disregarding Self-Discharge Rates**: Real batteries discharge 1-3% per month naturally even in deep sleep.\n"
            "2. **Thermal Runaway**: Overpowering linear voltage regulators (like L7805) without heat sinks causes thermal shutdown.\n"
            "3. **Inaccurate Duty Cycle Duty Estimates**: Forgetting power spikes during Wi-Fi transmission connects severely shortens runtime."
        ),
        "qa": (
            "**Q1: What is the difference between Power and Energy?**\n"
            "A: Power is instantaneous work rate (Watts), while energy is the accumulated work performed over a period of time (Watt-hours or Joules).\n\n"
            "**Q2: How do you convert 1 kWh into Joules?**\n"
            "A: 1 kWh = 1000 W * 3600 s = 3.6 x 10^6 Joules = 3.6 MJ.\n\n"
            "**Q3: Why do linear regulators get hot?**\n"
            "A: Linear regulators drop excess voltage by dissipating power as pure heat: P_heat = (V_in - V_out) * I_load.\n\n"
            "**Q4: What is the rating of 18650 Li-ion cell in Watt-hours if rated 3.7V 3000mAh?**\n"
            "A: E = 3.7V * 3.0Ah = 11.1 Wh."
        )
    },

    "ac-vs-dc": {
        "overview": (
            "Direct Current (DC) flows in one unidirectional path, while Alternating Current (AC) periodically reverses direction. Microcontrollers run on DC, while mains power grids deliver AC."
        ),
        "concept": (
            "Direct Current (DC) maintains a constant voltage polarity over time (e.g. 5V USB, 3.3V battery power). Electrons travel continuously from the negative terminal to the positive terminal. "
            "Alternating Current (AC) voltage oscillates sinusoidally, reversing direction at a frequency f (50Hz or 60Hz in power mains). AC is ideal for long-distance grid transmission using step-up/step-down transformers."
        ),
        "syntax": (
            "Sinusoidal AC Waveform Parameters:\n"
            "v(t) = V_peak * sin(2 * π * f * t)\n\n"
            "Root Mean Square (RMS) Voltage:\n"
            "V_rms = V_peak / sqrt(2) ≈ 0.707 * V_peak\n"
            "V_peak = V_rms * sqrt(2) ≈ 1.414 * V_rms\n\n"
            "Frequency & Period:\n"
            "f = 1 / T    [Frequency (Hz) = 1 / Period (seconds)]\n"
            "Mains Standards: 120V RMS @ 60Hz (North America), 230V RMS @ 50Hz (Europe/Asia)"
        ),
        "example": (
            "### Calculating Peak Voltage for 230V AC Mains Transformer Conversion\n\n"
            "```python\n"
            "import math\n\n"
            "v_rms = 230.0  # Standard AC Mains voltage\n"
            "freq = 50.0    # 50 Hz\n\n"
            "# Peak AC Voltage\n"
            "v_peak = v_rms * math.sqrt(2)\n\n"
            "# Peak-to-Peak Voltage\n"
            "v_pp = 2 * v_peak\n\n"
            "print(f'AC RMS Voltage: {v_rms:.1f} V')\n"
            "print(f'AC Peak Voltage: {v_peak:.1f} V')\n"
            "print(f'AC Peak-to-Peak: {v_pp:.1f} V')\n"
            "# Peak Voltage is ~325.3V!\n"
            "```\n\n"
            "When selecting AC-DC power converters or relay isolation, components must withstand the 325V peak, not just the 230V RMS value."
        ),
        "pitfall": (
            "1. **Connecting AC Mains Directly to DC Microcontrollers**: Instantly destroys low-voltage DC electronics and creates lethal shock hazards.\n"
            "2. **Selecting Rectifier Diodes Based Only on RMS Voltage**: Diodes in rectifiers experience Peak Inverse Voltage (PIV >= V_peak), needing ratings higher than RMS.\n"
            "3. **Confusing Frequency Standards**: Operating 60Hz magnetic transformers on 50Hz AC causes core saturation and overheating."
        ),
        "qa": (
            "**Q1: Why is AC used for electrical power transmission instead of DC?**\n"
            "A: AC voltage can be easily stepped up to ultra-high voltages (e.g. 400kV) using transformers to minimize I^2R power line losses over long distances, then stepped down safely.\n\n"
            "**Q2: What is RMS voltage?**\n"
            "A: Root Mean Square (RMS) is the equivalent DC voltage value that produces the identical heating power in a resistor as the AC wave.\n\n"
            "**Q3: What component converts AC to pulsating DC?**\n"
            "A: A Diode Bridge Rectifier.\n\n"
            "**Q4: Do microcontrollers require AC or DC power?**\n"
            "A: Microcontrollers require clean, regulated DC voltage (typically 3.3V or 5V)."
        )
    },

    # ── MODULE 2: Circuit Components ───────────────────────────────────────────
    "resistors": {
        "overview": (
            "Resistors limit current flow, divide voltages, and establish bias levels across electronic circuits. They are the most common passive component in IoT hardware."
        ),
        "concept": (
            "A resistor is a two-terminal passive component engineered to provide a specific electrical resistance. Resistors convert unwanted electrical energy into heat. "
            "Resistors are classified by value (Ω), tolerance (%), and power rating (W). Standard resistor color codes utilize 4 or 5 bands to indicate nominal value and precision."
        ),
        "syntax": (
            "4-Band Resistor Color Code:\n"
            "Band 1: 1st Digit\n"
            "Band 2: 2nd Digit\n"
            "Band 3: Multiplier (10^n)\n"
            "Band 4: Tolerance (Gold=5%, Silver=10%, Brown=1%)\n\n"
            "Color Values:\n"
            "Black=0, Brown=1, Red=2, Orange=3, Yellow=4,\n"
            "Green=5, Blue=6, Violet=7, Grey=8, White=9\n\n"
            "Example: Yellow - Violet - Red - Gold\n"
            "Digit 1 = 4, Digit 2 = 7, Multiplier = 10^2 (100), Tolerance = ±5%\n"
            "Value = 47 x 100 = 4700 Ω = 4.7 kΩ ± 5%"
        ),
        "example": (
            "### Python Resistor Color Code Decoder\n\n"
            "```python\n"
            "COLOR_CODES = {\n"
            "    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,\n"
            "    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9\n"
            "}\n\n"
            "def decode_4band(b1, b2, b3_mult):\n"
            "    d1 = COLOR_CODES[b1.lower()]\n"
            "    d2 = COLOR_CODES[b2.lower()]\n"
            "    mult = 10 ** COLOR_CODES[b3_mult.lower()]\n"
            "    value = (d1 * 10 + d2) * mult\n"
            "    return value\n\n"
            "value_ohms = decode_4band('yellow', 'violet', 'red')\n"
            "print(f'Resistor Value: {value_ohms/1000:.1f} kΩ')\n"
            "# Output: 4.7 kΩ\n"
            "```"
        ),
        "pitfall": (
            "1. **Using Standard Carbon Resistors in Precision Analog Circuits**: Carbon film resistors have higher thermal drift than Metal Film resistors.\n"
            "2. **Exceeding Voltage Rating**: Small SMD 0603 resistors have maximum working voltage limits (e.g. 50V) regardless of power calculations.\n"
            "3. **Assuming Nominal Resistance is Exact**: Standard 5% tolerance means a 100kΩ resistor can range between 95kΩ and 105kΩ."
        ),
        "qa": (
            "**Q1: What does pull-up and pull-down mean?**\n"
            "A: Pull-up resistors connect a signal line to VCC to keep it HIGH when idle; pull-down resistors connect it to GND to keep it LOW when idle.\n\n"
            "**Q2: What is SMD resistor 103 rating?**\n"
            "A: 10 x 10^3 Ω = 10,000 Ω = 10 kΩ.\n\n"
            "**Q3: What happens when resistors are connected in series vs parallel?**\n"
            "A: In series, resistances add (R_T = R1 + R2). In parallel, equivalent resistance drops (1/R_T = 1/R1 + 1/R2).\n\n"
            "**Q4: What is a potentiometer?**\n"
            "A: A 3-terminal manually adjustable variable resistor functioning as a voltage divider."
        )
    },

    "capacitors": {
        "overview": (
            "Capacitors store electrical energy in electrostatic fields. They filter power supply noise, block DC, smooth ripple, and provide timing circuits."
        ),
        "concept": (
            "A capacitor consists of two conducting plates separated by an insulating dielectric material (ceramic, electrolytic, film, tantalum). "
            "When voltage is applied, positive and negative charges accumulate on opposing plates. "
            "Capacitors oppose rapid changes in voltage: I = C * (dV/dt). They act as open circuits to steady DC and low-impedance paths to high-frequency AC signals."
        ),
        "syntax": (
            "Capacitance Equation:\n"
            "C = Q / V    [Farads (F) = Coulombs / Volt]\n\n"
            "Capacitive Reactance (Impedance to AC):\n"
            "X_c = 1 / (2 * π * f * C)  (Ohms)\n\n"
            "Standard Unit Scale:\n"
            "1 µF  = 10^-6 F   (Electrolytic decoupling caps 1µF - 1000µF)\n"
            "1 nF  = 10^-9 F   (Noise filtering caps)\n"
            "1 pF  = 10^-12 F  (Crystal oscillator load caps 12pF - 22pF)"
        ),
        "example": (
            "### Calculating Decoupling Filter Cutoff Frequency\n\n"
            "```python\n"
            "import math\n\n"
            "def lowpass_cutoff(r_ohms, c_farads):\n"
            "    return 1.0 / (2 * math.pi * r_ohms * c_farads)\n\n"
            "# RC Lowpass filter: 1kΩ and 100nF\n"
            "r = 1000.0\n"
            "c = 100e-9\n\n"
            "f_c = lowpass_cutoff(r, c)\n"
            "print(f'Cutoff Frequency (-3dB): {f_c:.1f} Hz')\n"
            "# Output: Cutoff Frequency: 1591.5 Hz\n"
            "```"
        ),
        "pitfall": (
            "1. **Reverse-Polarizing Electrolytic Capacitors**: Connecting an aluminum electrolytic cap backwards causes explosive failure.\n"
            "2. **Ignoring DC Bias Characteristic of Ceramic Capacitors**: High-density X5R/X7R MLCC capacitors can lose over 60% capacitance at their rated DC voltage.\n"
            "3. **Placing Decoupling Capacitors Far from Microcontroller Pins**: Long PCB traces introduce parasitic inductance that negates high-frequency noise filtering."
        ),
        "qa": (
            "**Q1: Why are decoupling capacitors placed right next to MCU VCC pins?**\n"
            "A: They act as local energy reservoirs supplying instantaneous current spikes when internal logic gates switch, suppressing voltage drops on the power rail.\n\n"
            "**Q2: What is ESR?**\n"
            "A: Equivalent Series Resistance — the internal electrical resistance of a real capacitor.\n\n"
            "**Q3: How do capacitors combine in series and parallel?**\n"
            "A: In parallel, capacitances add (C_T = C1 + C2). In series, total capacitance decreases (1/C_T = 1/C1 + 1/C2).\n\n"
            "**Q4: What capacitor type is non-polarized?**\n"
            "A: Ceramic, film, and mica capacitors are non-polarized."
        )
    },

    "inductors-and-coils": {
        "overview": (
            "Inductors store energy in magnetic fields. They are core components in DC-DC buck/boost converters, noise chokes, relays, motors, and wireless communication circuits."
        ),
        "concept": (
            "An inductor is a coil of wire wrapped around a magnetic core (ferrite or air). "
            "When current flows through the coil, it creates a magnetic field. "
            "Inductors oppose changes in electric current: V = L * (dI/dt). When current suddenly changes, the collapsing magnetic field produces a high back-EMF voltage kick."
        ),
        "syntax": (
            "Inductance Equation:\n"
            "V_induced = L * (dI / dt)\n\n"
            "Inductive Reactance (AC Impedance):\n"
            "X_L = 2 * π * f * L   (Ohms)\n\n"
            "Standard Units:\n"
            "1 H  = 1 Henry\n"
            "1 mH = 10^-3 H   (Relay coils, power inductors)\n"
            "1 µH = 10^-6 H   (Buck converter switching inductors 2.2µH - 47µH)"
        ),
        "example": (
            "### Calculating Back-EMF Voltage from a De-energized Relay Coil\n\n"
            "A 100mH relay coil carrying 100mA is switched off in 1 microsecond by a transistor without a flyback diode.\n\n"
            "```python\n"
            "l_henry = 0.100       # 100 mH\n"
            "delta_i = 0.100       # 100 mA to 0 mA\n"
            "delta_t = 1.0e-6      # 1 microsecond\n\n"
            "# Induced Back-EMF Voltage\n"
            "v_spike = l_henry * (delta_i / delta_t)\n\n"
            "print(f'Inductive Voltage Spike: {v_spike:.1f} V')\n"
            "# Output: 10,000 Volts!\n"
            "```\n\n"
            "This massive voltage spike will instantly destroy the switching transistor unless a Flyback Diode is connected across the coil."
        ),
        "pitfall": (
            "1. **Omitting Flyback Diodes Across Inductive Loads**: Relays, solenoids, and motors generate inductive spikes that destroy switching MOSFETs/BJT drivers.\n"
            "2. **Inductor Core Saturation**: Exceeding the rated saturation current causes inductance to collapse, causing overcurrent spikes.\n"
            "3. **Magnetic Crosstalk on PCB**: Placing inductors close together without shielding causes unwanted EMI coupling between signals."
        ),
        "qa": (
            "**Q1: What is a flyback diode?**\n"
            "A: A diode placed across an inductive load in reverse bias to safely dissipate inductive back-EMF current when the switch turns off.\n\n"
            "**Q2: How does an inductor behave at DC steady-state?**\n"
            "A: At DC steady-state (dI/dt = 0), an ideal inductor behaves as a pure short circuit (zero voltage drop).\n\n"
            "**Q3: What is the primary use of a ferrite bead?**\n"
            "A: A ferrite bead is a specialized inductor that attenuates high-frequency noise on power supply traces by dissipating high-frequency AC as heat.\n\n"
            "**Q4: What happens to inductive reactance as frequency increases?**\n"
            "A: Inductive reactance (X_L = 2*π*f*L) increases linearly with frequency."
        )
    },

    "series-and-parallel-circuits": {
        "overview": (
            "Analyzing series and parallel configurations allows engineers to determine equivalent impedance, branch currents, and node voltages across complex hardware systems."
        ),
        "concept": (
            "**Series Circuits**: Components are connected end-to-end in a single path. The identical current flows through every component (I_total = I1 = I2). Voltages add up (V_total = V1 + V2).\n\n"
            "**Parallel Circuits**: Components share common top and bottom nodes. The identical voltage exists across every parallel branch (V_total = V1 = V2). Currents add up (I_total = I1 + I2)."
        ),
        "syntax": (
            "Series Rules:\n"
            "R_total = R1 + R2 + R3 + ... + Rn\n"
            "C_total = 1 / (1/C1 + 1/C2 + ... + 1/Cn)\n"
            "L_total = L1 + L2 + L3 + ... + Ln\n\n"
            "Parallel Rules:\n"
            "R_total = 1 / (1/R1 + 1/R2 + ... + 1/Rn)\n"
            "C_total = C1 + C2 + C3 + ... + Cn\n"
            "L_total = 1 / (1/L1 + 1/L2 + ... + 1/Ln)\n\n"
            "Two Parallel Resistors Shortcut:\n"
            "R_eq = (R1 * R2) / (R1 + R2)"
        ),
        "example": (
            "### Python Solver for Equivalent Series-Parallel Networks\n\n"
            "```python\n"
            "def parallel(r1, r2):\n"
            "    return (r1 * r2) / (r1 + r2)\n\n"
            "# Circuit: R1 (100Ω) in series with parallel pair [R2(200Ω) || R3(200Ω)]\n"
            "r1 = 100.0\n"
            "r2 = 200.0\n"
            "r3 = 200.0\n\n"
            "r_p = parallel(r2, r3)     # 200 || 200 = 100Ω\n"
            "r_eq = r1 + r_p            # 100 + 100 = 200Ω\n\n"
            "print(f'Parallel Pair R2||R3: {r_p:.1f} Ω')\n"
            "print(f'Total Equivalent Resistance: {r_eq:.1f} Ω')\n"
            "```"
        ),
        "pitfall": (
            "1. **Connecting Batteries of Different Voltages in Parallel**: Causes massive recirculating current between cells, leading to thermal runaway or fire.\n"
            "2. **Series Component Failure Impact**: An open failure in a series branch halts the entire circuit; in parallel, remaining branches stay powered.\n"
            "3. **Assuming Equal Current in Parallel LEDs**: Variations in LED forward voltages cause current hogging in the lowest Vf LED."
        ),
        "qa": (
            "**Q1: If four 100Ω resistors are connected in parallel, what is the total equivalent resistance?**\n"
            "A: R_eq = 100 / 4 = 25Ω.\n\n"
            "**Q2: What happens if one light bulb fails open in a series Christmas light string?**\n"
            "A: All lights turn off because the current path is broken.\n\n"
            "**Q3: Are home electrical outlets wired in series or parallel?**\n"
            "A: Parallel, so each appliance receives full 120V/230V mains voltage independently.\n\n"
            "**Q4: How do you double battery voltage while keeping capacity the same?**\n"
            "A: Connect two identical batteries in series."
        )
    },

    "voltage-dividers": {
        "overview": (
            "Voltage dividers scale high analog voltages down to safe microcontroller ADC input levels (e.g. 0-3.3V) and provide bias networks for resistive sensors."
        ),
        "concept": (
            "A voltage divider consists of two resistors (R1 and R2) connected in series across an input voltage V_in. "
            "The output voltage V_out tapped from the junction between R1 and R2 is a linear fraction of V_in, proportional to R2 / (R1 + R2)."
        ),
        "syntax": (
            "Voltage Divider Equation:\n"
            "V_out = V_in * ( R2 / (R1 + R2) )\n\n"
            "Solving for R1 given V_in, V_out, R2:\n"
            "R1 = R2 * ( (V_in / V_out) - 1 )\n\n"
            "Loaded Voltage Divider Equation (with Load R_L connected to V_out):\n"
            "R2_eff = (R2 * R_L) / (R2 + R_L)\n"
            "V_out_loaded = V_in * ( R2_eff / (R1 + R2_eff) )"
        ),
        "example": (
            "### Designing a Battery Voltage Monitor Divider for ESP32 (3.3V ADC)\n\n"
            "Scale a 12.6V fully-charged 3S LiPo battery down to max 3.0V for safe ESP32 ADC measurement.\n\n"
            "```python\n"
            "v_in_max = 12.6   # Max Battery Voltage\n"
            "v_out_target = 3.0 # Target ADC Voltage\n"
            "r2 = 10000.0      # Pick R2 = 10 kΩ\n\n"
            "# Calculate required R1\n"
            "r1 = r2 * ((v_in_max / v_out_target) - 1)\n\n"
            "print(f'Calculated R1: {r1/1000:.2f} kΩ')\n"
            "# Pick standard E24 resistor value R1 = 32 kΩ\n\n"
            "r1_actual = 32000.0\n"
            "v_out_actual = v_in_max * (r2 / (r1_actual + r2))\n"
            "print(f'Actual Max ADC Voltage: {v_out_actual:.2f} V')\n"
            "```"
        ),
        "pitfall": (
            "1. **Loading Effect Errors**: Connecting a low-impedance input to a high-resistance voltage divider pulls down V_out significantly.\n"
            "2. **Using Voltage Dividers as Power Supplies**: Voltage dividers are extremely inefficient for powering active loads (V_out drops when load current is drawn).\n"
            "3. **Using Ultra-High Resistance Values with MCU ADCs**: Resistances above 100kΩ fail to sample accurately because ADC sampling capacitors cannot charge fast enough."
        ),
        "qa": (
            "**Q1: Can a voltage divider be used to step down 12V to power a 5V 1A Raspberry Pi?**\n"
            "A: NO! A voltage divider has high output impedance and cannot supply current without output voltage collapsing. Use a Buck Switching Converter.\n\n"
            "**Q2: What is the rule of thumb for load impedance on a voltage divider?**\n"
            "A: The load resistance R_L should be at least 10x (preferably 100x) larger than R2 to prevent voltage sag.\n\n"
            "**Q3: How do LDR (Light Dependent Resistor) sensors measure light using a voltage divider?**\n"
            "A: The LDR replaces R1 or R2. As light changes LDR resistance, V_out fluctuates proportionally for the ADC pin to read.\n\n"
            "**Q4: If R1 = R2, what is V_out?**\n"
            "A: V_out = 0.5 * V_in (exactly half)."
        )
    },

    # ── MODULE 3: Practical Electrical Skills ─────────────────────────────────
    "using-a-multimeter": {
        "overview": (
            "Digital Multimeters (DMM) are the indispensable diagnostic instrument for verifying voltages, measuring currents, testing continuity, and debugging hardware defects."
        ),
        "concept": (
            "A Digital Multimeter measures electrical parameters via internal precision analog-to-digital converters and shunt resistors. "
            "Proper terminal jack selection is critical: COM is always ground/black. Red probe connects to V/Ω for voltage/resistance and mA or 10A for current measurements."
        ),
        "syntax": (
            "Multimeter Dial Modes:\n"
            "V~   : AC Voltage Measurement\n"
            "V=   : DC Voltage Measurement (Battery, MCU rails)\n"
            "mA/A : Current Measurement (MUST BE IN SERIES)\n"
            "Ω    : Resistance Measurement (Circuit Powered OFF!)\n"
            "->|- : Diode Test / Semiconductor Junction Drop\n"
            "°))) : Continuity Buzzer (< 50Ω shorts beep)"
        ),
        "example": (
            "### Standard Procedure for Measuring Microcontroller Current Draw\n\n"
            "1. Turn OFF power to the circuit board.\n"
            "2. Move the red DMM probe to the **mA** or **10A** jack (COM stays in COM).\n"
            "3. Set dial to **DC mA** mode.\n"
            "4. Break the positive power lead from the supply.\n"
            "5. Connect the Red probe to the positive supply output, and Black probe to the MCU VCC pin.\n"
            "6. Apply power and observe steady-state and peak current consumption."
        ),
        "pitfall": (
            "1. **Measuring Voltage while Probes are in Current (A) Jacks**: Blows internal meter fuses or short-circuits power supplies with zero-resistance shunt.\n"
            "2. **Measuring Resistance on Powered Circuits**: Destroys multimeter internals and yields false readings.\n"
            "3. **Leaving Multimeter in Current Mode After Use**: Invites accidental short circuits on the next voltage test."
        ),
        "qa": (
            "**Q1: What does the continuity buzzer test indicate?**\n"
            "A: It beeps when resistance between probes is less than ~30-50Ω, indicating a low-resistance direct connection or short.\n\n"
            "**Q2: What happens if a DMM internal fuse is blown?**\n"
            "A: Current measurements will read 0.00A continuously, though voltage readings still function.\n\n"
            "**Q3: Why must current be measured in series?**\n"
            "A: All current flowing to the load must physically pass through the meter's internal low-resistance shunt resistor.\n\n"
            "**Q4: What is Auto-Ranging?**\n"
            "A: Feature where DMM automatically adjusts measurement scale for optimal resolution."
        )
    },

    "reading-circuit-diagrams": {
        "overview": (
            "Schematic diagrams are the standardized blueprint language of electronics. Mastering schematic symbols enables circuit analysis, breadboard assembly, and PCB layout."
        ),
        "concept": (
            "Schematics represent circuit connectivity using standardized graphical symbols rather than physical component appearances. "
            "Net names (like VCC, GND, RESET, SDA, SCL) connect points electrically across a drawing without drawing crossing wires everywhere."
        ),
        "syntax": (
            "Standard Schematic Symbols:\n"
            "GND (Ground)  : ⏚ or ⏛ (0V Reference)\n"
            "VCC / VDD     : ⬆ or ▲ (Positive Power Supply)\n"
            "Resistor      : Zig-zag line or Rectangle\n"
            "Capacitor     : Two parallel lines || (Curved line = Polarized (-))\n"
            "Diode / LED   : Triangle pointing to bar |◀ (LED has 2 arrows pointing out)\n"
            "Transistor    : BJT (Base, Collector, Emitter) / MOSFET (Gate, Drain, Source)\n"
            "IC / MCU      : Named rectangle with pin numbers & signals"
        ),
        "example": (
            "### Interpreting a Microcontroller Button Circuit Schematic\n\n"
            "```text\n"
            "   +5V (VCC)\n"
            "    |\n"
            "   [R1: 10kΩ Pull-up]\n"
            "    |\n"
            "    +-----> GPIO_PIN_4 (MCU Input)\n"
            "    |\n"
            "  [ SW1 (Push Button) ]\n"
            "    |\n"
            "   GND (0V)\n"
            "```\n\n"
            "- When SW1 is OPEN: GPIO_PIN_4 is pulled HIGH to 5V through 10kΩ.\n"
            "- When SW1 is CLOSED: GPIO_PIN_4 is shorted directly to GND (0V)."
        ),
        "pitfall": (
            "1. **Confusing Crossing Wires with Connected Wires**: Wires crossing without a dot junction are NOT connected; a solid dot indicates electrical connection.\n"
            "2. **Overlooking Pin Numbering vs Physical Pinouts**: IC schematic symbol pins are arranged logically by function, NOT physically by package pin order.\n"
            "3. **Ignoring Power and Ground Flags**: Forgetting that implicit power nets (VCC/GND) connect all matching power pins globally across multi-page schematics."
        ),
        "qa": (
            "**Q1: What does a dot at a wire intersection mean?**\n"
            "A: A dot indicates an electrical junction (four-way or three-way connection).\n\n"
            "**Q2: What is a Net Label in schematics?**\n"
            "A: A text label assigned to a wire (e.g. TX_DATA) that connects it virtually to all other wires with the same label anywhere in the schematic.\n\n"
            "**Q3: What is the difference between VCC, VDD, VSS, and VEE?**\n"
            "A: VCC/VEE refer to Collector/Emitter voltages in BJT circuits; VDD/VSS refer to Drain/Source voltages in IC/MOSFET circuits (VDD = +, VSS = GND).\n\n"
            "**Q4: What is a Reference Designator?**\n"
            "A: Unique alphanumeric component identifier on schematics (e.g. R1, C5, U2, Q1)."
        )
    },

    "breadboard-prototyping": {
        "overview": (
            "Breadboards enable solderless circuit construction for rapid testing, prototyping, and validating sensor hardware before manufacturing PCBs."
        ),
        "concept": (
            "A solderless breadboard consists of a plastic block containing spring metal clips beneath a grid of holes. "
            "Power rails run vertically along the sides for VCC and GND. Component tie-points in the center matrix are connected horizontally in 5-hole terminal strips."
        ),
        "syntax": (
            "Breadboard Internal Connections:\n"
            "Power Rails (Sides)   : Connected VERTICALLY in long columns (+ and -)\n"
            "Terminal Strips (Center): Connected HORIZONTALLY in 5-pin rows (a-b-c-d-e)\n"
            "Center Divider Gap    : Isolates opposing sides for DIP IC placement across notch"
        ),
        "example": (
            "### Best Practices Checklist for Breadboard Assembly\n\n"
            "1. Color-Code Wiring: **Red** for Positive Power, **Black** for Ground, **Yellow/Blue** for Data signals.\n"
            "2. Keep Wires Flat & Short: Avoid loose wire arches ('rat's nest') that snag or introduce stray capacitance.\n"
            "3. Always Connect Power Rails First: Run dedicated power and ground jumper wires from MCU board to side rails.\n"
            "4. Trim Component Leads: Cut resistor and LED legs short so components sit flush against the board surface."
        ),
        "pitfall": (
            "1. **Placing DIP IC Pins in the Same 5-Pin Strip**: Short-circuits all opposing pins on the chip together; always bridge IC across the central center gap.\n"
            "2. **High-Frequency & High-Current Prototyping Limitations**: Breadboards have ~2-5pF parasitic capacitance and max 500mA current limits per clip.\n"
            "3. **Intermittent Connections from Worn Spring Clips**: Loose breadboard sockets cause unpredictable signal drops and reset issues."
        ),
        "qa": (
            "**Q1: Why should you avoid building high-frequency RF circuits on breadboards?**\n"
            "A: Stray capacitance (~5pF) and inductance between adjacent metal clips degrade high-frequency (>10MHz) signals.\n\n"
            "**Q2: What is the maximum current rating of standard breadboard rails?**\n"
            "A: Typically ~500mA to 1A max; higher currents cause heating and melt plastic housings.\n\n"
            "**Q3: Why are DIP ICs placed straddling the center trough?**\n"
            "A: The trough isolates left-side pins from right-side pins so each pin connects to an independent 5-hole row.\n\n"
            "**Q4: How do you verify breadboard connections?**\n"
            "A: Use a DMM in Continuity mode with power removed."
        )
    },

    "safety-and-esd": {
        "overview": (
            "Electrostatic Discharge (ESD) and high voltage safety procedures prevent destructive silicon damage and protect engineers against electrical hazards."
        ),
        "concept": (
            "**Electrostatic Discharge (ESD)**: Sudden transfer of static charge accumulated on human skin (up to 15,000V) to delicate microchips, rupturing microscopic MOSFET gate oxides.\n\n"
            "**Electrical Safety**: High voltage (>50V DC / 30V AC) can overcome human skin resistance and cause fatal electric shock or ventricular fibrillation."
        ),
        "syntax": (
            "ESD Protection Controls:\n"
            "- Anti-Static Wrist Strap : 1MΩ series resistor to Earth Ground\n"
            "- ESD Mat                 : Static dissipative surface (10^6 - 10^9 Ω/sq)\n"
            "- ESD Packaging           : Shielding bags (Faraday cage effect) for MOSFETs/ICs\n\n"
            "Voltage Safety Limits:\n"
            "Safe Low Voltage (SELV)  : < 50V AC RMS, < 120V Ripple-Free DC\n"
            "Hazardous Voltage        : > 50V AC / 120V DC (Requires insulation, barriers, fused probes)"
        ),
        "example": (
            "### Setting Up an ESD-Safe Workstation\n\n"
            "1. Spread a dissipative ESD mat over the workbench.\n"
            "2. Attach the ESD mat grounding cord to mains Earth Ground or dedicated bench ground point.\n"
            "3. Wear a conductive wrist strap connected via a **1MΩ safety resistor** to the mat ground.\n"
            "4. Store sensitive microcontrollers (ESP32, STM32, CMOS sensors) inside metallic ESD shielding bags when not in use."
        ),
        "pitfall": (
            "1. **Direct Grounding Wrist Straps Without a 1MΩ Resistor**: Creates a dangerous direct path to ground if the engineer touches a live wire!\n"
            "2. **Latent ESD Damage**: Sub-lethal ESD zaps weaken gate oxide without immediate failure, causing unexplainable crashes weeks later in production.\n"
            "3. **Working on Mains AC Power with Both Hands**: Current can flow through one arm across the heart to the other arm."
        ),
        "qa": (
            "**Q1: Why is there a 1MΩ resistor inside anti-static wrist straps?**\n"
            "A: It slowly bleeds off static charges safely while protecting the human from high-current shock if they accidentally touch a live voltage source.\n\n"
            "**Q2: What is Latent ESD Defect?**\n"
            "A: Damage where a component functions initial factory testing but fails prematurely during field operation due to static stress.\n\n"
            "**Q3: Which electronic components are most sensitive to ESD?**\n"
            "A: MOSFETs, CMOS microcontrollers, high-speed RAM, and RF amplifiers.\n\n"
            "**Q4: What is the 'One-Hand Rule' in high voltage work?**\n"
            "A: Keep one hand in your pocket when testing live high-voltage circuits to prevent current passing through your chest between both arms."
        )
    },

    "power-supply-basics": {
        "overview": (
            "Power supply design ensures stable, noise-free voltage rails (5V, 3.3V, 1.8V) for microcontrollers, sensors, and wireless transceivers."
        ),
        "concept": (
            "Power supplies convert unregulated raw DC or AC input into clean, tightly regulated DC output. "
            "Linear Regulators (LDOs) use active feedback to burn excess voltage as heat, offering ripple-free output. "
            "Switching Regulators (Buck/Boost) rapidly switch inductors/capacitors to efficiently step voltage up or down with minimal heat."
        ),
        "syntax": (
            "Linear Regulator Power Dissipation:\n"
            "P_loss = (V_in - V_out) * I_load\n\n"
            "Switching Regulator Efficiency:\n"
            "Efficiency (η) = P_out / P_in = (V_out * I_out) / (V_in * I_in)  (Typically 85% - 95%)\n\n"
            "Regulator Types:\n"
            "LDO (Low Dropout)  : Dropping small ΔV (e.g. 5V -> 3.3V) with clean low noise.\n"
            "Buck Converter     : Efficient Step-Down (12V -> 3.3V @ high current).\n"
            "Boost Converter    : Efficient Step-Up (3.7V Li-ion -> 5V USB output).\n"
            "Buck-Boost         : Can step up or down depending on battery state."
        ),
        "example": (
            "### Thermal Calculation for AMS1117-3.3 LDO Regulator\n\n"
            "Input = 12V DC Adapter, Output = 3.3V to ESP32 drawing 200mA average.\n\n"
            "```python\n"
            "v_in = 12.0\n"
            "v_out = 3.3\n"
            "i_load = 0.200 # 200 mA\n\n"
            "# Power Dissipated as Heat\n"
            "p_heat = (v_in - v_out) * i_load # (12.0 - 3.3) * 0.2 = 1.74 Watts!\n\n"
            "# Thermal Resistance SOT-223 package: R_thja = 90 °C/W\n"
            "temp_rise = p_heat * 90.0\n"
            "ambient_temp = 25.0\n"
            "junction_temp = ambient_temp + temp_rise\n\n"
            "print(f'Power Heat Loss: {p_heat:.2f} W')\n"
            "print(f'Junction Temp: {junction_temp:.1f} °C')\n"
            "# Junction temp = 181.6°C -> EXCEEDS 125°C max limit! Regulator will thermal shut down!\n"
            "```\n\n"
            "Solution: Replace LDO with a DC-DC Buck Converter module (90% efficiency, minimal heat)."
        ),
        "pitfall": (
            "1. **Powering High-Current Loads via LDO from High Input Voltage**: Burning large ΔV at high currents causes thermal shutdown.\n"
            "2. **Omitting Regulator Input/Output Capacitors**: LDOs oscillate without manufacturer-recommended ceramic input and output capacitors.\n"
            "3. **Dropout Voltage Neglect**: Supplying 3.5V to a non-LDO 3.3V regulator that requires 2.0V dropout (V_in >= 5.3V) causes output voltage to drop below 3.3V."
        ),
        "qa": (
            "**Q1: What is Dropout Voltage in LDOs?**\n"
            "A: Minimum difference between V_in and V_out required for the regulator to maintain output regulation.\n\n"
            "**Q2: When should you prefer an LDO over a Buck Converter?**\n"
            "A: For low-current noise-sensitive analog applications (like precision ADCs, audio, RF receivers) where ΔV is small.\n\n"
            "**Q3: What is Power Ripple?**\n"
            "A: Small residual periodic AC variation in DC output voltage resulting from switching or AC rectification.\n\n"
            "**Q4: How does a Buck converter achieve >90% efficiency?**\n"
            "A: By rapidly switching a transistor fully ON and fully OFF (minimizing resistive loss) and using an inductor/capacitor filter to store energy."
        )
    }
}


def populate_electrical_content():
    with app.app_context():
        course = Course.query.filter_by(slug='electrical-fundamentals', is_deleted=False).first()
        if not course:
            print("[ERROR] Course electrical-fundamentals not found!")
            return

        print(f"Populating content for course: {course.title} ({course.slug})")

        total_sections = 0
        published_lessons = 0

        for mod in course.modules.all():
            print(f"\n--- Module: {mod.title} ---")
            for lesson in mod.lessons.filter_by(is_deleted=False).all():
                lesson_data = ELECTRICAL_LESSON_CONTENT.get(lesson.slug)
                if not lesson_data:
                    print(f"  [WARN] No content template found for lesson: {lesson.slug}")
                    continue

                sec_count = 0
                for stype, content in lesson_data.items():
                    sec = LessonSection.query.filter_by(
                        lesson_id=lesson.id,
                        section_type=stype
                    ).first()

                    stitle = stype.capitalize()
                    if stype == 'qa':
                        stitle = 'Q & A'
                    elif stype == 'concept':
                        stitle = 'Core Concept'

                    if not sec:
                        sec = LessonSection(
                            lesson_id=lesson.id,
                            section_type=stype,
                            title=stitle,
                            content_markdown=content,
                            content_html="",
                            sort_order=list(lesson_data.keys()).index(stype) + 1,
                            is_visible=True
                        )
                        db.session.add(sec)
                    else:
                        sec.content_markdown = content
                        sec.is_visible = True

                    sec_count += 1
                    total_sections += 1

                lesson.status = 'published'
                published_lessons += 1
                print(f"  [PUBLISHED] {lesson.title} ({sec_count} sections)")

        course.status = 'published'
        db.session.commit()

        print(f"\n========================================================")
        print(f"SUCCESS: {published_lessons} lessons published | {total_sections} sections populated!")
        print(f"Course 'electrical-fundamentals' is now fully PUBLISHED.")
        print(f"========================================================")


if __name__ == "__main__":
    populate_electrical_content()
