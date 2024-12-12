# Solution 1
"""
This was my initial Solution 1, and it works perfectly in a local environment.
However, I decided not to use it for deployment because it loads the Hugging Face translation model
(Helsinki-NLP/opus-mt-en-fi) locally, which requires a significant amount of memory.

When I deployed this on Render's free tier, memory limitations caused the application to fail.
Since the free tier instance doesn’t provide enough memory to load the model, this solution is impractical
for production in such environments. Instead, I chosen for a different approach (Solution 2) that uses Hugging Face’s
Inference API, which offloads the memory-intensive operations to their servers.
"""

from transformers import pipeline

translator = None  # Lazy-loaded global variable

def translate_to_finnish(text):
    global translator
    if translator is None:
        print("Loading translation model...")
        translator = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")
    result = translator(text, max_length=500)
    return result[0]['translation_text']


