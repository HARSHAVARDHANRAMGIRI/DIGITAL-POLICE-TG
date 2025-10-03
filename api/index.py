import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app from app.py
from app import app

# Expose the WSGI application for Vercel
application = app

# Serverless function handler for Vercel
def handler(request):
    return app(request.environ, request.start_response)