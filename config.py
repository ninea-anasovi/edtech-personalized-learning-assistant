import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Firestore Project ID
FIREBASE_PROJECT_ID = os.environ.get("FIREBASE_PROJECT_ID")