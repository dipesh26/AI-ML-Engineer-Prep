# Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for num in range(2, limit + 1):
        if num % 2 == 0:
            yield num

limit = int(input("Enter the number: "))
for i in even_generator(limit):
    print(i)