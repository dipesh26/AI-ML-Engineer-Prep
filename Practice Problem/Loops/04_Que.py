# Reverse a string using a loop.
string = str(input("Enter the String: "))
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed String: {reversed_string}")