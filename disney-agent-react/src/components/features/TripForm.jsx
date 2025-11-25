import React, { useState } from 'react';
import { useTripContext } from '../../context/TripContext';
import Button from '../ui/Button';
import Card from '../ui/Card';
import './TripForm.css';

const TripForm = () => {
  const { createTrip } = useTripContext();
  const [formData, setFormData] = useState({
    destination: 'Walt Disney World',
    partySize: 4,
    startDate: '',
    endDate: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.startDate || !formData.endDate) {
      alert('Please fill in all fields!');
      return;
    }

    if (new Date(formData.endDate) < new Date(formData.startDate)) {
      alert('End date must be after start date!');
      return;
    }

    createTrip(
      formData.destination,
      parseInt(formData.partySize),
      formData.startDate,
      formData.endDate
    );

    // Scroll to dashboard
    document.getElementById('dashboard')?.scrollIntoView({ behavior: 'smooth' });
  };

  const today = new Date().toISOString().split('T')[0];

  return (
    <section id="create-trip" className="trip-form-section">
      <div className="container">
        <div className="section-header">
          <h2>✨ Create Your Magical Trip</h2>
          <p>Start planning your Disney adventure by filling out the details below</p>
        </div>

        <Card className="trip-form-card fade-in">
          <h4 className="form-title">Trip <em>Details</em></h4>

          <form onSubmit={handleSubmit} className="trip-form">
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="destination">Destination:</label>
                <select
                  id="destination"
                  name="destination"
                  value={formData.destination}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select destination...</option>
                  <option value="Walt Disney World">Walt Disney World</option>
                  <option value="Disneyland Resort">Disneyland Resort</option>
                  <option value="Disneyland Paris">Disneyland Paris</option>
                  <option value="Tokyo Disney Resort">Tokyo Disney Resort</option>
                  <option value="Hong Kong Disneyland">Hong Kong Disneyland</option>
                  <option value="Shanghai Disney Resort">Shanghai Disney Resort</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="partySize">Party Size:</label>
                <input
                  type="number"
                  id="partySize"
                  name="partySize"
                  value={formData.partySize}
                  onChange={handleChange}
                  min="1"
                  max="20"
                  required
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="startDate">Start Date:</label>
                <input
                  type="date"
                  id="startDate"
                  name="startDate"
                  value={formData.startDate}
                  onChange={handleChange}
                  min={today}
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="endDate">End Date:</label>
                <input
                  type="date"
                  id="endDate"
                  name="endDate"
                  value={formData.endDate}
                  onChange={handleChange}
                  min={formData.startDate || today}
                  required
                />
              </div>
            </div>

            <div className="form-submit">
              <Button type="submit" variant="primary" size="large">
                ✨ Create Trip Plan
              </Button>
            </div>
          </form>
        </Card>
      </div>
    </section>
  );
};

export default TripForm;
