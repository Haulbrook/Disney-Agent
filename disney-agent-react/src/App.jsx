import React from 'react';
import { TripProvider, useTripContext } from './context/TripContext';
import Login from './components/features/Login';
import Hero from './components/features/Hero';
import Dashboard from './components/features/Dashboard';
import Countdown from './components/features/Countdown';
import Itinerary from './components/features/Itinerary';
import TripIdeas from './components/features/TripIdeas';
import Checklist from './components/features/Checklist';
import Footer from './components/layout/Footer';
import './styles/theme.css';
import './App.css';

function AppContent() {
  const { isLoggedIn } = useTripContext();

  if (!isLoggedIn) {
    return <Login />;
  }

  return (
    <div className="App">
      <Hero />
      <Dashboard />
      <Countdown />
      <Itinerary />
      <TripIdeas />
      <Checklist />
      <Footer />
    </div>
  );
}

function App() {
  return (
    <TripProvider>
      <AppContent />
    </TripProvider>
  );
}

export default App;
