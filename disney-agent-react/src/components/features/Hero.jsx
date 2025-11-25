import React from 'react';
import './Hero.css';

const Hero = () => {
  const scrollToSection = (id) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
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
            <nav className="hero-nav">
              <h4>Plan Your Magical Adventure:</h4>
              <ul>
                <li>
                  <a onClick={() => scrollToSection('dashboard')}>
                    Trip <em>Dashboard</em> <i className="fa fa-dashboard"></i>
                  </a>
                </li>
                <li>
                  <a onClick={() => scrollToSection('checklist')}>
                    View Your <em>Checklist</em> <i className="fa fa-check-square-o"></i>
                  </a>
                </li>
                <li>
                  <a onClick={() => scrollToSection('create-trip')}>
                    Create <em>New Trip</em> <i className="fa fa-plus-circle"></i>
                  </a>
                </li>
              </ul>
            </nav>
            <div className="hero-cta">
              <button onClick={() => scrollToSection('dashboard')} className="cta-button">
                <i className="fa fa-dashboard"></i> View Dashboard
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
