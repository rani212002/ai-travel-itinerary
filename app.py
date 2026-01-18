import streamlit as st


from itinerary_generator import generate_itinerary
from summarizer import summarize_itinerary
from prompt_templates import build_itinerary_prompt
st.write("✅ App started successfully   ")


st.set_page_config(page_title="AI Travel Itinerary Generator", layout="wide")

st.title("🌍 AI Travel Itinerary Generator")

destination = st.text_input("Destination")
days = st.slider("Trip Duration (Days)", 1, 14, 5)
budget = st.selectbox("Budget Level", ["Low", "Medium", "High"])
travel_type = st.selectbox(
    "Travel Type", ["Solo", "Family", "Adventure", "Relaxation"]
)

if st.button("Generate Itinerary"):
    if not destination:
        st.warning("Please enter a destination")
    else:
        with st.spinner("Generating itinerary..."):
            prompt = build_itinerary_prompt(destination, days, budget, travel_type)
            itinerary = generate_itinerary(prompt)
            summary = summarize_itinerary(itinerary)

        st.subheader("📌 Detailed Itinerary")
        st.write(itinerary)

        st.subheader("📝 Summarized Plan")
        st.success(summary)
