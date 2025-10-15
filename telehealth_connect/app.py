"""
TeleHealth Connect - Main Application Module
"""
from flask import Flask
from config import config
from extensions import db, login_manager
import os


def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    # Import models
    from models import patient, doctor, health_center, appointment

    # Register blueprints
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.appointments import appointments_bp
    from routes.doctor import doctor_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(doctor_bp)

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from models.patient import Patient
        return Patient.query.get(int(user_id))

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, host='0.0.0.0', port=5000)
