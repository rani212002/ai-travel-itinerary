from transformers import pipeline

# Load text generation model
generator = pipeline(
    "text-generation",
    model="gpt2",
    # max_length=600
)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}.
    Budget: {budget}
    Travel Type: {travel_type}

    Include:
    - Day-wise activities
    - Tourist attractions
    - Food recommendations
    - Travel tips
    """

    response = generator(prompt, num_return_sequences=1)
    return response[0]["generated_text"]
