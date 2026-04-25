#!/bin/bash

# Start Web Interface for Advanced Heap Operations

echo "=========================================="
echo "Advanced Heap Operations - Web Interface"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found!"
    echo "Please run ./setup.sh first to set up the environment."
    echo ""
    read -p "Would you like to run setup now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ./setup.sh
    else
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to activate virtual environment"
    exit 1
fi

# Check if Flask is installed
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Flask not found. Installing..."
    pip install flask
fi

echo ""
echo "Starting web server..."
echo "=========================================="
echo ""
echo "🌐 Web interface will be available at:"
echo "   http://localhost:5000"
echo ""
echo "📝 Features:"
echo "   • Run example programs"
echo "   • Interactive Python console"
echo "   • View heap information"
echo "   • Run unit tests"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Start the Flask app
cd web_interface
python3 app.py
