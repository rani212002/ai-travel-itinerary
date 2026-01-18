from openai import OpenAI

client = OpenAI(api_key="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")

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
Create a {days}-day travel itinerary for {destination}.

Return the output EXACTLY in this format:

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

Use REAL places and food from {destination}.
Do NOT add explanations.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
