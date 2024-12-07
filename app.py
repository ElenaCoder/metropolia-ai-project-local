from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Routes
@app.route("/1")
def home1():
    return jsonify({"message": "Hello, Flask!"})


if __name__ == "__main__":
    app.run(debug=True)
