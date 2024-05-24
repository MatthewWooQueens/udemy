import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
c1 = st.container()
col1, col2, col3= st.columns(3)
col_list = [col1,col2,col3]
with c1:
    st.title("The Best Company Ever")
    st.write("Far superior to all other companies")
    st.header("Our Team")

df = pd.read_csv('./data.csv')

for ind, data in df.iterrows():
    with col_list[ind % len(col_list)]:
        st.header(f"{data[0].capitalize()} {data[1].capitalize()}")
        st.write(data[2])
        st.image(f"./images/{data[3]}")
