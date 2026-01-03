from flask import Flask
from app.extensions import db, login_manager
from config import DevelopmentConfig, ProductionConfig
from app.routes.main import main_bp
import os

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(main_bp)

    return app
