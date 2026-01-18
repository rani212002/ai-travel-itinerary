from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(text):
    summary = summarizer(
        text,
        max_length=200,
        min_length=80,
        do_sample=False
    )
    return summary[0]["summary_text"]
