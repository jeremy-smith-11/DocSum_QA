# Document Summarization and Q&A Chatbot

## Overview

This project is a web application that enables users to upload PDF documents, extract and summarize their text content, and interact with a Q&A chatbot to get answers related to the document. The application leverages advanced models for text summarization and question-answering to provide valuable insights and answers.

## Features

- **PDF Upload**: Upload PDF files for processing.
- **Text Extraction**: Extract and clean text from the uploaded PDF.
- **Text Summarization**: Generate concise summaries of the extracted text.
- **Q&A Chatbot**: Ask questions related to the PDF content and receive relevant answers.
- **User-Friendly UI**: Clean and interactive interface with logo integration.

## Technologies

- **Streamlit**: Framework for building the web application.
- **Ollama / Llama3**: For text summarization and question-answering models.
- **PyPDF2**: For extracting text from PDF files.
- **Python**: Programming language used for development.

## Setup Instructions

### Prerequisites

Ensure Python 3.7 or higher is installed. Check your Python version with:

## Installation

1. Clone the repository:
````
git clone <repository_url>
cd <repository_directory>
````

2. Create a virtual environment (recommended):
````
python -m venv venv
````

3. Activate the virtual environment:
````
venv\Scripts\activate
````

4. Install the required packages:
````
pip install -r requirements.txt
````

## Configuration

### 1. Update app.py:

Make sure the path to the logo image and any other local paths are correctly set in the app.py file.

### 2. Set up your models:

Ensure that the models used in QA_chatbot.py are properly downloaded and accessible.

## Usage

### 1. Run the application:
````
streamlit run app.py
````

### 2. Interact with the application:

Upload PDF: Click the "Upload a PDF file" button to upload your PDF document.
Summarize: Click the "Summarize" button to get a summary of the extracted text.
Ask Questions: Enter your question in the text input field to get answers based on the PDF content.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project’s coding standards and includes tests where applicable.

### License

This project is licensed under the MIT License. 
### Acknowledgements

Ollama: For working with (local) Ollama and Llama large language models.
Streamlit: For making it easy to build interactive web applications.

Model	Hallucination Rate	Factual Consistency Rate	Answer Rate	Average Summary Length (Words)
Zhipu AI GLM-4-9B-Chat	1.3 %	98.7 %	100.0 %	58.1
GPT-4o	1.5 %	98.5 %	100.0 %	77.8
GPT-4o-mini	1.7 %	98.3 %	100.0 %	76.3
GPT-4-Turbo	1.7 %	98.3 %	100.0 %	86.2
GPT-4	1.8 %	98.2 %	100.0 %	81.1
GPT-3.5-Turbo	1.9 %	98.1 %	99.6 %	84.1
Microsoft Orca-2-13b	2.5 %	97.5 %	100.0 %	66.2
Intel Neural-Chat-7B-v3-3	2.6 %	97.4 %	100.0 %	60.7
Snowflake-Arctic-Instruct	3.0 %	97.0 %	100.0 %	68.7
Microsoft Phi-3-mini-128k-instruct	3.1 %	96.9 %	100.0 %	60.1
01-AI Yi-1.5-34B-Chat	3.7 %	96.3 %	100.0 %	83.7
Llama-3.1-405B-Instruct	3.9 %	96.1 %	99.6 %	85.7
Microsoft Phi-3-mini-4k-instruct	4.0 %	96.0 %	100.0 %	86.8
Mistral-Large2	4.1 %	95.9 %	100.0 %	77.4
Llama-3-70B-Chat-hf	4.1 %	95.9 %	99.2 %	68.5
Qwen2-72B-Instruct	4.7 %	95.3 %	100.0 %	100.1
Mixtral-8x22B-Instruct-v0.1	4.7 %	95.3 %	99.9 %	92.0
01-AI Yi-1.5-9B-Chat	4.9 %	95.1 %	100.0 %	85.7
Llama-3.1-70B-Instruct	5.0 %	95.0 %	100.0 %	79.6
Llama-3.1-8B-Instruct	5.4 %	94.6 %	100.0 %	71.0
Llama-2-70B-Chat-hf	5.9 %	94.1 %	99.9 %	84.9
Google Gemini-1.5-flash	6.6 %	93.4 %	98.1 %	62.8
Microsoft phi-2	6.7 %	93.3 %	91.5 %	80.8
Google Gemma-2-2B-it	7.0 %	93.0 %	100.0 %	62.2
Llama-3-8B-Chat-hf	7.4 %	92.6 %	99.8 %	79.7
Google Gemini-Pro	7.7 %	92.3 %	98.4 %	89.5
CohereForAI c4ai-command-r-plus	7.8 %	92.2 %	100.0 %	71.2
01-AI Yi-1.5-6B-Chat	7.9 %	92.1 %	100.0 %	98.9
databricks dbrx-instruct	8.3 %	91.7 %	100.0 %	85.9
Anthropic Claude-3-5-sonnet	8.6 %	91.4 %	100.0 %	103.0
Mistral-7B-Instruct-v0.3	9.5 %	90.5 %	100.0 %	98.4
Anthropic Claude-3-opus	10.1 %	89.9 %	95.5 %	92.1
Google Gemma-2-9B-it	10.1 %	89.9 %	100.0 %	70.2
Llama-2-13B-Chat-hf	10.5 %	89.5 %	99.8 %	82.1
Llama-2-7B-Chat-hf	11.3 %	88.7 %	99.6 %	119.9
Microsoft WizardLM-2-8x22B	11.7 %	88.3 %	99.9 %	140.8
Amazon Titan-Express	13.5 %	86.5 %	99.5 %	98.4
Google PaLM-2	14.1 %	85.9 %	99.8 %	86.6
Google Gemma-7B-it	14.8 %	85.2 %	100.0 %	113.0
Cohere-Chat	15.4 %	84.6 %	98.0 %	74.4
Anthropic Claude-3-sonnet	16.3 %	83.7 %	100.0 %	108.5
Google Gemma-1.1-7B-it	17.0 %	83.0 %	100.0 %	64.3
Anthropic Claude-2	17.4 %	82.6 %	99.3 %	87.5
Google Flan-T5-large	18.3 %	81.7 %	99.3 %	20.9
Cohere	18.9 %	81.1 %	99.8 %	59.8
Mixtral-8x7B-Instruct-v0.1	20.1 %	79.9 %	99.9 %	90.7
Apple OpenELM-3B-Instruct	24.8 %	75.2 %	99.3 %	47.2
Google Gemma-1.1-2B-it	27.8 %	72.2 %	100.0 %	66.8
Google Gemini-1.5-Pro	28.1 %	71.9 %	89.3 %	82.1
TII falcon-7B-instruct	29.9 %	70.1 %	90.0 %	75.5
