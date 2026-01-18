import streamlit as st
from itinerary_generator import generate_itinerary
from summarizer import summarize_itinerary
from utils import validate_inputs

st.set_page_config(page_title="AI Travel Itinerary Generator", layout="wide")
st.title("✈️ AI Travel Itinerary Generator")

# ---------------- Sidebar Inputs ----------------
st.sidebar.header("Enter Your Travel Preferences")
destination = st.sidebar.text_input("Destination")
days = st.sidebar.number_input("Number of Days", min_value=1, max_value=30, value=5)
budget = st.sidebar.selectbox("Budget Level", ["Low", "Medium", "High"])
travel_type = st.sidebar.selectbox("Travel Type", ["Solo", "Family", "Adventure", "Relaxation"])
generate_btn = st.sidebar.button("Generate Itinerary")

# ---------------- Main Logic ----------------
if generate_btn:
    is_valid, error_msg = validate_inputs(destination, days)
    if not is_valid:
        st.error(error_msg)
    else:
        with st.spinner("Generating detailed itinerary..."):
            detailed_itinerary = generate_itinerary(destination, days, budget, travel_type)

        with st.spinner("Summarizing itinerary..."):
            summary = summarize_itinerary(detailed_itinerary)

        # ---------------- Display Detailed Itinerary ----------------
        # st.subheader("📋 Detailed Travel Itinerary")
        # Use markdown to preserve line breaks
        st.markdown(detailed_itinerary.replace("\n", "  \n"))

        # ---------------- Display Summarized Itinerary ----------------
        st.subheader("📝 Concise Summary")
        # st.success(summary)