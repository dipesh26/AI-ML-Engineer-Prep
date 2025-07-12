# --- List ---
list = [3,6,4,7,6,2,0,1,8,3,7,4,6,5]
list2 = ['Apple','Mango','Banana','Cherry']
list3 = ['Chiku','Orange','MuskMelon','Watermelon']
print("List 1: ",list)
print("List 2: ",list2)
print("List 3: ",list3)
print("\n")

# --- List Methods ---

# .sort() 
# In Ascending Order. 
list.sort()
print(list)

# In Descending Order.
list.sort(reverse=True)
print(list)

# reverse()
list.reverse()
print(list)

# index()
print(list.index(4))

# count()
print(list.count(7))

# copy()
newlist = list.copy()
print(newlist)

# append()
list2.append("Grapes")
print(list2)

# insert()
list2.insert(2,"chiku")
print(list2)

# extend()
list2.extend(list3)
print(list2)

# Concatenating two lists:
print(list2 + list3)