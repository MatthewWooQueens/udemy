import streamlit as st
import plotly.express as px
import pandas as pd

def read():
    dates = []
    temp = []
    with open("data.txt", "r") as file:
        for line in file.readlines():
            s = line[:len(line)-1].split(',')
            print(s)
            dates.append(s[0])
            temp.append(s[1])
    return dates, temp
    #c = pd.read_csv('data.txt')
    #return c
    

def main():
    d, t= read()
    figure = px.line(x=d, y=t, labels={"x":"Date","y":"Temperature (c)"})
    st.plotly_chart(figure)

main()
