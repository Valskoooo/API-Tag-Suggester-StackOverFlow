import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Stack Overflow Tags Predictions API")
st.markdown("This is a simple web app that uses a Machine Learning model to predict tags for a given sentence.")
st.markdown("Please enter a sentence and the number of tags you want to predict.")
# Case de saisie de texte
user_input = st.text_input("Enter a sentence:")

# Afficher le texte saisi
if user_input:
    print(user_input)
    tags = requests.get(f'{API_URL}/tag/?n=5&s={user_input}')
    st.write("Resultat:", tags.json())