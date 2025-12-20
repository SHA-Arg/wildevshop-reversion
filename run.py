from app import create_app
from app.routes.cart import cart_bp

app = create_app()
app.register_blueprint(cart_bp)

if __name__ == "__main__":
    app.run(debug=True)
