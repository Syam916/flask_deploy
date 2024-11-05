# app/__init__.py
from flask import Flask
from .routes import main
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")
    app.config['DB_HOST'] = os.getenv("DB_HOST")
    app.config['DB_USER'] = os.getenv("DB_USER")
    app.config['DB_PASSWORD'] = os.getenv("DB_PASSWORD")
    app.config['DB_NAME'] = os.getenv("DB_NAME")
    
    app.register_blueprint(main)
    return app
