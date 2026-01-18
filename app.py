# app.py
import streamlit as st
from modules.itinerary_generator import generate_itinerary

st.title("AI Travel Itinerary Generator")

# User Inputs
destination = st.text_input("Destination")
days = st.number_input("Number of days", min_value=1, max_value=30, value=3)
budget = st.selectbox("Budget Level", ["Low", "Medium", "High"])
travel_type = st.selectbox("Travel Type", ["Solo", "Family", "Adventure", "Relaxation"])

if st.button("Generate Itinerary"):
    if not destination:
        st.warning("Please enter a destination.")
    else:
        with st.spinner("Generating itinerary..."):
            detailed_itinerary = generate_itinerary(destination, days, budget, travel_type)

        st.subheader("Detailed Itinerary")
        # Display each line properly
        st.text(detailed_itinerary)
