import React, { useState } from 'react';
import { useTripContext } from '../../context/TripContext';
import './Itinerary.css';

const Itinerary = () => {
  const { tripData } = useTripContext();
  const [selectedDay, setSelectedDay] = useState(0);

  // Use itinerary from tripData, or fall back to default
  const itinerary = tripData.itinerary && tripData.itinerary.length > 0
    ? tripData.itinerary
    : generateDefaultItinerary(tripData.startDate, tripData.endDate);

  const getTypeIcon = (type) => {
    switch (type) {
      case 'dining': return '🍽️';
      case 'ride': return '🎢';
      case 'show': return '✨';
      case 'special': return '⭐';
      case 'resort': return '🏨';
      case 'explore': return '🗺️';
      case 'activity': return '⛳';
      case 'event': return '📍';
      default: return '📍';
    }
  };

  // Format date range for display
  const getDateRange = () => {
    if (!tripData.startDate || !tripData.endDate) return 'Your Trip';
    const start = new Date(tripData.startDate);
    const end = new Date(tripData.endDate);
    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    return `${monthNames[start.getMonth()]} ${start.getDate()}-${end.getDate()} at ${tripData.destination}`;
  };

  if (!itinerary || itinerary.length === 0) {
    return (
      <section id="itinerary" className="itinerary-section">
        <div className="container">
          <div className="section-header">
            <h2>📅 Your Magical Itinerary</h2>
            <p>No itinerary added yet</p>
          </div>
          <div className="itinerary-empty">
            <p>Add your itinerary when creating a new trip to see your daily schedule here!</p>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="itinerary" className="itinerary-section">
      <div className="container">
        <div className="section-header">
          <h2>📅 Your Magical Itinerary</h2>
          <p>{getDateRange()}</p>
        </div>

        <div className="itinerary-tabs">
          {itinerary.map((day, index) => (
            <button
              key={index}
              className={`itinerary-tab ${selectedDay === index ? 'active' : ''} ${day.park || ''}`}
              onClick={() => setSelectedDay(index)}
            >
              <span className="tab-icon">{day.icon}</span>
              <span className="tab-date">{day.date.split(', ')[0]}</span>
            </button>
          ))}
        </div>

        <div className="itinerary-content">
          <div className="day-header">
            <div className="day-icon">{itinerary[selectedDay].icon}</div>
            <div className="day-info">
              <h3>{itinerary[selectedDay].date}</h3>
              <h4>{itinerary[selectedDay].title}</h4>
              {itinerary[selectedDay].hours && (
                <span className="park-hours">Park Hours: {itinerary[selectedDay].hours}</span>
              )}
            </div>
          </div>

          <div className="day-highlights">
            {itinerary[selectedDay].highlights && itinerary[selectedDay].highlights.length > 0 ? (
              itinerary[selectedDay].highlights.map((item, index) => (
                <div key={index} className={`highlight-item ${item.type}`}>
                  <span className="highlight-time">{item.time}</span>
                  <span className="highlight-icon">{getTypeIcon(item.type)}</span>
                  <span className="highlight-event">{item.event}</span>
                </div>
              ))
            ) : (
              <div className="highlight-item">
                <span className="highlight-time">All Day</span>
                <span className="highlight-icon">📅</span>
                <span className="highlight-event">Free day - plan your own adventure!</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
};

// Generate default itinerary based on trip dates
function generateDefaultItinerary(startDate, endDate) {
  if (!startDate || !endDate) return [];

  const itinerary = [];
  const start = new Date(startDate);
  const end = new Date(endDate);
  const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  let currentDate = new Date(start);
  let dayIndex = 0;

  while (currentDate <= end) {
    const dayName = dayNames[currentDate.getDay()];
    const monthName = monthNames[currentDate.getMonth()];
    const dateNum = currentDate.getDate();

    let title = 'Free Day';
    let icon = '📅';
    let highlights = [];

    // First day is arrival
    if (dayIndex === 0) {
      title = 'Arrival Day';
      icon = '✈️';
      highlights = [{ time: 'Afternoon', event: 'Resort Check-in', type: 'resort' }];
    }

    // Last day is departure
    const totalDays = Math.ceil((end - start) / (1000 * 60 * 60 * 24));
    if (dayIndex === totalDays) {
      title = 'Departure';
      icon = '👋';
      highlights = [{ time: 'Morning', event: 'Check-out', type: 'resort' }];
    }

    itinerary.push({
      date: `${dayName}, ${monthName.slice(0,3)} ${dateNum}`,
      fullDate: currentDate.toISOString().split('T')[0],
      title,
      icon,
      park: null,
      hours: null,
      highlights
    });

    currentDate.setDate(currentDate.getDate() + 1);
    dayIndex++;
  }

  return itinerary;
}

export default Itinerary;
