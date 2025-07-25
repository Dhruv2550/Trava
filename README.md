# Trava

**Trava** is a travel booking platform powered by a relational MySQL database and a Python-based CRUD interface. Designed for flexibility, maintainability, and scalability, Trava simplifies the process of managing users, trips, accommodations, bookings, payments, and more.

---

## 🧱 Project Overview

- **Database**: MySQL (11 tables, 3rd Normal Form)
- **Interface**: Python with PyMySQL
- **Features**:
  - Full **CRUD** support across all entities
  - **Real-time summary reports** for bookings, payments, and trips
  - **Deployment-ready** schema with ER diagram and documentation

---

## 📘 Key Entities

- `user` – Stores customer profiles and contact info  
- `trip` – Contains travel details such as dates and types  
- `destination` – Location and country info with ratings  
- `booking` – Manages reservations and status  
- `accommodation` – Hotel or stay details, pricing, and capacity  
- `transportation` – Travel options with companies and schedules  
- `activities` – Optional trip add-ons  
- `payments` – Payment method, amount, and status  
- `reviews` – User-submitted feedback and ratings  

> The database is fully normalized and supports robust data integrity and performance.

---

## 🔧 Technologies Used

- **MySQL** – For the relational database
- **PyMySQL** – Python MySQL connector
- **Python 3** – Backend interface and utilities

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/trava.git
cd trava
