# 🚀 FOSSEE Workshop Booking Platform

> A beautifully stylized, modern web platform designed to help coordinators and instructors seamlessly propose, schedule, and manage educational workshops.

The FOSSEE Workshop portal was recently modernized to utilize a cohesive **Glassmorphism Premium UI**, complete with dynamic gradients, soft frosted glass elements, and micro-animations, upgrading both the visual experience and operational flow.

---

## ✨ Key Features

### 🎨 Modern UI & UX
* **Premium Dashboard:** Fully redesigned dashboard interface with color-coded statistic cards, hero banners, and a responsive layout.
* **Glassmorphic Navigation:** Frosted glass, drop-downs with profile avatars, and dynamically updating routing.
* **Streamlined Auth Pages:** Split-screen authentication layouts ensuring comfortable user registration, log-ins, and credential management.

### 📊 Comprehensive Statistics
1. **Instructors & Admins:**
    * Monthly Workshop Counts and analytical dashboards.
    * Instructor and Coordinator performance breakdowns.
    * Upcoming Workshop previews.
2. **Open to All Coordinators/Users:**
    * State-wise workshop aggregations utilizing intuitive `Chart.js` bar visualizations.
    * Dedicated filtering tables to export CSVs or track history.

### 🛠️ Workshop Management Lifecycle
* **Propose Workshop:** Coordinators can actively submit workshop requests alongside scheduled dates. Note: Prior terms and conditions must be verified.
* **Approve/Reject (Instructors):** Instructors have designated authority to accept or reject incoming proposals, or collaboratively request to postpone.
* **Profile Management:** Auto-provisioned user profiles capturing institution details natively.

---

## 🔑 Demo & Test Credentials

For development and local testing purposes, you can jump straight into the application without needing to verify new profiles manually. We have pre-built robust accounts:

| Role Type | Username | Password | Email |
| :--- | :--- | :--- | :--- |
| **Admin Setup** | `admin` | `...` | `your-admin@email.com` |
| **Instructor** | `instructor1` | `password123` | `instructor1@example.com` |
| **Coordinator** | `coordinator1` | `password123` | `coordinator1@example.com` |

*(You can verify functionality using the Instructor account to accept workshops proposed by the Coordinator account).*

---

## 📸 Platform Previews

Drop your UI screenshots into the `/docs/screenshots/` folder to populate your visual gallery perfectly:

### 1. Instructor Dashboard
![Instructor Dashboard](docs/screenshots/instructor_dashboard.png)
*A look at the premium instructor toolkit with accepted and pending proposals.*

### 2. Coordinator Overview
![Coordinator Dashboard](docs/screenshots/coordinator_dashboard.png)
*The hub where new educators can propose standard workshops.*

### 3. Public Statistics & Analytics
![Global Statistics](docs/screenshots/statistics_chart.png)
*Bar chart visualizations of workshop density spread across different states.*

### 4. Split-Screen Authentication
![Secure Login Menu](docs/screenshots/split_login.png)
*The modernized split-screen sign-in gateway incorporating the FOSSEE mission.*

---

## 🚀 Getting Started Locally

1. Setup your Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install Core Requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Local Server:
   ```bash
   python manage.py runserver 8001
   ```
*(Check out `docs/Getting_Started.md` for extended configurations!)*

---
<p align="center">
  <i>Developed and Maintained by the FOSSEE group, IIT Bombay</i>
</p>
