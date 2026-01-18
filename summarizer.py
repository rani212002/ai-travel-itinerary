from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(itinerary_text):
    input_length = len(itinerary_text.split())

    # Dynamically set summary length
    max_len = min(120, max(30, input_length // 2))
    min_len = min(60, max(20, input_length // 4))

    summary = summarizer(
        itinerary_text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )[0]["summary_text"]

    return summary
