import torch
from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="facebook/bart-large-cnn",
    device=-1  # CPU
)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
Create a travel plan for {destination}.

Include:
Daily Activities,
Tourist Attractions,
Food Suggestions,
Travel Tips.

Use REAL places from {destination}.
Return in clear bullet points.
"""

    with torch.no_grad():
        output = generator(
            prompt,
            max_length=250,
            do_sample=False
        )

    return f"""
Day 1:
{output[0]['generated_text']}
"""
