from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(text: str) -> str:
    if len(text.split()) < 80:
        return text

    summary = summarizer(
        text[:1800],
        max_length=180,
        min_length=80,
        do_sample=False
    )[0]["summary_text"]

    return summary
