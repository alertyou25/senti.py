from flask import Flask, request, jsonify

app = Flask(__name__)

# List of high-risk keywords commonly found in phishing/scam messages
RISK_KEYWORDS = [
    "urgent", "immediate", "required", "suspicious", "lock", "confirm",
    "security code", "failure", "suspension", "legal", "warning"
]

@app.route("/")
def home():
    text = request.args.get("text", "").lower()
    
    if text:
        risk_score = 0
        for word in RISK_KEYWORDS:
            if word in text:
                risk_score += 1

        # Normalize risk to a percentage (adjust max risk as needed)
        max_risk = len(RISK_KEYWORDS)
        risk_percentage = (risk_score / max_risk) * 100
        risk_percentage = round(risk_percentage, 2)

        return f"Text: '{text}' <br> RiskOmeter: {risk_percentage}%"
    
    return "API is working. Add '?text=your-text' to the URL for sentiment analysis."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
