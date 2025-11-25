import React from 'react';
import Card from '../ui/Card';
import './TripIdeas.css';

const TripIdeas = () => {
  const ideas = [
    {
      icon: 'fa-cutlery',
      title: 'Character Dining',
      description: 'Meet your favorite Disney characters while enjoying delicious meals at themed restaurants.',
      tip: 'Book dining reservations 60 days in advance for the best selections!',
    },
    {
      icon: 'fa-camera',
      title: 'PhotoPass Memories',
      description: 'Capture every magical moment with Disney PhotoPass photographers throughout the parks.',
      tip: 'Look for Magic Shot locations where photographers add special Disney magic to your photos!',
    },
    {
      icon: 'fa-star',
      title: 'Evening Fireworks',
      description: 'Experience spectacular nighttime shows with fireworks, projections, and music.',
      tip: 'Arrive 30-45 minutes early to secure the best viewing spots near the castle!',
    },
  ];

  return (
    <section className="trip-ideas-section">
      <div className="container">
        <div className="section-header">
          <h2>💡 Trip Ideas & Suggestions</h2>
          <p>Make the most of your magical adventure</p>
        </div>

        <div className="grid grid-3">
          {ideas.map((idea, index) => (
            <Card key={index} variant="idea" hoverable={true}>
              <div className="idea-icon">
                <i className={`fa ${idea.icon}`}></i>
              </div>
              <h4>{idea.title}</h4>
              <p>{idea.description}</p>
              <div className="idea-tip">
                <strong>💡 Pro Tip:</strong> {idea.tip}
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TripIdeas;
