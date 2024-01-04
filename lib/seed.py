from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Restaurant
from faker import Faker

faker=Faker()

engine = create_engine("sqlite:///restaurants.db")

Session = sessionmaker(bind=engine)
session = Session()

#Deleting data in the database to allow creation of new records
session.query(Customer).delete()


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
        print(restaurant)
        session.add(restaurant)
    # Commit the changes 
    session.commit()

if __name__ == "__main__":
    add_data()
