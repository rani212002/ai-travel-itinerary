from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large",
    max_length=1200
)

def generate_itinerary(prompt):
    response = generator(prompt)
    return response[0]["generated_text"]
