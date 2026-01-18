import streamlit as st

from itinerary_generator import generate_itinerary
from summarizer import summarize_itinerary
from prompt_templates import build_itinerary_prompt

# -------------------------------------------------
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# -------------------------------------------------
st.set_page_config(
    page_title="AI Travel Itinerary Generator",
    layout="wide"
)

# -------------------------------------------------
# APP HEADER
# -------------------------------------------------
st.title("🌍 AI Travel Itinerary Generator")
st.caption("Generate detailed, day-wise travel plans using Generative AI")

# -------------------------------------------------
# USER INPUTS
# -------------------------------------------------
st.subheader("✈️ Trip Details")

destination = st.text_input("Destination (City / Country)")

days = st.slider(
    "Trip Duration (Days)",
    min_value=1,
    max_value=14,
    value=5
)

budget = st.selectbox(
    "Budget Level",
    ["Low", "Medium", "High"]
)

travel_type = st.selectbox(
    "Travel Type",
    ["Solo", "Family", "Adventure", "Relaxation"]
)

# -------------------------------------------------
# GENERATE BUTTON
# -------------------------------------------------
if st.button("🚀 Generate Itinerary"):
    if not destination:
        st.warning("⚠️ Please enter a destination")
    else:
        with st.spinner("Generating your travel itinerary..."):
            prompt = build_itinerary_prompt(
                destination,
                days,
                budget,
                travel_type
            )

            itinerary = generate_itinerary(prompt)
