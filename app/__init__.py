from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)

    from app.routes.shop import shop_bp
    app.register_blueprint(shop_bp)

    with app.app_context():
        db.create_all()

    return app
