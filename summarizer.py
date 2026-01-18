# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="facebook/bart-large-cnn"
# )

# def summarize_itinerary(text):
#     return summarizer(
#         text,
#         max_length=160,
#         min_length=80,
#         do_sample=False
#     )[0]["summary_text"]
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_itinerary(text):
    return summarizer(
        text,
        max_length=180,
        min_length=90,
        do_sample=False
    )[0]["summary_text"]
