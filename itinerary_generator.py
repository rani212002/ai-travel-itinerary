from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
You are a professional travel planner.

Generate a detailed {days}-day travel itinerary for {destination}.

Travel details:
- Budget level: {budget}
- Travel type: {travel_type}

IMPORTANT INSTRUCTIONS:
- Replace all placeholders with REAL activities, places, restaurants, and tips.
- Do NOT use words like "Activity 1", "Attraction 1", or "Restaurant 1".
- Provide realistic and specific information.

Use the following format strictly:

Day 1:
Daily Activities:
- <real activity>
- <real activity>

Tourist Attractions:
- <real attraction>
- <real attraction>

Food Suggestions:
- <real restaurant or local food>
- <real restaurant or local food>

Travel Tips:
- <real tip>
- <real tip>

Repeat this format for all days up to Day {days}.
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=300 * days,
        do_sample=True,
        temperature=0.9,
        top_p=0.95
    )

    itinerary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return itinerary
