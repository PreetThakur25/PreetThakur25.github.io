# AI-Based Smart Traffic Management System

An intelligent, edge-integrated traffic monitoring and adaptive signal control system leveraging computer vision and distributed IoT cameras. The system calculates real-time vehicular density, optimizes signal timings dynamically, and enforces emergency vehicle prioritization.

---

## Key Features

- **Real-Time Vehicle Detection & Tracking:** Utilizes YOLOv8 and OpenCV to accurately identify and count vehicles across multiple lanes.
- **Distributed Camera Ingestion:** Integrates multiple ESP32-CAM RTSP/HTTP video feeds for intersection-wide surveillance.
- **Adaptive Signal Timing:** Replaces static timers with density-driven algorithms that minimize intersection wait times and clear bottlenecks.
- **Emergency Vehicle Priority (Green Corridor):** Automatically recognizes emergency service vehicles (ambulances, fire engines) and forces temporary green corridors.
- **Summit & Exhibition Proven:** Exhibited at the AI Impact India Summit 2025.

---

## Architecture & Workflow

```
[ ESP32-CAM Nodes ] ---> [ RTSP / Stream Server ]
                                  |
                                  v
                      [ YOLOv8 Vehicle Detector ]
                                  |
                      [ Density & Queue Analytics ]
                                  |
                     [ Signal Scheduling Engine ] ---> [ Traffic Controller / API ]
```

---

## Tech Stack

- **Computer Vision:** OpenCV, YOLOv8
- **Edge / Hardware:** ESP32-CAM, Raspberry Pi
- **Core Languages:** Python, C++ (Arduino IDE for ESP32)
- **Protocols:** RTSP, HTTP, UART

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Preet-Thakur-25/Smart-Traffic-Management-System.git
   cd Smart-Traffic-Management-System
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Video Streams:**
   Update camera RTSP / IP endpoints in `config/streams.json`:
   ```json
   {
     "lanes": [
       {"id": "north", "stream_url": "http://192.168.1.50:81/stream"},
       {"id": "south", "stream_url": "http://192.168.1.51:81/stream"}
     ]
   }
   ```

4. **Run the Application:**
   ```bash
   python main.py --weights yolov8n.pt
   ```

---

## Author

- **Preet Pratap Singh Bhati**
- Email: preetthakur0625@gmail.com
- LinkedIn: [linkedin.com/in/preetthakur](https://linkedin.com/in/preetthakur)
- GitHub: [github.com/Preet Thakur 25](https://github.com/Preet-Thakur-25)
