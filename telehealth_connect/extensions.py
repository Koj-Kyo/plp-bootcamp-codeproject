"""
Extensions module for TeleHealth Connect
Centralizes Flask extensions to avoid circular imports
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
