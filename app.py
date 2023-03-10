import streamlit as st
from PIL import Image
from transformers import pipeline


summarizer = pipeline("summarization")

image = Image.open("Logo.png")
st.image(image)


st.title("  WELCOME TO SUMMERIZE ME")
st.markdown("------")


options = ["CODE1", "CODE2", "CODE3", "CODE4"]
selected_option = st.selectbox("Select an option", options)

if selected_option == "CODE1":
    st.write("You selected CODE1!")
    text = st.text_area('Enter Text Below :(Maximum limit 300words)', height=900)
    submit = st.button('Generate') 
    if submit: 
        st.subheader("Summary:")
        with st.spinner(text="This may take a moment..."):
            summWords = summarizer(text, max_length=max_lengthy, min_length=15, num_beams=num_beamer, do_sample=True, early_stopping=True, repetition_penalty=1.5, length_penalty=1.5)
        text2 =summWords[0]["summary_text"]
        st.success(text2)



