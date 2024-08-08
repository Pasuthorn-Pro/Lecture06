# List of heroes
heros = ["Ironman", "Thor", "Hulk", "Spiderman"]

# 1. Display Heroes
def display_heroes():
    for hero in heros:
        print(hero)

# 2. Add Hero
def add_hero(hero):
    heros.append(hero)
    print(f"{hero} has been added to the list.")

# 3. Insert Hero at specific position
def insert_hero(index, hero):
    heros.insert(index, hero)
    print(f"{hero} has been inserted at position {index}.")

# 4. Remove Hero
def remove_hero(hero):
    if hero in heros:
        heros.remove(hero)
        print(f"{hero} has been removed from the list.")
    else:
        print(f"{hero} is not in the list.")

# 5. Display Sorted Heroes (Ascending/Descending)
def display_sorted_heroes(order="ascending"):
    if order.lower() == "ascending":
        sorted_heroes = sorted(heros)
    elif order.lower() == "descending":
        sorted_heroes = sorted(heros, reverse=True)
    else:
        print("Invalid order specified. Please choose 'ascending' or 'descending'.")
        return

    print(f"Heroes List ({order.capitalize()}):")
    for hero in sorted_heroes:
        print(hero)


display_heroes()
add_hero("Captain America")
insert_hero(1, "Black Panther")
remove_hero("Thor")
display_sorted_heroes("ascending")
display_sorted_heroes("descending")