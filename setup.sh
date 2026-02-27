#!/bin/bash

echo "========================================"
echo "Badawy Timezone Converter - Setup"
echo "========================================"
echo ""

# Setup Backend
echo "Setting up Backend..."
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Backend setup complete!"
cd ..
echo ""

# Setup Frontend
echo "Setting up Frontend..."
cd frontend
npm install
echo "Frontend setup complete!"
cd ..
echo ""

echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To run the application:"
echo "1. Backend (in backend folder): python app.py"
echo "2. Frontend (in frontend folder): npm start"
echo ""
