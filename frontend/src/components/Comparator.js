import React, { useState } from 'react';
import '../styles/Comparator.css';

function Comparator() {
  const [timezones, setTimezones] = useState(['America/New_York', 'Europe/London', 'Asia/Cairo', 'Australia/Sydney']);
  const [allTimezones, setAllTimezones] = useState([]);
  const [comparison, setComparison] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [newTz, setNewTz] = useState('');

  React.useEffect(() => {
    fetchTimezones();
  }, []);

  const fetchTimezones = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/timezones');
      const data = await response.json();
      setAllTimezones(data.timezones);
    } catch (err) {
      setError('Failed to load timezones');
    }
  };

  const handleCompare = async () => {
    if (timezones.length === 0) {
      setError('Please add at least one timezone');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/api/compare', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ timezones }),
      });

      const data = await response.json();
      setComparison(data.comparison);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const addTimezone = () => {
    if (newTz && !timezones.includes(newTz)) {
      setTimezones([...timezones, newTz]);
      setNewTz('');
    }
  };

  const removeTimezone = (tz) => {
    setTimezones(timezones.filter((t) => t !== tz));
  };

  return (
    <div className="comparator">
      <h2>Compare Timezones</h2>

      <div className="timezone-selector">
        <div className="select-group">
          <select value={newTz} onChange={(e) => setNewTz(e.target.value)}>
            <option value="">Select a timezone to add</option>
            {allTimezones.map((tz) => (
              <option key={tz} value={tz}>
                {tz}
              </option>
            ))}
          </select>
          <button onClick={addTimezone}>Add</button>
        </div>

        <div className="selected-timezones">
          {timezones.map((tz) => (
            <div key={tz} className="timezone-tag">
              {tz}
              <button onClick={() => removeTimezone(tz)}>×</button>
            </div>
          ))}
        </div>

        <button onClick={handleCompare} className="compare-btn" disabled={loading}>
          {loading ? 'Comparing...' : 'Compare Now'}
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      {comparison && (
        <div className="comparison-grid">
          {comparison.map((item, index) => (
            <div key={index} className="comparison-card">
              <h3>{item.timezone}</h3>
              <p className="datetime">{item.formatted}</p>
              <p className="offset">{item.offset}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Comparator;
