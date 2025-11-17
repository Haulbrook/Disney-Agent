import React from 'react';
import './styles/theme.css';
import './App.css';

function App() {
  // Simple test render to debug blank screen
  return (
    <div className="App">
      <h1 style={{padding: '40px', textAlign: 'center', color: '#746bab'}}>
        🏰 Disney Trip Planner Loading...
      </h1>
      <p style={{textAlign: 'center', color: '#666'}}>
        If you see this, React is working! Debugging components...
      </p>
    </div>
  );
}

export default App;
