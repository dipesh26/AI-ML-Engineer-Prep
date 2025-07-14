# Create a function that takes two numbers as parameters and returns their sum.

def sum_of_two_numbers(num1, num2):
    return num1 + num2

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
sum = sum_of_two_numbers(num1,num2)
print(f"Sum: {sum}")