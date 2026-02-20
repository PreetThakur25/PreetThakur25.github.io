# Smart Bulb Monitoring System

A hardware-software embedded systems project that uses an **Arduino microcontroller**, a **PIR motion sensor**, and an **LDR (Light Dependent Resistor)** to automate smart bulb control and perform real-time health monitoring — streamed live to a PC via Python over serial communication.

---

## Overview

This project demonstrates a practical IoT/embedded workflow — from sensor interfacing at the hardware level, to real-time data acquisition and monitoring on the software side. The system:

- Detects **ambient light intensity** using an LDR to determine bulb health (good vs. faulty)
- Detects **human motion** using a PIR sensor to automatically control an LED bulb
- Streams all sensor readings over **UART serial** to a connected PC
- Provides a **Python monitoring script** that reads and displays live Arduino output in the terminal

---

## Tech Stack

| Layer       | Technology                          |
|-------------|-------------------------------------|
| Hardware    | Arduino UNO                         |
| Sensors     | PIR Motion Sensor, LDR (Analog + Digital) |
| Display     | 7-Segment Display (single digit)    |
| Language    | C++ (Arduino), Python               |
| Protocol    | UART Serial (9600 baud)             |
| PC Monitor  | Python `pyserial`                   |

---

## Project Structure

```
smart_bulb_monitoring/
│
├── monitoring.py                    # Python serial monitor — reads live data from Arduino
│
Arduino/
│
├── ldr_test/
│   └── ldr_test.ino                 # Digital LDR: detects bulb as good or faulty
│
├── sketch_aug19a/
│   └── sketch_aug19a.ino            # PIR + LDR combo: motion-triggered LED + light reading
│
├── sketch_aug20b/
│   └── sketch_aug20b.ino            # Analog LDR: reads raw light intensity (0–1023)
│
├── Single_led_7segment_test/
│   └── Single_led_7segment_test.ino # 7-segment countdown (9 → 0) using bitmask encoding
│
├── Strip_led_test/
│   └── Strip_led_test.ino           # Basic built-in LED blink test
│
└── ultrasonic_test/
    └── ultrasonic_test.ino          # HC-SR04 ultrasonic distance measurement
```

---

## How It Works

### 1. Bulb Health Detection (`ldr_test.ino`)

An LDR is connected to digital pin **D12**. Since a working bulb emits light that the LDR picks up, the pin state determines health:

```
HIGH → "Bulb is faulty"  (no light detected)
LOW  → "Bulb is good"    (light is present)
```

Readings are printed to Serial every **500ms**.

---

### 2. Motion-Triggered Smart Bulb (`sketch_aug19a.ino`)

Combines a **PIR sensor** (D2) and an **LDR** (A0) with an LED (D3):

- Waits idle until motion is detected
- On motion: turns LED ON, reads LDR light intensity, holds for 3 seconds, then auto-shuts off
- Avoids false re-triggers with a 500ms debounce delay

```
PIR HIGH → LED ON (3s) → LDR Reading → LED OFF
```

---

### 3. Raw Light Intensity Logging (`sketch_aug20b.ino`)

Reads the LDR on analog pin **A0**, outputting a value from **0 to 1023** every 500ms — useful for calibration and threshold tuning.

---

### 4. 7-Segment Countdown Display (`Single_led_7segment_test.ino`)

Drives a single 7-segment display using **7 GPIO pins (D2–D8)**. Uses a bitmask lookup table to render digits 0–9, executing a countdown from 9 to 0 with 1-second intervals, then halts.

---

### 5. Ultrasonic Distance Sensor (`ultrasonic_test.ino`)

Interfaces with an **HC-SR04** (trig: D9, echo: D10). Sends a 10µs trigger pulse, measures echo return time, and computes distance using:

```
distance (cm) = duration × 0.0343 / 2
```

Outputs every 100ms with a 30ms timeout (approximately 5m max range).

---

### 6. Python Serial Monitor (`monitoring.py`)

Connects to the Arduino via a configurable COM port and reads live serial output:

```python
# Configurable
arduino_port = "COM9"   # Windows
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate, timeout=1)
```

Runs in a continuous loop, printing every line from the Arduino until interrupted with `Ctrl+C`, then safely closes the serial port.

---

## Setup & Usage

### Hardware Requirements

- Arduino UNO (or compatible)
- LDR sensor module
- PIR motion sensor (HC-SR501 or equivalent)
- HC-SR04 Ultrasonic sensor
- Single-digit common-cathode 7-segment display
- LED + 220Ω resistor
- Jumper wires, breadboard

### Software Requirements

```bash
pip install pyserial
```

Arduino IDE (or VS Code with Arduino extension) for flashing `.ino` sketches.

### Running the Monitor

1. Flash the desired `.ino` sketch to your Arduino via Arduino IDE
2. Connect the Arduino to your PC via USB
3. Identify the COM port (Device Manager on Windows)
4. Update `monitoring.py`:
   ```python
   arduino_port = "COM9"  # Change to your port
   ```
5. Run the monitor:
   ```bash
   python monitoring.py
   ```
6. Live sensor readings will stream in the terminal. Press `Ctrl+C` to stop.

---

## Key Concepts Demonstrated

- **Digital & Analog sensor interfacing** with Arduino GPIO
- **UART Serial communication** between embedded hardware and a host PC
- **Real-time data streaming** using Python `pyserial`
- **Bitmask-based segment encoding** for 7-segment display control
- **Sensor fusion** (PIR + LDR) for context-aware automation
- **Pulse-echo distance measurement** with timeout handling
- **Graceful resource cleanup** in Python (`finally` block for serial port)

---

## Platform Notes

| OS      | Serial Port Format     |
|---------|------------------------|
| Windows | `COM3`, `COM9`, etc.   |
| Linux   | `/dev/ttyUSB0`         |
| Linux   | `/dev/ttyACM0` (some Arduino models) |

---

## Author

Built as a hands-on embedded systems and IoT project, integrating hardware sensor design with Python-based real-time monitoring.
