#!/bin/bash

# Advanced Heap Operations - Setup Script
# This script sets up the development environment

echo "=========================================="
echo "Advanced Heap Operations - Setup"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to create virtual environment"
    exit 1
fi

echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to activate virtual environment"
    exit 1
fi

echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Verify installation
echo "Verifying installation..."
python3 -c "import matplotlib; import numpy; print('✓ All dependencies verified')"

if [ $? -ne 0 ]; then
    echo "❌ Error: Dependency verification failed"
    exit 1
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To activate the virtual environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run examples:"
echo "  python3 examples/basic_operations.py"
echo "  python3 examples/graph_algorithms.py"
echo ""
echo "To run tests:"
echo "  python3 -m unittest tests.test_fibonacci_heap -v"
echo ""
echo "To deactivate the virtual environment:"
echo "  deactivate"
echo ""


