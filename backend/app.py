from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from routes.timezone_routes import timezone_bp
from routes.contact_routes import contact_bp
import os
import sys

# Get the absolute path to the frontend folder
# Support both normal and PyInstaller bundled execution
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # Running as PyInstaller exe
    base_path = sys._MEIPASS
    frontend_folder = os.path.join(base_path, 'frontend')
    print(f"[PyInstaller Mode] Base: {base_path}")
    print(f"[PyInstaller Mode] Frontend: {frontend_folder}")
else:
    # Running as script
    frontend_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
    print(f"[Script Mode] Frontend: {frontend_folder}")

app = Flask(__name__)
CORS(app)

# Register API blueprints FIRST (this handles /api/* routes)
app.register_blueprint(timezone_bp)
app.register_blueprint(contact_bp)

# Set up static folder after blueprints
app.static_folder = frontend_folder
app.static_url_path = '/static'

@app.route('/')
def serve_index():
    """Serve the main index.html"""
    return send_from_directory(frontend_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files and frontend routes"""
    # Try to serve as a file first
    file_path = os.path.join(frontend_folder, path)
    if os.path.isfile(file_path):
        return send_from_directory(frontend_folder, path)
    
    # For all other routes, serve index.html (SPA routing)
    return send_from_directory(frontend_folder, 'index.html')

@app.errorhandler(404)
def not_found(e):
    """Handle 404 - for API routes not found"""
    return jsonify({'error': 'Resource not found'}), 404

if __name__ == '__main__':
    print(f"Serving frontend from: {frontend_folder}")
    print(f"Frontend folder exists: {os.path.exists(frontend_folder)}")
    app.run(debug=True, port=5000, host='127.0.0.1')

