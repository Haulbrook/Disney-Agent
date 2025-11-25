import React, { useState } from 'react';
import { useTripContext } from '../../context/TripContext';
import './Login.css';

const Login = () => {
  const { loginWithCode, createTripWithCode } = useTripContext();
  const [mode, setMode] = useState('select'); // 'select', 'login', 'create'
  const [tripCode, setTripCode] = useState('');
  const [error, setError] = useState('');
  const [newTripCode, setNewTripCode] = useState('');

  // Create trip form state
  const [destination, setDestination] = useState('Walt Disney World');
  const [partySize, setPartySize] = useState(4);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    setError('');

    if (!tripCode.trim()) {
      setError('Please enter a trip code');
      return;
    }

    const result = loginWithCode(tripCode);
    if (!result.success) {
      setError(result.error);
    }
  };

  const handleCreateTrip = (e) => {
    e.preventDefault();
    setError('');

    if (!startDate || !endDate) {
      setError('Please select trip dates');
      return;
    }

    if (new Date(endDate) <= new Date(startDate)) {
      setError('End date must be after start date');
      return;
    }

    const code = createTripWithCode(destination, partySize, startDate, endDate);
    setNewTripCode(code);
    setMode('success');
  };

  return (
    <div className="login-page">
      <div className="login-castle-bg"></div>
      <div className="login-container">
        <div className="login-header">
          <div className="castle-icon">🏰</div>
          <h1>Disney Trip Planner</h1>
          <p>Your magical vacation starts here</p>
        </div>

        {mode === 'select' && (
          <div className="login-options">
            <button
              className="login-option-btn existing"
              onClick={() => setMode('login')}
            >
              <span className="option-icon">🔑</span>
              <span className="option-text">
                <strong>Enter Trip Code</strong>
                <small>Access an existing trip</small>
              </span>
            </button>

            <div className="login-divider">
              <span>or</span>
            </div>

            <button
              className="login-option-btn create"
              onClick={() => setMode('create')}
            >
              <span className="option-icon">✨</span>
              <span className="option-text">
                <strong>Create New Trip</strong>
                <small>Start planning your adventure</small>
              </span>
            </button>
          </div>
        )}

        {mode === 'login' && (
          <form className="login-form" onSubmit={handleLogin}>
            <button
              type="button"
              className="back-btn"
              onClick={() => { setMode('select'); setError(''); setTripCode(''); }}
            >
              ← Back
            </button>

            <div className="form-group">
              <label>Enter Your Trip Code</label>
              <input
                type="text"
                value={tripCode}
                onChange={(e) => setTripCode(e.target.value.toUpperCase())}
                placeholder="e.g., ABC123"
                maxLength={6}
                className="trip-code-input"
              />
            </div>

            {error && <div className="error-message">{error}</div>}

            <button type="submit" className="submit-btn">
              Enter Trip
            </button>
          </form>
        )}

        {mode === 'create' && (
          <form className="create-form" onSubmit={handleCreateTrip}>
            <button
              type="button"
              className="back-btn"
              onClick={() => { setMode('select'); setError(''); }}
            >
              ← Back
            </button>

            <div className="form-group">
              <label>Destination</label>
              <select
                value={destination}
                onChange={(e) => setDestination(e.target.value)}
              >
                <option value="Walt Disney World">Walt Disney World</option>
                <option value="Disneyland">Disneyland</option>
                <option value="Disney Cruise">Disney Cruise</option>
              </select>
            </div>

            <div className="form-group">
              <label>Party Size</label>
              <input
                type="number"
                min="1"
                max="20"
                value={partySize}
                onChange={(e) => setPartySize(parseInt(e.target.value) || 1)}
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Start Date</label>
                <input
                  type="date"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                />
              </div>

              <div className="form-group">
                <label>End Date</label>
                <input
                  type="date"
                  value={endDate}
                  onChange={(e) => setEndDate(e.target.value)}
                />
              </div>
            </div>

            {error && <div className="error-message">{error}</div>}

            <button type="submit" className="submit-btn create">
              Create My Trip
            </button>
          </form>
        )}

        {mode === 'success' && (
          <div className="success-screen">
            <div className="success-icon">🎉</div>
            <h2>Trip Created!</h2>
            <p>Your magical trip code is:</p>
            <div className="trip-code-display">{newTripCode}</div>
            <p className="code-note">
              Save this code! You'll need it to access your trip from any device.
            </p>
            <button
              className="submit-btn"
              onClick={() => window.location.reload()}
            >
              Start Planning
            </button>
          </div>
        )}

        <div className="login-footer">
          <div className="mickey-decoration">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
