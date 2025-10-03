#!/usr/bin/env python3
"""
Quick Start Script for DIGITAL POLICE TG
Run this to start the application quickly
"""

import os
import sys
import subprocess

def check_python():
    """Check if Python 3.7+ is available"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements!")
        print("Please run: pip install -r requirements.txt")
        return False

def start_app():
    """Start the Flask application"""
    print("🚀 Starting DIGITAL POLICE TG...")
    print("🌐 Website will be available at: http://localhost:5000")
    print("📱 Demo accounts available (see README.md)")
    print("\n" + "="*50)
    print("Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    
    try:
        from app import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all files are in the correct location")
        return False
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        return False

def main():
    """Main function"""
    print("🚔 DIGITAL POLICE TG - Quick Start")
    print("="*40)
    
    # Check Python version
    if not check_python():
        return
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        print("Make sure you're in the project directory")
        return
    
    # Check if app.py exists
    if not os.path.exists("app.py"):
        print("❌ app.py not found!")
        print("Make sure you're in the project directory")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Start the application
    start_app()

if __name__ == "__main__":
    main()
