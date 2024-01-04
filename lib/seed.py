from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer
from faker import Faker

fake=Faker()

if __name__=='main':
    engine=create_engine("sqlite:///restaurants.db")

    Session=sessionmaker(bind=engine)
    session=Session()

    customers=[
        Customer(
            first_name=fake.name(),
            last_name=fake.name()
        )
        for _ in range(5)
    ]

    session.bulk_save_objects(customers)
    session.commit()