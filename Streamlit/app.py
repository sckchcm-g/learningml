import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Hello, Streamlit!")

## Display a simple text
st.write("thsi is is a simple text.")

## Create a simple dataframe

df=  pd.DataFrame({
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": [10, 20, 30, 40, 50],
    "Column 3": [100, 200, 300, 400, 500]
})

#Display the dataframe
st.write("This is the dataframe:")
st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)