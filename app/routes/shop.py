from flask import Blueprint, render_template
from app.models.product import Product

shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)
