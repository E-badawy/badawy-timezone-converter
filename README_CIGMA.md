# 🌍 CIGMA Timezone Converter

A fast, easy-to-use timezone converter for managing time across the world. Convert times, check current times in any timezone, and compare multiple timezones simultaneously.

## ✨ Features

- **Timezone Converter** - Convert times between 596+ timezones
- **Current Time** - View live current time in any timezone
- **Timezone Comparator** - Compare multiple timezones at once
- **Beautiful UI** - Modern, responsive design with purple gradient theme
- **Desktop App** - Standalone executable (.exe) for Windows
- **Web App** - Deploy online for free using Render.com
- **Mobile App** - Install as PWA on phones and tablets
- **About & Contact** - Learn about CIGMA and get in touch

## 🚀 Quick Start

### Desktop Application

1. Navigate to the `dist` folder
2. Double-click `RUN.bat`
3. App launches automatically in your browser
4. Visit `http://127.0.0.1:5000`

**File:** `BadawyTimezoneConverter.exe` (55 MB, includes all dependencies)

### Running from Source

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask server
cd backend
python app.py

# Visit in browser
http://127.0.0.1:5000
```

## 📋 Pages & Sections

### Main Features
- **Converter Tab** - Select two timezones and a date/time, see the conversion
- **Current Time Tab** - View current time in any timezone with live updates
- **Compare Tab** - Add multiple timezones to see their current times side-by-side

### Additional Pages
- **About Tab** - Learn about CIGMA Timezone Converter
- **Contact Tab** - Send us a message

## 📧 Contact Information

- **Email:** officialbadawy@gmail.com
- **Phone:** 08065440075
- **Hours:** Monday - Friday, 9 AM - 6 PM (WAT)

## 🌐 Deploy to the Cloud

### Free Hosting with Render.com

See `DEPLOYMENT_GUIDE.md` for detailed instructions:

1. Push code to GitHub
2. Connect to Render.com
3. Deploy with one click
4. Get live URL for sharing

## 📱 Install as Mobile App

The app is a Progressive Web App (PWA):

1. Visit the web app URL in your browser
2. Click the install icon in the address bar
3. Choose "Install app"
4. App appears on your homescreen!

## 🛠️ Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Timezone Data:** pytz (596+ timezones)
- **Desktop:** PyInstaller (Windows executable)
- **Hosting:** Render.com (free tier available)

## 📦 Project Structure

```
badawy-timezone-converter/
├── backend/
│   ├── app.py                 # Flask main application
│   ├── requirements.txt        # Python dependencies
│   └── routes/
│       ├── timezone_routes.py # Timezone API endpoints
│       └── contact_routes.py  # Contact form handling
├── frontend/
│   ├── index.html             # Main application
│   ├── debug.html             # Debug version
│   └── test.html              # API test page
├── dist/
│   ├── BadawyTimezoneConverter.exe  # Desktop app
│   └── RUN.bat                # Launcher script
├── DEPLOYMENT_GUIDE.md        # Cloud deployment instructions
└── Procfile                   # Render.com configuration
```

## 🔧 API Endpoints

All endpoints are prefixed with `/api/`

### GET `/api/timezones`
Returns all available timezones
```json
{
  "timezones": ["Africa/Abidjan", "Africa/Accra", ...],
  "count": 596
}
```

### POST `/api/convert`
Convert time between timezones
```json
{
  "datetime": "2026-02-13T12:00:00",
  "from_tz": "America/New_York",
  "to_tz": "Asia/Tokyo"
}
```

### POST `/api/current`
Get current time in timezone
```json
{
  "timezone": "UTC"
}
```

### POST `/api/compare`
Compare multiple timezones
```json
{
  "timezones": ["UTC", "America/New_York", "Asia/Tokyo"]
}
```

### POST `/api/contact`
Send contact form message
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Feedback",
  "message": "Great app!"
}
```

## 🎨 Customization

### Change Colors
Edit the gradient in `frontend/index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Contact Info
Edit `frontend/index.html` contact section and `backend/routes/contact_routes.py`

## 🐛 Troubleshooting

**App won't start?**
- Check if port 5000 is available
- Run as Administrator on Windows
- Check `requirements.txt` packages are installed

**Contact form not working?**
- Configure Gmail App Password in `contact_routes.py`
- Check firewall settings
- Verify email credentials

**Desktop app file not found?**
- Rebuild with: `python build_exe.py` (requires PyInstaller)

## 📄 License

Built with ❤️ by CIGMA Team

## 🙏 Support

For issues, questions, or feedback:
- Email: officialbadawy@gmail.com
- Phone: 08065440075

---

**Made with Flask, Python, and lots of timezone math! 🕐🌍**
