heros = ["Ironman", "Thor", "Hulk", "Superman", "Spiderman"]
h2 = ["Dr.strange", "Cpt.America", "Black Phanter", "Ant man"]

heros.insert(0, h2[0])
print(heros.index("Thor"))
heros.insert(heros.index("Thor"), h2[1])
print(heros)
heros.remove("Superman")
heros.append("Ant Man")
print(heros)
heros.sort()
print(heros)
heros.reverse()
print(heros)
newheros = heros
newheros[0] = "Wonder Woman"
print(heros)
copyheros = [] + heros
print(copyheros)
copyheros[0] = "Human"
print(heros)
print(copyheros)