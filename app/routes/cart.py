from flask import Blueprint, render_template

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/cart")
def cart_view():
    return "<h1>Carrito (en construcción)</h1>"
