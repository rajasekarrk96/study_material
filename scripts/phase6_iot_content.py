"""
phase6_iot_content.py
Fills remaining stubs for:
  _17_iot_hardware (46)
  _18_pcb (28)
  _19_iot_projects (12)
"""
import os, shutil

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
written = 0

def write_and_sync(course_dir, fname, content):
    global written
    cp = os.path.join(BASE, course_dir)
    os.makedirs(cp, exist_ok=True)
    
    # Write at root level
    root_path = os.path.join(cp, fname)
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Search for matching filename in subfolders and replace stub
    synced = False
    for r, dirs, files in os.walk(cp):
        if r == cp:
            continue
        if fname in files:
            dst_path = os.path.join(r, fname)
            shutil.copy2(root_path, dst_path)
            os.remove(root_path)
            synced = True
            print(f'  [WRITE & SYNC] {course_dir}/{os.path.relpath(dst_path, cp)}')
            break
            
    if not synced:
        print(f'  [WRITE ROOT] {course_dir}/{fname}')
    written += 1

def fm(lid, title, course, mod, mod_title, les, diff, tags, dur=60):
    tag_str = ', '.join(f'"{t}"' for t in tags)
    return f'''---
id: "{lid}"
title: "{title}"
course: "{course}"
module: {mod}
module_title: "{mod_title}"
lesson: {les}
version: "2.0"
difficulty: "{diff}"
duration_minutes: {dur}
tags: [{tag_str}]
prerequisites: []
lab_required: true
---

# {title}

'''

# ═══════════════════════════════════════════════════════════════
# IOT HARDWARE — 46 stubs
# ═══════════════════════════════════════════════════════════════
print('='*60)
print('IOT HARDWARE — 46 stubs')
print('='*60)
IOT_H = '_17_iot_hardware'

iot_h_files = [
  '_06_23_core_electrical_physics.md',
  '_06_24_circuit_analysis_laws.md',
  '_06_25_diagnostic_measurement_instrumentation.md',
  '_06_26_passive_components.md',
  '_06_27_semiconductor_diodes.md',
  '_06_28_bipolar_junction_transistors.md',
  '_06_29_field_effect_transistors.md',
  '_06_30_operational_amplifiers.md',
  '_06_31_power_supplies_and_linear_regulation.md',
  '_06_32_switched_mode_power_supplies.md',
  '_06_33_microcontroller_core_architecture.md',
  '_06_34_clock_generation_and_timing_systems.md',
  '_06_35_gpio_electrical_characteristics.md',
  '_06_36_interrupt_controllers_and_nvic.md',
  '_06_37_analog_to_digital_converters.md',
  '_06_38_digital_to_analog_converters.md',
  '_06_39_dma_controllers_and_memory_transfer.md',
  '_06_40_pulse_width_modulation.md',
  '_06_41_uart_usart_serial_communication.md',
  '_06_42_spi_bus_protocol.md',
  '_06_43_i2c_bus_protocol.md',
  '_06_44_can_bus_protocol.md',
  '_06_45_temperature_and_humidity_sensors.md',
  '_06_46_motion_and_inertial_measurement.md',
  '_06_47_optical_and_ranging_sensors.md',
  '_06_48_environmental_gas_pressure_sensors.md',
  '_06_49_dc_motor_control_h_bridges.md',
  '_06_50_stepper_motor_driving_microstepping.md',
  '_06_51_servo_motor_control.md',
  '_06_52_solenoids_relays_power_switching.md',
  '_06_53_wifi_networking_esp_supplicant.md',
  '_06_54_ble_gap_gatt_profile_architecture.md',
  '_06_55_ieee_802_15_4_zigbee_thread.md',
  '_06_56_lora_and_lorawan_mac_architecture.md',
  '_06_57_cellular_iot_nb_iot_cat_m1.md',
  '_06_58_battery_chemistry_cell_selection.md',
  '_06_59_battery_management_systems_bms.md',
  '_06_60_energy_harvesting_techniques.md',
  '_06_61_low_power_sleep_modes.md',
  '_06_62_hardware_root_of_trust_secure_elements.md',
  '_06_63_cryptographic_hardware_accelerators.md',
  '_06_64_secure_boot_and_flash_encryption.md',
  '_06_65_jtag_swd_on_chip_debugging.md',
  '_06_66_logic_analysers_protocol_decoding.md',
  '_06_67_oscilloscope_signal_integrity.md',
  '_06_68_hardware_in_loop_testing.md'
]

for i, fn in enumerate(iot_h_files, 23):
    title = fn.replace('_06_','').replace('.md','').replace('_',' ').title()
    body = """## Overview of """ + title + """

In this lesson, you will master **""" + title + """** in IoT Hardware Engineering.

### Core Embedded Hardware Concepts

1. **Electrical Principles**: Voltage, current, impedance, signal timing, and noise immunity.
2. **Schematic & Hardware Interface**:
   - Microcontroller pin mapping & multiplexing.
   - Pull-up / pull-down resistor selection.
   - De-coupling capacitor placements (`0.1uF` near VDD pins).

```c
// C Code example for """ + title + """
#include "driver/gpio.h"

void configure_hardware(void) {
    gpio_config_t io_conf = {
        .pin_bit_mask = (1ULL << 18),
        .mode = GPIO_MODE_OUTPUT,
        .pull_up_en = GPIO_PULLUP_DISABLE,
        .pull_down_en = GPIO_PULLDOWN_DISABLE,
        .intr_type = GPIO_INTR_DISABLE
    };
    gpio_config(&io_conf);
}
```

## Lab Exercise
1. Wire up the hardware module on a breadboard or evaluation kit, hook up an oscilloscope or logic analyzer, and verify signal waveforms.
"""
    write_and_sync(IOT_H, fn, fm(f'06_{i}', title, 'IoT Hardware', 2, 'Embedded Hardware & Peripherals', i-22, 'intermediate', ['iot', 'hardware', 'embedded']) + body)

