
# 🌟 **LLM App Project**

## Overview
This project uses **LangChain**, **OpenAI embeddings**, and **Pinecone** to query information from PDF documents. The app processes text from PDFs, generates embeddings, and allows interactive querying of the extracted data.

---

## Features
- Extract and split text from PDF files into manageable chunks.
- Generate embeddings using OpenAI.
- Store and query the data using Pinecone as a vector store.

---

## Setup Instructions

### 1. Install Dependencies
Run the following command to install all required libraries:
```bash
pip install langchain openai pinecone-client PyPDF2 tqdm
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```plaintext
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 3. Initialize Pinecone
Set up your Pinecone index using their dashboard and configure the `index_name` in your script.

---

## Usage

### 1. Process a PDF
Use `PyPDFLoader` to extract text from a PDF file:
```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("path/to/your/pdf/file.pdf")
documents = loader.load()
```

### 2. Chunk the Text
Split the extracted text into manageable chunks for embedding generation:
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = splitter.split_documents(documents)
```

### 3. Generate Embeddings
Use OpenAI to generate embeddings for the extracted text:
```python
from langchain.embeddings.openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
vectors = embedding.embed_documents([chunk.page_content for chunk in chunks])
```

### 4. Store Embeddings in Pinecone
Store the embeddings in Pinecone for efficient retrieval:
```python
from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "your-index-name"

vector_store = Pinecone.from_documents(
    documents=chunks,
    embeddings=embedding,
    index_name=index_name
)
```

### 5. Query the System
Retrieve relevant documents and use GPT-4 to answer queries:
```python
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4")
qa_chain = load_qa_chain(llm)

query = "What is the use case for AI in daily life?"
results = vector_store.similarity_search(query, k=2)
response = qa_chain.run(input_documents=results, question=query)
print(response)
```

---

## 🛠️ Key Technologies
- **LangChain**: For building language model applications.
- **OpenAI GPT-4**: For generating intelligent, conversational responses.
- **Pinecone**: For vector storage and retrieval of embeddings.
- **PyPDF2**: For handling PDF content.

---

## 🛡️ License
This project is licensed under the MIT License. Contributions are welcome!

---
