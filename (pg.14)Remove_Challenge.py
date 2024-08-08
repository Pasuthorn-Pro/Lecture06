fruit_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
more_fruits = ["apple", "strawberry"]
apple_position = []

for fruit in more_fruits:
    fruit_with_duplicates.append(fruit)

index =0
for fruit in fruit_with_duplicates:
    if fruit == "apple":
        apple_position.append(index)
    index = index + 1

fruit_with_duplicates.pop(apple_position[-1])
fruit_with_duplicates.pop(apple_position[0])

print(f"Fruits after remove: {fruit_with_duplicates}")