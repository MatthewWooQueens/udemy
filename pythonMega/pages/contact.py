import streamlit as st
import pandas as pd
from send_email import send_email

st.header("Contact Us")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    topics = pd.read_csv("./pages/topics.csv")
    discuss = st.selectbox("What topic do you want to discuss?", topics["topic"])
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
