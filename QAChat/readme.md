# 🤖 **LangChain Q&A Demo**

A **Streamlit-powered application** that uses LangChain and OpenAI to answer user questions interactively. With this tool, you can explore how **large language models** can process and respond to your queries in real-time.

---

## 🚀 **Features**

- **AI-Powered Responses**: Uses OpenAI's GPT-3.5 Turbo (via LangChain) to provide insightful answers.
- **Interactive Interface**: A user-friendly Streamlit application for seamless interaction.
- **Customizable Parameters**: Modify the OpenAI model's behavior (e.g., temperature) to suit your needs.

---

## 🛠️ **Tech Stack**

- **Python**: Core programming language.
- **LangChain**: Framework for building language model-powered applications.
- **OpenAI GPT-3.5**: Generates AI-based responses.
- **Streamlit**: Simplifies building web-based user interfaces.
- **dotenv**: Manages environment variables.

---

## ⚙️ **Setup and Installation**

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo-name/langchain-qa-demo.git
cd langchain-qa-demo
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
### 3. Add Your OpenAI API Key
Create a .env file in the project root directory and add your OpenAI API key:

```bash
OPEN_API_KEY=your_openai_api_key
```

### 4. Run the Application
Start the Streamlit app with the following command:

```bash
streamlit run app.py
```