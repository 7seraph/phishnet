import React, { useState } from "react";
import axios from "axios";

function EmailClassifier() {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState(null);
  const [insights, setInsights] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Classify the email
      const response = await axios.post("http://127.0.0.1:5000/api/classify", { email });
      setResult(response.data);

      // Fetch insights from the backend
      const insightsResponse = await axios.post("http://127.0.0.1:5000/api/insights", {
        email,
        prediction: response.data.prediction,
      });
      setInsights(insightsResponse.data.insights);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="10"
          cols="50"
          placeholder="Paste your email body here..."
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        ></textarea>
        <br />
        <button type="submit">Classify</button>
      </form>
      {result && (
        <div className="result-box">
          <h2>Prediction: {result.prediction}</h2>
          <p>Confidence: {result.confidence}</p>
          {insights && (
            <div>
              <h3>Insights:</h3>
              <p>{insights}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default EmailClassifier;