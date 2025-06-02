import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name:")

age=st.slider("select your age", 0, 100, 25)

st.write(f"You are {age} years old!")

options = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Choose a programming language:", options)
st.write(f"You selected: {choice}")


if name:
    st.write(f"Hello, {name}!")


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

uploaded_files = st.file_uploader("choose a csv file", type="csv")

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)
