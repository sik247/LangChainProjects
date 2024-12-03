# 📚 **PDF Query LangChain Project**

This project leverages **LangChain**, **OpenAI embeddings**, and **Cassandra** to analyze and query PDFs. It includes functionality for chunking text, storing embeddings, and querying information using vector stores.

---

## 🚀 **Features**

- Extract and process text from PDF files.
- Generate embeddings using OpenAI models.
- Store and query embeddings in Cassandra using LangChain's vector store utilities.
- Interactive querying of PDF content.

---

## 🛠️ **Dependencies**

Install the required dependencies using:
```bash
pip install -q cassio datasets langchain openai tiktoken PyPDF2
```
HK
this is not markdown because i cant copy and paste this


You're right. Here's a pure Markdown version that you can easily copy and paste:

markdown

Copy
# 📚 **PDF Query LangChain Project**

This project leverages **LangChain**, **OpenAI embeddings**, and **Cassandra** to analyze and query PDFs. It includes functionality for chunking text, storing embeddings, and querying information using vector stores.

## 🚀 Features

- Extract and process text from PDF files
- Generate embeddings using OpenAI models
- Store and query embeddings in Cassandra using LangChain's vector store utilities
- Interactive querying of PDF content

## 🛠️ Dependencies


⚙️ Setup
### 1. Install Dependencies
Run the following command to ensure all necessary Python libraries are installed:
```bash
pip install -q cassio datasets langchain openai tiktoken PyPDF2
pip install -r requirements.txt
```
### 2. Set Up Environment Variables
Create a .env file in the project root with the following:

```bash
OPEN_API_KEY=your_openai_api_key
ASTRADB_APPLICATION_TOKEN=your_astra_db_application_token
ASTRA_DB_ID=your_astra_db_id
```
### 3. Install Poppler for PDF Processing
If you need to convert PDFs to text or images and are missing utilities like pdftotext, install Poppler. For macOS:
```bash
brew install poppler
```
📚 Usage
### 1. Initialize Database
Before running the code, initialize Cassandra using:

```bash 
import cassio
cassio.init(
    token=os.getenv("ASTRADB_APPLICATION_TOKEN"), 
    database_id=os.getenv("ASTRA_DB_ID")
)
```
### 2. Process PDF
Read a PDF file and initialize PdfReader:

```bash
from PyPDF2 import PdfReader
pdf_reader = PdfReader("World Bank Annual Report 2024.pdf")
```
### 3. Generate Embeddings
Use OpenAI for generating embeddings:

```bash 
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

llm = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
embedding = OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY"))
```
### 4. Create Vector Store
Initialize the Cassandra vector store to store embeddings:

```bash 
from langchain.vectorstores.cassandra import Cassandra

astra_vector_store = Cassandra(
    embedding=embedding,
    table_name="QA_Demo",
    session=None,
    keyspace=None
)
```
### 5. Split Text into Chunks
Split text into manageable chunks for embedding and querying:

```bash 
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len
)
text_chunks = text_splitter.split_text(raw_text)
```
### 6. Store Chunks in Vector Store
Store the chunks into the initialized Cassandra vector store for querying:
```bash
astra_vector_store.add_texts(text_chunks)
```
### 7. Query the Vector Store
Query the vector store interactively using LangChain utilities.

💡 Key Libraries
LangChain: Framework for processing and embedding text
OpenAI: Provides embeddings for text
Cassandra: Vector store for storing and querying embeddings
PyPDF2: Library for reading PDF files

🛡️ License
This project is open-source under the MIT license. Contributions are welcome!



