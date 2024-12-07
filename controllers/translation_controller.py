from flask import request, jsonify
from services.translation_service import translate_to_finnish


def translate_text(request):
    text = request.form.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    translation = translate_to_finnish(text)
    return jsonify({"translated_text": translation})
