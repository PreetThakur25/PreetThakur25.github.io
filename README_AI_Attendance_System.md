# AI Attendance System with Face Verification

An embedded automated facial recognition attendance management solution deploying biometric verification directly onto edge hardware with PostgreSQL backends.

---

## Key Features

- **Edge Verification:** Runs real-time face localization and feature matching using OpenCV and lightweight deep learning models on Raspberry Pi.
- **Anti-Spoofing & Validation:** Incorporates liveness checks to prevent static photo or screen spoofing attempts.
- **Automated Audit Records:** Logs entry/exit timestamps directly into relational PostgreSQL storage with zero manual record-keeping.
- **Administrative Reporting Dashboard:** Instant generation of daily/monthly attendance ratios and missing log queries.

---

## Tech Stack

- **Hardware:** Raspberry Pi 4, Pi Camera Module
- **Computer Vision:** OpenCV, FaceNet / InsightFace
- **Backend & Database:** Python, PostgreSQL, SQLAlchemy

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Preet-Thakur-25/AI-Attendance-System.git
   cd AI-Attendance-System
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Configuration:**
   Configure connection strings in `config.py` pointing to your PostgreSQL instance.

4. **Enrollment & Execution:**
   - Enroll new faces:
     ```bash
     python register_face.py --name "Preet Bhati" --id 101
     ```
   - Start verification service:
     ```bash
     python main.py
     ```

---

## Author

- **Preet Pratap Singh Bhati**
- Email: preetthakur0625@gmail.com
- LinkedIn: [linkedin.com/in/preetthakur](https://linkedin.com/in/preetthakur)
