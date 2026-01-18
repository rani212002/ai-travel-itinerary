def build_itinerary_prompt(destination, days, budget, travel_type):
    return f"""
You are an expert travel planner.

Generate a {days}-day travel itinerary for the destination: {destination}.

User Preferences:
- Budget Level: {budget}
- Travel Type: {travel_type}

STRICT FORMAT (do not change format):

Day 1:
Morning:
Afternoon:
Evening:
Tourist Attractions:
Food Recommendations:
Travel Tips:

Day 2:
Morning:
Afternoon:
Evening:
Tourist Attractions:
Food Recommendations:
Travel Tips:

(Continue same format until Day {days})

Rules:
- Be realistic and detailed
- Use bullet points inside each section
- Keep language simple and clear
"""
