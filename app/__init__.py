from flask import Flask
from app.routes.cart import cart_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "dev-secret"

    app.register_blueprint(cart_bp)

    from app.services.cart_service import cart_count

    @app.context_processor
    def inject_cart():
        return dict(cart_count=cart_count)

    return app
