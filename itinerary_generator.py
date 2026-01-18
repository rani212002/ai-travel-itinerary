from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use FLAN-T5 Large (instruction-following)
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
Create a detailed {days}-day travel itinerary for {destination}.
Budget: {budget}.
Travel type: {travel_type}.

For each day, include clearly labeled sections:
1. Daily Activities
2. Tourist Attractions
3. Food Suggestions
4. Travel Tips

Format output for readability.
"""

    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    itinerary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return itinerary
