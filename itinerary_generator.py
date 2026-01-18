from transformers import pipeline

# Stronger instruction-following model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"  # ⬅ MUCH better than small
)

def generate_itinerary(prompt: str) -> str:
    output = generator(
        prompt,
        max_length=1200,
        do_sample=False,
        repetition_penalty=1.1
    )

    text = output[0]["generated_text"].strip()

    # Fallback if model under-generates
    if len(text.split()) < 50:
        return (
            "Day 1:\n"
            "Morning:\n- City sightseeing\n\n"
            "Afternoon:\n- Visit local attractions\n\n"
            "Evening:\n- Explore local food\n\n"
            "Tourist Attractions:\n- Popular landmarks\n\n"
            "Food Recommendations:\n- Local cuisine\n\n"
            "Travel Tips:\n- Plan transport in advance\n"
        )

    return text
