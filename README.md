# food-ordering-system
Food ordering system in Python | Get order → print cheque as PDF file → see order status on separate HTML page.


## How do we save menu items?
- `menu.json` file is used to store menu items.
    ```
    {
        "1": {
            "name": "🍕 Pizza",
            "price": "9.90"
        },
        "2": {
            "name": "🍔 Burger",
            "price": "5.90"
        },
        "3": {
            "name": "🌭 Hot-dog",
            "price": "3.00"
        }
    }
    ```

## How do we save order info? 
- `orders.json` file is used to store order info.
    ```
    {
        "1": {
            "status": "In progress",
            "creation_time": "...",
            "cost": "$45",
            "meals": {
                "1": 2,
                "2": 1
            }
        },
        "2": {
            "status": "Ready",
            "creation_time": "...",
            "cost": "$45",
            "meals": {
                "1": 2,
                "2": 1
            }
        }
    }
    ```