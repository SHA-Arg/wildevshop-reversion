from flask import Blueprint

shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/")
def home():
    return "Wildevshop funcionando ✅"
