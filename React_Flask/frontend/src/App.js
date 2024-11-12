import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState('');
  const [message, setMessage] = useState('');
  const [isValidating, setIsValidating] = useState(false);

  // Frontend validation (immediate feedback)
  const checkNumberLocally = (value) => {
    if (value === '') {
      setMessage('');
      return;
    }
    
    if (!isNaN(value) && value.trim() !== '') {
      setMessage('Looks like a number! Click Check to verify.');
    } else {
      setMessage('This doesn\'t look like a number.');
    }
  };

  // Backend validation (when Check button is clicked)
  const checkNumberServer = async () => {
    setIsValidating(true);
    try {
      const response = await fetch('http://localhost:5000/api/validate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number: input })
      });
      
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      setMessage('Error connecting to server');
    }
    setIsValidating(false);
  };

  return (
    <div className="p-6 max-w-sm mx-auto">
      <div className="space-y-4">
        <h1 className="text-xl font-bold">Number Validator</h1>
        
        {/* Input field */}
        <div>
          <input
            type="text"
            value={input}
            onChange={(e) => {
              setInput(e.target.value);
              checkNumberLocally(e.target.value);
            }}
            className="border p-2 rounded w-full"
            placeholder="Enter a number"
          />
        </div>

        {/* Check button */}
        <button
          onClick={checkNumberServer}
          disabled={isValidating || input.trim() === ''}
          className="bg-blue-500 text-white px-4 py-2 rounded 
                     disabled:bg-gray-300 disabled:cursor-not-allowed"
        >
          {isValidating ? 'Checking...' : 'Check'}
        </button>

        {/* Message display */}
        {message && (
          <div className={`p-2 rounded ${
            message.includes('valid') ? 'bg-green-100' : 'bg-red-100'
          }`}>
            {message}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;