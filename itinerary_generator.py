from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
Create a {days}-day travel itinerary for {destination}.
Budget: {budget}.
Travel type: {travel_type}.

Use this exact format for each day:

Day 1:
Daily Activities:
- Activity 1
- Activity 2

Tourist Attractions:
- Attraction 1
- Attraction 2

Food Suggestions:
- Restaurant 1
- Restaurant 2

Travel Tips:
- Tip 1
- Tip 2

Repeat the same format for all days from Day 1 to Day {days}.
Do not add extra paragraphs or unnecessary explanations.
"""

    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=800 + (days * 200),  # more tokens for multiple days
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    itinerary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return itinerary
