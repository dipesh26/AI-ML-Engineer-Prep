# Create a lambda function to compute the cube of a number.

num = int(input("Enter the Number: "))
cube = lambda num: num ** 3
print(f"Cube of \"{num}\": {cube(num)}")