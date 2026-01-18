import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.eval()

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
List REAL places in {destination} in the format below.

Day 1:
Daily Activities:
- Visit a famous landmark in {destination}
- Explore a popular area in {destination}

Tourist Attractions:
- One famous museum in {destination}
- One famous historical place in {destination}

Food Suggestions:
- One famous restaurant in {destination}
- One local food item in {destination}

Travel Tips:
- One useful travel tip for {destination}
- One useful safety tip for {destination}
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=False,
            num_beams=4
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
