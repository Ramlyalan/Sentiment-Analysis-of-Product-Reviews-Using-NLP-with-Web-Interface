# Sentiment-Analysis-of-Product-Reviews-Using-NLP-with-Web-Interface
This project is a web-based Sentiment Analysis application that analyzes the sentiment of product reviews using Natural Language Processing (NLP) techniques. Users can input a review manually or via voice input, and the system will predict whether the review sentiment is Positive, Negative, or Neutral along with a confidence score.

Key Features
🔍 Analyze Product Reviews: Enter any review to get its sentiment analysis in real time.

✨ Beautiful User Interface: Clean and modern design for an easy user experience.

📝 Review History: Keeps track of all your analyzed reviews along with their sentiment and confidence scores.

🎤 Voice Input Support: Allows users to input reviews using voice recognition for quick analysis.

⚡ Real-time Prediction: Uses TextBlob for efficient polarity-based sentiment analysis.

Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

NLP Library: TextBlob

How It Works
The user enters or dictates a product review.

The app preprocesses the input and calculates the sentiment polarity.

The output displays the Sentiment (Positive/Negative/Neutral) and Confidence Level.

Each analysis is saved in the history log visible on the interface.

Future Enhancements
Integration with custom-trained ML models for advanced sentiment analysis.

Permanent storage of history using SQLite database.

Exporting analysis history to CSV for business use cases.

Chart visualizations for positive/negative/neutral sentiment distribution.
