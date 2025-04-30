from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    # Get text from URL query parameter
    text = request.args.get("text", "")
    
    if text:
        # Analyze sentiment
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        return f"Sentiment for the text '{text}' is: {polarity}"
    return "API is working. Add '?text=your-text' to the URL for sentiment analysis."

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
