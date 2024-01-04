from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Restaurant, Review
from faker import Faker

faker=Faker()

engine = create_engine("sqlite:///restaurants.db")

Session = sessionmaker(bind=engine)
session = Session()

#Deleting data in the database to allow creation of new records
session.query(Customer).delete()
session.query(Restaurant).delete()
session.query(Review).delete()

def add_data():

    customers=[
        Customer(
            first_name=faker.first_name(), last_name=faker.last_name()
        )
        for _ in range(5)
    ]

    for customer in customers:
        session.add(customer)

    #Creating restaurants
    restaurants=[
        Restaurant(
            name=faker.company(), price=faker.random_int(1,5)
        )
        for _ in range(5)
    ]

    for restaurant in restaurants:
        session.add(restaurant)
    

    reviews=[
        Review(
            customers=faker.random_element(customers) ,restaurants=faker.random_element(restaurants), star_rating=faker.random_int(1,10)
        )
        for _ in range(15)
    ]

    for review in reviews:
        session.add(review)

    # Commit the changes 
    session.commit()    

if __name__ == "__main__":
    add_data()
