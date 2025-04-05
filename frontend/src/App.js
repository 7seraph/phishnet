import React from "react";
import "./App.css";
import EmailClassifier from "./components/EmailClassifier";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Email Classifier</h1>
      </header>
      <main>
        <EmailClassifier />
      </main>
    </div>
  );
}

export default App;