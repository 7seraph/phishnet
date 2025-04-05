# app.py
from flask import Flask, request, jsonify, render_template
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = joblib.load("phishing_detector.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email", "")
        prediction = model.predict([email])[0]
        prob = model.predict_proba([email])[0][prediction]
        result = {
            "prediction": "fake" if prediction == 1 else "real",
            "confidence": round(float(prob), 3)
        }
        return render_template("index.html", result=result, email=email)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
