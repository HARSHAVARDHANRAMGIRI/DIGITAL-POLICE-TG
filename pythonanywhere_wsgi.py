"""
WSGI Configuration for PythonAnywhere Deployment

Instructions:
1. Upload this project to PythonAnywhere
2. Go to Web tab and create a new web app
3. Choose "Manual configuration" and Python 3.10
4. Edit the WSGI configuration file and replace with this content
5. Update YOUR_USERNAME below with your PythonAnywhere username
6. Click Reload to start your app

Your app will be live at: https://YOUR_USERNAME.pythonanywhere.com
"""

import sys
import os

# ===== IMPORTANT: Replace YOUR_USERNAME with your actual PythonAnywhere username =====
project_home = '/home/YOUR_USERNAME/digital-police-tg'

# Add your project directory to sys.path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables for production
os.environ['FLASK_ENV'] = 'production'
os.environ['PYTHONUNBUFFERED'] = '1'

# Import Flask app
from app import app as application

# Optional: Add logging for debugging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Digital Police TG application starting...')