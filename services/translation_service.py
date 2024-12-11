import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

def translate_to_finnish(text):
    url = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fi"
    token = os.getenv("HUGGING_FACE_API_TOKEN")
    if not token:
        raise ValueError("HUGGING_FACE_API_TOKEN is not set in environment variables")

    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": text}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["translation_text"]
    else:
        raise RuntimeError(f"Translation API failed: {response.text}")
