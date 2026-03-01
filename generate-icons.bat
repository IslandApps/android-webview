@echo off
REM Android WebView App Icon Generator - Windows Script
REM This script generates all required app icons from a single logo.png

echo ==========================================
echo   Android WebView App Icon Generator
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if Pillow is installed
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo Installing Pillow (image processing library)...
    pip install Pillow
    if errorlevel 1 (
        echo ERROR: Failed to install Pillow
        echo Please run: pip install Pillow
        pause
        exit /b 1
    )
)

REM Run the icon generator
echo Generating icons...
python assets\generate_icons.py

echo.
echo Done! Press any key to exit...
pause >nul
