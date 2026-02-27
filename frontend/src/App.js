import React, { useState, useEffect } from 'react';
import './App.css';
import Converter from './components/Converter';
import Comparator from './components/Comparator';
import CurrentTime from './components/CurrentTime';

function App() {
  const [activeTab, setActiveTab] = useState('converter');

  return (
    <div className="app">
      <header className="app-header">
        <h1>🌍 Badawy Timezone Converter</h1>
        <p>Convert and compare times across the world</p>
      </header>

      <nav className="nav-tabs">
        <button
          className={`tab-button ${activeTab === 'converter' ? 'active' : ''}`}
          onClick={() => setActiveTab('converter')}
        >
          Converter
        </button>
        <button
          className={`tab-button ${activeTab === 'current' ? 'active' : ''}`}
          onClick={() => setActiveTab('current')}
        >
          Current Time
        </button>
        <button
          className={`tab-button ${activeTab === 'comparator' ? 'active' : ''}`}
          onClick={() => setActiveTab('comparator')}
        >
          Compare
        </button>
      </nav>

      <main className="app-main">
        {activeTab === 'converter' && <Converter />}
        {activeTab === 'current' && <CurrentTime />}
        {activeTab === 'comparator' && <Comparator />}
      </main>

      <footer className="app-footer">
        <p>© 2024 Badawy Timezone Converter | Bringing the world closer</p>
      </footer>
    </div>
  );
}

export default App;
