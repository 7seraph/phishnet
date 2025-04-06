# app.py
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import joblib
from flask_cors import CORS
from letta_client import Letta
import traceback

app = Flask(__name__)
CORS(app)
model = joblib.load("phishing_detector.pkl")

load_dotenv()

# Initialize Letta client
#client = Letta(base_url="http://localhost:3000")
import os

# Retrieve Letta token from environment variable
letta_token = os.getenv("LETTA_TOKEN")
if not letta_token:
    raise ValueError("LETTA_TOKEN environment variable is not set")

client = Letta(token=letta_token)

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

@app.route("/api/classify", methods=["POST"])
def classify_email():
    data = request.get_json()
    email = data.get("email", "")
    prediction = model.predict([email])[0]
    prob = model.predict_proba([email])[0][prediction]
    result = {
        "prediction": "fake" if prediction == 1 else "real",
        "confidence": round(float(prob), 3)
    }
    return jsonify(result)

@app.route("/api/insights", methods=["POST"])
def get_insights():
    try:
        data = request.get_json(force=True)
        print("Received JSON data:", data)

        email = data.get("email")
        prediction = data.get("prediction")

        if not email or not prediction:
            return jsonify({"error": "Both 'email' and 'prediction' fields are required"}), 400

        agent_id = "agent-8f6710e5-b428-4616-b2c6-4043b31a1557"

        letta_response = client.agents.messages.create(
            agent_id=agent_id,
            messages=[
                {
                    "role": "user",
                    "content": f"The email below was classified as '{prediction}'. Explain why it might be considered '{prediction}':\n\n{email}",
                }
            ],
        )

        print("Letta response:", letta_response)

        # Fixed line
        insights = letta_response.messages[-1].content.strip()

        return jsonify({"insights": insights})
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)
