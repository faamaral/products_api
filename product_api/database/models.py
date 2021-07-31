from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float

database = SQLAlchemy()


class Product(database.Model):
    __tablename__ = 'products'

    id = database.Column('id',database.Integer, primary_key=True)
    name = database.Column('name',database.String(50), nullable=False, index=True)
    description = database.Column('description',database.Text)
    manufacturer = database.Column('manufacturer',database.String(35), nullable=False)
    price = database.Column('price',Float)
    amount = database.Column('amount',database.Integer, nullable=False)

    def __init__(self, name, description, manufacturer, price, amount):
        self.name = name
        self.description = description
        self.manufacturer = manufacturer
        self.price = price
        self.amount = amount

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'manufacturer': self.manufacturer,
            'price': self.price,
            'amount': self.amount
        }

    def __repr__(self):
        return f'<Product -> {self.name}>'
