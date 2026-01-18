from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def generate_itinerary(prompt):
    output = generator(
        prompt,
        max_length=600,
        do_sample=False
    )
    return output[0]["generated_text"]
