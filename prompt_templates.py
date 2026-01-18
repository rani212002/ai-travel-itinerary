def build_itinerary_prompt(destination, days, budget, travel_type):
    return f"""
You are a professional travel planner.

Create a {days}-day detailed travel itinerary for:
Destination: {destination}
Budget: {budget}
Travel Type: {travel_type}

Include for each day:
- Morning, Afternoon, Evening activities
- Tourist attractions
- Local food recommendations
- Travel tips

Make it well-structured and realistic.
"""
