from flask import Flask, request, jsonify, render_template
from controllers.translation_controller import translate_text

app = Flask(__name__)


# @app.route("/1")
# def home1():
#     return jsonify({"message": "Hello, Flask!"})

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    return translate_text(request)


if __name__ == "__main__":
    app.run(debug=True)
