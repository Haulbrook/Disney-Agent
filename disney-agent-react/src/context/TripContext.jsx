import React, { createContext, useContext, useState, useEffect } from 'react';

const TripContext = createContext();

export const useTripContext = () => {
  const context = useContext(TripContext);
  if (!context) {
    throw new Error('useTripContext must be used within a TripProvider');
  }
  return context;
};

// Generate a random trip code
function generateTripCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = '';
  for (let i = 0; i < 6; i++) {
    code += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return code;
}

export const TripProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentTripCode, setCurrentTripCode] = useState(null);
  const [tripData, setTripData] = useState({
    destination: 'Walt Disney World',
    partySize: 4,
    startDate: '2025-12-06',
    endDate: '2025-12-13',
    checklist: [],
    itinerary: [],
    createdAt: null,
  });

  // Check for existing session on mount
  useEffect(() => {
    try {
      const savedTripCode = localStorage.getItem('currentTripCode');
      if (savedTripCode) {
        const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
        if (allTrips[savedTripCode]) {
          setTripData(allTrips[savedTripCode]);
          setCurrentTripCode(savedTripCode);
          setIsLoggedIn(true);
        }
      }
    } catch (error) {
      console.error('Error loading trip data:', error);
      localStorage.removeItem('currentTripCode');
    }
  }, []);

  // Save to localStorage whenever tripData changes
  useEffect(() => {
    try {
      if (currentTripCode && tripData.createdAt) {
        const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
        allTrips[currentTripCode] = tripData;
        localStorage.setItem('disneyTrips', JSON.stringify(allTrips));
        localStorage.setItem('currentTripCode', currentTripCode);
      }
    } catch (error) {
      console.error('Error saving trip data:', error);
    }
  }, [tripData, currentTripCode]);

  // Login with existing trip code
  const loginWithCode = (code) => {
    const upperCode = code.toUpperCase().trim();
    try {
      const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
      if (allTrips[upperCode]) {
        setTripData(allTrips[upperCode]);
        setCurrentTripCode(upperCode);
        setIsLoggedIn(true);
        localStorage.setItem('currentTripCode', upperCode);
        return { success: true };
      } else {
        return { success: false, error: 'Trip code not found' };
      }
    } catch (error) {
      return { success: false, error: 'Error accessing trip data' };
    }
  };

  // Create new trip with trip code
  const createTripWithCode = (destination, partySize, startDate, endDate) => {
    const newCode = generateTripCode();
    const checklist = generateChecklist(destination, partySize, startDate, endDate);
    const newTripData = {
      destination,
      partySize,
      startDate,
      endDate,
      checklist,
      createdAt: new Date().toISOString(),
      tripCode: newCode,
    };

    setTripData(newTripData);
    setCurrentTripCode(newCode);
    setIsLoggedIn(true);

    // Save immediately
    const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
    allTrips[newCode] = newTripData;
    localStorage.setItem('disneyTrips', JSON.stringify(allTrips));
    localStorage.setItem('currentTripCode', newCode);

    return newCode;
  };

  // Logout
  const logout = () => {
    setIsLoggedIn(false);
    setCurrentTripCode(null);
    setTripData({
      destination: 'Walt Disney World',
      partySize: 4,
      startDate: '2025-12-06',
      endDate: '2025-12-13',
      checklist: [],
      itinerary: [],
      createdAt: null,
    });
    localStorage.removeItem('currentTripCode');
  };

  // Update itinerary
  const updateItinerary = (itinerary) => {
    setTripData((prev) => {
      const updated = { ...prev, itinerary };
      // Save immediately
      if (currentTripCode) {
        const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
        allTrips[currentTripCode] = updated;
        localStorage.setItem('disneyTrips', JSON.stringify(allTrips));
      }
      return updated;
    });
  };

  const updateChecklistItem = (id, completed) => {
    setTripData((prev) => ({
      ...prev,
      checklist: prev.checklist.map((item) =>
        item.id === id ? { ...item, completed } : item
      ),
    }));
  };

  const deleteChecklistItem = (id) => {
    setTripData((prev) => ({
      ...prev,
      checklist: prev.checklist.filter((item) => item.id !== id),
    }));
  };

  // Add new checklist item
  const addChecklistItem = (title, description, category = 'Custom', priority = 'medium') => {
    const newItem = {
      id: `item-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
      title,
      description,
      category,
      priority,
      completed: false,
    };
    setTripData((prev) => ({
      ...prev,
      checklist: [...prev.checklist, newItem],
    }));
  };

  const clearData = () => {
    if (window.confirm('Are you sure you want to delete this trip? This cannot be undone.')) {
      const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
      delete allTrips[currentTripCode];
      localStorage.setItem('disneyTrips', JSON.stringify(allTrips));
      logout();
    }
  };

  const saveData = () => {
    if (currentTripCode) {
      const allTrips = JSON.parse(localStorage.getItem('disneyTrips') || '{}');
      allTrips[currentTripCode] = tripData;
      localStorage.setItem('disneyTrips', JSON.stringify(allTrips));
      alert('Trip data saved successfully!');
    }
  };

  return (
    <TripContext.Provider
      value={{
        tripData,
        isLoggedIn,
        currentTripCode,
        loginWithCode,
        createTripWithCode,
        logout,
        updateItinerary,
        addChecklistItem,
        updateChecklistItem,
        deleteChecklistItem,
        clearData,
        saveData,
      }}
    >
      {children}
    </TripContext.Provider>
  );
};

// Helper function to generate checklist based on trip details
function generateChecklist(destination, partySize, startDate, endDate) {
  const baseItems = [
    { category: 'Planning', priority: 'high', title: 'Book Resort Hotel', description: 'Reserve your Disney resort accommodation' },
    { category: 'Planning', priority: 'high', title: 'Purchase Park Tickets', description: 'Buy park hopper tickets for all days' },
    { category: 'Planning', priority: 'high', title: 'Make Dining Reservations', description: 'Book restaurants 60 days in advance' },
    { category: 'Planning', priority: 'medium', title: 'Book Lightning Lane', description: 'Purchase Genie+ and Individual Lightning Lanes' },
    { category: 'Planning', priority: 'medium', title: 'Plan Each Park Day', description: 'Create daily itineraries for each park' },
    { category: 'Packing', priority: 'high', title: 'Pack Comfortable Shoes', description: 'Bring broken-in walking shoes' },
    { category: 'Packing', priority: 'high', title: 'Pack Sunscreen', description: 'SPF 50+ for Florida sun' },
    { category: 'Packing', priority: 'medium', title: 'Bring Portable Chargers', description: 'Keep devices charged all day' },
    { category: 'Packing', priority: 'medium', title: 'Pack Rain Ponchos', description: 'Florida afternoon showers are common' },
    { category: 'Packing', priority: 'low', title: 'Bring Autograph Book', description: 'For character meet and greets' },
    { category: 'Pre-Trip', priority: 'high', title: 'Download My Disney Experience App', description: 'Essential for park navigation' },
    { category: 'Pre-Trip', priority: 'medium', title: 'Link Park Tickets to App', description: 'Connect all tickets and reservations' },
    { category: 'Pre-Trip', priority: 'medium', title: 'Set Up Mobile Order', description: 'Save time with mobile food ordering' },
    { category: 'Pre-Trip', priority: 'low', title: 'Create Disney PhotoPass Account', description: 'Capture all your magical moments' },
  ];

  return baseItems.map((item, index) => ({
    ...item,
    id: `item-${Date.now()}-${index}`,
    completed: false,
  }));
}
