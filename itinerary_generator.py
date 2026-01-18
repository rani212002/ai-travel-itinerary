import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
You are a professional travel planner.

Generate a detailed {days}-day travel itinerary for {destination}.

Travel details:
- Budget level: {budget}
- Travel type: {travel_type}

IMPORTANT INSTRUCTIONS:
- Use real places, activities, food, and tips.
- No placeholders like Activity 1 or Restaurant 1.

Format:

Day 1:
Daily Activities:
- ...

Tourist Attractions:
- ...

Food Suggestions:
- ...

Travel Tips:
- ...

Repeat for all days.
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=min(800, 150 * days),
            do_sample=True,
            temperature=0.8,
            top_p=0.9
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)