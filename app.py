from flask import Flask, render_template, request, session, redirect
from textblob import TextBlob

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session tracking

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        review = request.form['review']
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        confidence = round(abs(polarity) * 100, 2)

        # Update history
        session['history'].append({'review': review, 'sentiment': sentiment, 'confidence': confidence})
        session.modified = True

        return render_template('index.html', sentiment=sentiment, confidence=confidence, history=session['history'])

    return render_template('index.html', history=session['history'])

if __name__ == "__main__":
    app.run(debug=True)