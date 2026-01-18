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
    model="google/flan-t5-base"   # base is more stable on CPU
)

def generate_section(prompt, tokens=200):
    response = generator(
        prompt,
        max_new_tokens=tokens,
        do_sample=False
    )
    return response[0]["generated_text"].strip()


def generate_itinerary(destination, days, budget, travel_type):

    day_wise = generate_section(
        f"""
Create a {days}-day day-wise family-friendly itinerary for {destination}.
Return clearly separated Day 1, Day 2, Day 3 activities only.
""",
        350
    )

    attractions = generate_section(
        f"""
List major tourist attractions in {destination} suitable for a {travel_type} trip.
Use bullet points.
""",
        150
    )

    food = generate_section(
        f"""
List local food and family-friendly food options in {destination}.
Use bullet points.
""",
        150
    )

    shopping = generate_section(
        f"""
Suggest shopping places and souvenirs in {destination}.
Use bullet points.
""",
        120
    )

    lodging = generate_section(
        f"""
Suggest low budget family-friendly hotels or homestays in {destination}.
Do not include prices.
Use bullet points.
""",
        120
    )

    tips = generate_section(
        f"""
Provide travel tips for a family trip to {destination}.
Weather, safety, best time to visit.
Use bullet points.
""",
        150
    )

    final_itinerary = f"""
📅 DAY-WISE ITINERARY
{day_wise}

📍 TOURIST ATTRACTIONS
{attractions}

🍽️ FOOD RECOMMENDATIONS
{food}

🛍️ SHOPPING SUGGESTIONS
{shopping}

🏨 LODGING SUGGESTIONS
{lodging}

🧳 TRAVEL TIPS
{tips}
"""

    return final_itinerary
