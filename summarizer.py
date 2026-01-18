from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1
)

def summarize_itinerary(text):
    summary = summarizer(
        text[:2000],  # ⬅ prevent token overflow
        max_length=150,
        min_length=60,
        do_sample=False
    )
    return summary[0]["summary_text"]
