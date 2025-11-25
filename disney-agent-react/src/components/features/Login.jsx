import React, { useState } from 'react';
import { useTripContext } from '../../context/TripContext';
import './Login.css';

// Parse itinerary text into structured data
function parseItinerary(text, startDate, endDate) {
  const lines = text.split('\n');
  const itinerary = [];

  // Get all days between start and end
  const start = new Date(startDate);
  const end = new Date(endDate);
  const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  // Create day entries
  let currentDate = new Date(start);
  let dayIndex = 0;

  while (currentDate <= end) {
    const dayName = dayNames[currentDate.getDay()];
    const monthName = monthNames[currentDate.getMonth()];
    const dateNum = currentDate.getDate();

    itinerary.push({
      date: `${dayName}, ${monthName.slice(0,3)} ${dateNum}`,
      fullDate: currentDate.toISOString().split('T')[0],
      title: 'Free Day',
      icon: '📅',
      park: null,
      hours: null,
      highlights: []
    });

    currentDate.setDate(currentDate.getDate() + 1);
    dayIndex++;
  }

  // Parse the text to find day info and events
  let currentDayIndex = -1;
  const parkKeywords = {
    'animal kingdom': { title: 'Animal Kingdom', icon: '🦁', park: 'animal-kingdom' },
    'magic kingdom': { title: 'Magic Kingdom', icon: '🏰', park: 'magic-kingdom' },
    'hollywood studios': { title: 'Hollywood Studios', icon: '🎬', park: 'hollywood-studios' },
    'epcot': { title: 'EPCOT', icon: '🌍', park: 'epcot' },
    'disney springs': { title: 'Disney Springs', icon: '🛍️', park: null },
    'arrival': { title: 'Arrival Day', icon: '✈️', park: null },
    'departure': { title: 'Departure', icon: '👋', park: null },
    'rest day': { title: 'Rest Day', icon: '😴', park: null },
    'christmas party': { title: 'Christmas Party', icon: '🎄', park: 'magic-kingdom' },
    'very merry': { title: 'Christmas Party', icon: '🎄', park: 'magic-kingdom' },
  };

  for (const line of lines) {
    const lowerLine = line.toLowerCase().trim();

    // Check for day headers (e.g., "Saturday | December 6", "DECEMBER 6", "Sunday | December 7")
    const dateMatch = line.match(/(?:sunday|monday|tuesday|wednesday|thursday|friday|saturday)?\s*\|?\s*(?:december|january|february|march|april|may|june|july|august|september|october|november)\s+(\d{1,2})/i);
    if (dateMatch) {
      const dayNum = parseInt(dateMatch[1]);
      // Find matching day in itinerary
      currentDayIndex = itinerary.findIndex(day => {
        const d = new Date(day.fullDate);
        return d.getDate() === dayNum;
      });
      continue;
    }

    // If we have a current day, look for park/activity info
    if (currentDayIndex >= 0 && currentDayIndex < itinerary.length) {
      // Check for park keywords
      for (const [keyword, info] of Object.entries(parkKeywords)) {
        if (lowerLine.includes(keyword)) {
          itinerary[currentDayIndex].title = info.title;
          itinerary[currentDayIndex].icon = info.icon;
          itinerary[currentDayIndex].park = info.park;
          break;
        }
      }

      // Check for park hours (e.g., "9:00-10:00", "8:00 AM - 6:00 PM")
      const hoursMatch = line.match(/(\d{1,2}:\d{2})\s*(?:AM|PM)?\s*[-–]\s*(\d{1,2}:\d{2})\s*(?:AM|PM)?/i);
      if (hoursMatch && !line.match(/\d{1,2}:\d{2}\s+(?:AM|PM)?\s+\w/)) {
        itinerary[currentDayIndex].hours = `${hoursMatch[1]} - ${hoursMatch[2]}`;
      }

      // Check for time-based events (e.g., "11:15 Tusker House", "3:00 PM Check-in")
      const eventMatch = line.match(/(\d{1,2}:\d{2})\s*(?:AM|PM)?\s+(.+)/i);
      if (eventMatch) {
        const time = eventMatch[1];
        let event = eventMatch[2].trim();

        // Clean up event text
        event = event.replace(/[*]/g, '').trim();

        // Skip if it's just a park hours range
        if (event.match(/^\d{1,2}:\d{2}/)) continue;

        // Determine event type
        let type = 'event';
        const eventLower = event.toLowerCase();

        if (eventLower.includes('check-in') || eventLower.includes('checkout') || eventLower.includes('check-out')) {
          type = 'resort';
        } else if (eventLower.includes('breakfast') || eventLower.includes('lunch') || eventLower.includes('dinner') ||
                   eventLower.includes('cafe') || eventLower.includes('restaurant') || eventLower.includes('house') ||
                   eventLower.includes('cantina') || eventLower.includes('steakhouse') || eventLower.includes('banquet') ||
                   eventLower.includes('prime time') || eventLower.includes('park fare') || eventLower.includes("tony's") ||
                   eventLower.includes("oga's") || eventLower.includes('rix') || eventLower.includes('akershus')) {
          type = 'dining';
        } else if (eventLower.includes('fireworks') || eventLower.includes('parade') || eventLower.includes('fantasmic') ||
                   eventLower.includes('luminous') || eventLower.includes('happily ever')) {
          type = 'show';
        } else if (eventLower.includes('party') || eventLower.includes('surprise')) {
          type = 'special';
        }

        // Format time
        let formattedTime = time;
        const hour = parseInt(time.split(':')[0]);
        if (line.toLowerCase().includes('pm') || (hour >= 1 && hour < 7)) {
          formattedTime = `${time} PM`;
        } else if (line.toLowerCase().includes('am') || hour >= 7) {
          formattedTime = `${time} AM`;
        }

        itinerary[currentDayIndex].highlights.push({
          time: formattedTime,
          event: event,
          type: type
        });
      }
    }
  }

  // Add default highlights for days without any
  itinerary.forEach((day, index) => {
    if (day.highlights.length === 0) {
      if (day.title === 'Arrival Day') {
        day.highlights.push({ time: 'Afternoon', event: 'Resort Check-in', type: 'resort' });
      } else if (day.title === 'Departure') {
        day.highlights.push({ time: 'Morning', event: 'Check-out', type: 'resort' });
      } else if (day.park) {
        day.highlights.push({ time: 'All Day', event: `Enjoy ${day.title}!`, type: 'activity' });
      }
    }
  });

  return itinerary;
}

