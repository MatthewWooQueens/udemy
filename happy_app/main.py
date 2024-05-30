import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")
df = df.select_dtypes(include="number")
opts = list(df.columns.values)
for ind, data in enumerate(opts):
    opts[ind] = opts[ind].replace("_", " ").title()

st.title("In Search for Happiness")
xaxis = st.selectbox("Select the data for the X-axis", options = opts)
yaxis = st.selectbox("Select the data for the Y-axis", options = opts)
st.subheader(f"{xaxis} and {yaxis}")

xdata = df.iloc[:, opts.index(xaxis)]
ydata = df.iloc[:, opts.index(yaxis)]


figure = px.scatter(x=xdata, y=ydata, labels={"x":xaxis,"y":yaxis}, )
st.plotly_chart(figure)
