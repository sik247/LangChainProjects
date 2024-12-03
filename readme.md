# 📚 **AI Projects Collection**

This repository includes three unique projects designed to leverage AI technologies for practical applications like financial analysis and interactive Q&A.

---

## 🌟 **Project 1: Personal CPA - Balance Sheet Edition**

### **Overview**
This Streamlit-based application uses **Google Gemini AI** to analyze balance sheets. Users can upload their own financial documents or use the default Apple 2024 Q3 balance sheet to extract meaningful insights and answer accounting-related questions.

### **Features**
- AI-powered financial analysis for uploaded or default balance sheets.
- Visual preview of the first page of the balance sheet PDF.
- Interactive Q&A to address specific accounting queries.

### **Setup Instructions**
1. **Install Dependencies**:
```bash
   pip install streamlit google-generativeai dotenv pillow PyPDF2 pdf2image
```
2. **et Up Environment Variables: Create a .env file in the root directory**:
```bash
GEM_API=your_google_gemini_api_key
```

Run the Application:
```bash 
streamlit run app.py
```
### **Usage**
- Upload a balance sheet PDF or use the default file.
- Preview the first page of the balance sheet.
- Enter questions to receive AI-generated responses tailored to your queries.


  


# 🌟 **Project 2: LangChain Q&A Demo**

### **Overview**
This project demonstrates how to use LangChain and OpenAI GPT-3.5 Turbo to build an interactive Q&A application. It allows users to ask questions and get AI-powered responses through a Streamlit interface.

### **Features**
- Generate insightful responses using OpenAI GPT-3.5.
- Simple and intuitive user interface for dynamic Q&A interactions.
### **Setup Instructions**
- Install Dependencies:
```bash
pip install langchain openai streamlit python-dotenv
```
- Set Up Environment Variables: Create a .env file with your OpenAI API key:

```bash
OPEN_API_KEY=your_openai_api_key
```
Run the Application:

```bash 
streamlit run app.py
```

# 🌟 **Project 3: PDF Query LangChain Project**

## Overview
This project uses **LangChain**, **OpenAI embeddings**, and **Cassandra** to query information from PDF documents. The app processes text from PDFs, generates embeddings, and allows interactive querying of the extracted data.

---

## Features
- Extract and split text from PDF files into manageable chunks.
- Generate embeddings using OpenAI.
- Store and query the data using Cassandra as a vector store.

---

## Setup Instructions

### 1. Install Dependencies
Run the following command to install all required libraries:
```bash
pip install cassio datasets langchain openai tiktoken PyPDF2 tqdm
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```bash
OPEN_API_KEY=your_openai_api_key
ASTRADB_APPLICATION_TOKEN=your_astra_db_application_token
ASTRA_DB_ID=your_astra_db_id
```

### 3. Install Poppler for PDF Processing
Poppler is required for PDF image conversion. Install it with:
```bash
brew install poppler
```

---

## Usage

### 1. Process a PDF
Use `PdfReader` to extract text from a PDF file:
```python
from PyPDF2 import PdfReader

pdf_reader = PdfReader("path/to/your/pdf/file.pdf")
```

### 2. Generate Embeddings
Use OpenAI to generate embeddings for the extracted text:
```python
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

embedding = OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY"))
```

### 3. Store and Query Embeddings
Store the embeddings in Cassandra and query them interactively:
```python
from langchain.vectorstores.cassandra import Cassandra

vector_store = Cassandra(
    embedding=embedding,
    table_name="PDF_Demo",
    session=None,
    keyspace=None
)
```

---

## 🛠️ Key Technologies
- **Google Generative AI**: For advanced content generation and analysis.
- **LangChain**: For building language model applications.
- **OpenAI GPT-3.5 Turbo**: For generating intelligent, conversational responses.
- **Streamlit**: For creating interactive web interfaces.
- **Cassandra**: For vector storage and retrieval of embeddings.
- **PyPDF2** and **pdf2image**: For handling and visualizing PDF content.

---

## 🛡️ License
This project is licensed under the MIT License. Contributions are welcome!

---






