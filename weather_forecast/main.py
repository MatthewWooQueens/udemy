import streamlit as st

st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast slider", min_value=1, max_value=5, help="Select number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

