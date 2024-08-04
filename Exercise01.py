def Heroes():
    heros = ["Ironman", "Thor", "Hulk", "Spiderman"]
    print(heros)

    heros.append("Captain America")
    print(heros)

    index_heros = 5
    heros.insert(index_heros, "Hawkeye")
    print(heros)

    heros.remove("Hawkeye")
    print(heros)

    heros.sort()
    print(heros)

    heros.reverse()
    print(heros)
    
Heroes()