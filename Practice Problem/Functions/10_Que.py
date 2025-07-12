# Create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter the Number: "))
print(f"Factorial of {num} : {factorial(num)}")