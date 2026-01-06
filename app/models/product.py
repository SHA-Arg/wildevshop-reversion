from app import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # ARS (demo)
    category = db.Column(db.String(80), nullable=False, default="General")
    stock = db.Column(db.Integer, nullable=False, default=10)
    image_url = db.Column(db.String(400), nullable=False)
    description = db.Column(db.Text, nullable=False, default="")
    created_at = db.Column(db.DateTime, default=datetime, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"
