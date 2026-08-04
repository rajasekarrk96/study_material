# Power and Energy

> **Course**: Electrical Fundamentals | **Module**: Basic Electrical Theory | **Difficulty**: beginner

---

Power determines heat generation and energy consumption in IoT devices. Calculating power dissipation is critical for thermal management and battery life estimation.

---



---

Electrical Power (P) is the rate at which electrical energy is converted into another energy form (such as heat, light, or mechanical motion), measured in Watts (W = J/s). Electrical Energy (E) is the total power consumed over time (E = P * t), typically measured in Joules (J) or Watt-hours (Wh) / milliamp-hours (mAh) for battery-operated IoT sensors.

---

Power Equations:
P = V * I             (Watts)
P = I^2 * R           (Resistive heat loss)
P = V^2 / R           (Voltage-driven power)

Energy Equations:
E = P * t             (Joules when t in seconds, Wh when t in hours)
Battery Capacity (Wh) = Nominal Voltage (V) * Battery Capacity (Ah)
Battery Life (hours)  = Battery Capacity (mAh) / Average Current Draw (mA)

---

### Calculating ESP32 Battery Life on a 2500 mAh LiPo Cell

An IoT sensor wakes up for 2 seconds every 60 seconds. Active current = 120 mA, Deep Sleep current = 15 µA (0.015 mA).

```python
# Battery Life Estimation Script
battery_capacity_mah = 2500.0

active_current_ma = 120.0
active_time_sec = 2.0

sleep_current_ma = 0.015
sleep_time_sec = 58.0

total_cycle_sec = active_time_sec + sleep_time_sec

# Average Current Draw over 1 cycle
avg_current_ma = ((active_current_ma * active_time_sec) + (sleep_current_ma * sleep_time_sec)) / total_cycle_sec

# Battery Runtime in Hours and Days
runtime_hours = battery_capacity_mah / avg_current_ma
runtime_days = runtime_hours / 24.0

print(f'Average Current: {avg_current_ma:.3f} mA')
print(f'Estimated Runtime: {runtime_days:.1f} days ({runtime_days/365:.2f} years)')
```

---

1. **Disregarding Self-Discharge Rates**: Real batteries discharge 1-3% per month naturally even in deep sleep.
2. **Thermal Runaway**: Overpowering linear voltage regulators (like L7805) without heat sinks causes thermal shutdown.
3. **Inaccurate Duty Cycle Duty Estimates**: Forgetting power spikes during Wi-Fi transmission connects severely shortens runtime.

---

**Q1: What is the difference between Power and Energy?**
A: Power is instantaneous work rate (Watts), while energy is the accumulated work performed over a period of time (Watt-hours or Joules).

**Q2: How do you convert 1 kWh into Joules?**
A: 1 kWh = 1000 W * 3600 s = 3.6 x 10^6 Joules = 3.6 MJ.

**Q3: Why do linear regulators get hot?**
A: Linear regulators drop excess voltage by dissipating power as pure heat: P_heat = (V_in - V_out) * I_load.

**Q4: What is the rating of 18650 Li-ion cell in Watt-hours if rated 3.7V 3000mAh?**
A: E = 3.7V * 3.0Ah = 11.1 Wh.

---

**Q1: What is the difference between Power and Energy?**
A: Power is instantaneous work rate (Watts), while energy is the accumulated work performed over a period of time (Watt-hours or Joules).

**Q2: How do you convert 1 kWh into Joules?**
A: 1 kWh = 1000 W * 3600 s = 3.6 x 10^6 Joules = 3.6 MJ.

**Q3: Why do linear regulators get hot?**
A: Linear regulators drop excess voltage by dissipating power as pure heat: P_heat = (V_in - V_out) * I_load.

**Q4: What is the rating of 18650 Li-ion cell in Watt-hours if rated 3.7V 3000mAh?**
A: E = 3.7V * 3.0Ah = 11.1 Wh.

---



---



---



---



---
