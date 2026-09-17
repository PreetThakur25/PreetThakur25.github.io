# Women Safety Surveillance System

An edge-deployable computer vision solution engineered for real-time situational awareness, threat detection, and distress alert generation using non-verbal SOS cue identification.

---

## Key Features

- **Real-Time SOS Gesture Recognition:** Employs Google MediaPipe hand landmark detection and OpenCV to identify standardized distress and SOS hand gestures.
- **Crowd & Threat Analytics:** Detects anomalous movement patterns, sudden clustering, and isolated individual distress scenarios.
- **Automated Incident Logging:** Captures timestamped evidentiary frame clips and metadata when triggers are identified.
- **Low-Latency Edge Execution:** Optimized to run efficiently on edge nodes without external cloud GPU dependencies.

---

## Tech Stack

- **Languages:** Python
- **Computer Vision:** OpenCV, MediaPipe
- **Machine Learning & Inference:** NumPy, SciPy

---

## Getting Started

1. **Clone Repository:**
   ```bash
   git clone https://github.com/Preet-Thakur-25/Women-Safety-Surveillance-System.git
   cd Women-Safety-Surveillance-System
   ```

2. **Install Dependencies:**
   ```bash
   pip install opencv-python mediapipe numpy
   ```

3. **Run Detection Pipeline:**
   ```bash
   python detect_gestures.py --source 0
   ```

---

## Author

- **Preet Pratap Singh Bhati**
- Email: preetthakur0625@gmail.com
- LinkedIn: [linkedin.com/in/preetthakur](https://linkedin.com/in/preetthakur)
