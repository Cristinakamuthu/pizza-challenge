from flask import Flask, jsonify, make_response, request
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

    restaurant_dict = [restaurant.to_dict() for restaurant in restaurants]

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

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    deleted = Restaurant.query.filter(Restaurant.id == id).first()

    if deleted == None:
        response_body = {
            "message": "Restaurant not found."
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else:
        db.session.delete(deleted)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": " Restaurant deleted successfully!"
        }

        response = make_response(jsonify(response_body), 200)
        return response
    
@app.route('/pizzas')
def get_pizza():
    pizza = Pizza.query.all()

    pizza_dict = [pizz.to_dict() for pizz in pizza ]

    response = make_response(jsonify(pizza_dict), 200)

    return response

@app.route('/restaurantpizzas',method = ['GET','POST'])
def post_restaurantpizzas():

    if request.method == 'GET':
        restaurantpizza = []
        for restaurantspizza in RestaurantPizza.query.all():
            restaurantpizza_dict = restaurantspizza.to_dict()
            restaurantpizza.append(restaurantpizza_dict)

            response = make_response(restaurantpizza,200)

            return response
        else:
            request.method == 'POST':
            new_restaurantpizza = RestaurantPizza(
                price = request.form.get("price")
                restaurant_id= request.form.get("restaurant_id")
                pizza_id = request.form.get("pizza_id")
            )

            db.session.add(new_restaurantpizza)
            db.session.commit()

            new_restaurantpizza_dict = new_restaurantpizza.to_dict()

            response = make_response(new_restaurantpizza_dict, 201)

            return response





if __name__ == '__main__':
    app.run(port=5555, debug=True)
