import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]
st.title("Iris Species Classification")
st.write("### Input Features")
st.write(f"**Sepal Length:** {sepal_length} cm")
st.write(f"**Sepal Width:** {sepal_width} cm")
st.write(f"**Petal Length:** {petal_length} cm")
st.write(f"**Petal Width:** {petal_width} cm")
st.write("### Predicted Species")
st.write(f"**Species:** {predicted_species}")
st.write("### Model Information")
st.write("This model uses a Random Forest Classifier trained on the Iris dataset to predict the species of iris flowers based on their sepal and petal dimensions.")
st.write("### About the Iris Dataset")
st.write("The Iris dataset is a classic dataset in machine learning, consisting of 150 samples from three species of iris flowers (Iris setosa, Iris versicolor, and Iris virginica). Each sample has four features: sepal length, sepal width, petal length, and petal width.")
