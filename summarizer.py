from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_itinerary(itinerary_text):
    summary = summarizer(itinerary_text, max_length=200, min_length=100, do_sample=False)
    return summary[0]['summary_text']
