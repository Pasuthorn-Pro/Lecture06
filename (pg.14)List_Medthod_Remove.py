fruit_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruit_with_duplicates:
    fruit_with_duplicates.remove("apple")
print(f"Fruits after remove: {fruit_with_duplicates}")