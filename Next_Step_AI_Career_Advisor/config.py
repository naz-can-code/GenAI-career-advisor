"""
Configuration file for Google Generative AI integration
Loads API credentials from .env file securely
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google Generative AI Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_MODEL = 'gemini-2.5-flash'

# Validate API key is configured
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Get your free key from: https://aistudio.google.com/app/apikey")
