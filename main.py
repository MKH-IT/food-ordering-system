"""
NOTES! 
- Order will not be deleted for now. We will show last 20 IN-PROGRESS orders, ordered by earlist creation time. 
- What if there more than 20 IN-PROGRESS orders? No problem.
"""

from collections import defaultdict
import sys
from pprint import pprint
import datetime

from helpers import read_json


def _get_menu() -> dict:
    data = read_json("menu.json")
    return data


def _create_order_ui():
    # Read menu items.
    for meal_id, meal_info in _get_menu().items():
        print(f"{meal_id} ✷ {meal_info["name"]} ✷ {meal_info["price"]}")

    # Get order items from customer.
    order_meals = defaultdict(int)

    while True:
        choice = input("Select the meal (or enter 0 to exit): ")

        if choice == "0":
            break
        
        if choice not in _get_menu():
            print("You selected wrong menu item. Please, repeat!")
            continue
            
        quantity = int(input("Quantity: "))
        order_meals[choice] += quantity

    print("\n")
    print("*** Your order ***")
    total_price = 0
    for order_meal, quantity in order_meals.items():
        meal_name = _get_menu()[order_meal]["name"]
        meal_price = _get_menu()[order_meal]["price"]
        print(f"{meal_name} ✷ Quantity: {quantity} ✷ ${meal_price} per piece")
        price = float(meal_price) * quantity
        total_price += price
        
    print(f"Your total price 💰: ${total_price}")
    print(f"Order creation time ⏰: {datetime.datetime.now()}")

    # Save back to JSON.
    order_id = int(meal_id) + 1
    ...


def _create_order():
    ...


def _update_order():
    ...


def _get_orders():
    ...


def application_menu():
    print("\n")
    print('*** OOO "MKH CENTRE FAST FOOD" ***')
    print("1. Create order")
    print("2. Update order status") 
    print("3. Tablo") 
    print("0. Exit")



def _exit_application():
    sys.exit()


def main():
    application_menu()
    choice = input("Enter: ")
    print("\n")

    routes = {
        "1": _create_order_ui,
        "2": _update_order,
        "3": _get_orders,
        "0": _exit_application,
    }

    try:

        if choice in routes:           
            routes[choice]()
        else:
            print("Wrong input! Please, repeat!")

    except Exception:
        print("Error occured! Please, repeat!")


if __name__ == "__main__":
    while True:
        main()