const Login = () => {
  const { loginWithCode, createTripWithCode, updateItinerary } = useTripContext();
  const [mode, setMode] = useState('select'); // 'select', 'login', 'create', 'itinerary', 'success'
  const [tripCode, setTripCode] = useState('');
  const [error, setError] = useState('');
  const [newTripCode, setNewTripCode] = useState('');
  const [itineraryText, setItineraryText] = useState('');

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
    setMode('itinerary');
  };

  const handleItinerarySubmit = () => {
    if (itineraryText.trim()) {
      const parsed = parseItinerary(itineraryText, startDate, endDate);
      updateItinerary(parsed);
    }
    setMode('success');
  };

  const handleSkipItinerary = () => {
    // Create basic itinerary with just dates
    const parsed = parseItinerary('', startDate, endDate);
    updateItinerary(parsed);
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
              Continue
            </button>
          </form>
        )}

        {mode === 'itinerary' && (
          <div className="itinerary-setup">
            <button
              type="button"
              className="back-btn"
              onClick={() => setMode('create')}
            >
              ← Back
            </button>

            <div className="setup-header">
              <span className="setup-icon">📋</span>
              <h3>Add Your Itinerary</h3>
              <p>Paste your trip itinerary below and we'll organize it for you!</p>
            </div>

            <div className="form-group">
              <label>Paste Itinerary (from your travel agent, PDF, etc.)</label>
              <textarea
                value={itineraryText}
                onChange={(e) => setItineraryText(e.target.value)}
                placeholder="Paste your daily itinerary here...

Example:
Saturday | December 6
Arrival Day
3:00 PM Resort Check-in

Sunday | December 7
Animal Kingdom
11:15 Tusker House"
                rows={10}
                className="itinerary-textarea"
              />
            </div>

            <div className="setup-actions">
              <button
                type="button"
                className="submit-btn"
                onClick={handleItinerarySubmit}
              >
                Parse & Continue
              </button>
              <button
                type="button"
                className="skip-btn"
                onClick={handleSkipItinerary}
              >
                Skip for Now
              </button>
            </div>

            <p className="setup-note">
              Don't worry - you can always update your itinerary later!
            </p>
          </div>
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
