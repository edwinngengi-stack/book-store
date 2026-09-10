@app.route('/api/setup-database-xyz')
def setup_database_xyz():
    from app import db  # Adjust this import to match how your app imports the db instance
    try:
        db.create_all()
        return "Database tables built successfully!", 200
    except Exception as e:
        return f"Error building database: {str(e)}", 500
