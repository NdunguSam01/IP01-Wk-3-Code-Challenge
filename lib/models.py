from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base=declarative_base()

class Customer(Base):

    __tablename__='customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name=Column(String)
    last_name=Column(String)

    reviews = relationship('Review', back_populates='customers')
    restaurants = relationship('Restaurant',secondary='reviews' ,back_populates='customers')

    def __repr__(self):
        return f"Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
    
    def review(self):
        return self.reviews
    
    def restaurant(self):
        return self.restaurants
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        ratings=[]
        if self.reviews:
            customer_reviews=self.review()
            for review in customer_reviews:
                ratings.append(review.star_rating)

            return max(ratings)
        
    def add_review(self, restaurant, star_rating):
        new_review=Review(customer_id=self.id, restaurant_id=restaurant, star_rating=star_rating)
        self.reviews.append(new_review)
        return new_review

    def delete_review(self, restaurant, session): #Passing in the session in order to delete the rows from the table
        deleted_reviews=[review for review in self.reviews if review.restaurants == restaurant]

        for review in deleted_reviews:
            session.delete(review)

        session.commit()
        session.refresh(self)
        
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
    
    @classmethod
    def fanciest_restaurant(cls, session):
        fanciest_restaurants=session.query(cls).order_by(cls.price.desc()).first()
        return (f"The fanciest restaurant in {fanciest_restaurants.name} with a price of ${fanciest_restaurants.price}")

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]
    
    
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

    def full_review(self):
        return (f"Review for {self.restaurants.name} by {self.customers.full_name()}: {self.star_rating} stars.")