from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(text: str) -> str:
    # If text is too short, no need to summarize
    if len(text.split()) < 50:
        return text

    max_len = min(120, max(30, len(text.split()) // 3))

    result = summarizer(
        text[:1500],
        max_length=max_len,
        min_length=30,
        do_sample=False
    )
    return result[0]["summary_text"]
