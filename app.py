from flask import Flask, render_template, request
from sentiment_core import analyze_sentiment, get_sentiment_scores

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    scores = None
    text = ""
    
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            sentiment = analyze_sentiment(text)
            scores = get_sentiment_scores(text)
    
    return render_template(
        "index.html",
        sentiment=sentiment,
        scores=scores,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
