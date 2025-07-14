# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()

for item in items:
    if item in unique_items:
        print(f"Duplicate item: {item}")
        break
    unique_items.add(item)