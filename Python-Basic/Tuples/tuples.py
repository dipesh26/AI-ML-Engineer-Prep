tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple)

# Tuple With One Item
# tuple = ('Apple',)
# print(tuple)

# Indexing
print(tuple[1])

# Negative Indexing
print(tuple[-1])

# Range of Indexes
print(tuple[3:6])

# Range of Negative Indexes
print(len(tuple))
print(tuple[-4:-1])

# Check if Item Exists
if "cherry" in tuple:
    print("Yes Cherry is present in this tuple")
else:
    print("no")

# Join Two Tuples
tuple2 = (1,2,3,4,5)
tuple3 = tuple + tuple2
print(tuple3)

# Multiply Tuples
tuple3 = tuple * 2
print(tuple3)