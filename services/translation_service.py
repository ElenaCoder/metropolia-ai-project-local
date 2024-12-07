from transformers import pipeline

# Load the model only once to save resources
translator = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")


def translate_to_finnish(text):
    """Translate English text to Finnish."""
    try:
        translated = translator(text)[0]["translation_text"]
        return translated
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Translation failed."
