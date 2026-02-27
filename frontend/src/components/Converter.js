import React, { useState, useEffect } from 'react';
import '../styles/Converter.css';

function Converter() {
  const [timezones, setTimezones] = useState([]);
  const [fromTz, setFromTz] = useState('America/New_York');
  const [toTz, setToTz] = useState('Asia/Cairo');
  const [datetime, setDatetime] = useState(new Date().toISOString().slice(0, 16));
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch timezones on mount
  useEffect(() => {
    fetchTimezones();
  }, []);

  const fetchTimezones = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/timezones');
      const data = await response.json();
      setTimezones(data.timezones);
    } catch (err) {
      setError('Failed to load timezones');
    }
  };

  const handleConvert = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/api/convert', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          datetime: datetime,
          from_tz: fromTz,
          to_tz: toTz,
        }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const swapTimezones = () => {
    setFromTz(toTz);
    setToTz(fromTz);
  };

  return (
    <div className="converter">
      <h2>Timezone Converter</h2>
      <form onSubmit={handleConvert} className="converter-form">
        <div className="form-group">
          <label>Date & Time:</label>
          <input
            type="datetime-local"
            value={datetime}
            onChange={(e) => setDatetime(e.target.value)}
            required
          />
        </div>

        <div className="timezone-row">
          <div className="form-group">
            <label>From:</label>
            <select value={fromTz} onChange={(e) => setFromTz(e.target.value)}>
              {timezones.map((tz) => (
                <option key={tz} value={tz}>
                  {tz}
                </option>
              ))}
            </select>
          </div>

          <button type="button" className="swap-btn" onClick={swapTimezones}>
            ⇄
          </button>

          <div className="form-group">
            <label>To:</label>
            <select value={toTz} onChange={(e) => setToTz(e.target.value)}>
              {timezones.map((tz) => (
                <option key={tz} value={tz}>
                  {tz}
                </option>
              ))}
            </select>
          </div>
        </div>

        <button type="submit" className="convert-btn" disabled={loading}>
          {loading ? 'Converting...' : 'Convert'}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}

      {result && (
        <div className="result">
          <div className="result-box original">
            <h3>Original Time</h3>
            <p className="timezone">{result.original.timezone}</p>
            <p className="datetime">{new Date(result.original.datetime).toLocaleString()}</p>
            <p className="offset">{result.original.offset}</p>
          </div>

          <div className="arrow">→</div>

          <div className="result-box converted">
            <h3>Converted Time</h3>
            <p className="timezone">{result.converted.timezone}</p>
            <p className="datetime">{new Date(result.converted.datetime).toLocaleString()}</p>
            <p className="offset">{result.converted.offset}</p>
          </div>

          <div className="time-diff">
            <p>Time difference: <strong>{result.time_difference_hours > 0 ? '+' : ''}{result.time_difference_hours} hours</strong></p>
          </div>
        </div>
      )}
    </div>
  );
}

export default Converter;
