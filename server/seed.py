from app import app 
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    db.session.commit()

    r1 = Restaurant(name="Mama's Kitchen", address="123 Food St")
    r2 = Restaurant(name="Pizza Palace", address="456 Dough Rd")
    r3 = Restaurant(name="Tom's Diner", address="789 Sauce Ave")

    
    p1 = Pizza(name="Pepperoni", ingredients="cheese, pepperoni, tomato sauce")
    p2 = Pizza(name="Margherita", ingredients="cheese, tomato, basil")
    p3 = Pizza(name="BBQ Chicken", ingredients="chicken, BBQ sauce, onions")

    db.session.add_all([r1, r2, r3, p1, p2, p3])
    db.session.commit()

    
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=15, restaurant=r2, pizza=p3)
    rp4 = RestaurantPizza(price=8, restaurant=r3, pizza=p1)
    rp5 = RestaurantPizza(price=9, restaurant=r3, pizza=p2)

    db.session.add_all([rp1, rp2, rp3, rp4, rp5])
    db.session.commit()

    print("🌱 Seed data loaded!")
