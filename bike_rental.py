import json
import datetime
import smtplib

def calculate_cost(rental_duration):
    price = 10 + ((rental_duration-1) * 5)
    print(price)

def save_rental(rental):
    with open('rental.json', 'w') as f:
        json.dump(rent_bike(),f)


def rent_bike(customer_name, rental_duration):
    customer_name = input("Please, enter your name: ")
    rental_duration = int(input("Please enter rental duration: "))
    calculate_cost(rental_duration)
    save_rental()
    
