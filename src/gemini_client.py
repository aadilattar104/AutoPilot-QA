import google.generativeai as genai
from src.config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

def call_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return response text"""
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text
