from flask import request, jsonify
from services.translation_service import translate_to_finnish


def translate_text(request):
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "Input text cannot be empty."}), 400

        translated_text = translate_to_finnish(text)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
