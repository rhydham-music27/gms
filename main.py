# final assembly of app
from src.auth import *
from src.customer import *
from src.inventory import *
from src.sales import *

# creating a user
# Auth.createUser("rhydham mittal","Welcome@2025")
# login in system
user_name = input("enter the user name: ")
password = input("enter the password: ")
# item_name: str,purchased_by, quantity: int, phone_number
if Auth.authenticate(user_name=user_name, password=password):
    while True:
        customer_name = input("enter the name of buyer: ")
        item_name = input("enter the name of item: ")
        quantity = int(input("enter the quantity: "))
        phone_number = int(input("enter the phone_number of buyer: "))
        try:
            Sales.get_order(item_name,customer_name,quantity,phone_number)
        except Exception as e:
            print(e)



else:
    print("Wrong Password")
