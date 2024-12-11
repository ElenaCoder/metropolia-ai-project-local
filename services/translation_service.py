# Solution 1
"""
This was my initial solution, and it works perfectly in a local environment.
However, I decided not to use it for deployment because it loads the Hugging Face translation model
(Helsinki-NLP/opus-mt-en-fi) locally, which requires a significant amount of memory.

When I deployed this on Render's free tier, memory limitations caused the application to fail.
Since the free tier instance doesn’t provide enough memory to load the model, this solution is impractical
for production in such environments. Instead, I opted for a different approach that uses Hugging Face’s
Inference API, which offloads the memory-intensive operations to their servers.
"""

# from transformers import pipeline

# translator = None  # Lazy-loaded global variable

# def translate_to_finnish(text):
#     global translator
#     if translator is None:
#         print("Loading translation model...")
#         translator = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")
#     result = translator(text, max_length=500)
#     return result[0]['translation_text']


# Solution 2
"""
This solution uses Hugging Face’s Inference API instead of loading the model locally.

The key benefit of this approach is that it significantly reduces memory usage, as the translation model
(Helsinki-NLP/opus-mt-en-fi) runs on Hugging Face’s servers rather than the local environment.

This makes it ideal for deployment on platforms with limited resources, like the free tier on Render.
"""

import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

def translate_to_finnish(text):
    """Translate English text to Finnish using Hugging Face API."""
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
