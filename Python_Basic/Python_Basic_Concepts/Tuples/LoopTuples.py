fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") 

# Loop Through a Tuple
for x in fruits:
    print(x)
print("\n")

# Loop Through the Index Numbers
for x in range(len(fruits)):
    print(fruits[x])
    x = x+1
print("\n")

# Using a While Loop
x = 0
while x < len(fruits):
    print(fruits[x])
    x = x + 1
