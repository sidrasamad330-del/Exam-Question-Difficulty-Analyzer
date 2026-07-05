import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("questions.csv")

# Prepare data
X = data["question"]
y = data["difficulty"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train the model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Prediction function
def predict_difficulty(question):
    question_vector = vectorizer.transform([question])
    prediction = model.predict(question_vector)
    return prediction[0]