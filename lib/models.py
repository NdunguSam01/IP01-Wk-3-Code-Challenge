from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base=declarative_base()

class Customer(Base):

    __tablename__='customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name=Column(String)
    last_name=Column(String)

    reviews = relationship('Review', back_populates='customers')
    restaurants = relationship('Restaurant',secondary='reviews' ,back_populates='customers',viewonly=True)

    def __repr__(self):
        return f"Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
    
    def review(self):
        return self.reviews
    
    def restaurant(self):
        return self.restaurants

class Restaurant(Base):

    __tablename__='restaurants'

    id=Column(Integer(), primary_key=True)
    name=Column(String(55))
    price=Column(Integer())

    reviews = relationship('Review', back_populates='restaurants')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants' ,viewonly=True)

    def __repr__(self):
        return f"Restaurant(id={self.id}, name={self.name}, price={self.price})"

    def review(self):
        return self.reviews
    
    def customer(self):
        return self.customers

class Review(Base):

    __tablename__='reviews'

    review_id=Column(Integer(), primary_key=True, autoincrement=True)
    star_rating=Column(Integer)
    customer_id=Column(Integer(), ForeignKey('customers.id'))
    restaurant_id=Column(Integer(), ForeignKey('restaurants.id'))

    customers = relationship('Customer', back_populates='reviews')
    restaurants = relationship('Restaurant', back_populates='reviews')

    def __repr__(self):
        return f"Review(id={self.review_id}, star_rating={self.star_rating}, restaurant_id={self.restaurant_id}, customer_id={self.customer_id})"
    
    def customer(self):
        return self.customers
    
    def restaurant(self):
        return self.restaurants
