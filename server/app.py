from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def original():
    return "yuhuuuuuuu welcome to my backend api application tbh i am so excitedddddddddddddddd yarr so in this we have a few routes to use in the url .. one restaurants .. then restaurants with id thenthe rest are just CRUD operations... have fun!!!!!!!!!!"


@app.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()

    restaurant_dict = restaurants.to_dict()

    response = make_response(jsonify(restaurant_dict), 200)

    return response

@app.route('/restaurants/<int:id>')
def individual_restaurant(id):
    individual = Restaurant.query.filter(Restaurant.id == id).first()

    if not individual:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)

    individual_dict = individual.to_dict()

    response = make_response(jsonify(individual_dict), 200)
    return response





if __name__ =='__main__':
    app.run(port=5555, debug=True)
  


