# food-ordering-system
Food ordering system in Python | Get order → print cheque as PDF file → see order status on separate HTML page.


## How do we save menu items?
- `menu.json` file is used to store menu items.
    ```
    {
        "#1": {
            "name": "Pizza",
            "price": "$2",
            "description": "..."
        },
        "#2": {
            "name": "Burger",
            "price": "$2",
            "description": "..."
        }
    }
    ```

## How do we save order info? 
- `orders.json` file is used to store order info.
    ```
    {
        "#1": {
            "status": "In progress",
            "creation_time": "...",
            "cost": "$45",
            "meals": ["#1", "#2"]
        },
        "#2": {
            "status": "In progress",
            "creation_time": "...",
            "cost": "$45",
            "meals": ["#1", "#2"]
        }
    }
    ```