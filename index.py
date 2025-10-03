import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

# This is required for Vercel to find the WSGI application
application = app

# For local development
if __name__ == "__main__":
    app.run()