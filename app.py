import streamlit as st

@st.cache_resource
def load_models():
    from itinerary_generator import generate_itinerary
    from summarizer import summarize_itinerary
    return generate_itinerary, summarize_itinerary

generate_itinerary, summarize_itinerary = load_models()
