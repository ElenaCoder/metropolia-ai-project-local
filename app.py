from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from controllers.translation_controller import translate_text
from middlewares.error_handler import handle_errors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register middleware
app.register_error_handler(Exception, handle_errors)


# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    return translate_text(request)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
