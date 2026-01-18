from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",  # ⬅ smallest, safest
    device=-1
)

def generate_itinerary(prompt):
    return generator(
        prompt,
        max_length=512,
        do_sample=False
    )[0]["generated_text"]
