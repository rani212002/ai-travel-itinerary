import streamlit as st
from groq import Groq

# 🔍 DEBUG: force error if key missing
if "GROQ_API_KEY" not in st.secrets:
    st.error("GROQ_API_KEY not found in Streamlit secrets")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]

# 🔍 DEBUG: show key prefix (safe)
st.write("Groq key prefix:", api_key[:4])

client = Groq(api_key=api_key)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
You are a professional travel planner.

Generate a detailed {days}-day travel itinerary for {destination}.

Travel details:
- Budget: {budget}
- Travel type: {travel_type}

Provide REAL places, activities, restaurants, and tips.
Do NOT use placeholders.

Format EXACTLY like this:

Day 1:
Daily Activities:
- ...

Tourist Attractions:
- ...

Food Suggestions:
- ...

Travel Tips:
- ...

Repeat for all days up to Day {days}.
"""

    response = client.chat.completions.create(
        model="groq/compound-mini",  # smaller model for testing
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=50
    )

    return response.choices[0].message.content
