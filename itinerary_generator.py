from transformers import pipeline

# Load text generation model
generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=700
)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}.
    Budget: {budget}.
    Travel type: {travel_type}.
    The itinerary should include clear sections for each day:
    1. Daily Activities
    2. Tourist Attractions
    3. Food Suggestions
    4. Travel Tips

    Format the output so each day is separated and each section is labeled.
    """

    response = generator(prompt)[0]["generated_text"]

    return response
