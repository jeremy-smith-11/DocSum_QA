import streamlit as st
import ollama
import requests
import PyPDF2
import os
import time
#from summarizer import summarize_text
#from pdf_extractor import extract_text_from_pdf
#from text_cleaner import  clean_text
from QA_chatbot import ask_question
import base64

# set summary to blank
summary =""

# Set page title and icon
st.set_page_config(
    page_title="USCIS Summarizer & Q&A Chatbot",
    page_icon=":book:",  # Emoji icon or you can use an image path
    layout="wide",  # Optional: can be "centered" or "wide"
    initial_sidebar_state="expanded",
    menu_items={
        'About': " A text summarizer is an AI-based tool that creates summaries of any piece of writing, from lists of bullet points to news articles to research papers. This tool can help you speed up summarizing so you have more time to focus on big ideas and meaningful work!"
    }
)

# define extract text
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Pre process the document
def clean_text(text):
    # Remove newline characters
   # text = text.replace('\n', ' ')
    # Remove multiple spaces
 #   text = re.sub(r'\s+', ' ', text)
    # Remove special characters and digits (if not relevant)
#    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()

#summarization
def document_summary():
     document_string = extract_text_from_pdf(uploaded_file)
     summary = ollama.chat(model='llama3:latest', messages=[
          {
          'role': 'system',
          'content': 'Your goal is to summarize the text that is given to you in roughly 300 words. It is a text document. Only output the summary without any additional text. Only include information that is part of the document. Focus on providing a summary in freeform text with a summary of the key points of the document. Do not include your own opinion or analysis.'
          },
     {
          'role': 'user',
          'content': document_string,
     },
     ])
     return summary['message']['content']

#rest summarization
def document_summary_rest():
     document_string = extract_text_from_pdf(uploaded_file)

     prompt = """Your goal is to summarize the text that is given to you in roughly 300 words. It is a text document. Only output the summary without any additional text. Only include information that is part of the document. Focus on providing a summary in freeform text with a summary of the key points of the document. Do not include your own opinion or analysis."""

     OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

     OLLAMA_PROMPT = f"{prompt}: {document_string}"
     OLLAMA_DATA = {
          "model": 'llama3:latest',
          "prompt": OLLAMA_PROMPT,
          "stream": False,
          "keep_alive": "1m",
     }

     summary = requests.post(OLLAMA_ENDPOINT, json=OLLAMA_DATA)
     return summary.json()["response"]




# Function to load and encode the logo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to the logo
logo_path = "8943377.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# Custom CSS
st.markdown(f"""
    <style>
        .main {{
            background-color: #003865; /* USCIS Blue */
        }}
        .stTextInput > div > div > input {{
            border: 2px solid #A6192E; /* USCIS Red */
        }}
        .stButton>button {{
            background-color: #131720; /* Dark Grey */ 
            color: white;
            border-radius: 5px;
            border: 2px solid #FFFFFF; /* White */
        }}
        .stButton>button:hover {{
            background-color: #131720; /* Dark Grey */ 
            border: 2px solid #A6192E; /* USCIS Red */
        }}
        .header {{
            display: flex;
            align-items: center;
            text-align: center;
            justify-content: space-between;
            background-color: #006BA6; /* USCIS Light Blue Background for header */
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}
        .logo {{
            width: 100px;
        }}
    </style>
""", unsafe_allow_html=True)


# App title with logo
st.markdown(f"""
    <div class="header">
        <h2>USCIS Document Summarization and Q&A Chatbot</h2>
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
    <hr>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
#    clean_text = None
#    start = time.time()
#    if clean_text is None:
#        with st.status("Running...", expanded=True) as status:
#            try:
#                clean_text = clean_text(raw_text)
#            except Exception as e:
#                status.update(label="Error", state="error", expanded=False)
#                st.error(f"An error occurred: {e}")
#                result = ""
#         
#       if clean_text:
#            st.info(f"Time taken: {time.time() - start:.2f} seconds", icon="⏱️")
        
    
    raw_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(raw_text)
    
    # Display extracted text
    st.subheader("Extracted Text")
    st.text_area("Extracted Text", cleaned_text, height=150)

    
    # Summarization section
    st.subheader("Document Summary")
    #button magic
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False  
        st.text_area("Summary", summary, height=150)
    def click_button():
        st.session_state.clicked = True
    st.button("Summarize", on_click=click_button)
    if st.session_state.clicked:
        # The message and nested widget will remain on the page
        st.text_area("Summary", document_summary_rest(), height=150)
        

    
    # Q&A section
    st.subheader("Ask Questions About the PDF")
    question = st.text_input("Enter your question:")
    if question:
        answer = ask_question(question, cleaned_text)
        st.subheader("Answer")
        st.info(answer)
