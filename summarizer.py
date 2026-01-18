from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1
)

def summarize_itinerary(text):
    return summarizer(
        text[:1500],
        max_length=130,
        min_length=60,
        do_sample=False
    )[0]["summary_text"]
