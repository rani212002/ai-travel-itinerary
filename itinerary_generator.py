from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_itinerary(prompt):
    response = generator(
        prompt,
        max_length=700,
        do_sample=False
    )

    return response[0]["generated_text"]
