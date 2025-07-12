size = 10
for i in range(size):
    spaces = ' ' * i
    stars = '*' * (2 * (size - i) - 1)
    print(spaces + stars)
print("\n")