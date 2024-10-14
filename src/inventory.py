import pandas as pd

inventory = pd.read_csv("data/inventory.csv")
item_list = []

for i in inventory["item name"]:
    item_list.append(i)


class Inventory:

    def addItems(item_name, item_price, stock):
        global inventory, item_list
        if item_name in item_list:
            print("item exists")
            return False
        else:
            with open("data/inventory.csv", "a") as inventory:
                inventory.write("\n{},{},{}".format(item_name, item_price, stock))
            return True

    def addStock(item_name, stock_number):
        global item_list, inventory
        if item_name in item_list:
            print("item found")
            print(int(inventory["stock"][item_list.index(item_name)]) + stock_number)
            inventory.at[item_list.index(item_name), "stock"] = (
                int(inventory["stock"][item_list.index(item_name)]) + stock_number
            )
            return True
        else:
            print("item not found")

    def deleteItems(item_name):
        if item_name in item_list:
            print("item found")
            inventory.drop(index=item_list.index(item_name))
            print(inventory)
            return True
        else:
            print("item not found")
            return False


def update():
    inventory.to_csv("data/inventory.csv", index=False)


if __name__ == "__main__":
    print(inventory)
