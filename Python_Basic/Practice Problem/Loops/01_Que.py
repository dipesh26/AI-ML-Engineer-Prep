# Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, -10, -11, 12, 13, -14, 15]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
print(f"Count of Positive numbers in list: {positive_number_count}")