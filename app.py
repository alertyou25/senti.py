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
        # Convert to percentage
        sentiment_percentage = polarity * 100
        # Display the text and its sentiment percentage on the homepage
        return f"Text: '{text}' <br> RiskOmeter: {sentiment_percentage}%"
    
    # If no text is provided, display the instructions
    return "API is working. Add '?text=your-text' to the URL for sentiment analysis."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
