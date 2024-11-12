// This is your frontend (App.js)
import React, { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState("Loading...");

  // This runs when the page loads
  useEffect(() => {
    // Get data from Flask
    fetch('http://localhost:5000/api/hello')
      .then(response => response.json())
      .then(data => {
        setMessage(data.message);
      });
  }, []);

  return (
    <div className="p-4">
      <h1>My Flask + React App</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;