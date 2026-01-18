import streamlit as st
import warnings

from itinerary_generator import generate_itinerary
from summarizer import summarize_itinerary
from prompt_templates import build_itinerary_prompt

# ------------------ BASIC SETUP ------------------
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="AI Travel Itinerary Generator",
    layout="wide"
)

st.write("✅ App started successfully")

st.title("🌍 AI Travel Itinerary Generator")
st.markdown(
    "Generate **personalized, day-wise travel itineraries** using Generative AI."
)

# ------------------ USER INPUTS ------------------
destination = st.text_input("Destination", placeholder="e.g. Paris")
days = st.slider("Trip Duration (Days)", 1, 14, 5)
budget = st.selectbox("Budget Level", ["Low", "Medium", "High"])
travel_type = st.selectbox(
    "Travel Type", ["Solo", "Family", "Adventure", "Relaxation"]
)

# ------------------ GENERATE BUTTON ------------------
if st.button("Generate Itinerary"):
    if not destination.strip():
        st.warning("⚠️ Please enter a destination")
    else:
        with st.spinner("✈️ Generating your personalized itinerary..."):
            prompt = build_itinerary_prompt(destination, days, budget, travel_type)
            itinerary = generate_itinerary(prompt)
            summary = summarize_itinerary(itinerary)

      st.divider()
st.subheader("📌 Detailed Day-wise Itinerary")

# DEBUG: show raw output first
with st.expander("🔍 Raw AI Output (Debug)", expanded=False):
    st.text(itinerary)

# Formatted display
day_blocks = itinerary.split("Day ")

for block in day_blocks:
    if block.strip().startswith(tuple(str(i) for i in range(1, 15))):
        day_title = "Day " + block.split(":")[0]
        day_content = block.replace(block.split(":")[0] + ":", "").strip()

        with st.expander(day_title, expanded=True):
            st.markdown(day_content)


        # ------------------ SUMMARY SECTION ------------------
        st.divider()
        st.subheader("📝 Concise Travel Summary")
        st.success(summary)

        # ------------------ FOOTER ------------------
        st.caption(
            "🤖 Powered by HuggingFace Generative AI models | Built with Streamlit"
        )
