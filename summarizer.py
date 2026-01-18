from transformers import pipeline

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(itinerary_text):
    # Adjust max_length dynamically based on input length
    input_length = len(itinerary_text.split())
    
    # Ensure summary length is reasonable (shorter than input)
    max_len = min(150, max(30, input_length // 2))  # at most 150 tokens, at least 30
    min_len = min(80, max(20, max_len // 2))        # at least 20, at most half of max_len

    summary = summarizer(
        itinerary_text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )[0]["summary_text"]

    return summary
