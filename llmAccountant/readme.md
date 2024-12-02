# 📊 Personal CPA - Balance Sheet Edition

A powerful **AI-driven financial assistant** designed to extract insights from balance sheets and answer accounting-related queries. Leveraging **Google Gemini AI**, this application reads PDF files and provides detailed, professional-grade financial analysis. The default example uses Apple's 2024 Q3 balance sheet, but users can upload their own financial documents for personalized insights.

---

## 🚀 Features

- **Generative AI Analysis**: Uses Google Gemini AI to interpret and analyze balance sheet PDFs.
- **Dynamic File Support**: Processes both the preloaded Apple balance sheet and user-uploaded files.
- **Visual PDF Preview**: Displays the first page of the PDF as an image for intuitive user interaction.
- **User Queries**: Allows users to input specific questions about the financial data for tailored responses.
- **Streamlit Interface**: A user-friendly, web-based interface for seamless interaction.

---

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Framework for building interactive web applications.
- **Google Generative AI (Gemini)**: Advanced AI model for understanding and processing documents.
- **pdf2image**: Converts PDF pages to images for visual previews.
- **PyPDF2**: Extracts text from PDF documents.
- **Pillow**: Handles image processing.

---
## ⚙️ Installation

Follow these steps to set up the project on your local machine:

### 1. Install Dependencies
Install the required Python packages using:
```bashgit re
pip install -r requirements.txt
```


### 3. Add Your Gemini API Key to a .env File
Create a .env file in the project root and add your API key:

```bash 
GEM_API=your_google_gemini_api_key
```
### 4. Install poppler-utils (Required for PDF Image Preview)
If you’re using macOS, you can install Poppler via Homebrew:

```bash
brew install poppler
```
### 5. Run the Application
Start the Streamlit app with the following command:
```bash
streamlit run app.py
```