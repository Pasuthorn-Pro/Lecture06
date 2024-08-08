inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(invetory, item_name, quantity_sold):
    for item in inventory:
        if item_name == item[0]:
            item[1] = item[1] - quantity_sold

def calculate_total_value(inventory):
    total_value = 0
    for item in inventory:
        total_value += item["quantity"] * item["unit_price"]
    
    total_value = calculate_total_value(inventory)
    return total_value

def find_most_expensive(inventory):
    if not inventory:
        return None
    highest_price = 0

    for item in inventory:
        item_price = item["quantity"] * item["unit_price"]
        if item_price > highest_price:
            highest_price = item_price
            most_expensive_item = item["item"]

    return most_expensive_item

