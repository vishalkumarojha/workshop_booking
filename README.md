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
| **Admin Setup** | `admin` | `adminpassword` | `your-admin@email.com` |
| **Instructor** | `instructor1` | `password123` | `instructor1@example.com` |
| **Coordinator** | `coordinator1` | `password123` | `coordinator1@example.com` |

*(You can verify functionality using the Instructor account to accept workshops proposed by the Coordinator account).*

---

## 📸 Platform Previews

Drop your UI screenshots into the `/docs/screenshots/` folder to populate your visual gallery perfectly:
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/81ac632c-6391-4081-8332-bc4a433c360c" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/46c0b9cc-7077-4a66-af70-59ca3b6b253c" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/1993bfe3-129a-44b8-aaa4-f13cbaa96f59" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/201c5457-28c7-4cff-bf71-30d99758d438" />



### 1. Instructor Dashboard
![Instructor Dashboard]()
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/39364fa9-3cdb-4202-a89c-e1f7372f9571" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/e4e2ffda-cbbf-4a60-abe0-abc16566cd2e" />

*A look at the premium instructor toolkit with accepted and pending proposals.*

### 2. Coordinator Overview
![Coordinator Dashboard]()
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/25045ef4-9792-46ac-be20-247418d06437" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/51a61b0d-a9c0-4e0f-b577-58f8850e2e54" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/a1007de5-b613-4402-a0f3-b0fcff032a65" />



*The hub where new educators can propose standard workshops.*

### 3. Public Statistics & Analytics
![Global Statistics]
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/25045ef4-9792-46ac-be20-247418d06437" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/51a61b0d-a9c0-4e0f-b577-58f8850e2e54" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/a1007de5-b613-4402-a0f3-b0fcff032a65" />
*Bar chart visualizations of workshop density spread across different states.*
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/eec9b64d-1de7-4319-8359-cb81409982cd" />



---
other UI interface 
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/41e8004d-6c01-459d-aa45-373b7bb17f4e" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/08cce8f3-23a7-4786-9858-9eff470a643d" />
<img width="1917" height="1007" alt="image" src="https://github.com/user-attachments/assets/017898df-3523-4199-ad77-490db27797e6" />

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
