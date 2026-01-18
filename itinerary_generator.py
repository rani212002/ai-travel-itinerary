import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.eval()

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
Fill in the details for the following travel itinerary using REAL places from {destination}.
Do NOT explain anything. Just fill the bullets.

Day 1:
Daily Activities:
- 
- 

Tourist Attractions:
- 
- 

Food Suggestions:
- 
- 

Travel Tips:
- 
- 
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            do_sample=False,
            num_beams=5,
            repetition_penalty=1.2
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
