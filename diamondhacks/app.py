# app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("phishing_detector.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")
    prediction = model.predict([message])[0]
    prob = model.predict_proba([message])[0][prediction]
    return jsonify({
        "prediction": int(prediction),
        "confidence": round(float(prob), 3)
    })

if __name__ == "__main__":
    app.run(debug=True)
