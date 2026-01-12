from transformers import pipeline

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(itinerary_text):
    summary = summarizer(
        itinerary_text,
        max_length=150,
        min_length=60,
        do_sample=False
    )
    return summary[0]["summary_text"]
