def build_itinerary_prompt(destination, days, budget, travel_type):
    return f"""
You are a professional travel planner AI.

Create a detailed {days}-day travel itinerary for {destination}.

User preferences:
- Budget: {budget}
- Travel type: {travel_type}

IMPORTANT:
Follow the EXACT format below. Do NOT add introductions or conclusions.

Day 1:
Morning:
- ...
Afternoon:
- ...
Evening:
- ...
Tourist Attractions:
- ...
Food Recommendations:
- ...
Travel Tips:
- ...

Day 2:
Morning:
- ...
Afternoon:
- ...
Evening:
- ...
Tourist Attractions:
- ...
Food Recommendations:
- ...
Travel Tips:
- ...

Repeat this format until Day {days}.
"""
