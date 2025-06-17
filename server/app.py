from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

db.init_app(app)

@app.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()

    restaurant_list = [r.to_dict() for r in restaurants]

    response = make_response(jsonify(restaurant_list), 200)

    return response

if __name__ =='__main__':
    app.run(port=5555, debug=True)
  


