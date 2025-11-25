import React from 'react';
import './Footer.css';

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="footer">
      <div className="container">
        <button onClick={scrollToTop} className="scroll-top-btn">
          Back To Top
        </button>
        <p className="footer-main">✨ Built with magic and love for Disney families ✨</p>
        <p className="footer-sub">Powered by React • Modernized with FrontEndAestheticAgent</p>
      </div>
    </footer>
  );
};

export default Footer;
