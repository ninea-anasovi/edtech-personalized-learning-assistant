from flask import Flask
from app.web.routes import main_blueprint
from app.data.firestore_client import FirestoreDB

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    # Initialize Firestore
    FirestoreDB.initialize()

    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)