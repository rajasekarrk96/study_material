# Raspberry Pi Hardware Overview

> **Course**: Raspberry Pi | **Module**: Raspberry Pi Fundamentals | **Difficulty**: beginner

---

The Raspberry Pi is a single-board computer (SBC) featuring a Broadcom ARM SoC, 40-pin GPIO header, HDMI outputs, USB, Ethernet, and Wi-Fi.

---

Unlike microcontrollers that execute bare-metal loops, the Raspberry Pi runs a full Linux Operating System (Raspberry Pi OS), supporting multi-threading, Python, Docker, and complex networking.

---

40-Pin GPIO Header Summary:
- 3.3V Power (Pins 1, 17)
- 5V Power (Pins 2, 4)
- Ground (Pins 6, 9, 14, 20, 25, 30, 34, 39)
- GPIO Pins (BCM numbering 2-27)

---

### Inspecting Raspberry Pi System Specs via Terminal

```bash
# Check CPU Info
cat /proc/cpuinfo

# Check RAM Memory Usage
free -h

# Check CPU Temperature
vcgencmd measure_temp
```

---

1. Powering Pi with insufficient 5V USB adapter causes brownout undervoltage throttles (yellow lightning bolt icon).
2. Unplugging power without running `sudo shutdown` corrupts microSD card file system.

---

**Q1: What is the difference between BCM and BOARD pin numbering?**
A: BOARD uses physical pin position (1-40); BCM uses Broadcom SOC GPIO channel numbers.

---
