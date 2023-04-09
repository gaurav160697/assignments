import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_food_item(self, name, quantity, price, discount, stock, menu):
        food_item = FoodItem(name, quantity, price, discount, stock)
        menu[food_item.food_id] = food_item
        print(f"{name} added to the menu with food ID: {food_item.food_id}")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock, menu):
        if food_id not in menu:
            print("Food item not found.")
            return
        food_item = menu[food_id]
        food_item.name = name
        food_item.quantity = quantity
        food_item.price = price
        food_item.discount = discount
        food_item.stock = stock
        print(f"{name} updated with food ID: {food_id}")

    def view_food_items(self, menu):
        if not menu:
            print("No food items found.")
            return
        print("Food ID\t\tName\t\tQuantity\tPrice\t\tDiscount\tStock")
        for food_id, food_item in menu.items():
            print(f"{food_id}\t\t{food_item.name}\t\t{food_item.quantity}\t\t{food_item.price}\t\t{food_item.discount}\t\t{food_item.stock}")

    def remove_food_item(self, food_id, menu):
        if food_id not in menu:
            print("Food item not found.")
            return
        menu.pop(food_id)
        print(f"Food item with food ID: {food_id} removed from the menu.")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_new_order(self, menu):
        if not menu:
            print("No food items available.")
            return
        print("List of Food Items")
        print("Food ID\t\tName\t\tQuantity\tPrice\t\tDiscount\tStock")
        for food_id, food_item in menu.items():
            print(f"{food_id}\t\t{food_item.name}\t\t{food_item.quantity}\t\t{food_item.price}\t\t{food_item.discount}\t\t{food_item.stock}")
        order_items = []
        while True:
            food_ids = input("Enter food item IDs to order (separated by comma): ")
            food_ids = [int(food_id) for food_id in food_ids.split(",")]
            for food_id in food_ids:
                if food_id not in menu:
                    print(f"Food item with food ID {food_id} not found in the menu.")
                    continue
                order_items.append(menu[food_id])
            if order_items:
                break
            else:
                print("No valid food item IDs entered.")
        print("Selected Food Items")
        print("Food ID\t\tName\t\tQuantity\tPrice\t\tDiscount\tStock")
        for food_item in order_items:
            print(f"{food_item.food_id}\t\t{food_item.name}\t\t{food_item.quantity}\t
