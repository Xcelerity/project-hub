import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.png", width = 300)

with col2:
    st.title("K Chiruhaas")
    p1 = """ Hi, I am Chiruhaas.I have done my Dual Degree(Bachelors and Masters) in the 
    field of Mathematics and Computing. I am passionate about technology and coding!
    """
    st.write(p1)

p2 = """Here, you’ll find some of the the Python apps and projects I’ve built!"""
st.write(p2)

df = pd.read_csv("info.csv", sep = ";")

col3,space,col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df.iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"], width=200)
        st.write(f"[Source Code]{row['url']}")

with col4:
    for index, row in df.iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"], width=200)
        st.write(f"[Source Code]{row['url']}")