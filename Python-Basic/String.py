# Accessing characters of string
name = "Dipesh"
print(name[3])
print("\n")

# Looping through the string using for loop
names = "Dipesh,Devang"
for character in names:
    print(character)
print("\n")

# Finding length of the String using len() function
fruit = "Mango,Banana"
print("Length of the fruit is: ",len(fruit))
print("\n")

# String Slicing using "variable[]" function
fruits = "Mango,Banana,cheery"
print("Length of the fruits is: ",len(fruits))
print(fruits[1:5]) # positive String Slicing
print(fruits[-15:-9])   # Negative String Slicing
