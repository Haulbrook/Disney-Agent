import React, { useState } from 'react';
import { useTripContext } from '../../context/TripContext';
import Card from '../ui/Card';
import Button from '../ui/Button';
import './Checklist.css';

const Checklist = () => {
  const { tripData, addChecklistItem, updateChecklistItem, deleteChecklistItem } = useTripContext();
  const [showAddForm, setShowAddForm] = useState(false);
  const [newItem, setNewItem] = useState({
    title: '',
    description: '',
    category: 'Custom',
    priority: 'medium',
  });

  const handleAddItem = (e) => {
    e.preventDefault();
    if (!newItem.title.trim()) return;

    addChecklistItem(
      newItem.title.trim(),
      newItem.description.trim(),
      newItem.category,
      newItem.priority
    );

    // Reset form
    setNewItem({
      title: '',
      description: '',
      category: 'Custom',
      priority: 'medium',
    });
    setShowAddForm(false);
  };

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
            <h3>No checklist items yet!</h3>
            <p>Add your first item to start tracking your trip planning</p>
            <button
              className="add-first-item-btn"
              onClick={() => setShowAddForm(true)}
            >
              + Add First Item
            </button>
          </div>

          {showAddForm && (
            <div className="add-item-form-container">
              <AddItemForm
                newItem={newItem}
                setNewItem={setNewItem}
                onSubmit={handleAddItem}
                onCancel={() => setShowAddForm(false)}
              />
            </div>
          )}
        </div>
      </section>
    );
  }

  const categories = [...new Set(tripData.checklist.filter(item => item.category).map(item => item.category))];

  return (
    <section id="checklist" className="checklist-section">
      <div className="container">
        <div className="section-header">
          <h2>✅ Your Trip Planning Checklist</h2>
          <p>Never forget the essentials for your magical adventure!</p>
        </div>

        {/* Add Item Button */}
        <div className="add-item-section">
          {!showAddForm ? (
            <button
              className="add-item-btn"
              onClick={() => setShowAddForm(true)}
            >
              <span className="add-icon">+</span>
              Add New Checklist Item
            </button>
          ) : (
            <AddItemForm
              newItem={newItem}
              setNewItem={setNewItem}
              onSubmit={handleAddItem}
              onCancel={() => setShowAddForm(false)}
            />
          )}
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
                      <h4>{item.title || 'Untitled'}</h4>
                      {item.priority && (
                        <span className={`priority-badge priority-${item.priority}`}>
                          ⭐ {item.priority.toUpperCase()}
                        </span>
                      )}
                    </div>
                    <p>{item.description || ''}</p>
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

// Separate component for the add item form
const AddItemForm = ({ newItem, setNewItem, onSubmit, onCancel }) => {
  return (
    <form className="add-item-form" onSubmit={onSubmit}>
      <h4>Add New Item</h4>

      <div className="form-row">
        <div className="form-group">
          <label>Title *</label>
          <input
            type="text"
            value={newItem.title}
            onChange={(e) => setNewItem({ ...newItem, title: e.target.value })}
            placeholder="e.g., Pack snacks for park days"
            required
          />
        </div>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label>Description</label>
          <input
            type="text"
            value={newItem.description}
            onChange={(e) => setNewItem({ ...newItem, description: e.target.value })}
            placeholder="Optional details..."
          />
        </div>
      </div>

      <div className="form-row two-col">
        <div className="form-group">
          <label>Category</label>
          <select
            value={newItem.category}
            onChange={(e) => setNewItem({ ...newItem, category: e.target.value })}
          >
            <option value="Custom">Custom</option>
            <option value="Planning">Planning</option>
            <option value="Packing">Packing</option>
            <option value="Pre-Trip">Pre-Trip</option>
            <option value="Day-Of">Day-Of</option>
            <option value="Reminders">Reminders</option>
          </select>
        </div>

        <div className="form-group">
          <label>Priority</label>
          <select
            value={newItem.priority}
            onChange={(e) => setNewItem({ ...newItem, priority: e.target.value })}
          >
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </div>
      </div>

      <div className="form-actions">
        <button type="submit" className="submit-btn">
          Add Item
        </button>
        <button type="button" className="cancel-btn" onClick={onCancel}>
          Cancel
        </button>
      </div>
    </form>
  );
};

export default Checklist;
