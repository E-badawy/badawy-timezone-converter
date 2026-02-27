# Badawy Timezone Converter - Backend

Flask API for timezone conversion and comparison.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /api/timezones` - Get all available timezones
- `POST /api/convert` - Convert time between timezones
- `POST /api/current` - Get current time in a timezone
- `POST /api/compare` - Compare current time across multiple timezones

## Example Requests

### Convert timezone
```json
{
  "datetime": "2024-02-13T14:30:00",
  "from_tz": "America/New_York",
  "to_tz": "Asia/Cairo"
}
```

### Get current time
```json
{
  "timezone": "Asia/Cairo"
}
```

### Compare timezones
```json
{
  "timezones": ["America/New_York", "Europe/London", "Asia/Cairo", "Australia/Sydney"]
}
```
