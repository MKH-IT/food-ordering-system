"""
NOTES! 
- Order will not be deleted for now. We will show last 20 IN-PROGRESS orders, ordered by earlist creation time. 
- What if there more than 20 IN-PROGRESS orders? No problem.
"""

from collections import defaultdict
import sys
from pprint import pprint
import datetime

from helpers import read_json, write_json

MAX_ORDERS_CAN_BE_HANDLED = 3
MENU_ITEM_ORDER_LIMIT = 20

def _get_menu() -> dict:
    """
    Read menu items from JSON file.
    """
    data = read_json("menu.json")
    return data


def _get_orders() -> dict:
    """
    Read orders from JSON file.
    """
    data = read_json("orders.json")
    return data


def _create_order_ui():
    """
    Order creation presenation layer. Save order.
    Print cheque.
    Update tablo.
    """
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

        if quantity >= MENU_ITEM_ORDER_LIMIT:
            print(f"Sorry, you can order only {MENU_ITEM_ORDER_LIMIT} items at once. Please, repeat!")
            continue

        order_meals[choice] += quantity

    # Remove orders with negative quantities.
    order_meals = {meal_id: quantity for meal_id, quantity in order_meals.items() if quantity > 0}

    print("\n*** Your order ***")
    total_price = 0
    for order_meal, quantity in order_meals.items():
        meal_name = _get_menu()[order_meal]["name"]
        meal_price = _get_menu()[order_meal]["price"]
        print(f"{meal_name} ✷ Quantity: {quantity} ✷ ${meal_price} per piece")
        price = float(meal_price) * quantity
        total_price += price

    total_price = round(total_price, 2)
        
    print(f"Your total price 💰: ${total_price}")
    print(f"Order creation time ⏰: {datetime.datetime.now()}")

    # Save order to JSON.
    _create_order(order_meals, total_price)


def _create_order(order_meals: dict, total_price: float):
    """
    Save order to JSON.
    """
    orders = _get_orders()

    if not orders:
        order_id = 1
    else:
        max_order_id = max(orders.keys(), key=int)
        order_id = int(max_order_id) + 1

        if order_id >= MAX_ORDERS_CAN_BE_HANDLED:
            order_id_ = 1
            while order_id_ <= MAX_ORDERS_CAN_BE_HANDLED:
                if orders[str(order_id_)]["status"] == "Ready":
                    order_id = order_id_
                    break
                order_id_ = order_id_ + 1
            else:
                print("We cannot handle your order. Please, try again later.")
                return

    order_item = {
        "status": "In progress",
        "creation_time": str(datetime.datetime.now()),
        "cost": total_price,
        "meals": {
            meal_id: quantity for meal_id, quantity in order_meals.items()
        }
    }

    # Write order to JSON.
    orders[str(order_id)] = order_item
    write_json(orders, "orders.json")
    print(f"\n*** Thank you! *** \nYour order number is {order_id}.")


def _update_order_status_ui():
    """
    Update order status. Remove order from JSON.
    """
    orders = _get_orders()
    if not orders:
        print("No orders to update.")
        return
    
    order_id = input("Please enter order ID to update to 'Ready': ")

    if order_id not in orders.keys():
        print("You entered wrong order ID. Please, repeat!")
        return
    
    if orders[order_id]["status"] == "Ready":
        print("You cannot update status of Ready order.")
        return

    orders[order_id]["status"] = "Ready"
    
    # Write order to JSON.
    write_json(orders, "orders.json")   
    print(f"Order {order_id} is ready.")
    print("***MUSIC***")
    

def _get_orders_ui():
    orders = _get_orders()

    if not orders:
        print("No orders to show.")
        return
    
    print("\n*** Orders ***")
    for order_id, order_info in orders.items():
        print(f"Order ID: {order_id} ✷ Status: {order_info['status']} ✷ Creation time: {order_info['creation_time']} ✷ Cost: ${order_info['cost']}")


def application_menu():
    print('\n*** OOO "MKH CENTRE FAST FOOD" ***')
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
        "2": _update_order_status_ui,
        "3": _get_orders_ui,
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
