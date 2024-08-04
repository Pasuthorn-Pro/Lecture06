animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
first_dog_index = animals.index("dog")
print(f"The first occurrence of 'dog' is at index: {first_dog_index}")

Second_Dog_Index = animals.index("dog", first_dog_index + 1)
print(f"The second occurrence of 'dog' is at index: {Second_Dog_Index}")