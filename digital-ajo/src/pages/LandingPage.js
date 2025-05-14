import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/LandingPage.css';

function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="landing-container">
      <div className="landing-card">
        <h1 className="logo">Digital Ajo</h1>
        <p className="tagline">Digital Ajo for your trusted circles.</p>

        <div className="button-group">
          <button 
            className="btn-primary"
            onClick={() => navigate('/create-group')}
          >
            Start a New Group
          </button>
          <button 
            className="btn-secondary"
            onClick={() => navigate('/join-group')}
          >
            Join a Group
          </button>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
