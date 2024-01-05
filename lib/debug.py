#!/usr/bin/env python3

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Restaurant, Review

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine("sqlite:///restaurants.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    #Review customer: Returning the customer instance for a review
    print("\nReview customer: Returning the customer instance for a review")
    for reviews in session.query(Review).all():
        customer=reviews.customer()
        print(f"Customer name: {customer.first_name} {customer.last_name}\n")

    #Review restaurant: Returning the restaurant instance for a review
    print("\nReview restaurant: Returning the restaurant instance for a review")
    for reviews in session.query(Review).all():
        restaurant=reviews.restaurant()
        print(f"Restaurant name: {restaurant.name}\n")

    #Restaurant reviews: Returning a collection of all the reviews for the Restaurant
    restaurants=session.query(Restaurant).all()
    print("\nReturning a list of all restaurants and their reviews\n")
    for restaurant in restaurants:
        reviews=restaurant.review()
        print(f"Restaurant name:{restaurant.name}")
        for review in reviews:
            print(f"Review ID:{review.review_id} \nStar rating:{review.star_rating}\n")


    #Restaurant customers: Returning a collection of all the customers who reviewed the Restaurant
    restaurants=session.query(Restaurant).all()
    print("\nReturning a collection of all the customers who reviewed the Restaurant")
    for restaurant in restaurants:
        print(f"\nCustomers who reviewed {restaurant.name}:")
        all_customers=restaurant.customer()
        for customer in all_customers:
            print(f"{customer.first_name} {customer.last_name}")

    #Customer reviews: Returns a collection of all the reviews that the customer has left
    customers=session.query(Customer).all()
    print("\nReturning a collection of all the reviews that the customer has left")
    for customer in customers:
        print(f"\n{customer.first_name} {customer.last_name} has lef the following reviews:")
        for review in customer.review():
            print(f"Restaurant name: {review.restaurant().name} \nStar rating:{review.star_rating}\n")

    #Customer restauurants: Returns a collection of all the restaurants that the customer has reviewed
    customers=session.query(Customer).all()
    print("\nReturning a collection of all the restaurants that the customer has reviewed")
    for customer in customers:
        print(f"\n{customer.first_name} {customer.last_name} has reviewed the following restaurants:")
        for restaurant in customer.restaurant():
            print(f"{restaurant.name}")
