from src.inventory import *
from src.sales import *
from datetime import datetime

customer_list = []
for customer in pd.read_csv("data/record.csv")["customer_name"]:
    customer_list.append(customer)
# print(customer_list)


def record(customer_name, phone_number):
    with open("data/record.csv", "a") as customer_record:
        customer_record.write(
            "\n{},{},{}".format(
                customer_name,
                datetime.now().strftime("%d/%m/%y-%H:%M:%S"),
                phone_number,
            )
        )


def find(customer):
    if customer in customer_list:
        print(
            "customer found at row number {}".format(customer_list.index(customer) + 1)
        )
    else:
        print("there is no record of any transaction")
