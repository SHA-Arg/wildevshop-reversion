import products
from flask import Blueprint, render_template
from app.models.product import Product

shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/")
def home():
    return render_template("templates/shop/index.html", products=products)

