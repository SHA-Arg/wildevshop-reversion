from flask import Blueprint, redirect, url_for, render_template
from app.services.cart_service import get_cart, cart_total

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

@cart_bp.route("/")
def view():
    return render_template(
        "cart/view.html",
        cart=get_cart(),
        total=cart_total()
    )
