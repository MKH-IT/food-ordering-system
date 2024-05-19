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

MAX_ORDERS_CAN_BE_HANDLED = 12
MENU_ITEM_ORDER_LIMIT = 50


def print_application_menu() -> None:
    print('\n*** OOO "MKH IT PARK CAFE" ***')
    print("1. Create order")
    print("2. Update order status") 
    print("3. Tablo") 
    print("0. Exit")


def get_menu() -> dict:
    """
    Read menu items from JSON file.
    """
    data = read_json("menu.json")
    return data


def get_orders() -> dict:
    """
    Read orders from JSON file.
    """
    data = read_json("orders.json")
    return data


def print_menu_items() -> None:
    menu = get_menu()

    print("\n*** Menu ***")
    print("-" * 30)
    for meal_id, meal_info in menu.items():
        print(f"{meal_id} ✷ {meal_info["name"]} ✷ {meal_info["price"]}")
    print("-" * 30)


def _create_order_ui() -> None:
    """
    Print items to screen. Select items.
    Print cheque.
    Update tablo.
    """
    menu = get_menu()
    print_menu_items()
    order_meals = _get_order_meals(menu)

    print("\n*** Your order ***")
    total_price = 0
    for order_meal, quantity in order_meals.items():
        meal_name = menu[order_meal]["name"]
        meal_price = menu[order_meal]["price"]
        print(f"{meal_name} ✷ Quantity: {quantity} ✷ ${meal_price} per piece")
        price = float(meal_price) * quantity
        total_price += price

    total_price = round(total_price, 2)
        
    print(f"Your total price 💰: ${total_price}")
    print(f"Order creation time ⏰: {datetime.datetime.now()}")

    # Print cheque.
    _generate_cheque(order_meals, total_price)

    # Save order to JSON.
    order_id = _create_order(order_meals, total_price)

    if not order_id:
        return

    # Place order to tablo.
    _update_tablo(order_id, "In progress")
    print(f"\n*** Thank you! *** \nYour order number is {order_id}.")


def _get_order_meals(menu: dict):
    order_meals = defaultdict(int)

    while True:
        choice = input("Select the meal (or enter 0 to exit): ")

        if choice == "0":
            break
        
        if choice not in menu:
            print("You selected wrong menu item. Please, repeat!")
            continue
            
        quantity = int(input("Quantity: "))

        if order_meals[choice] + quantity > MENU_ITEM_ORDER_LIMIT:
            print(f"Sorry, you can order only {MENU_ITEM_ORDER_LIMIT} items at once. Please, repeat!")
            continue

        order_meals[choice] += quantity

        # Remove meal from order if quantity is 0 or less.
        if order_meals[choice] <= 0:
            del order_meals[choice]
    
    return order_meals



def _generate_cheque(order_meals: dict, total_price: float) -> None:
    ...


def _update_tablo(order_id: int, status: str) -> None:
    ...


def _create_order(order_meals: dict, total_price: float) -> int:
    """
    Generate order ID, save order to JSON and return order ID.
    """

    orders = get_orders()
    new_order_id = _generate_order_id(orders)

    if new_order_id == 0:
        print("Sorry, we cannot accept more orders now. Please, try later.")
        return
    
    order_item = {
        "status": "In progress",
        "creation_time": str(datetime.datetime.now()),
        "cost": total_price,
        "meals": {
            meal_id: quantity for meal_id, quantity in order_meals.items()
        }
    }
    orders[str(new_order_id)] = order_item
    write_json(orders, "orders.json")

    return new_order_id


def _generate_order_id(orders: dict) -> int:
    """
    Generate order ID
    """
    
    last_order_id = 1 if not orders else max(orders.keys(), key=int)
    new_order_id = int(last_order_id) + 1

    if new_order_id >= MAX_ORDERS_CAN_BE_HANDLED:
        order_id_ = 1
        while order_id_ <= MAX_ORDERS_CAN_BE_HANDLED:
            if orders[str(order_id_)]["status"] == "Ready":
                new_order_id = order_id_
                break
            order_id_ = order_id_ + 1
        else:
            new_order_id = 0

    return new_order_id


def _update_order_status_ui():
    """
    Update order status. Remove order from JSON.
    """
    orders = get_orders()

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

    # Update tablo.
    _update_tablo(int(order_id), "Ready")
    

def _get_orders_ui():
    orders = get_orders()

    if not orders:
        print("No orders to show.")
        return
    
    print("\n*** Orders ***")
    for order_id, order_info in orders.items():
        print(f"{order_id} ✷ {order_info['status']} ✷ {order_info['creation_time']} ✷ ${order_info['cost']}")


def _exit_application():
    sys.exit()


def main():
    print_application_menu()
    choice = input("Enter: ")

    routes = {
        "1": _create_order_ui,
        "2": _update_order_status_ui,
        "3": _get_orders_ui,
        "0": _exit_application,
    }

    # try:

    if choice in routes:           
        routes[choice]()
    else:
        print("Wrong input! Please, repeat!")

    # except Exception:
    #     print("Error occured! Please, repeat!")


if __name__ == "__main__":
    while True:
        main()
