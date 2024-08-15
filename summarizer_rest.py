import json
import ollama
import requests
import PyPDF2

def document_summary_rest():
     document_string = extract_text_from_pdf(file)

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