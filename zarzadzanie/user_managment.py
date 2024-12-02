import json
import random
import re
import os

user_data = {}

def add_user(user_data:dict):
    name = str(input("Please enter your name: "))
    pesel = int(input("Please enter your pesel number: "))
    regon = int(input("Please enter your regon number: "))
    nip = int(input("Please enter your nip number: "))
    #def validate_pesel(pesel):
    #def validate_regon(regon):
    #def validate_nip(nip):

    user_data = {
        "name":name,
        "pesel":pesel,
        "regon":regon,
        "nip":nip
    }
    with open("/home/u340456/zarzadzanie/data/users.json", "w") as f:
        json.dump(user_data, f, indent = 4)

add_user(0)

