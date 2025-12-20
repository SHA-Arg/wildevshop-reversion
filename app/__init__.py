from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.shop import shop_bp
    app.register_blueprint(shop_bp)

    return app
