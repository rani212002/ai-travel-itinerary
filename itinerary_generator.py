# from transformers import pipeline

# Load text generation model
# generator = pipeline(
#     "text-generation",
#     model="gpt2",
    # max_length=600
# )

# def generate_itinerary(destination, days, budget, travel_type):
#     prompt = f"""
#     Create a detailed {days}-day travel itinerary for {destination}.
#     Budget: {budget}
#     Travel Type: {travel_type}

#     Include:
#     - Day-wise activities
#     - Tourist attractions
#     - Food recommendations
#     - Travel tips
#     """

#     response = generator(prompt, num_return_sequences=1)
#     return response[0]["generated_text"]

from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
You are a professional travel planner.

Create a detailed {days}-day family-friendly travel itinerary for {destination}.

Budget: {budget}
Travel Type: {travel_type}

STRICTLY include the following sections:

Day-wise Itinerary:
- Day 1:
- Day 2:
- Day 3:

Tourist Attractions:
- Bullet points

Food Recommendations:
- Local dishes
- Family-friendly restaurants

Shopping Suggestions:
- Local markets
- Souvenirs

Lodging Suggestions:
- Budget hotels or homestays

Travel Tips:
- Weather
- Safety
- Best time to visit

Do NOT include flights, airlines, pricing, or insurance details.
"""

    response = generator(
        prompt,
        max_new_tokens=700,
        do_sample=False
    )

    return response[0]["generated_text"]
