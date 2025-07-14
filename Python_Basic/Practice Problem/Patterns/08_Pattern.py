size = 10
for i in range(size):
    count = size - i
    spaces = ' ' * (count-1)
    stars = "*" * (2*i+1)
    print(spaces+stars)
print("\n")