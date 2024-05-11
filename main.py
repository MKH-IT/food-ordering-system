"""
NOTES! 
- Order will not be deleted for now. We will show last 20 IN-PROGRESS orders, ordered by earlist creation time. 
- What if there more than 20 IN-PROGRESS orders? No problem.
"""

def application_menu():
    print("1. Создать заказ")
    print("2. Обновить статус заказа") 
    print("3. Табло") 
    print("0. Выйти")


def _create_order():
    ...


def _update_order():
    ...


def _get_orders():
    ...


def _exit_application():
    ...


def main():
    application_menu()
    choice = int(input("Введите: "))

    routes = {
        1: _create_order,
        2: _update_order,
        3: _get_orders,
        0: _exit_application,
    }

    try:

        if choice in routes:           
            routes.get(choice)
        else:
            print("Неправильный ввод! Пожалуйста, повторите!")

    except:
        print("Возникла ошибка! Пожалуйста, повторите!")

if __name__ == "__main__":
    while True:
        main()
