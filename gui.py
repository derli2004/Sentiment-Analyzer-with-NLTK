import tkinter as tk
import pandas as pd
from sentiment_core import analyze_sentiment, get_sentiment_scores

# Read CSV file
def read_csv_and_analyze():
    try:
        df = pd.read_csv('sentiment_data.csv')
        results = []
        for text in df['text']:
            sentiment = analyze_sentiment(text)
            scores = get_sentiment_scores(text)
            result_text = f"Text: {text}\nSentiment: {sentiment}\n"
            result_text += f"Details:\n"
            result_text += f" - Positive: {scores['pos']:.2f}\n"
            result_text += f" - Neutral : {scores['neu']:.2f}\n"
            result_text += f" - Negative: {scores['neg']:.2f}\n"
            result_text += f" - Compound: {scores['compound']:.2f}\n\n"
            results.append(result_text)
        
        # Display results in the output_label
        output_label.config(text="\n".join(results))
    
    except Exception as e:
        output_label.config(text=f"Error reading CSV: {e}")

# Main GUI logic
def analyze():
    text = entry.get("1.0", tk.END).strip()
    if text:
        sentiment = analyze_sentiment(text)
        scores = get_sentiment_scores(text)
        result_text = f"Sentiment: {sentiment}\n\n"
        result_text += f"Details:\n"
        result_text += f" - Positive: {scores['pos']:.2f}\n"
        result_text += f" - Neutral : {scores['neu']:.2f}\n"
        result_text += f" - Negative: {scores['neg']:.2f}\n"
        result_text += f" - Compound: {scores['compound']:.2f}"
        output_label.config(text=result_text)

# Create main window
app = tk.Tk()
app.title("Sentiment Analyzer")
app.geometry("550x450")
app.configure(bg="#f4f4f4")
app.resizable(False, False)

# Center the window on screen
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = int((screen_width / 2) - (550 / 2))
y = int((screen_height / 2) - (450 / 2))
app.geometry(f"550x450+{x}+{y}")

# Welcome label
welcome = tk.Label(app, text="😊 Welcome to Sentiment Analyzer App 😊", font=("Helvetica", 16, "bold"), bg="#f4f4f4", fg="#333")
welcome.pack(pady=20)

# Instruction label
instruction = tk.Label(app, text="Enter a sentence to analyze its sentiment:", font=("Helvetica", 12), bg="#f4f4f4", fg="#555")
instruction.pack(pady=5)

# Input Text Box
entry = tk.Text(app, height=5, width=60, font=("Arial", 11))
entry.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(app, text="Analyze Sentiment", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=analyze)
analyze_button.pack(pady=10)

# Analyze CSV Button
analyze_csv_button = tk.Button(app, text="Analyze Sentiments from CSV", font=("Helvetica", 12, "bold"), bg="#FF9800", fg="white", padx=10, pady=5, command=read_csv_and_analyze)
analyze_csv_button.pack(pady=10)

# Output Label
output_label = tk.Label(app, text="", font=("Courier", 11), justify="left", bg="#f4f4f4", fg="#222")
output_label.pack(pady=15)

# Start GUI loop
app.mainloop()
