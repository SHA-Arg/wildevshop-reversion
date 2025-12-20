from flask import Blueprint, render_template

shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/")
def home():
    products = []
    return render_template("shop/index.html", products=products)
