inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(invetory, item_name, quantity_sold):
    for item in inventory:
        if item_name == item[0]:
            item[1] = item[1] - quantity_sold