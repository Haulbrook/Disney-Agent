import React, { useState } from 'react';
import './Itinerary.css';

const Itinerary = () => {
  const [selectedDay, setSelectedDay] = useState(0);

  const itinerary = [
    {
      date: 'Saturday, Dec 6',
      title: 'Arrival Day',
      icon: '✈️',
      park: null,
      highlights: [
        { time: '3:00 PM', event: 'Resort Check-in', type: 'resort' },
        { time: 'Evening', event: 'Disney Springs', type: 'explore' },
      ]
    },
    {
      date: 'Sunday, Dec 7',
      title: 'Animal Kingdom',
      icon: '🦁',
      park: 'animal-kingdom',
      hours: '8:00 AM - 6:00 PM',
      highlights: [
        { time: 'Rope Drop', event: 'Flight of Passage', type: 'ride' },
        { time: '11:15 AM', event: 'Tusker House', type: 'dining' },
        { time: 'Afternoon', event: 'Kilimanjaro Safaris', type: 'ride' },
      ]
    },
    {
      date: 'Monday, Dec 8',
      title: 'Magic Kingdom',
      icon: '🏰',
      park: 'magic-kingdom',
      hours: '9:00 AM - 10:00 PM',
      highlights: [
        { time: '11:00 AM', event: 'Hall of Presidents - SURPRISE!', type: 'special' },
        { time: '12:20 PM', event: "Tony's Town Square", type: 'dining' },
        { time: 'Evening', event: 'Happily Ever After Fireworks', type: 'show' },
      ]
    },
    {
      date: 'Tuesday, Dec 9',
      title: 'Rest Day + Party',
      icon: '🎄',
      park: null,
      highlights: [
        { time: '9:25 AM', event: '1900 Park Fare', type: 'dining' },
        { time: 'Afternoon', event: 'Mini Golf', type: 'activity' },
        { time: '4:00 PM', event: "Mickey's Very Merry Christmas Party", type: 'special' },
      ]
    },
    {
      date: 'Wednesday, Dec 10',
      title: 'Hollywood Studios',
      icon: '🎬',
      park: 'hollywood-studios',
      hours: '9:00 AM - 7:00 PM',
      highlights: [
        { time: 'Rope Drop', event: 'Slinky Dog Dash', type: 'ride' },
        { time: '11:00 AM', event: "50's Prime Time Cafe", type: 'dining' },
        { time: '3:05 PM', event: "Oga's Cantina", type: 'dining' },
        { time: 'Evening', event: 'Fantasmic!', type: 'show' },
      ]
    },
    {
      date: 'Thursday, Dec 11',
      title: 'EPCOT',
      icon: '🌍',
      park: 'epcot',
      hours: '9:00 AM - 9:30 PM',
      highlights: [
        { time: 'Rope Drop', event: 'Frozen Ever After', type: 'ride' },
        { time: '11:05 AM', event: 'Akershus Royal Banquet Hall', type: 'dining' },
        { time: 'Evening', event: 'Luminous Fireworks', type: 'show' },
      ]
    },
    {
      date: 'Friday, Dec 12',
      title: 'Magic Kingdom',
      icon: '🏰',
      park: 'magic-kingdom',
      hours: '9:00 AM - 6:00 PM',
      highlights: [
        { time: 'All Day', event: 'Ride Favorites Again!', type: 'ride' },
        { time: '6:45 PM', event: 'Steakhouse 71', type: 'dining' },
      ]
    },
    {
      date: 'Saturday, Dec 13',
      title: 'Departure',
      icon: '👋',
      park: null,
      highlights: [
        { time: '7:15 AM', event: 'Rix Sports Bar Breakfast', type: 'dining' },
        { time: '11:00 AM', event: 'Check-out', type: 'resort' },
      ]
    },
  ];

  const getTypeIcon = (type) => {
    switch (type) {
      case 'dining': return '🍽️';
      case 'ride': return '🎢';
      case 'show': return '✨';
      case 'special': return '⭐';
      case 'resort': return '🏨';
      case 'explore': return '🗺️';
      case 'activity': return '⛳';
      default: return '📍';
    }
  };

  return (
    <section className="itinerary-section">
      <div className="container">
        <div className="section-header">
          <h2>📅 Your Magical Itinerary</h2>
          <p>December 6-13 at Walt Disney World</p>
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
            {itinerary[selectedDay].highlights.map((item, index) => (
              <div key={index} className={`highlight-item ${item.type}`}>
                <span className="highlight-time">{item.time}</span>
                <span className="highlight-icon">{getTypeIcon(item.type)}</span>
                <span className="highlight-event">{item.event}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Itinerary;
