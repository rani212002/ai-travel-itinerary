# import streamlit as st
# from itinerary_generator import generate_itinerary
# from summarizer import summarize_itinerary

# st.set_page_config(page_title="AI Travel Itinerary Generator", layout="wide")

# st.title("🌍 AI Travel Itinerary Generator")
# st.write("Generate personalized travel plans using Generative AI")

# # User Input Form
# with st.form("travel_form"):
#     destination = st.text_input("Destination")
#     days = st.number_input("Number of Days", min_value=1, max_value=30, value=3)
#     budget = st.selectbox("Budget", ["Low", "Medium", "High"])
#     travel_type = st.selectbox(
#         "Travel Type",
#         ["Solo", "Family", "Adventure", "Relaxation"]
#     )

#     submit = st.form_submit_button("Generate Itinerary")

# # Processing..
# if submit:
#     with st.spinner("Generating itinerary..."):
#         itinerary = generate_itinerary(destination, days, budget, travel_type)
#         summary = summarize_itinerary(itinerary)

#     st.subheader("📌 Summarized Travel Plan")
#     st.success(summary)

#     st.subheader("📖 Detailed Itinerary")
#     st.write(itinerary)

import streamlit as st
from itinerary_generator import generate_itinerary
from summarizer import summarize_itinerary

st.set_page_config(page_title="AI Travel Itinerary Generator", layout="wide")

st.title("🌍 AI Travel Itinerary Generator")

with st.form("travel_form"):
    destination = st.text_input("Destination", "Manali")
    days = st.number_input("Number of Days", 1, 10, 3)
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    travel_type = st.selectbox("Travel Type", ["Family", "Solo", "Adventure", "Relaxation"])
    submit = st.form_submit_button("Generate")

if submit:
    with st.spinner("Generating itinerary..."):
        itinerary = generate_itinerary(destination, days, budget, travel_type)
        summary = summarize_itinerary(itinerary)

    st.subheader("📌 Summarized Plan")
    st.success(summary)

    st.subheader("📖 Detailed Itinerary")
    st.text(itinerary)
