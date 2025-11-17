import React from 'react';
import { TripProvider } from './context/TripContext';
import Hero from './components/features/Hero';
import Dashboard from './components/features/Dashboard';
import Countdown from './components/features/Countdown';
import TripIdeas from './components/features/TripIdeas';
import Checklist from './components/features/Checklist';
import TripForm from './components/features/TripForm';
import Footer from './components/layout/Footer';
import './styles/theme.css';
import './App.css';

function App() {
  return (
    <TripProvider>
      <div className="App">
        <Hero />
        <Dashboard />
        <Countdown />
        <TripIdeas />
        <Checklist />
        <TripForm />
        <Footer />
      </div>
    </TripProvider>
  );
}

export default App;
