import { createContext, useContext, useState, useEffect } from 'react';

const TripContext = createContext();

const getInitialTripData = () => {
  const defaultData = {
    destination: 'Walt Disney World',
    partySize: 4,
    startDate: '2025-12-06',
    endDate: '2025-12-13',
    checklist: [],
    createdAt: null,
  };

  try {
    const savedTrip = localStorage.getItem('disneyTripData');
    if (savedTrip) {
      return JSON.parse(savedTrip);
    }
  } catch (error) {
    console.error('Error loading trip data from localStorage:', error);
    localStorage.removeItem('disneyTripData');
  }
  return defaultData;
};

// eslint-disable-next-line react-refresh/only-export-components
export const useTripContext = () => {
  const context = useContext(TripContext);
  if (!context) {
    throw new Error('useTripContext must be used within a TripProvider');
  }
  return context;
};

export const TripProvider = ({ children }) => {
  const [tripData, setTripData] = useState(getInitialTripData);

  // Save to localStorage whenever tripData changes
  useEffect(() => {
    try {
      if (tripData.createdAt) {
        localStorage.setItem('disneyTripData', JSON.stringify(tripData));
      }
    } catch (error) {
      console.error('Error saving trip data to localStorage:', error);
    }
  }, [tripData]);

  const createTrip = (destination, partySize, startDate, endDate) => {
    const checklist = generateChecklist(destination, partySize, startDate, endDate);
    setTripData({
      destination,
      partySize,
      startDate,
      endDate,
      checklist,
      createdAt: new Date().toISOString(),
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

  const clearData = () => {
    if (window.confirm('Are you sure you want to clear all trip data?')) {
      setTripData({
        destination: 'Walt Disney World',
        partySize: 4,
        startDate: '',
        endDate: '',
        checklist: [],
        createdAt: null,
      });
      localStorage.removeItem('disneyTripData');
    }
  };

  const saveData = () => {
    localStorage.setItem('disneyTripData', JSON.stringify(tripData));
    alert('Trip data saved successfully!');
  };

  return (
    <TripContext.Provider
      value={{
        tripData,
        createTrip,
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
function generateChecklist(_destination, _partySize, _startDate, _endDate) {

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
