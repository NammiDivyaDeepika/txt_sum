import streamlit as st
import streamlit_extras
from PIL import Image
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
#from C1 import summary

summarizer = pipeline("summarization")

image = Image.open("Logo.png")
st.image(image)


st.title("  WELCOME TO SUMMERIZE ME")
st.markdown("------")


options = ["CODE1", "CODE2", "CODE3", "CODE4"]
selected_option = st.selectbox("Select an option", options)

if selected_option == "CODE1":
    st.write("You selected CODE1!")
    max_lengthy = st.slider('Maximum summary length (words)', min_value=30, max_value=150, value=60, step=10)
    num_beamer = st.slider('Speed vs quality of summary (1 is fastest)', min_value=1, max_value=8, value=4, step=1)
    text = st.text_area('Enter Text Below :', height=900)
    submit = st.button('Generate') 
    if submit: 
        st.subheader("Summary:")
        with st.spinner(text="This may take a moment..."):
            summWords = summarizer(text, max_length=max_lengthy, min_length=15, num_beams=num_beamer, do_sample=True, early_stopping=True, repetition_penalty=1.5, length_penalty=1.5)
        text2 =summWords[0]["summary_text"]
        st.success(text2)


elif selected_option == "CODE2":
    st.write("You selected CODE2!")
    max_lengthy = st.slider('Maximum summary length (words)', min_value=30, max_value=150, value=60, step=10)
    num_beamer = st.slider('Speed vs quality of summary (1 is fastest)', min_value=1, max_value=8, value=4, step=1)
    text3 = st.text_area('Enter Text Below :', height=900)
    submit = st.button('Generate') 
    if submit:
        st.success(text2)
