import pandas as pd
from src.inventory import *
from src.customer import *
from src.customer import record

sales = pd.read_csv("data/sales.csv")


# print(sales)
class Sales:
    def get_order(item_name: str,purchased_by, quantity: int, phone_number):
        

        if item_name in item_list:
            if quantity < int(inventory["stock"][item_list.index(item_name)]):

                with open("data/sales.csv", "a") as sale:
                    sale.write(
                        "\n{},{},{},{}".format(
                            item_name,
                            quantity,
                            int(inventory["item price "][item_list.index(item_name)])
                            * quantity,
                            purchased_by,
                        )
                    )
                inventory.at[item_list.index(item_name), "stock"] = int(
                    int(inventory["stock"][item_list.index(item_name)]) - quantity
                )
                record(purchased_by, phone_number)
                update()

            else:
                print("out of stock item")
        else:
            print("item not found")

    def create_receipt(self, item_name: str, quantity: int, purchsed_by, price):
        pass


if __name__ == "__main__":
    Sales.get_order("potato", 4)
