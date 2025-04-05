import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Load dataset
path = "C:/Users/Kevin Tran/.cache/kagglehub/datasets/naserabdullahalam/phishing-email-dataset/versions/1"
df = pd.read_csv(path + "/Enron.csv")

# Preprocess dataset
df.columns = ['subject', 'body', 'label']

df['subject'] = df['subject'].fillna("")
df['body'] = df['body'].fillna("")

df['text'] = df['subject'] + " " + df['body']
df['label'] = df['label'].map({0: 0, 1: 1})  # 0 = real, 1 = fake

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Create pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "phishing_detector.pkl")