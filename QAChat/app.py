from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 


def get_openai_response(question):
    llm = OpenAI(api_key = os.getenv("OPEN_API_KEY"), model_name = "gpt-3.5-turbo-instruct", temperature = 0.5)
    response = llm(question)
    return response 

st.set_page_config(page_title = "Q&A Demo")
st.header("Lainchain Application")

input = st.text_input("Input: ", key = "input")
response = get_openai_response(input)

submit = st.button("Please ask a question")


if submit: 
    st.subheader("Response:")
    st.write(response)


