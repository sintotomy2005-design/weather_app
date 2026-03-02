import os

class Config:
    # Flask Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    
    # Database Settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Other settings
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY') or 'your_default_weather_api_key'
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'WARNING')