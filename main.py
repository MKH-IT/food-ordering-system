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


def main():
    application_menu()
    choice = int(input("Введите: "))

    if choice == 1:
        ...
    elif choice == 2:
        ...
    elif choice == 3:
        ...
    elif choice == 0:
        ...
    else:
        print("Неверный ввод! Пожалуйста, повторите!")

if __name__ == "__main__":
    while True:
        main()
