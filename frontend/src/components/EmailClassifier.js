import React, { useState } from "react";
import axios from "axios";

function EmailClassifier() {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5000/", { email });
      setResult(response.data);
    } catch (error) {
      console.error("Error classifying email:", error);
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
        <div>
          <h2>Prediction: {result.prediction}</h2>
          <p>Confidence: {result.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default EmailClassifier;