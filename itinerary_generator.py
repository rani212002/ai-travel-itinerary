# # # modules/itinerary_generator.py
# # import os
# # from dotenv import load_dotenv

# # from groq import Groq
# # load_dotenv()

# # client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# # def generate_itinerary(destination, days, budget, travel_type):
# #     prompt = f"""
# #     Create a {days}-day travel itinerary for {destination}.
# #     Budget: {budget}, Travel Type: {travel_type}.
    
# #     Format the itinerary exactly like this:

# #     Day 1:
# #     Morning:
# #     • Activity 1
# #     • Activity 2

# #     Afternoon:
# #     • Activity 1

# #     Evening:
# #     • Activity 1

# #     Tourist Attractions:
# #     • Attraction 1
# #     • Attraction 2

# #     Food Recommendations:
# #     • Food 1
# #     • Food 2

# #     Travel Tips:
# #     • Tip 1
# #     • Tip 2

# #     Repeat this format for all days.
# #     """
    
# #     response = client.chat.completions.create(
# #         model="llama3-70b-8192",
# #         messages=[
# #             {"role": "user", "content": prompt}
# #         ],
# #         temperature=0.7,
# #         max_tokens=1500
# #     )
# # #     response = openai.chat.completions.create(
# # #     model="gpt-4",
# # #     messages=[{"role": "user", "content": prompt}],
# # #     max_tokens=1500
# # # )

    
# #     return response.choices[0].message.content
# import os
# from groq import Groq

# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# def generate_itinerary(destination, days, budget, travel_type):
#     prompt = f"""
# You are a professional travel planner.

# Generate a detailed {days}-day travel itinerary for {destination}.

# Travel details:
# - Budget: {budget}
# - Travel type: {travel_type}

# Provide REAL places, activities, restaurants, and tips.
# Do NOT use placeholders.

# Format:

# Day 1:
# Daily Activities:
# - ...

# Tourist Attractions:
# - ...

# Food Suggestions:
# - ...

# Travel Tips:
# - ...

# Repeat for all days up to Day {days}.
# """

#     response = client.chat.completions.create(
#         model="llama3-70b-8192",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.8,
#         max_tokens=1500
#     )

#     return response.choices[0].message.content
import streamlit as st
from groq import Groq

# Create Groq client using Streamlit secrets
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

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
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=1500
    )

    return response.choices[0].message.content
