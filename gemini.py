import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)
# Used to securely store your API key
load_dotenv()
api_key=os.getenv('GEMINI_AI_API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
while(True):
    question = input("Input: ")
    if question == "":
        break
    response = model.generate_content(question)
    print("Response: " + response.text)