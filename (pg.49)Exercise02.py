# Initial Inventory
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]
def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            break

def calculate_total_value(inventory):
    total_value = 0
    for item in inventory:
        total_value += item[1] * item[2]
    return total_value

def find_most_expensive(inventory):
    most_expensive_item = inventory[0]
    for item in inventory:
        if item[2] > most_expensive_item[2]:
            most_expensive_item = item
    return most_expensive_item[0]

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            break
    else:
        inventory.append([item_name, quantity, price])


# Action 1: Update inventory after selling 20 bananas
update_inventory(inventory, "Banana", 20)
print(inventory)  # Check inventory after update

# Action 2: Calculate the total value of the inventory
total_value = calculate_total_value(inventory)
print("Total Value:", total_value)

# Action 3: Find the most expensive item
most_expensive = find_most_expensive(inventory)
print("Most Expensive Item:", most_expensive)

# Action 4: Add "Eggs" with 30 units at $0.25, then update it to 50 units at $0.30
add_item(inventory, "Eggs", 30, 0.25)
print(inventory)  # Check inventory after adding Eggs

add_item(inventory, "Eggs", 50, 0.30)
print(inventory)  # Check inventory after updating Eggs