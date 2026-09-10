
import os
from app import create_app, db

# 1. Initialize the Flask application
app = create_app()

# 2. Automatically create all missing database tables on startup
with app.app_context():
    try:
        db.create_all()
        print("Database tables initialized successfully!")
    except Exception as e:
        print(f"Database initialization warning: {e}")

# 3. Boot the application server engine
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
