# Vizolane ERP - Multi-Tenant School Management System

A robust, enterprise-grade multi-tenant web application engineered to manage administrative, academic, and financial operations across multiple educational institutions under complete logical isolation.

---

## Key Features

- **Multi-Tenant Architecture:** Secure schema or tenant-identifier data segregation preventing cross-institution data leakage.
- **Role-Based Access Control (RBAC):** Granular permission layers for Super Administrators, School Principals, Teachers, Accountants, and Students.
- **Academic & Attendance Management:** Automated student roll-call tracking, grade logging, and timetable scheduling.
- **Fee Management & Invoicing:** Record generation, transaction logs, and ledger tracking.
- **RESTful API Services:** Modular endpoints designed for easy integration with frontend portals and mobile apps.

---

## Tech Stack

- **Backend:** Python, Flask, Flask-RESTful, Flask-Login, SQLAlchemy
- **Database:** PostgreSQL
- **Frontend / Templates:** HTML5, CSS3, JavaScript, Bootstrap
- **Deployment & Tooling:** Git, Vercel / Cloud Containerization

---

## Quick Start

1. **Clone Repository:**
   ```bash
   git clone https://github.com/Preet-Thakur-25/Vizolane-ERP.git
   cd Vizolane-ERP
   ```

2. **Virtual Environment & Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Database:**
   Update `.env` with your PostgreSQL database URL:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/vizolane_erp
   SECRET_KEY=your_secure_secret_key
   ```

4. **Run Migrations & Server:**
   ```bash
   flask db upgrade
   python run.py
   ```

---

## Author

- **Preet Pratap Singh Bhati**
- Email: preetthakur0625@gmail.com
- LinkedIn: [linkedin.com/in/preetthakur](https://linkedin.com/in/preetthakur)
