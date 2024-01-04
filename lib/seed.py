from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer
from faker import Faker

faker=Faker()

engine = create_engine("sqlite:///restaurants.db")

Session = sessionmaker(bind=engine)
session = Session()

#Deleting data in the database to allow creation of new records
session.query(Customer).delete()


def add_customers():

    customers=[
        Customer(
            first_name=faker.first_name(), last_name=faker.last_name()
        )
        for _ in range(5)
    ]

    for customer in customers:
        session.add(customer)

    # Commit the changes 
    session.commit()

if __name__ == "__main__":
    add_customers()
