from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",   # ⬅ use BASE not LARGE
    device=-1
)

def generate_itinerary(prompt):
    result = generator(
        prompt,
        max_length=700,
        do_sample=False
    )
    return result[0]["generated_text"]
