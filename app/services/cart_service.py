from flask import session

def get_cart():
    return session.get("cart", {})

def add_to_cart(product_id, product):
    cart = get_cart()
    if product_id in cart:
        cart[product_id]["qty"] += 1
    else:
        cart[product_id] = {
            "name": product["name"],
            "price": product["price"],
            "qty": 1
        }
    session["cart"] = cart

def cart_count():
    cart = get_cart()
    return sum(item["qty"] for item in cart.values())

def cart_total():
    cart = get_cart()
    return sum(item["price"] * item["qty"] for item in cart.values())
