#!/bin/bash

echo "=== Building Mac Executable ==="

# Check if icon.png exists
if [ ! -f "icon.png" ]; then
    echo "❌ Error: icon.png not found!"
    echo "Please add your icon.png file to this directory."
    exit 1
fi

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Run the build script
echo "Building executable..."
python3 build_mac.py

echo "Build process completed!" 