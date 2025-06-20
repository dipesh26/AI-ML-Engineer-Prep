size = 10
for i in range(size):
    print("*")
print("\n")

for i in range(size):
    print("*" * size)
print("\n")

for i in range(size):
    count = size - i
    print("*" * count)
print("\n")

for i in range(size):
    print("*" * (i+1))
print("\n")

for i in range(size):
    count = size - i
    spaces = ' ' * i
    stars = "*" * count
    print(spaces+stars)
print("\n")

for i in range(size):
    count = size - i
    spaces = ' ' * count
    stars = "*" * (i+1)
    print(spaces+stars)
print("\n")

for i in range(size):
    spaces = ' ' * i
    stars = '*' * (2 * (size - i) - 1)
    print(spaces + stars)
print("\n")

for i in range(size):
    count = size - i
    spaces = ' ' * (count-1)
    stars = "*" * (2*i+1)
    print(spaces+stars)
print("\n")