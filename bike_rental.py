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
    with open(report_file, "w") as f:
        json.dump(rentals, f, indent=4)
    print(f"Daily report generated: {report_file}")

def send_rental_invoice_email(customer_email:str, rental_details:dict):
    from email.mime.text import MIMEText
    try:
        message = MIMETEXT(f"Thank you for renting a bike \n\n Details: {rental_details}")
        message['Subject'] = "Bike rental invoice"
        message['To'] = customer_email
        message['From'] = "email@email.com"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("mail wprowdz", "a tu haslo")
            server.send_message(message)

    except Exception as e:
        print(f"Failed to send email: {e}")
