from transformers import pipeline

translator = None  # Lazy-loaded global variable

def translate_to_finnish(text):
    global translator
    if translator is None:
        print("Loading translation model...")
        translator = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")
    result = translator(text, max_length=500)
    return result[0]['translation_text']