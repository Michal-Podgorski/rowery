import json
from datetime import datetime
import smtplib
import os


file_path = "data/remtal.json"

def calculate_cost(rental_duration:int)-> int:
    if rental_duration <=1:
        return 10
    return 10 + ((rental_duration-1) * 5)
    

def save_rental(rental:dict):

    rentals = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            rentals = json.load(f)
    rentals.append(rental)

    with open(file_path, "w") as f:
        json.dump(rentals, f, indent=4)
    


def rent_bike(customer_name, rental_duration):
    cost = calculate_cost(rental_duration)
    rental = {
        "customer_name": customer_name,
        "rental_duration": rental_duration,
        "cost": cost,
        "rental_time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    }
    save_rental(rental)
    return f"Rental: save: {rental}"

def load_rentals()->list:
    if not os.path.exists(file_path):
        print("No rentals found")
        return []
    with open(file_path, "r") as f:
        return json.load(f)


def cancel_rental(customer_name:str):
    rentals = load_rentals()
    update = [r for r in rentals if r["customer_name"] != customer_name]

    if len(rentals) == len(update):
        print(f"No rental found for {customer_name}")
        return 

    with open(file_path, "w") as f:
        json.dump(update, f, indent=4)
        print(f"Rental for {customer_name} has been canceled.")

def generate_daily_report():
    rentals = load_rentals()
    date = datetime.now().strftime("%Y-%m-%d")

    report_file = f"data/daily_report_{date}.json"
