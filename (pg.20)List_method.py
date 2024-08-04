heros = ["Ironman", "Thor", "Hulk", "Superman", "Spiderman"]
h2 = ["Dr.strange", "Cpt.America", "Black Phanter", "Ant man"]

heros.insert(0, h2[0])
print(heros.index("Thor"))
heros.insert(heros.index("Thor"), h2[1])
print(heros)