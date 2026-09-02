# 🌍 Smart Tourist Planner

<p align="center">
  <b>A Flask-based travel planning application that helps users generate personalized trip plans, estimate hotel costs, create itineraries, and save trip details.</b>
</p>

---

## 📖 Overview

Smart Tourist Planner is a web application designed to simplify travel planning. Users can enter their destination, trip duration, number of members, and budget to receive a personalized travel plan.

The application generates:
- 📅 Day-wise itinerary
- 🏨 Hotel recommendations
- 💰 Estimated hotel cost
- 🛣️ Suggested travel route
- 💾 Trip saving functionality

---

# ✨ Features

- 🌍 Personalized trip planning
- 📅 Automatic day-wise itinerary generation
- 🏨 Hotel recommendation system
- 💰 Hotel cost estimation
- 👨‍👩‍👧 Group travel cost calculation
- 🛣️ Suggested tourist route
- 💾 Save trip details to MongoDB
- 📦 REST API using Flask
- 🌐 Responsive web interface

---

# 🛠 Tech Stack

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MongoDB

### Frontend
- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```
Smart-Tourist-Planner/
│
├── app.py
├── requirements.txt
├── index.html
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Dharamraj05/smart-tourist-planner.git
```

## Move into Project

```bash
cd smart-tourist-planner
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start MongoDB

Make sure MongoDB is running locally on:

```
mongodb://127.0.0.1:27017/
```

## Run the Application

```bash
python app.py
```

The server will start on:

```
http://localhost:5000
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/destinations` | Check server status |
| POST | `/api/generatePlan` | Generate travel plan |
| POST | `/api/book-hotel` | Book selected hotel |
| POST | `/api/save-trip` | Save trip details |

---

# 📸 Screenshots

> Add screenshots here after running the project.

- Home Page
- Travel Planner Form
- Generated Itinerary
- Hotel Recommendation
- Booking Confirmation

---

# 💡 Future Improvements

- Google Maps Integration
- Weather API
- Hotel Booking API
- User Authentication
- Payment Gateway
- AI-based Destination Recommendation
- Email Confirmation
- Trip History Dashboard

---

# 👨‍💻 Author

**Dharamraj**

GitHub: https://github.com/Dharamraj05

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.

It helps support the project and motivates future improvements.
