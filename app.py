from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import uuid
import random

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["tourist_planner"]
trips_collection = db["trips"]

@app.route("/api/destinations", methods=["GET"])
def destinations():
    return jsonify({"message": "Server OK"}), 200

@app.route("/api/generatePlan", methods=["POST"])
def generate_plan():
    data = request.json
    destination = data.get("destination")
    days = int(data.get("days"))
    members = int(data.get("members"))
    budget = int(data.get("budget"))

    attractions = ["City Tour", "Museum", "Adventure Park", "Beach Walk", "Temple Visit"]

    hotels = [
        {"name": "Luxury Suites", "rating": 5, "price": 220, "amenities": ["WiFi", "Pool"]},
        {"name": "Comfort Inn", "rating": 4, "price": 140, "amenities": ["WiFi"]},
        {"name": "Budget Stay", "rating": 3, "price": 90,  "amenities": ["Breakfast"]},
    ]

    route = {
        "path": attractions[:4],
        "distance": round(random.uniform(50, 300), 1)
    }

    itinerary = []
    for d in range(1, days + 1):
        itinerary.append({
            "day": d,
            "activities": [
                {"title": "Morning Sightseeing", "time": "9:00 AM", "duration_hours": 2},
                {"title": "Lunch Break", "time": "1:00 PM", "duration_hours": 1},
                {"title": "Evening Activity", "time": "5:00 PM", "duration_hours": 2}
            ]
        })

    rooms_needed = (members + 1) // 2
    hotel_costs = []

    for h in hotels:
        total_price = h["price"] * rooms_needed * days
        per_person = total_price / members

        hotel_costs.append({
            "name": h["name"],
            "rating": h["rating"],
            "amenities": h["amenities"],
            "total": total_price,
            "perPerson": per_person
        })

    hotel_costs = sorted(hotel_costs, key=lambda x: x["total"])
    recommended = hotel_costs[0]

    response = {
        "route": route,
        "itinerary": itinerary,
        "hotels": hotels,
        "costs": {
            "members": members,
            "roomsNeeded": rooms_needed,
            "hotelCosts": hotel_costs,
            "recommended": recommended
        }
    }

    return jsonify(response)

@app.route("/api/book-hotel", methods=["POST"])
def book_hotel():
    data = request.json

    confirmation = {
        "bookingId": str(uuid.uuid4()),
        "hotelName": data["hotelName"],
        "destination": data["destination"],
        "members": data["members"],
        "days": data["days"],
        "rooms": data["rooms"],
        "totalCost": data["totalCost"],
        "status": "Confirmed",
        "timestamp": datetime.now().isoformat()
    }

    return jsonify({"confirmation": confirmation}), 200

@app.route("/api/save-trip", methods=["POST"])
def save_trip():
    data = request.json
    data["timestamp"] = datetime.now()

    try:
        trips_collection.insert_one(data)
        return jsonify({"message": "Trip saved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
