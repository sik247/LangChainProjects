import streamlit as st 
from dotenv import load_dotenv
import os 
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path

from PyPDF2 import PdfReader

load_dotenv() #load all enviroment variables 

genai.configure(api_key = os.environ["GEM_API"])

st.set_page_config(
    page_title = "Invoice Reader",
    layout = "centered"

)


st.header("Personal CPA - Balance Sheet Edition")

#function to load gemini pro vision 
model = genai.GenerativeModel(model_name = 'gemini-1.5-pro')

# samplepdf = genai.upload_file('/Users/sanginkang/Desktop/LangChain/invoiceextractro/FY23_Q1_Consolidated_Financial_Statements.pdf')

# user_upload = st.file_uploader("Would you like to search information from the balance sheet of a different company?[Default: Apple 2024 q3]", type = ['pdf'])
# extrapdf = samplepdf if user_upload is None else genai.upload_file(user_upload)
#     # loaded user's pdf 
#     #make the pdf's users new upad -> what is 

default_pdf_path = '/Users/sanginkang/Desktop/LangChain/llmAccountant/FY23_Q1_Consolidated_Financial_Statements.pdf'
# Display a preview of a PDF file
def display_pdf_images(pdf_path, uploaded_file=None):
    """Converts the first page of a PDF to an image and displays it."""
    try:
        if uploaded_file:  # If a file is uploaded by the user
            pages = convert_from_path(uploaded_file, first_page=1, last_page=1)
        else:  # Use the default file
            pages = convert_from_path(pdf_path, first_page=1, last_page=1)
        
        for page in pages:
            st.image(page, caption="PDF Preview (First Page)", use_container_width=True)
    except Exception as e:
        st.error(f"Error loading PDF image: {e}")

# File uploader for user-provided PDF
user_upload = st.file_uploader(
    "Upload a balance sheet PDF [Default: Apple 2024 Q3 Balance Sheet]",
    type=['pdf']
)

# Decide which file to use
if user_upload is not None:
    # User uploaded a file
    display_pdf_images(None, user_upload)
    extrapdf = genai.upload_file(user_upload)
else:
    # No file uploaded; use the default file
    st.subheader("Default File: Apple 2024 Q3 Balance Sheet")
    display_pdf_images(default_pdf_path)
    extrapdf = genai.upload_file(default_pdf_path)


def get_gemini_response(input, file, prompt): #input is the role of model/ prompt is the message 
    #gemini takes all prompts as a list 
    response = model.generate_content([input,file, prompt])
    return response 



input_prompt = """You are a certified CPA. Given a balance sheet, please provide necessary accoutning information and answer questions regarding the balance sheet"""
user_prompt = st.text_input("Please enter what information you need to find from the Balance Sheet")
submit = st.button("Ask the CPA")
if submit:

    with st.spinner("Find Relevant Information"):
        result = get_gemini_response(input_prompt,user_upload,user_prompt)
        st.subheader('Here is the relevant response')
        st.write(result.text)
