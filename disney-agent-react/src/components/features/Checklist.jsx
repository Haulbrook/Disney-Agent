import React from 'react';
import { useTripContext } from '../../context/TripContext';
import Card from '../ui/Card';
import Button from '../ui/Button';
import './Checklist.css';

const Checklist = () => {
  const { tripData, updateChecklistItem, deleteChecklistItem } = useTripContext();

  if (!tripData.createdAt || tripData.checklist.length === 0) {
    return (
      <section id="checklist" className="checklist-section">
        <div className="container">
          <div className="section-header">
            <h2>✅ Your Trip Planning Checklist</h2>
            <p>Never forget the essentials for your magical adventure!</p>
          </div>
          <div className="empty-state">
            <i className="fa fa-magic empty-icon"></i>
            <h3>Create Your Trip Plan First!</h3>
            <p>Scroll down to create your trip and generate your personalized checklist</p>
          </div>
        </div>
      </section>
    );
  }

  const categories = [...new Set(tripData.checklist.map(item => item.category))];

  return (
    <section id="checklist" className="checklist-section">
      <div className="container">
        <div className="section-header">
          <h2>✅ Your Trip Planning Checklist</h2>
          <p>Never forget the essentials for your magical adventure!</p>
        </div>

        {categories.map(category => (
          <div key={category} className="checklist-category">
            <h3 className="category-title">📁 {category}</h3>
            <div className="checklist-grid">
              {tripData.checklist
                .filter(item => item.category === category)
                .map(item => (
                  <Card
                    key={item.id}
                    variant="checklist"
                    className={item.completed ? 'completed' : ''}
                    hoverable={true}
                  >
                    <div className="checklist-header">
                      <h4>{item.title}</h4>
                      <span className={`priority-badge priority-${item.priority}`}>
                        ⭐ {item.priority.toUpperCase()}
                      </span>
                    </div>
                    <p>{item.description}</p>
                    <div className="checklist-actions">
                      <label className="checkbox-label">
                        <input
                          type="checkbox"
                          checked={item.completed}
                          onChange={(e) => updateChecklistItem(item.id, e.target.checked)}
                        />
                        <span>{item.completed ? 'Completed' : 'Mark as complete'}</span>
                      </label>
                      <Button
                        variant="danger"
                        size="small"
                        onClick={() => deleteChecklistItem(item.id)}
                      >
                        Delete
                      </Button>
                    </div>
                  </Card>
                ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Checklist;
