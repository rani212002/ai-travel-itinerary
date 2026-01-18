from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(text):
    return summarizer(
        text[:1200],
        max_length=120,
        min_length=60,
        do_sample=False
    )[0]["summary_text"]
