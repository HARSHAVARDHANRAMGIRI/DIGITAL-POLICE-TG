"""
Vercel Serverless Function Entry Point
This file is required for Vercel to properly deploy Flask applications
"""
import sys
import os

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel serverless function handler
app = app