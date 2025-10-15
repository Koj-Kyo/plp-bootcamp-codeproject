"""
Quick start script for TeleHealth Connect
This ensures the app runs with proper context
"""
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        print("✓ Database tables created/verified")

    print("✓ Starting TeleHealth Connect...")
    print("✓ Visit http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
