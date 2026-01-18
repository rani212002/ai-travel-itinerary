from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(itinerary_text):
    summary = summarizer(
        itinerary_text,
        max_length=150,
        min_length=80,
        do_sample=False
    )[0]["summary_text"]
    return summary
