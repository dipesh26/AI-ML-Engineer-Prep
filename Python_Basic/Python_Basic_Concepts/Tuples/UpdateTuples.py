# You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Change Tuple Values
x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")   # tuple
print("--Change Tuple Values--")
print(type(x),x)

temp = list(x)    # Convert the tuple into a list.
print(type(temp),temp)

temp[2] = "WaterMelon"    # Change the value of list at index [2] to "WaterMelon".
print(type(temp),temp)

x = tuple(temp)    # Convert the list back into a tuple.
print(type(x),x)
print("\n")


# Add Items
print("--Add Items--")
temp = list(x)
print(type(temp),temp)

temp.append("cherry")
print(type(temp),temp)

x = tuple(temp)
print(type(x),x)
print("\n")


# Remove Items
print("--Remove Items--")
temp = list(x)
print(type(temp),temp)

temp.remove('kiwi')
print(type(temp),temp)

x = tuple(temp)
print(type(x),x)
print("\n")


# pop Items
print("--pop Items--")
temp = list(x)
print(type(temp),temp)

temp.pop(3)
print(type(temp),temp)

x = tuple(temp)
print(type(x),x)