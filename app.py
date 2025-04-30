from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    return " API is working"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return jsonify({"sentiment": polarity})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
