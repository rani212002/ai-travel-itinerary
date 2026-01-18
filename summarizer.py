from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(text):
    if len(text.split()) < 40:
        return text

    summary = summarizer(
        text,
        max_length=120,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]
