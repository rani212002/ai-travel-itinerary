# modules/itinerary_generator.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("GROK_API_KEY")

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
    
    response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=1500
)
    
    return response.choices[0].message.content
