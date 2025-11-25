import React from 'react';
import { useTripContext } from '../../context/TripContext';
import './Hero.css';

const Hero = () => {
  const { currentTripCode, logout } = useTripContext();

  const scrollToSection = (id) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleLogout = () => {
    if (window.confirm('Are you sure you want to switch trips? Make sure you saved your trip code!')) {
      logout();
    }
  };

  return (
    <section className="hero">
      <div className="hero-container">
        <div className="hero-content">
          <div className="hero-sidebar">
            <div className="logo">
              <h1>💫 Disney Trip Planner</h1>
              <p className="subtitle">Modern Edition</p>
            </div>

            {currentTripCode && (
              <div className="trip-code-badge">
                <span className="badge-label">Trip Code</span>
                <span className="badge-code">{currentTripCode}</span>
              </div>
            )}

            <nav className="hero-nav">
              <h4>Plan Your Magical Adventure:</h4>
              <ul>
                <li>
                  <a onClick={() => scrollToSection('dashboard')}>
                    Trip <em>Dashboard</em> <i className="fa fa-dashboard"></i>
                  </a>
                </li>
                <li>
                  <a onClick={() => scrollToSection('itinerary')}>
                    Daily <em>Itinerary</em> <i className="fa fa-calendar"></i>
                  </a>
                </li>
                <li>
                  <a onClick={() => scrollToSection('checklist')}>
                    View Your <em>Checklist</em> <i className="fa fa-check-square-o"></i>
                  </a>
                </li>
              </ul>
            </nav>
            <div className="hero-cta">
              <button onClick={() => scrollToSection('dashboard')} className="cta-button">
                <i className="fa fa-dashboard"></i> View Dashboard
              </button>
              <button onClick={handleLogout} className="logout-button">
                <i className="fa fa-sign-out"></i> Switch Trip
              </button>
            </div>
          </div>

          <div className="hero-welcome">
            <div className="welcome-overlay"></div>
            <div className="welcome-content">
              <i className="fa fa-magic floating-icon"></i>
              <h2>Welcome to Your</h2>
              <h3>Magical Planning Journey</h3>
              <p>Organize every detail of your Disney adventure with our modern trip planner</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
