# Compute the factorial of a number using a while loop.
n = int(input("Enter the Number: "))
fact = 1

while n > 0:
    fact = fact * n
    n = n -1
print(f"Factorial: {fact}")