#!/bin/bash
# Android WebView App Icon Generator - Unix Script
# This script generates all required app icons from a single logo.png

echo "=========================================="
echo "  Android WebView App Icon Generator"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

# Check if Pillow is installed
if ! python3 -c "import PIL" &> /dev/null; then
    echo "Installing Pillow (image processing library)..."
    pip3 install Pillow
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install Pillow"
        echo "Please run: pip3 install Pillow"
        exit 1
    fi
fi

# Run the icon generator
echo "Generating icons..."
python3 assets/generate_icons.py

echo ""
echo "Done!"