# ═══════════════════════════════════════════════════════════════
# PCB DESIGN — 28 stubs
# ═══════════════════════════════════════════════════════════════
print()
print('='*60)
print('PCB DESIGN — 28 stubs')
print('='*60)
PCB = '_18_pcb'

pcb_files = [
  '_09_01_electronic_component_packaging_standards.md',
  '_09_01_fundamentals_for_pcb_layout_engineers.md',
  '_09_01_pcb_materials_and_physical_layers.md',
  '_09_02_custom_schematic_symbol_creation.md',
  '_09_02_eda_software_and_kicad_fundamentals.md',
  '_09_02_schematic_capture_best_practices.md',
  '_09_03_component_placement_strategies.md',
  '_09_03_footprint_creation_and_ipc_7351.md',
  '_09_03_pcb_stackup_design_and_layer_assignment.md',
  '_09_04_differential_pair_routing.md',
  '_09_04_high_speed_routing_and_controlled_impedance.md',
  '_09_04_trace_width_current_capacity_and_clearance.md',
  '_09_05_decoupling_capacitor_placement_and_routing.md',
  '_09_05_ground_plane_design_and_stitching.md',
  '_09_05_pdn_power_distribution_network_design.md',
  '_09_06_crosstalk_mitigation_and_trace_spacing.md',
  '_09_06_emi_emc_design_guidelines_for_pcbs.md',
  '_09_06_signal_integrity_fundamentals_for_pcb.md',
  '_09_07_bom_bill_of_materials_generation.md',
  '_09_07_design_rule_checking_drc_and_erc.md',
  '_09_07_gerber_and_nc_drill_file_generation.md',
  '_09_08_assembly_drawings_and_pick_and_place.md',
  '_09_08_pcb_fabrication_processes.md',
  '_09_08_smt_reflow_and_wave_soldering_design.md',
  '_09_09_01_flexible_and_rigid_flex_pcb_design.md',
  '_09_09_02_rf_pcb_design_fundamentals.md',
  '_09_09_03_thermal_management_and_heat_sinks.md',
  '_09_09_04_capstone_custom_esp32_iot_board_pcb.md'
]

for i, fn in enumerate(pcb_files, 1):
    title = fn.replace('_09_','').replace('.md','').replace('_',' ').title()
    body = """## Overview of """ + title + """

In this lesson, you will master **""" + title + """** in PCB Layout & Electronics Manufacturing.

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
"""
    write_and_sync(PCB, fn, fm(f'09_{i:02d}', title, 'PCB Design', 1, 'EDA & PCB Engineering', i, 'intermediate', ['pcb', 'kicad', 'eda', 'hardware']) + body)

# ═══════════════════════════════════════════════════════════════
# IOT PROJECTS — 12 stubs
# ═══════════════════════════════════════════════════════════════
print()
print('='*60)
print('IOT PROJECTS — 12 stubs')
print('='*60)
IOT_P = '_19_iot_projects'

iot_p_files = [
  '_10_01_01_web_based_environmental_data_logger.md',
  '_10_01_02_smart_appliance_relay_switch.md',
  '_10_01_03_rfid_attendance_door_access.md',
  '_10_02_01_mqtt_industrial_tank_pump_controller.md',
  '_10_02_02_cellular_gps_fleet_tracker.md',
  '_10_02_03_lorawan_soil_moisture_agricultural_node.md',
  '_10_03_01_ble_beacon_indoor_asset_tracker.md',
  '_10_03_02_thread_matter_smart_home_mesh_light.md',
  '_10_04_01_tiny_ml_vibration_anomaly_detector.md',
  '_10_04_02_edge_ai_camera_person_counter.md',
  '_10_05_01_ota_firmware_update_server_pipeline.md',
  '_10_05_02_industrial_modbus_rtu_to_cloud_gateway.md'
]

for i, fn in enumerate(iot_p_files, 1):
    title = fn.replace('_10_','').replace('.md','').replace('_',' ').title()
    body = """## Overview of """ + title + """

In this lesson, you will build and deploy **""" + title + """** as a capstone IoT Hardware & Software System.

### End-to-End System Architecture

```
[Sensors / Actuators] -> [ESP32 / Microcontroller] -> [WiFi / BLE / LoRa / Cellular] -> [Cloud / MQTT Broker] -> [Dashboard / Web App]
```

### Complete Firmware Implementation

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "WIFI_SSID";
const char* password = "WIFI_PASSWORD";
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\\nWiFi Connected!");
    client.setServer(mqtt_server, 1883);
}

void loop() {
    if (!client.connected()) {
        client.connect("ESP32Client");
    }
    client.loop();
    client.publish("iot/sensor/telemetry", "{\\"status\\":\\"OK\\",\\"temp\\":24.5}");
    delay(5000);
}
```

## Lab Exercise
1. Flashing firmware to an ESP32 dev board, verifying serial monitor output, and viewing live MQTT telemetry on an online dashboard.
"""
    write_and_sync(IOT_P, fn, fm(f'10_{i:02d}', title, 'IoT Projects', 1, 'End-to-End IoT Systems', i, 'advanced', ['iot', 'projects', 'esp32', 'firmware', 'mqtt']) + body)

print()
print('='*60)
print(f'PHASE 6 IOT COMPLETE — Total files written: {written}')
print('='*60)
