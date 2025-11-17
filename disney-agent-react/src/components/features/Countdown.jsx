import React from 'react';
import { useTripContext } from '../../context/TripContext';
import { useCountdown } from '../../hooks/useCountdown';
import './Countdown.css';

const Countdown = () => {
  const { tripData } = useTripContext();
  const countdown = useCountdown(tripData.startDate);

  if (!tripData.createdAt || !countdown.isValid) {
    return (
      <section className="countdown-section">
        <div className="container">
          <div className="countdown-display">
            <h2>⏰ Countdown to Magic</h2>
            <div className="countdown-timer">
              <span className="countdown-text">Create your trip to see the countdown!</span>
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section className="countdown-section">
      <div className="container">
        <div className="countdown-display">
          <h2>⏰ Countdown to Magic</h2>
          <div className="countdown-timer">
            <div className="countdown-grid">
              <div className="countdown-item">
                <span className="countdown-value">{countdown.days}</span>
                <span className="countdown-label">Days</span>
              </div>
              <div className="countdown-item">
                <span className="countdown-value">{countdown.hours}</span>
                <span className="countdown-label">Hours</span>
              </div>
              <div className="countdown-item">
                <span className="countdown-value">{countdown.minutes}</span>
                <span className="countdown-label">Minutes</span>
              </div>
              <div className="countdown-item">
                <span className="countdown-value">{countdown.seconds}</span>
                <span className="countdown-label">Seconds</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Countdown;
