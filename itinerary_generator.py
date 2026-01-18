import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
Create a {days}-day travel itinerary for {destination}.

Return the answer EXACTLY in this format:

Day 1:
Daily Activities:
- Visit a famous landmark in {destination}
- Explore a popular local area

Tourist Attractions:
- One famous museum or monument in {destination}
- One well-known tourist place in {destination}

Food Suggestions:
- One famous restaurant in {destination}
- One popular local food item

Travel Tips:
- One practical travel tip
- One safety tip

Rules:
- Use REAL places from {destination}
- Do NOT explain anything
- Do NOT add extra text
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
