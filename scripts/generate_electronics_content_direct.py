"""
generate_electronics_content_direct.py
=======================================
Direct content generator for Electronics Basics course.
Populates high-quality technical markdown content across all 20 lessons and sets published status.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

ELECTRONICS_LESSON_CONTENT = {

    # ── MODULE 1: Semiconductor Devices ─────────────────────────────────────────
    "diodes": {
        "overview": (
            "Diodes are semiconductor one-way valves for electric current. "
            "They are essential for reverse polarity protection, rectification, signal clipping, and flyback protection in IoT hardware."
        ),
        "concept": (
            "A semiconductor diode consists of a P-N junction formed by joining P-type (positive hole majority) and N-type (negative electron majority) silicon. "
            "In Forward Bias (Anode > Cathode by ~0.7V for silicon), the depletion region shrinks and current flows freely. "
            "In Reverse Bias (Cathode > Anode), the depletion region expands, blocking current flow until breakdown voltage is reached."
        ),
        "syntax": (
            "Diode Equation (Shockley Model):\n"
            "I = I_s * (exp(V / (n * V_t)) - 1)\n\n"
            "Key Specifications:\n"
            "V_f  : Forward Voltage Drop (~0.7V Silicon, ~0.3V Schottky, 1.8-3.3V LED)\n"
            "I_f  : Maximum Continuous Forward Current\n"
            "PIV  : Peak Inverse Voltage (Max Reverse Voltage before breakdown)\n"
            "t_rr : Reverse Recovery Time (High speed switching factor)"
        ),
        "example": (
            "### Reverse Polarity Protection Circuit using Schottky Diode\n\n"
            "Connect a 1N5819 Schottky Diode (Vf = 0.3V) in series with positive battery input to protect an ESP32 board.\n\n"
            "```python\n"
            "v_battery = 5.0    # Input battery voltage\n"
            "v_f_schottky = 0.3 # Low forward drop Schottky\n"
            "i_load = 0.250     # 250 mA MCU consumption\n\n"
            "v_mcu_vcc = v_battery - v_f_schottky\n"
            "p_diode_loss = v_f_schottky * i_load\n\n"
            "print(f'MCU Operating VCC: {v_mcu_vcc:.2f} V')\n"
            "print(f'Diode Power Dissipation: {p_diode_loss * 1000:.1f} mW')\n"
            "# Output: VCC = 4.70V, Dissipation = 75.0 mW\n"
            "```"
        ),
        "pitfall": (
            "1. **Using Standard 1N4007 Diodes in High-Speed Switching (PWM/DC-DC)**: Slow reverse recovery time (t_rr) causes high switching losses and overheating; use Schottky or Ultrafast diodes.\n"
            "2. **Exceeding Diode Peak Inverse Voltage**: Exceeding PIV in AC rectifiers causes reverse avalanche breakdown.\n"
            "3. **Ignoring Diode Thermal Voltage Drift**: Forward voltage Vf drops by ~2mV/°C as temperature rises, which can cause thermal runaway in parallel diodes."
        ),
        "qa": (
            "**Q1: Why are Schottky diodes preferred in battery-powered IoT systems?**\n"
            "A: They feature much lower forward voltage drops (0.2V - 0.4V vs 0.7V for silicon diodes), minimizing wasted power.\n\n"
            "**Q2: What is the Anode and Cathode polarity?**\n"
            "A: Anode is positive (+); Cathode is negative (-), marked with a silver/black line band on the physical diode package.\n\n"
            "**Q3: Can diodes be placed in parallel to double current capacity?**\n"
            "A: Not directly without current-sharing resistors, because the diode with slightly lower Vf will draw most current, overheat, and fail.\n\n"
            "**Q4: What is Zener breakdown?**\n"
            "A: Controlled reverse voltage breakdown engineered to maintain a constant voltage across the diode for voltage regulation."
        )
    },

    "rectifiers": {
        "overview": (
            "Rectifiers convert alternating current (AC) into pulsating direct current (DC). They are the foundational front-end of all mains-powered DC supply adapters."
        ),
        "concept": (
            "Rectification utilizes diode directional conduction to allow only positive half-cycles of AC through. "
            "Half-Wave Rectifiers use 1 diode (50% efficiency). "
            "Full-Wave Bridge Rectifiers use 4 diodes arranged in a diamond bridge to invert negative half-cycles into positive pulses, maximizing output power and doubling ripple frequency for easier smoothing."
        ),
        "syntax": (
            "Full-Wave Bridge Rectifier Equations:\n"
            "V_dc_avg = (2 * V_peak) / π ≈ 0.636 * V_peak\n"
            "V_dc_peak = V_ac_peak - (2 * V_f_diode)\n\n"
            "Filter Capacitor Ripple Voltage Equation:\n"
            "V_ripple = I_load / (f_ripple * C_filter)\n"
            "Note: f_ripple = 2 * f_ac (100Hz for 50Hz mains, 120Hz for 60Hz mains)"
        ),
        "example": (
            "### Sizing Filter Capacitor for 12V DC 1A Power Supply\n\n"
            "Design a 12V 1A DC supply with max 1.0V AC ripple from a 50Hz AC Transformer.\n\n"
            "```python\n"
            "i_load = 1.0        # 1 Ampere\n"
            "f_mains = 50.0      # 50 Hz AC\n"
            "f_ripple = 2 * f_mains # 100 Hz full-wave\n"
            "v_ripple_max = 1.0  # 1V max peak-to-peak ripple\n\n"
            "# Calculate required smoothing capacitance: C = I / (f * V_ripple)\n"
            "c_farads = i_load / (f_ripple * v_ripple_max)\n"
            "c_uf = c_farads * 1e6\n\n"
            "print(f'Minimum Filter Capacitance: {c_uf:.0f} µF')\n"
            "# Output: 10,000 µF\n"
            "```"
        ),
        "pitfall": (
            "1. **Forgetting 2x Diode Drops in Bridge Rectifiers**: Total voltage drop is 2 * Vf (~1.4V for silicon diodes), reducing peak DC voltage.\n"
            "2. **Selecting Inadequate Capacitor Ripple Current Rating**: High load current causes smoothing caps to heat up and dry out if ripple current rating is exceeded.\n"
            "3. **Inadequate PIV Rating**: Bridge diodes experience Peak Inverse Voltage equal to peak AC voltage."
        ),
        "qa": (
            "**Q1: What is the main advantage of a full-wave bridge rectifier over a half-wave rectifier?**\n"
            "A: Full-wave rectifies both AC half-cycles, producing double the average DC voltage and twice the ripple frequency (making filtering much easier).\n\n"
            "**Q2: Why is a filter capacitor placed across the rectifier output?**\n"
            "A: It charges up during voltage peaks and discharges into the load during voltage troughs, smoothing pulsating DC into steady DC.\n\n"
            "**Q3: What is Diode PIV in a bridge rectifier?**\n"
            "A: Peak Inverse Voltage = V_peak.\n\n"
            "**Q4: What is ripple voltage?**\n"
            "A: Residual AC fluctuations remaining on a DC voltage line after rectification and filtering."
        )
    },

    "transistors-bjt": {
        "overview": (
            "Bipolar Junction Transistors (BJTs) are current-controlled semiconductor amplifiers and switches used to drive relays, LEDs, motors, and buzzers from low-power MCU GPIO pins."
        ),
        "concept": (
            "A BJT has three terminals: Base (B), Collector (C), and Emitter (E). "
            "A small current entering the Base ($I_B$) controls a much larger current flowing between Collector and Emitter ($I_C = \\beta \\times I_B$). "
            "In Switching Applications, the BJT operates in Saturation (Fully ON, $V_{CE} \\approx 0.2V$) or Cutoff (Fully OFF, $I_C = 0$)."
        ),
        "syntax": (
            "BJT Key Equations:\n"
            "I_C = β * I_B           (Active Amplification Region)\n"
            "I_E = I_C + I_B\n"
            "V_BE ≈ 0.7V             (Forward Biased Base-Emitter Junction)\n\n"
            "Saturation Rule of Thumb for Switching:\n"
            "Target I_B = I_C / 10   (Forced beta of 10 to ensure deep saturation)\n"
            "R_base = (V_gpio - V_BE) / I_B"
        ),
        "example": (
            "### Designing an NPN BJT (2N2222) Relay Driver Circuit\n\n"
            "Drive a 5V relay coil requiring 80mA using a 3.3V ESP32 GPIO pin.\n\n"
            "```python\n"
            "v_gpio = 3.3    # ESP32 High voltage\n"
            "v_be = 0.7      # Base-emitter drop\n"
            "i_collector = 0.080 # 80 mA relay current\n\n"
            "# Saturation overdrive factor (forced beta = 10)\n"
            "i_base = i_collector / 10.0 # 8 mA Base current\n\n"
            "r_base = (v_gpio - v_be) / i_base\n"
            "print(f'Calculated Base Resistor: {r_base:.1f} Ω')\n"
            "# Pick standard resistor R_base = 330 Ω\n"
            "```"
        ),
        "pitfall": (
            "1. **Connecting Base Directly to MCU GPIO Without Resistor**: Destroys the MCU pin and Base-Emitter junction due to unlimited forward current.\n"
            "2. **Operating BJT in Linear Region When Switching**: Causes excessive $V_{CE}$ drop, causing high power dissipation ($P = V_{CE} \\times I_C$) and overheating.\n"
            "3. **Forgetting Flyback Diode Across Relays**: Inductive kickback destroys Collector-Emitter junction on turn-off."
        ),
        "qa": (
            "**Q1: What is the difference between NPN and PNP BJTs?**\n"
            "A: NPN turns ON when Base voltage is pulled above Emitter (+0.7V); PNP turns ON when Base is pulled below Emitter (-0.7V).\n\n"
            "**Q2: What is Beta (hFE)?**\n"
            "A: DC Current Gain ratio ($I_C / I_B$), typically ranging between 50 and 300.\n\n"
            "**Q3: What is VCE(sat)?**\n"
            "A: Collector-Emitter Saturation Voltage (~0.1V - 0.3V) when transistor is fully turned ON as a switch.\n\n"
            "**Q4: Which BJT terminal is connected to Ground in low-side NPN switching?**\n"
            "A: Emitter terminal."
        )
    },

    "mosfets": {
        "overview": (
            "Metal-Oxide-Semiconductor Field-Effect Transistors (MOSFETs) are voltage-controlled switches offering near-zero gate current, extremely low ON-resistance ($R_{DS(on)}$), and high switching speeds."
        ),
        "concept": (
            "A MOSFET has three terminals: Gate (G), Drain (D), and Source (S). "
            "An electric field applied to the insulated Gate voltage controls charge carrier channel formation between Drain and Source. "
            "Unlike BJTs, MOSFETs draw zero continuous Gate DC current ($I_G = 0$), making them ideal for driving heavy loads (motors, solenoids, high-power LEDs) directly from microcontrollers."
        ),
        "syntax": (
            "MOSFET Key Parameters:\n"
            "V_GS(th) : Gate-Source Threshold Voltage (Voltage where channel begins conducting)\n"
            "R_DS(on) : Drain-Source On-Resistance when fully turned ON (e.g. 5mΩ - 50mΩ)\n"
            "V_GS_max : Absolute maximum Gate-Source voltage (typically ±20V)\n"
            "I_D_max  : Maximum continuous Drain Current\n\n"
            "Power Loss in ON State:\n"
            "P_conduction = I_D^2 * R_DS(on)"
        ),
        "example": (
            "### High-Side PWM Motor Control with N-Channel Logic-Level MOSFET (IRLZ44N)\n\n"
            "Drive a 12V 5A DC Motor using a 3.3V GPIO pin running PWM.\n\n"
            "```python\n"
            "i_drain = 5.0        # 5 Amps Motor Current\n"
            "r_dson = 0.022       # 22 mΩ ON-Resistance at VGS = 3.3V\n\n"
            "# Conduction Power Dissipation\n"
            "p_loss = (i_drain ** 2) * r_dson\n\n"
            "print(f'MOSFET Heat Loss: {p_loss:.2f} Watts')\n"
            "# Output: 0.55 Watts (Minimal heating, no large heatsink required)\n"
            "```"
        ),
        "pitfall": (
            "1. **Using Standard MOSFETs instead of Logic-Level MOSFETs at 3.3V**: Standard MOSFETs require $V_{GS} = 10V$ to turn fully ON; driving them at 3.3V causes high $R_{DS(on)}$ and catastrophic thermal destruction.\n"
            "2. **Leaving the Gate Floating**: Floating Gate accumulates static charge causing erratic partial ON switching; always add a 10kΩ Gate pull-down resistor to Ground.\n"
            "3. **Ignoring Gate Capacitance ($C_{iss}$) in High-Speed PWM**: High gate charge requires high peak driver current during fast PWM switching."
        ),
        "qa": (
            "**Q1: What is a Logic-Level MOSFET?**\n"
            "A: A MOSFET engineered with a low threshold voltage ($V_{GS(th)} < 2.0V$) to turn fully ON ($R_{DS(on)}$ specified) at 3.3V or 5V logic levels.\n\n"
            "**Q2: What is the purpose of a Gate resistor?**\n"
            "A: A small series Gate resistor (22Ω - 100Ω) limits current ringing spikes charging the internal MOSFET Gate capacitance during switching.\n\n"
            "**Q3: How does N-Channel differ from P-Channel MOSFET?**\n"
            "A: N-Channel is used for Low-Side switching (placed between load and GND, turned ON with +VGS); P-Channel is used for High-Side switching (between VCC and load, turned ON by pulling Gate LOW).\n\n"
            "**Q4: What is the Body Diode?**\n"
            "A: An intrinsic internal diode formed between Source and Drain in power MOSFETs."
        )
    },

    "zener-diodes-and-voltage-regulation": {
        "overview": (
            "Zener diodes exploit controlled reverse breakdown voltage to provide simple, low-cost voltage regulation, reference voltages, and overvoltage clamp protection."
        ),
        "concept": (
            "Unlike standard diodes that are damaged by reverse breakdown, Zener diodes are specifically doped to break down predictably at a precise Zener Voltage ($V_Z$). "
            "When reverse-biased above $V_Z$, the voltage across the Zener remains virtually constant over a wide range of reverse currents ($I_Z$)."
        ),
        "syntax": (
            "Zener Shunt Regulator Equations:\n"
            "V_out = V_Z\n"
            "R_series = (V_in - V_Z) / (I_load + I_Z_min)\n\n"
            "Power Dissipation Constraints:\n"
            "P_zener = V_Z * I_Z\n"
            "P_zener_max must not exceed rating (e.g. 500mW or 1W)"
        ),
        "example": (
            "### Designing 3.3V Zener Voltage Clamp for ADC Overvoltage Protection\n\n"
            "Protect a 3.3V MCU ADC input against accidental 12V voltage spikes.\n\n"
            "```python\n"
            "v_spike = 12.0     # Fault Input Voltage\n"
            "v_zener = 3.3     # Clamp Voltage\n"
            "i_zener_target = 0.010 # 10 mA clamp current\n\n"
            "r_limit = (v_spike - v_zener) / i_zener_target\n"
            "p_zener = v_zener * i_zener_target\n\n"
            "print(f'Current Limiting Resistor: {r_limit:.0f} Ω')\n"
            "print(f'Zener Power: {p_zener*1000:.1f} mW')\n"
            "# Use 820 Ω series resistor and 3.3V 500mW Zener\n"
            "```"
        ),
        "pitfall": (
            "1. **Exceeding Maximum Zener Current ($I_{ZT}$)**: Burning out Zener diode during prolonged overvoltage input conditions.\n"
            "2. **Poor Regulation Under Heavy Load**: If load current increases significantly, Zener current drops below $I_{Z(min)}$, causing output voltage regulation to collapse.\n"
            "3. **Zener Voltage Temperature Coefficient**: Zener voltages >5V increase with temperature, while Zeners <5V decrease with temperature."
        ),
        "qa": (
            "**Q1: How is a Zener diode connected for voltage regulation?**\n"
            "A: Connected in REVERSE BIAS across the load with a series current-limiting resistor.\n\n"
            "**Q2: What is the main limitation of a Zener shunt regulator?**\n"
            "A: Extremely poor efficiency at low load currents because unconsumed power is continuously burned in the Zener diode.\n\n"
            "**Q3: Can a Zener diode protect GPIO pins against static/spikes?**\n"
            "A: Yes, Zener diodes or TVS (Transient Voltage Suppressor) diodes clamp overvoltages to safe logic levels.\n\n"
            "**Q4: What is the typical minimum Zener operating current ($I_{ZK}$)?**\n"
            "A: Typically 1mA to 5mA to reach the flat knee region of the V-I curve."
        )
    },

    # ── MODULE 2: Operational Amplifiers ──────────────────────────────────────
    "op-amp-basics": {
        "overview": (
            "Operational Amplifiers (Op-Amps) are versatile analog building blocks used for signal conditioning, filtering, amplification, and mathematical operations in sensor interfacing."
        ),
        "concept": (
            "An Op-Amp is a high-gain DC-coupled differential amplifier with two inputs: Non-Inverting ($V_+$) and Inverting ($V_-$), and one output ($V_{\\text{out}}$). "
            "Ideal Op-Amp Golden Rules:\n"
            "1. **Infinite Input Impedance**: Zero current enters input terminals ($I_+ = I_- = 0$).\n"
            "2. **Virtual Short**: When negative feedback is applied, the op-amp adjusts output to make $V_+ = V_-$."
        ),
        "syntax": (
            "Op-Amp Open Loop Equation:\n"
            "V_out = A_OL * (V_+ - V_-)\n"
            "A_OL = Open-loop gain (typically 100,000+ or 100dB)\n\n"
            "Golden Rules for Negative Feedback:\n"
            "Rule 1: I_+ = 0  and  I_- = 0\n"
            "Rule 2: V_+ = V_-  (Virtual Short)"
        ),
        "example": (
            "### Unity Gain Voltage Follower (Buffer) Circuit\n\n"
            "Connect Output directly back to Inverting Input ($V_-$). Apply sensor voltage to $V_+$.\n\n"
            "```python\n"
            "# Voltage Follower Buffer Analysis\n"
            "# V_out = V_+ (Gain = 1.0)\n"
            "v_sensor = 2.45 # High impedance sensor output\n"
            "v_out = v_sensor\n"
            "print(f'Buffered Output Voltage: {v_out:.2f} V')\n"
            "```\n\n"
            "The Buffer provides high input impedance to the sensor and low output impedance to drive the ADC without loading error."
        ),
        "pitfall": (
            "1. **Exceeding Op-Amp Input Common-Mode Range**: Operating non-rail-to-rail op-amps near supply rails causes phase reversal or distortion.\n"
            "2. **Omitting Power Supply Decoupling Capacitors**: Causes parasitic high-frequency self-oscillation.\n"
            "3. **Ignoring Slew Rate Limits**: High-frequency signals become distorted if required $dV/dt$ exceeds op-amp Slew Rate ($V/\\mu s$)."
        ),
        "qa": (
            "**Q1: What is Negative Feedback?**\n"
            "A: Feeding a portion of the output signal back to the inverting input ($V_-$) to stabilize gain, increase bandwidth, and reduce distortion.\n\n"
            "**Q2: What is a Rail-to-Rail Op-Amp?**\n"
            "A: An op-amp designed so input and output voltage swings can reach the positive and negative power supply rails.\n\n"
            "**Q3: What is Gain-Bandwidth Product (GBW)?**\n"
            "A: Constant product of amplifier gain and cutoff frequency (e.g. 1MHz GBW means Gain=100 has 10kHz bandwidth).\n\n"
            "**Q4: What is Input Offset Voltage?**\n"
            "A: Small differential voltage required between inputs to force output voltage to zero."
        )
    },

    "inverting-and-non-inverting-amplifier": {
        "overview": (
            "Inverting and Non-Inverting amplifiers are the two fundamental closed-loop gain configurations used to scale weak sensor signals to microcontroller levels."
        ),
        "concept": (
            "**Inverting Amplifier**: Input is applied through $R_{\\text{in}}$ to the inverting terminal ($V_-$). The output is inverted (180° phase shift) with Closed-Loop Gain $A_v = -R_f / R_{\\text{in}}$.\n\n"
            "**Non-Inverting Amplifier**: Input is applied directly to non-inverting terminal ($V_+$). The output maintains input phase with Closed-Loop Gain $A_v = 1 + (R_f / R_1)$ and ultra-high input impedance."
        ),
        "syntax": (
            "Inverting Gain Formula:\n"
            "V_out = - (R_f / R_in) * V_in\n"
            "Input Impedance = R_in\n\n"
            "Non-Inverting Gain Formula:\n"
            "V_out = (1 + (R_f / R1)) * V_in\n"
            "Input Impedance = Extremely High (Giga-ohms)"
        ),
        "example": (
            "### Designing Non-Inverting Amplifier for 0-100mV Strain Gauge Sensor\n\n"
            "Amplify 0-100mV sensor output up to 0-3.3V for ESP32 ADC ($A_v = 33$).\n\n"
            "```python\n"
            "v_in_max = 0.100  # 100 mV\n"
            "v_out_max = 3.30  # 3.3V ADC Max\n\n"
            "gain = v_out_max / v_in_max # Gain = 33.0\n\n"
            "# Pick R1 = 1 kΩ\n"
            "r1 = 1000.0\n"
            "r_f = r1 * (gain - 1.0) # 1000 * 32 = 32 kΩ\n\n"
            "print(f'Required Feedback Resistor Rf: {r_f/1000:.1f} kΩ')\n"
            "```"
        ),
        "pitfall": (
            "1. **Saturation at Power Rails**: Attempting to amplify input such that calculated $V_{\\text{out}}$ exceeds supply rail clips the waveform.\n"
            "2. **Low Input Impedance of Inverting Amplifier**: Inverting configuration input impedance equals $R_{\\text{in}}$, which can load weak high-resistance sensors.\n"
            "3. **Using High-Value Resistors (>1MΩ)**: Creates noise and thermal offset errors from input bias currents."
        ),
        "qa": (
            "**Q1: Which configuration offers higher input impedance: Inverting or Non-Inverting?**\n"
            "A: Non-Inverting, because input goes directly to the insulated Op-Amp gate/base.\n\n"
            "**Q2: How do you achieve a gain of less than 1 (attenuation) with an Op-Amp?**\n"
            "A: Use an Inverting Amplifier with $R_f < R_{\\text{in}}$.\n\n"
            "**Q3: Can a single-supply op-amp produce a negative output voltage?**\n"
            "A: No, single-supply op-amps powered from 0V and 5V cannot swing below Ground (0V).\n\n"
            "**Q4: What is Virtual Ground in an inverting amplifier?**\n"
            "A: The inverting node ($V_-$) is held at 0V potential by feedback matching $V_+ = 0V$, though not physically grounded."
        )
    },

    "comparator": {
        "overview": (
            "Comparators compare two analog voltages and output a crisp HIGH or LOW digital signal indicating which input voltage is higher."
        ),
        "concept": (
            "A comparator operates in open-loop mode (no negative feedback). "
            "If $V_+ > V_-$, Output goes saturation HIGH ($V_{CC}$). "
            "If $V_+ < V_-$, Output goes saturation LOW ($GND$). "
            "Hysteresis (positive feedback) is added to prevent output chatter caused by noise near the threshold."
        ),
        "syntax": (
            "Basic Comparator Rule:\n"
            "V_out = HIGH (VCC) if V_+ > V_-\n"
            "V_out = LOW  (GND) if V_+ < V_-\n\n"
            "Hysteresis Thresholds (Schmitt Trigger):\n"
            "V_TH_high = Threshold for switching LOW -> HIGH\n"
            "V_TL_low  = Threshold for switching HIGH -> LOW\n"
            "V_hysteresis = V_TH_high - V_TL_low"
        ),
        "example": (
            "### Over-Temperature Threshold Detector using LM393 Comparator\n\n"
            "Trigger alarm pin HIGH when NTC thermistor node drops below 1.65V (Reference = 1.65V).\n\n"
            "```python\n"
            "v_ref = 1.65    # Set reference voltage on V_-\n"
            "v_sensor = 1.40 # Temperature spiked, V_+ drops to 1.40V\n\n"
            "if v_sensor > v_ref:\n"
            "    state = 'NORMAL (0V)'\n"
            "else:\n"
            "    state = 'ALARM OVERTEMP (5V)'\n\n"
            "print(f'Comparator Output: {state}')\n"
            "```"
        ),
        "pitfall": (
            "1. **Omitting Hysteresis on Noisy Signals**: Causes rapid output oscillation ('chattering') when input is near threshold level.\n"
            "2. **Omitting Pull-Up Resistors on Open-Collector Comparators (LM393)**: Open-collector outputs cannot drive HIGH without an external pull-up resistor to VCC.\n"
            "3. **Using Slow Standard Op-Amps as Fast Comparators**: Standard op-amps have long saturation recovery times when driven into rails."
        ),
        "qa": (
            "**Q1: What is a Schmitt Trigger?**\n"
            "A: A comparator configuration incorporating positive feedback to create hysteresis band for noise immunity.\n\n"
            "**Q2: What is an Open-Collector / Open-Drain Comparator Output?**\n"
            "A: Output stage consisting of an uncommitted internal transistor collector that requires an external pull-up resistor to define the HIGH voltage.\n\n"
            "**Q3: What is the main difference between an Op-Amp and a dedicated Comparator IC?**\n"
            "A: Comparators are optimized for ultra-fast open-loop switching and saturation recovery; op-amps are optimized for linear closed-loop amplification.\n\n"
            "**Q4: How do you adjust hysteresis width?**\n"
            "A: By changing the ratio of the positive feedback resistor to the input resistor."
        )
    },

    "summing-amplifier": {
        "overview": (
            "Summing Amplifiers combine multiple analog input voltages into a single weighted composite output, commonly used in audio mixing and DAC signal reconstruction."
        ),
        "concept": (
            "A Summing Amplifier is an inverting op-amp variant with multiple input resistors ($R_1, R_2, R_3$) connected to the virtual ground node ($V_-$). "
            "Because no current enters $V_-$, the currents from all input branches sum together into the single feedback resistor $R_f$."
        ),
        "syntax": (
            "Summing Amplifier Output Equation:\n"
            "V_out = - R_f * ( (V1 / R1) + (V2 / R2) + (V3 / R3) )\n\n"
            "If R1 = R2 = R3 = R:\n"
            "V_out = - (R_f / R) * (V1 + V2 + V3)"
        ),
        "example": (
            "### 3-Bit R-2R Ladder DAC Summing Stage\n\n"
            "Sum 3 digital signals (V1=3.3V, V2=0V, V3=3.3V) with equal 10kΩ resistors and Rf = 10kΩ.\n\n"
            "```python\n"
            "v1, v2, v3 = 3.3, 0.0, 3.3\n"
            "r1 = r2 = r3 = 10000.0\n"
            "r_f = 10000.0\n\n"
            "v_out = - r_f * ((v1/r1) + (v2/r2) + (v3/r3))\n"
            "print(f'Summed Inverted Output: {v_out:.2f} V')\n"
            "# Followed by Inverting Buffer (Gain=-1) -> +6.60V (scaled down by attenuator)\n"
            "```"
        ),
        "pitfall": (
            "1. **Exceeding Output Rails when Summing Multiple Signals**: Summing multiple positive signals can easily drive output to negative rail limit.\n"
            "2. **Channel Crosstalk**: Unequal input source impedances alter weighting coefficients.\n"
            "3. **Phase Inversion**: Remembering output is inverted relative to input sum unless followed by an inverting stage."
        ),
        "qa": (
            "**Q1: How do you create an averaging amplifier?**\n"
            "A: Set $R_f = R / N$, where $N$ is the number of inputs, making $V_{\\text{out}} = -\\frac{V_1 + V_2 + ... + V_N}{N}$.\n\n"
            "**Q2: Why do input signals not interfere with each other in a summing amplifier?**\n"
            "A: Because they all connect to the Virtual Ground node ($0V$), providing complete isolation between input channels.\n\n"
            "**Q3: Can DC offset voltages be added to AC signals using a summing amplifier?**\n"
            "A: Yes, apply AC signal to $V_1$ and DC offset voltage to $V_2$.\n\n"
            "**Q4: What is an audio mixer circuit?**\n"
            "A: A summing amplifier using potentiometers for each input resistor to adjust channel volume levels."
        )
    },

    "op-amp-applications-in-iot": {
        "overview": (
            "Op-amps are critical interface bridges in IoT nodes for active filtering, instrumentation amplification, current sensing, and photodiode signal conditioning."
        ),
        "concept": (
            "Real-world IoT sensors produce weak, noisy, high-impedance signals (microvolts to millivolts). "
            "Op-amps condition these raw signals through: Instrumentation Amplifiers (differential sensor bridges), Transimpedance Amplifiers (photodiode light sensors), Active Low-Pass Filters (anti-aliasing for ADC), and High-Side Current Shunt Sensing."
        ),
        "syntax": (
            "Instrumentation Amplifier Gain Formula:\n"
            "Gain = 1 + (2 * R1 / R_gain)\n\n"
            "Transimpedance Amplifier (TIA Light Sensor):\n"
            "V_out = I_photodiode * R_feedback\n\n"
            "Active Sallen-Key 2nd Order Low-Pass Cutoff:\n"
            "f_c = 1 / (2 * π * sqrt(R1 * R2 * C1 * C2))"
        ),
        "example": (
            "### Transimpedance Amplifier (TIA) Photodiode Sensor Interface\n\n"
            "Convert 0-10µA photodiode current into 0-3.3V for ESP32 ADC.\n\n"
            "```python\n"
            "i_photo_max = 10.0e-6  # 10 µA max\n"
            "v_adc_max = 3.3        # 3.3V\n\n"
            "# Calculate TIA Feedback Resistor: Rf = V_out / I_in\n"
            "r_f = v_adc_max / i_photo_max\n"
            "print(f'TIA Feedback Resistor: {r_f/1000:.0f} kΩ')\n"
            "# Output: 330 kΩ\n"
            "```"
        ),
        "pitfall": (
            "1. **Aliasing Distortion without Active Anti-Aliasing Filter**: ADC sampling higher frequencies than Nyquist rate distorts readings.\n"
            "2. **High-Side Current Sensing Common-Mode Range**: Standard op-amps fail when sensing current on 12V rails; use dedicated Current Sense Amplifiers (INA180).\n"
            "3. **Photodiode Parasitic Capacitance Instability**: Requires small feedback capacitor across $R_f$ to prevent TIA oscillation."
        ),
        "qa": (
            "**Q1: What is an Instrumentation Amplifier (InAmp)?**\n"
            "A: An integrated 3-op-amp precision differential amplifier providing high Common-Mode Rejection Ratio (CMRR) and high input impedance for Wheatstone bridges.\n\n"
            "**Q2: What is CMRR?**\n"
            "A: Common-Mode Rejection Ratio — ability of an amplifier to reject identical noise present on both differential inputs.\n\n"
            "**Q3: Why is an active filter better than a passive RC filter?**\n"
            "A: Active filters provide gain, sharper cutoff roll-off slopes (-40dB/dec), and eliminate loading impedance issues.\n\n"
            "**Q4: What is Nyquist theorem?**\n"
            "A: Sampling frequency must be at least 2x the highest signal frequency to prevent aliasing."
        )
    },

    # ── MODULE 3: Digital Electronics ─────────────────────────────────────────
    "number-systems": {
        "overview": (
            "Binary (Base-2), Hexadecimal (Base-16), and Decimal (Base-10) are the core numerical representations used in microcontrollers, memory addresses, and bitwise operations."
        ),
        "concept": (
            "Computers operate exclusively on Binary digits (Bits: 0 and 1) representing low and high voltages. "
            "Hexadecimal groups 4 binary bits (a Nibble) into a single compact character (0-9, A-F), simplifying memory address reading and register configuration."
        ),
        "syntax": (
            "Base Systems:\n"
            "Binary (0b)       : Base 2  [Digits: 0, 1]\n"
            "Decimal           : Base 10 [Digits: 0-9]\n"
            "Hexadecimal (0x)   : Base 16 [Digits: 0-9, A, B, C, D, E, F]\n\n"
            "Byte & Bit Sizes:\n"
            "1 Bit = 0 or 1\n"
            "1 Nibble = 4 Bits  (e.g. 0b1010 = 0xA)\n"
            "1 Byte = 8 Bits    (Range: 0 - 255 Unsigned / -128 to +127 Signed 2's Comp)\n"
            "1 Word = 16 Bits or 32 Bits (MCU Architecture dependent)"
        ),
        "example": (
            "### Python Number Base Conversions & Bitwise Operations\n\n"
            "```python\n"
            "value = 0x3A # Hexadecimal 0x3A\n\n"
            "dec_val = int(value)\n"
            "bin_val = bin(value)\n"
            "hex_val = hex(value)\n\n"
            "print(f'Decimal: {dec_val}')     # 58\n"
            "print(f'Binary: {bin_val}')       # 0b111010\n"
            "print(f'Hex: {hex_val}')         # 0x3a\n"
            "```"
        ),
        "pitfall": (
            "1. **Signed Integer Overflow in 2's Complement**: Incrementing +127 in signed 8-bit int flips bit 7, yielding -128.\n"
            "2. **Endianness Confusion**: Little-Endian (ARM Cortex-M) stores least-significant byte first in memory; Big-Endian stores most-significant byte first.\n"
            "3. **Off-by-One Bit Shifts**: Shifting bits beyond data type width causes silent truncation."
        ),
        "qa": (
            "**Q1: How do you represent negative numbers in binary?**\n"
            "A: Using Two's Complement: Invert all bits (1's complement) and add 1.\n\n"
            "**Q2: What is 0xFF in decimal?**\n"
            "A: 255 (Max unsigned 8-bit value).\n\n"
            "**Q3: How many hex digits represent a 32-bit register?**\n"
            "A: 8 hex digits (e.g. `0x40021000`).\n\n"
            "**Q4: What is ASCII?**\n"
            "A: 7-bit/8-bit binary code mapping numbers 0-127 to printable characters."
        )
    },

    "logic-gates": {
        "overview": (
            "Logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR) are the primitive digital building blocks executing Boolean logic in silicon."
        ),
        "concept": (
            "Logic gates process high (1 / VCC) and low (0 / GND) voltage states. "
            "NAND and NOR are Universal Gates because any arbitrary Boolean logic function can be constructed using exclusively NAND or NOR gates."
        ),
        "syntax": (
            "Truth Tables Summary:\n"
            "AND  : Y = A • B       (HIGH only if A=1 AND B=1)\n"
            "OR   : Y = A + B       (HIGH if A=1 OR B=1)\n"
            "NOT  : Y = Ā           (Inverts input)\n"
            "NAND : Y = NOT(A • B)  (LOW only if A=1 AND B=1)\n"
            "NOR  : Y = NOT(A + B)  (HIGH only if A=0 AND B=0)\n"
            "XOR  : Y = A ⊕ B       (HIGH if inputs are DIFFERENT)\n"
            "XNOR : Y = NOT(A ⊕ B)  (HIGH if inputs are IDENTICAL)"
        ),
        "example": (
            "### Python Bitwise Operations Equivalent to Logic Gates\n\n"
            "```python\n"
            "a = 0b1100\n"
            "b = 0b1010\n\n"
            "print(f'AND : {bin(a & b)}')  # 0b1000\n"
            "print(f'OR  : {bin(a | b)}')  # 0b1110\n"
            "print(f'XOR : {bin(a ^ b)}')  # 0b0110\n"
            "print(f'NOT : {bin(~a & 0xF)}') # 0b0011\n"
            "```"
        ),
        "pitfall": (
            "1. **Leaving CMOS Logic Gate Inputs Unconnected**: Unused CMOS gate inputs float, pick up EMI noise, and cause high shoot-through supply current.\n"
            "2. **Confusing Bitwise (&, |) with Logical (&&, ||) Operators in C**: Bitwise evaluates bit-by-bit; logical evaluates truthiness of entire expression.\n"
            "3. **Propagation Delay Accumulation**: Chaining many gate stages introduces propagation delay skew in high-speed clocks."
        ),
        "qa": (
            "**Q1: Why are NAND gates called universal gates?**\n"
            "A: Because AND, OR, NOT, and XOR functions can all be implemented using combinations of NAND gates.\n\n"
            "**Q2: What is the XOR gate used for in digital arithmetic?**\n"
            "A: XOR performs binary addition without carry (Sum output of Half Adder).\n\n"
            "**Q3: What should you do with unused inputs on a 74HC00 NAND chip?**\n"
            "A: Tie unused input pins to VCC or GND.\n\n"
            "**Q4: What is De Morgan's Law?**\n"
            "A: $\\overline{A \\cdot B} = \\bar{A} + \\bar{B}$ and $\\overline{A + B} = \\bar{A} \\cdot \\bar{B}$."
        )
    },

    "combinational-circuits": {
        "overview": (
            "Combinational logic circuits compute outputs based purely on current inputs without memory (e.g. Multiplexers, Decoders, Adders)."
        ),
        "concept": (
            "In combinational logic, output state depends strictly on instant input combinations. "
            "Key ICs:\n"
            "- **Multiplexer (MUX)**: Selects 1 of $N$ input channels to route to a single output using $S$ select lines.\n"
            "- **Decoder / Demultiplexer**: Converts binary code into single active output line.\n"
            "- **Adder**: Performs binary addition (Half Adder & Full Adder)."
        ),
        "syntax": (
            "Multiplexer 4-to-1 Equation:\n"
            "Y = (I0 • S1' • S0') + (I1 • S1' • S0) + (I2 • S1 • S0') + (I3 • S1 • S0)\n\n"
            "Full Adder Equations:\n"
            "Sum   = A ⊕ B ⊕ C_in\n"
            "C_out = (A • B) + (C_in • (A ⊕ B))"
        ),
        "example": (
            "### Expanding Microcontroller Analog Inputs using CD74HC4067 16-Channel Analog MUX\n\n"
            "```python\n"
            "# Select Analog Channel 9 (Binary 1001) using 4 GPIO Select Pins (S0-S3)\n"
            "channel = 9\n"
            "s0 = (channel >> 0) & 1 # 1\n"
            "s1 = (channel >> 1) & 1 # 0\n"
            "s2 = (channel >> 2) & 1 # 0\n"
            "s3 = (channel >> 3) & 1 # 1\n\n"
            "print(f'Select Pins [S3 S2 S1 S0] = [{s3} {s2} {s1} {s0}]')\n"
            "# Set MCU GPIOs to 1, 0, 0, 1 to read Channel 9 on single ADC pin\n"
            "```"
        ),
        "pitfall": (
            "1. **Glitching (Glitches/Race Conditions)**: Temporary incorrect output spikes occurring when inputs transition due to unequal gate delays.\n"
            "2. **Analog MUX On-Resistance ($R_{on}$)**: Analog multiplexers introduce internal resistance (~70Ω) affecting analog readings.\n"
            "3. **Exceeding MUX Voltage Range**: Passing negative or overvoltage signals through 74HC4067 MUX clamps/distorts signals."
        ),
        "qa": (
            "**Q1: What is the difference between a Multiplexer and Demultiplexer?**\n"
            "A: MUX routes multiple inputs to 1 output; DEMUX routes 1 input to multiple outputs.\n\n"
            "**Q2: How many select lines does an 8-to-1 MUX require?**\n"
            "A: 3 select lines ($2^3 = 8$).\n\n"
            "**Q3: What is a Priority Encoder?**\n"
            "A: Encoder that outputs binary code of highest-priority active input line.\n\n"
            "**Q4: What is a BCD to 7-Segment Decoder?**\n"
            "A: IC (e.g. 74HC4511) converting 4-bit binary coded decimal into 7 segment outputs for LED displays."
        )
    },

    "sequential-circuits": {
        "overview": (
            "Sequential logic incorporates memory elements (Flip-Flops, Latches) where outputs depend on current inputs and past state history, driven by clock pulses."
        ),
        "concept": (
            "Unlike combinational logic, sequential circuits store state using memory elements. "
            "Flip-Flops (D-Type, JK, T) update output state on clock edges (Rising/Falling). "
            "Registers, Counters, and Shift Registers (74HC595) are fundamental sequential blocks."
        ),
        "syntax": (
            "D Flip-Flop Characteristic:\n"
            "Q(next) = D  (sampled on Clock Edge)\n\n"
            "T Flip-Flop (Toggle / Frequency Divider):\n"
            "Q(next) = Q' if T=1 on Clock Edge (Divides frequency by 2)\n\n"
            "74HC595 Shift Register Pins:\n"
            "DS    : Serial Data Input\n"
            "SHCP  : Shift Register Clock\n"
            "STCP  : Storage Latch Clock\n"
            "Q0-Q7 : 8 Parallel Outputs"
        ),
        "example": (
            "### Bit-Banging 8-Bit Data to 74HC595 Shift Register\n\n"
            "```python\n"
            "# Python simulation of 74HC595 Shift Register\n"
            "def shift_out(data_byte):\n"
            "    parallel_pins = [0] * 8\n"
            "    for bit in range(8):\n"
            "        # Extract MSB first\n"
            "        bit_val = (data_byte >> (7 - bit)) & 1\n"
            "        parallel_pins[bit] = bit_val\n"
            "    return parallel_pins\n\n"
            "pins = shift_out(0b10110001)\n"
            "print(f'Parallel Outputs Q7..Q0: {pins}')\n"
            "```"
        ),
        "pitfall": (
            "1. **Violating Setup and Hold Times**: Changing D input too close to clock edge causes **Metastability** (unpredictable floating state).\n"
            "2. **Clock Jitter / Bouncing Clocks**: Mechanical switch noise on clock pins causes multiple unwanted flip-flop triggers.\n"
            "3. **Asynchronous Reset Hazards**: Glitches on asynchronous Clear/Reset lines unintentionally wipe registers."
        ),
        "qa": (
            "**Q1: What is the difference between a Latch and a Flip-Flop?**\n"
            "A: A Latch is level-triggered (transparent when EN is high); a Flip-Flop is edge-triggered (samples on clock transition).\n\n"
            "**Q2: What is Metastability?**\n"
            "A: Hazardous state where flip-flop output hovers in an invalid intermediate voltage between 0 and 1 when setup/hold time is violated.\n\n"
            "**Q3: How does a 74HC595 shift register expand MCU GPIO pins?**\n"
            "A: Uses 3 MCU pins (Data, Clock, Latch) to drive 8 or more parallel outputs.\n\n"
            "**Q4: How do you construct a divide-by-2 frequency counter?**\n"
            "A: Connect Q-bar back to D input on a D Flip-Flop."
        )
    },

    "digital-ic-families": {
        "overview": (
            "Digital IC Families (TTL vs CMOS: 74HC, 74HCT, 74LVC) define voltage thresholds, switching speed, power consumption, and logic level compatibility."
        ),
        "concept": (
            "**TTL (Transistor-Transistor Logic)**: Uses BJTs (5V supply). $V_{IH} = 2.0V$, $V_{IL} = 0.8V$. Higher static power consumption.\n\n"
            "**CMOS (Complementary MOS)**: Uses PMOS+NMOS pairs (1.8V-5V). Low static power, high input impedance. Thresholds scale as percentage of VCC ($V_{IH} = 0.7V_{CC}$)."
        ),
        "syntax": (
            "Logic Threshold Voltage Comparison:\n"
            "5V TTL     : V_IL = 0.8V, V_IH = 2.0V\n"
            "5V CMOS    : V_IL = 1.5V, V_IH = 3.5V\n"
            "3.3V LVCMOS: V_IL = 0.8V, V_IH = 2.0V\n\n"
            "Compatibility Issue:\n"
            "3.3V Output (VOH = 3.0V) -> Drives 5V TTL (VIH = 2.0V)  -> OK!\n"
            "3.3V Output (VOH = 3.0V) -> Drives 5V CMOS (VIH = 3.5V) -> FAILS! Requires Level Shifter!"
        ),
        "example": (
            "### Logic Level Shifting between 5V Sensor and 3.3V ESP32\n\n"
            "```python\n"
            "# Bidirectional MOSFET Level Shifter Simulation\n"
            "v_hv = 5.0  # 5V Sensor side\n"
            "v_lv = 3.3  # 3.3V ESP32 side\n\n"
            "# 5V TX to 3.3V RX via Voltage Divider (1k / 2k)\n"
            "r1, r2 = 1000.0, 2000.0\n"
            "v_esp_rx = v_hv * (r2 / (r1 + r2))\n"
            "print(f'Scaled 5V Signal to ESP32 RX: {v_esp_rx:.2f} V')\n"
            "# Output: 3.33V (Safe for 3.3V MCU)\n"
            "```"
        ),
        "pitfall": (
            "1. **Connecting 5V Logic Directly to Non-5V-Tolerant 3.3V MCU Pins**: Overvoltage destroys internal ESD protection diodes and GPIO silicon.\n"
            "2. **Assuming 74HC Inputs Work with 3.3V Logic on 5V VCC**: 74HC requires $V_{IH} = 3.5V$ at 5V VCC; 3.3V signal is ignored! Use **74HCT** (TTL thresholds at 5V VCC).\n"
            "3. **Floating CMOS Inputs**: Unused CMOS inputs oscillate between rails, causing excessive power draw."
        ),
        "qa": (
            "**Q1: What does the 'T' in 74HCT stand for?**\n"
            "A: TTL-compatible inputs (allows 3.3V/5V TTL signals to drive the 5V CMOS IC).\n\n"
            "**Q2: What is Noise Margin?**\n"
            "A: Difference between worst-case output voltage ($V_{OH}/V_{OL}$) and input threshold voltage ($V_{IH}/V_{IL}$) providing immunity against noise spikes.\n\n"
            "**Q3: Are ESP32 GPIO pins 5V tolerant?**\n"
            "A: Official datasheet specifies ESP32 pins are NOT 5V tolerant (Max 3.6V).\n\n"
            "**Q4: What is Fan-Out?**\n"
            "A: Maximum number of digital gate inputs a single digital output can drive without signal degradation."
        )
    },

    # ── MODULE 4: Practical Electronics ───────────────────────────────────────
    "soldering-techniques": {
        "overview": (
            "Soldering creates reliable metallurgical and electrical joints between electronic components and PCB pads using molten filler metal."
        ),
        "concept": (
            "Soldering relies on wetting: molten solder alloy (60/40 Lead-Tin or SAC300 Lead-Free) dissolves a microscopic layer of copper to form an intermetallic bond. "
            "Flux removes copper oxides during heating to allow clean solder flow."
        ),
        "syntax": (
            "Soldering Temperatures:\n"
            "Leaded Solder (Sn63/Pb37)   : Melt Temp = 183°C, Iron Set = 315°C - 340°C\n"
            "Lead-Free (SAC305)          : Melt Temp = 217°C, Iron Set = 350°C - 370°C\n\n"
            "Ideal Joint Anatomy:\n"
            "- Concave fillet shape (like a shiny volcano)\n"
            "- Smooth 45° wetting angle against component lead and copper pad"
        ),
        "example": (
            "### 4-Step Through-Hole Soldering Technique\n\n"
            "1. Clean PCB pad and component lead with isopropyl alcohol.\n"
            "2. Apply heated iron tip simultaneously to BOTH the copper pad and component lead for 1.5 - 2 seconds.\n"
            "3. Feed solder wire into the JUNCTION of pad and tip (NOT directly onto the iron tip) until concave fillet forms.\n"
            "4. Remove solder wire first, then remove iron tip; allow joint to cool undisturbed for 3 seconds."
        ),
        "pitfall": (
            "1. **Cold Solder Joint**: Moving component while cooling or insufficient heat creates dull, grainy, high-resistance unreliable joint.\n"
            "2. **Solder Bridges**: Excess solder shorts adjacent fine-pitch pins; fix using desoldering braid/wick and flux.\n"
            "3. **Thermal Damage to ICs**: Applying iron tip longer than 5 seconds overheats semiconductor die."
        ),
        "qa": (
            "**Q1: Why is flux essential in soldering?**\n"
            "A: Flux removes surface oxidation from metals when heated, preventing re-oxidation so solder wets cleanly.\n\n"
            "**Q2: What causes a 'Cold Joint'?**\n"
            "A: Insufficient heat transfer or physical movement during solder solidification.\n\n"
            "**Q3: How do you clean flux residue from a finished PCB?**\n"
            "A: Scrub with 99% Isopropyl Alcohol (IPA) and an ESD-safe brush.\n\n"
            "**Q4: What is Desoldering Braid (Wick)?**\n"
            "A: Finely woven copper wire pre-coated with flux that absorbs molten unwanted solder via capillary action."
        )
    },

    "pcb-reading-and-assembly": {
        "overview": (
            "Printed Circuit Board (PCB) assembly converts schematics into physical hardware products using copper traces, surface-mount (SMD), and through-hole (THD) components."
        ),
        "concept": (
            "A PCB consists of FR4 fiberglass substrate layered with copper traces (typically 1 oz/sq.ft = 35µm thickness). "
            "Silkscreen prints component reference designators and pin 1 indicators. Solder mask covers non-soldered copper to prevent short circuits."
        ),
        "syntax": (
            "PCB Layer Breakdown:\n"
            "Copper Layers     : Top / Bottom / Inner (Signal, Power, GND Planes)\n"
            "Solder Mask       : Protective green/black/blue polymer coating\n"
            "Silkscreen        : White text layer (R1, C1, U1, pin numbers, logos)\n"
            "Vias              : Plated holes connecting traces across different layers\n"
            "Component Types   : THD (Through-Hole Device) vs SMD/SMT (Surface Mount)"
        ),
        "example": (
            "### Assembly Order Checklist for Populating PCBA\n\n"
            "1. Inspection: Verify PCB for shorts/opens using schematic netlist.\n"
            "2. Lowest Height Components First: Solder SMD resistors, capacitors, and diodes.\n"
            "3. Medium Components: Solder ICs, transistors, and small modules.\n"
            "4. Tallest Components Last: Solder electrolytic caps, connectors, terminal blocks, headers.\n"
            "5. Post-Assembly Cleanup & Visual Inspection under microscope."
        ),
        "pitfall": (
            "1. **Reverse IC Orientation**: Aligning Pin 1 dot/notch incorrectly damages IC upon power-up.\n"
            "2. **Tombstoning in SMD Reflow**: Unequal thermal mass or solder paste application causes SMD chip resistor to lift vertically on one pad.\n"
            "3. **Insufficient Thermal Relief Nets on Ground Plane**: Soldering pads connected to large ground planes without thermal relief spokes dissipates heat into board faster than iron can supply."
        ),
        "qa": (
            "**Q1: How is Pin 1 identified on an IC chip?**\n"
            "A: Identified by a small circular dot mark near Pin 1 or a U-shaped notch at top of IC package.\n\n"
            "**Q2: What is a Via?**\n"
            "A: A copper-plated hole drilled through PCB layers to electrically route signals between layers.\n\n"
            "**Q3: What is thermal relief on PCB pads?**\n"
            "A: Pattern connecting a pad to a copper plane using narrow spokes to prevent heat sinking during soldering.\n\n"
            "**Q4: What is FR4?**\n"
            "A: Standard flame-retardant glass-reinforced epoxy laminate material used as PCB substrate."
        )
    },

    "signal-conditioning": {
        "overview": (
            "Signal conditioning modifies raw sensor signals through filtering, amplification, attenuation, and isolation to match microcontroller ADC sampling requirements."
        ),
        "concept": (
            "Real-world sensor signals are often noisy, weak, offset from 0V, or contain unwanted high-frequency interference. "
            "Signal conditioning stages:\n"
            "1. Attenuation / Level Shifting\n"
            "2. Low-Pass RC / Active Filtering\n"
            "3. Amplification (Op-Amp)\n"
            "4. Galvanic Isolation (Optocoupler)"
        ),
        "syntax": (
            "RC Passive Low-Pass Filter:\n"
            "f_cutoff = 1 / (2 * π * R * C)\n"
            "Attenuation at f > f_c = -20 dB/decade\n\n"
            "Optocoupler Galvanic Isolation:\n"
            "Input : LED (Current limited by R_in)\n"
            "Output: Phototransistor (Completely electrically isolated from input)"
        ),
        "example": (
            "### Python Simulation of RC Low-Pass Filter on Noisy ADC Data\n\n"
            "```python\n"
            "# Exponential Moving Average (Digital Software RC Filter)\n"
            "def rc_filter(new_sample, prev_output, alpha=0.1):\n"
            "    return (alpha * new_sample) + ((1.0 - alpha) * prev_output)\n\n"
            "filtered_val = 0.0\n"
            "raw_samples = [1.2, 3.5, 1.3, 1.4, 1.2, 4.0, 1.3] # Spikes at index 1 and 5\n\n"
            "for sample in raw_samples:\n"
            "    filtered_val = rc_filter(sample, filtered_val)\n"
            "    print(f'Raw: {sample:.1f}V -> Filtered: {filtered_val:.2f}V')\n"
            "```"
        ),
        "pitfall": (
            "1. **Impedance Mismatching Between Filter and ADC**: Low ADC input resistance shifts passive RC filter cutoff frequency.\n"
            "2. **Omitting Anti-Aliasing Filter Before ADC**: High frequency noise folds back into measurement band as false low-frequency signals.\n"
            "3. **Ignoring Optocoupler CTR (Current Transfer Ratio)**: CTR drops over age and temperature, causing incomplete switching."
        ),
        "qa": (
            "**Q1: What is Galvanic Isolation?**\n"
            "A: Complete electrical separation between two circuits (no shared ground/DC path), preventing high-voltage ground loops and safety hazards.\n\n"
            "**Q2: What is an Optocoupler (Optoisolator)?**\n"
            "A: Component using light (internal LED and phototransistor) to transfer signals across an isolation barrier.\n\n"
            "**Q3: What is the purpose of an anti-aliasing filter?**\n"
            "A: Low-pass filter removing frequencies above half the ADC sampling rate (Nyquist frequency).\n\n"
            "**Q4: How do you convert a 4-20mA industrial current loop sensor to 0-3.3V for MCU ADC?**\n"
            "A: Pass 4-20mA current through a precision 165Ω resistor ($V = 0.020A \\times 165\\Omega = 3.3V$ max)."
        )
    },

    "emi-and-noise-reduction": {
        "overview": (
            "Electromagnetic Interference (EMI) and noise reduction techniques shield Sensitive IoT circuits from switching transients, RF interference, and ground loops."
        ),
        "concept": (
            "Noise enters circuits via Conducted Emissions (power lines, shared ground traces) or Radiated Emissions (electromagnetic fields). "
            "Mitigation strategies:\n"
            "1. Decoupling capacitors (0.1µF MLCC + 10µF Tantalum)\n"
            "2. Solid Ground Planes (minimize ground loop area)\n"
            "3. Shielded cables & Twisted pair wires (cancel differential noise)\n"
            "4. Ferrite Beads on power entries"
        ),
        "syntax": (
            "Differential Mode vs Common Mode Noise:\n"
            "V_diff   = V_signal1 - V_signal2  (Desired Data)\n"
            "V_common = (V_signal1 + V_signal2) / 2 (Corrupting Noise)\n\n"
            "Twisted Pair Rejection:\n"
            "Equal noise induced in both twisted wires cancels out in differential receiver"
        ),
        "example": (
            "### PCB Layout Rules for Low-Noise Analog Design\n\n"
            "1. **Star Grounding**: Separate Analog Ground (AGND) from Digital Ground (DGND), connecting them at a SINGLE star point under ADC IC.\n"
            "2. **Continuous Ground Plane**: Never split ground planes under high-speed data traces.\n"
            "3. **Bypass Capacitors**: Place 100nF ceramic cap within < 2mm of every IC power pin.\n"
            "4. **Trace Angle**: Use 45° bends instead of 90° right angles on high-speed traces to minimize EMI reflection."
        ),
        "pitfall": (
            "1. **Creating Ground Loops**: Connecting ground at multiple points creates a loop antenna picking up magnetic AC hum.\n"
            "2. **Running High-Speed Digital Traces Parallel to Sensitive Analog Inputs**: Capacitive crosstalk corrupts sensor readings.\n"
            "3. **Omitting Ferrite Beads on DC Power Entrances**: Allows switching noise from AC adapters to enter MCU board."
        ),
        "qa": (
            "**Q1: What is a Ground Loop?**\n"
            "A: Unwanted current path formed when two connected devices ground at different potential points, creating circulating noise currents.\n\n"
            "**Q2: Why are differential signals (like RS485, CAN bus, USB) highly immune to noise?**\n"
            "A: Because noise affects both twisted signal lines equally, and the receiver measures the difference ($V_+ - V_-$), cancelling out common noise.\n\n"
            "**Q3: What is a Faraday Shield?**\n"
            "A: Metal enclosure surrounding sensitive electronics grounded to block external RF fields.\n\n"
            "**Q4: What capacitor value is standard for high-frequency MCU decoupling?**\n"
            "A: 0.1 µF (100 nF) surface-mount ceramic capacitor."
        )
    },

    "datasheets-and-component-selection": {
        "overview": (
            "Reading datasheets proficiently allows engineers to select optimal components, verify absolute maximum ratings, and extract critical operating specs."
        ),
        "concept": (
            "A Datasheet is the legal technical specification document published by component manufacturers. "
            "Key sections:\n"
            "1. **Features & Description**\n"
            "2. **Absolute Maximum Ratings** (Destruction limits! Never exceed!)\n"
            "3. **Electrical Characteristics** (Min, Typ, Max operating specs)\n"
            "4. **Pin Configuration & Functional Block Diagram**\n"
            "5. **Typical Application Schematics & Mechanical Package Dimensions**"
        ),
        "syntax": (
            "Critical Datasheet Parameters to Audit:\n"
            "Absolute Max Ratings : V_CC_max, I_out_max, T_junction_max (DO NOT OPERATE HERE!)\n"
            "Operating Conditions : V_CC_recommended, T_ambient (-40°C to +85°C Industrial)\n"
            "Quiescent Current    : I_Q (Current drawn when idle — critical for battery life!)\n"
            "Package Footprint    : SOT-23, SOIC-8, QFN-32, LQFP-48"
        ),
        "example": (
            "### Component Selection Decision Matrix for Battery IoT Node\n\n"
            "```python\n"
            "# Comparing LDO Regulators for 3.3V 100mA Battery Sensor Node\n"
            "ldos = [\n"
            "    {'name': 'AMS1117-3.3', 'iq_ua': 5000, 'vdrop_mv': 1100, 'cost_usd': 0.10},\n"
            "    {'name': 'MCP1700-3302', 'iq_ua': 1.6,   'vdrop_mv': 178,  'cost_usd': 0.35},\n"
            "    {'name': 'TPS7A02',     'iq_ua': 0.025, 'vdrop_mv': 205,  'cost_usd': 0.75},\n"
            "]\n\n"
            "# Select lowest quiescent current (Iq) for multi-year battery node\n"
            "best = min(ldos, key=lambda x: x['iq_ua'])\n"
            "print(f\"Best Battery LDO: {best['name']} (Iq = {best['iq_ua']} µA)\")\n"
            "# Output: MCP1700 or TPS7A02 for ultra-low sleep current!\n"
            "```"
        ),
        "pitfall": (
            "1. **Designing at Absolute Maximum Ratings**: Operating a chip at its 6.0V max rating when recommended is 5.5V causes catastrophic field failures.\n"
            "2. **Ignoring Package Thermal Resistance ($R_{\\theta JA}$)**: Overlooking thermal limits leads to thermal throttling or component burnout.\n"
            "3. **Not Checking Component Availability and Lifecycle Status**: Selecting NRND (Not Recommended for New Designs) or EOL (End of Life) components delays production."
        ),
        "qa": (
            "**Q1: What does Absolute Maximum Rating mean in a datasheet?**\n"
            "A: Stress limits beyond which permanent physical damage to the device will occur; not intended for functional operation.\n\n"
            "**Q2: What is Quiescent Current ($I_Q$)?**\n"
            "A: Circuit current consumed by the IC itself when operating with zero load output.\n\n"
            "**Q3: What does EOL stand for in component sourcing?**\n"
            "A: End of Life — manufacturer is discontinuing production of the component.\n\n"
            "**Q4: What is the industrial operating temperature range?**\n"
            "A: Industrial range is -40°C to +85°C (Commercial is 0°C to +70°C, Automotive is -40°C to +125°C)."
        )
    }
}


def populate_electronics_content():
    with app.app_context():
        course = Course.query.filter_by(slug='electronics-basics', is_deleted=False).first()
        if not course:
            print("[ERROR] Course electronics-basics not found!")
            return

        print(f"Populating content for course: {course.title} ({course.slug})")

        total_sections = 0
        published_lessons = 0

        for mod in course.modules.all():
            print(f"\n--- Module: {mod.title} ---")
            for lesson in mod.lessons.filter_by(is_deleted=False).all():
                lesson_data = ELECTRONICS_LESSON_CONTENT.get(lesson.slug)
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
        print(f"Course 'electronics-basics' is now fully PUBLISHED.")
        print(f"========================================================")


if __name__ == "__main__":
    populate_electronics_content()
