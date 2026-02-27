# Badawy Timezone Converter 🌍

A modern, full-stack timezone conversion application built with Flask and React.

## Features

✨ **Convert Times** - Instantly convert times between any two timezones
🕐 **Current Time** - Check the current time in any timezone with live updates
📊 **Compare Timezones** - View and compare current time across multiple timezones simultaneously
🎨 **Modern UI** - Beautiful, responsive interface with gradient design
⚡ **Fast & Reliable** - Powered by Python's pytz library for accurate timezone handling

## Project Structure

```
badawy-timezone-converter/
├── backend/                    # Flask API
│   ├── app.py                 # Main application
│   ├── requirements.txt       # Python dependencies
│   └── routes/
│       └── timezone_routes.py # API endpoints
├── frontend/                   # React UI
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── styles/           # Component styles
│   │   └── App.js            # Main app
│   ├── package.json          # NPM dependencies
│   └── public/               # Static files
└── setup.bat/setup.sh        # Installation scripts
```

## Quick Start

### Windows
```bash
setup.bat
```

### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

## Running the Application

### Backend
```bash
cd backend
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
python app.py
```
Backend runs on: `http://localhost:5000`

### Frontend
```bash
cd frontend
npm start
```
Frontend runs on: `http://localhost:3000`

## API Endpoints

### Get All Timezones
```
GET /api/timezones
```

### Convert Between Timezones
```
POST /api/convert
Body: {
  "datetime": "2024-02-13T14:30:00",
  "from_tz": "America/New_York",
  "to_tz": "Asia/Cairo"
}
```

### Get Current Time
```
POST /api/current
Body: {
  "timezone": "Asia/Cairo"
}
```

### Compare Multiple Timezones
```
POST /api/compare
Body: {
  "timezones": ["America/New_York", "Europe/London", "Asia/Cairo", "Australia/Sydney"]
}
```

## Technologies Used

**Backend:**
- Python 3.x
- Flask - Web framework
- Flask-CORS - Cross-origin requests
- pytz - Timezone handling
- python-dateutil - Date utilities

**Frontend:**
- React 18
- CSS3 with gradients and animations
- Responsive design

## Features Breakdown

### 1. Converter Tab
- Select two timezones
- Pick any date and time
- Swap timezones with one click
- View the converted time and time difference

### 2. Current Time Tab
- Select any timezone
- See current time with automatic updates (every second)
- Display timezone offset

### 3. Comparator Tab
- Add multiple timezones
- View all current times simultaneously
- Remove timezones as needed
- Beautiful card-based layout

## Color Scheme

- Primary: #667eea (Purple Blue)
- Secondary: #764ba2 (Deep Purple)
- Background: Gradient from primary to secondary
- Text: Clean white and dark gray

## Future Enhancements

- 🔔 Scheduled time notifications
- 📱 Mobile app (React Native)
- 💾 Save favorite timezones
- 🌙 Dark/Light theme toggle
- 📈 Historical timezone offset changes
- 🔐 User accounts and preferences

## License

MIT License - Free to use and modify

## Author

Built with ❤️ by Badawy Team

---

**Ready to convert time zones? Let's go!** 🚀
