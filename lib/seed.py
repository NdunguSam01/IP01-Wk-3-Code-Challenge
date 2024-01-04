from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer
from faker import Faker

fake=Faker()
engine = create_engine('sqlite:///restaurants.db') 
Base.metadata.bind=engine

Session=sessionmaker(bind=engine)
session=Session()


def add_data():
    
    Samuel_Muigai=Customer(first_name="Samuel", last_name="Muigai")
    session.add(Samuel_Muigai)
    session.commit()

if __name__=='main':
    add_data()
