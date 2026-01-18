# modules/itinerary_generator.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROK_API_KEY = os.getenv("GROK_API_KEY")
GROK_API_URL = "https://api.grok.com/v1/generate"

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
    Create a {days}-day travel itinerary for {destination}.
    Budget: {budget}, Travel Type: {travel_type}.
    
    Format the itinerary exactly like this:

    Day 1:
    Morning:
    • Activity 1
    • Activity 2

    Afternoon:
    • Activity 1

    Evening:
    • Activity 1

    Tourist Attractions:
    • Attraction 1
    • Attraction 2

    Food Recommendations:
    • Food 1
    • Food 2

    Travel Tips:
    • Tip 1
    • Tip 2

    Repeat this format for all days.
    """
    
    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4",
        "prompt": prompt,
        "max_tokens": 1500
    }

    response = requests.post(GROK_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        return f"Error: {response.status_code}, {response.text}"
