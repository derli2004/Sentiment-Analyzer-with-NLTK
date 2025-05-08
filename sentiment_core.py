import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']
    
    if compound >= 0.5:
        return "Positive"
    elif compound <= -0.5:
        return "Negative"
    elif -0.5 < compound < 0:
        return "Not too good"
    else:
        return "Neutral"

def get_sentiment_scores(text):
    return sia.polarity_scores(text)
