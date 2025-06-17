from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-restaurantpizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)

    restaurantpizzas = db.relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    def __repr__(self):
        return f'<Restaurant {self.name} at {self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurantpizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    ingredients = db.Column(db.String)

    restaurantpizzas = db.relationship(
        'RestaurantPizza',
        back_populates='pizza',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    def __repr__(self):
        return f'<Pizza {self.name} contains {self.ingredients}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'

    serialize_rules = ('-restaurant.restaurantpizzas', '-pizza.restaurantpizzas')

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id', ondelete='CASCADE'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id', ondelete='CASCADE'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='restaurantpizzas')
    pizza = db.relationship('Pizza', back_populates='restaurantpizzas')

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='price_between_1_and_30'),
    )

    def __repr__(self):
        return f"<RestaurantPizza ({self.id}) of {self.price}/10>"
