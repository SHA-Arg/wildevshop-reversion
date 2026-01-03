from flask import Flask
from .extensions import db, login_manager


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)

    @app.route("/")
    def home():
        return "App running"

    return app


