import streamlit as st
import plotly.express as px
st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast slider", min_value=1, max_value=5, help="Select number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

def get_data(days):
    dates = ['2022-25-16', '2022-26-10', '2022-27-10']
    temperatures = [10,12,15]
    temperatures = [days*i for i in temperatures]
    
    return dates, temperatures

d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x":"Date","y":"Temperature (c)"})
st.plotly_chart(figure)
