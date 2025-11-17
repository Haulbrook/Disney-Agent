import React from 'react';
import { useTripContext } from '../../context/TripContext';
import Card from '../ui/Card';
import Button from '../ui/Button';
import './Dashboard.css';

const Dashboard = () => {
  const { tripData, saveData, clearData } = useTripContext();

  const completedCount = tripData.checklist.filter(item => item.completed).length;
  const totalCount = tripData.checklist.length;
  const percentage = totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0;

  return (
    <section id="dashboard" className="dashboard-section">
      <div className="container">
        <div className="section-header">
          <h2>📋 Trip Dashboard</h2>
          <p>Your trip overview and progress at a glance</p>
        </div>

        <div className="grid grid-3">
          <Card variant="summary" hoverable={false}>
            <h4>Trip Details</h4>
            {tripData.createdAt ? (
              <div className="trip-details">
                <p><strong>Destination:</strong> {tripData.destination}</p>
                <p><strong>Party Size:</strong> {tripData.partySize} guests</p>
                <p><strong>Dates:</strong> {new Date(tripData.startDate).toLocaleDateString()} - {new Date(tripData.endDate).toLocaleDateString()}</p>
              </div>
            ) : (
              <p className="empty-message">Create your trip to see details here</p>
            )}
          </Card>

          <Card variant="summary" hoverable={false}>
            <h4>Checklist Progress</h4>
            <div className="progress-display">
              <div className="progress-circle">
                <span>{percentage}%</span>
              </div>
              <div className="progress-stats">
                <p><strong>{completedCount}</strong> of <strong>{totalCount}</strong> completed</p>
              </div>
            </div>
          </Card>

          <Card variant="summary" hoverable={false}>
            <h4>Quick Actions</h4>
            <div className="action-buttons">
              <Button onClick={saveData} variant="primary" size="small">
                💾 Save Trip
              </Button>
              <Button onClick={clearData} variant="danger" size="small">
                🗑️ Clear Data
              </Button>
            </div>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default Dashboard;
