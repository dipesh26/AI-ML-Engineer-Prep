# Given a string, find the first non-repeated character.
string = str(input("Enter the String: "))  # teeter

for char in string:
    if string.count(char) == 1:
        print(f"First Non-repeated character in string: {char}")
        break