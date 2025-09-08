import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get the key from environment
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")   # 👈 must match the variable name in your .env
MODEL_NAME = "gemini-1.5-flash"

UPLOAD_FOLDER = "data/uploads"
ALLOWED_EXTENSIONS = {"pdf"}
