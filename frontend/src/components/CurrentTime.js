import React, { useState, useEffect } from 'react';
import '../styles/CurrentTime.css';

function CurrentTime() {
  const [timezones, setTimezones] = useState([]);
  const [selectedTz, setSelectedTz] = useState('Asia/Cairo');
  const [currentTime, setCurrentTime] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTimezones();
  }, []);

  useEffect(() => {
    if (selectedTz) {
      fetchCurrentTime();
    }
  }, [selectedTz]);

  const fetchTimezones = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/timezones');
      const data = await response.json();
      setTimezones(data.timezones);
    } catch (err) {
      setError('Failed to load timezones');
    }
  };

  const fetchCurrentTime = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/api/current', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ timezone: selectedTz }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error);
      }

      const data = await response.json();
      setCurrentTime(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Auto-refresh every second
  useEffect(() => {
    const interval = setInterval(() => {
      fetchCurrentTime();
    }, 1000);

    return () => clearInterval(interval);
  }, [selectedTz]);

  return (
    <div className="current-time">
      <h2>Current Time by Timezone</h2>

      <div className="form-group">
        <label>Select Timezone:</label>
        <select value={selectedTz} onChange={(e) => setSelectedTz(e.target.value)}>
          {timezones.map((tz) => (
            <option key={tz} value={tz}>
              {tz}
            </option>
          ))}
        </select>
      </div>

      {error && <div className="error-message">{error}</div>}

      {currentTime && (
        <div className="current-time-display">
          <div className="time-box">
            <p className="timezone">{currentTime.timezone}</p>
            <p className="time">{currentTime.formatted}</p>
            <p className="offset">{currentTime.offset}</p>
          </div>
        </div>
      )}

      {loading && <div className="loading">Loading...</div>}
    </div>
  );
}

export default CurrentTime;
