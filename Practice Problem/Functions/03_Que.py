# Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    if a.isdigit() and b.isdigit():
        return int(a) * int(b)
    elif a.isdigit():
        return int(a) * b
    elif b.isdigit():
        return a * int(b)

a = input("Enter 1st value: ") 
b = input("Enter 2nd value: ") 
print(multiply(a, b))