# 📘 KPA Form Data API – Backend Assignment

## 👨‍💻 Developer:
**Name**: Siddavatam Manoj Kumar Reddy  
**Email**: siddavatammanoj07@gmail.com  

---

## ✅ Project Overview

This project implements **two API endpoints** based on the KPA form data Postman collection and Swagger documentation using **Django REST Framework** and **JWT authentication**.

---

## 🚀 Tech Stack Used

- Python 3.12  
- Django 5.x  
- Django REST Framework  
- SimpleJWT (for JWT Auth)  
- PostgreSQL  

---

## 🔐 Authentication

- JWT-based login via:  
  **POST** `/api/token/`  
  with payload:
  ```json
  {
    "username": "admin",
    "password": "admin"
  }