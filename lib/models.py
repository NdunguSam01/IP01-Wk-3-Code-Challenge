from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine=create_engine("sqlite:///restaurants.db")

Base=declarative_base()

class Customer(Base):

    __tablename__='customers'

    id=Column(Integer(), primary_key=True, autoincrement=True)
    first_name=Column(String(55))
    last_name=Column(String(55))

    def __repr__(self):
        return f"Customer ID: {self.id} \n Customer name: {self.first_name} {self.last_name}"

class Restaurant(Base):

    __tablename__='restaurants'

    id=Column(Integer(), primary_key=True, autoincrement=True)
    name=Column(String(55))
    price=Column(Integer())

class Reviews(Base):

    __tablename__='reviews'

    review_id=Column(Integer(), primary_key=True, autoincrement=True)
    customer_id=Column(Integer(), ForeignKey('customers.id'))
    restaurant_id=Column(Integer(), ForeignKey('restaurants.id'))

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

