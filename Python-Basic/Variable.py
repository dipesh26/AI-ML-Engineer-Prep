# variables are like a container that stores data values in it.

print("#Variables")
x = 5            # x is variable which storing the value. 
y = "Dipesh"     # y is variable which storing the value.  
print(x)
print(y)
print("\n")

# variable do not need to be declared with any paticular data type, and can even change type after they have been set.

print("#Do not need paticular data type.")
x = 5            # x is of type int. 
x = "Dipesh"     # y is of type str.  
print(x)
print("\n")

# Casting (if you want to specify the data types)

print("#Casting")
x = int(5)      
y = str("Dipesh")
z = float(3.2)    
print(x)
print(y)
print(z)
print("\n")

# Get the Type (to get the data type of the variable)
# type() function is used to get the data type.
# String value can be declared either by using single('') or double("") quote.

print("#Get the Type & #String value")
x = 5            
y = "Dipesh" 
z = 'Dipesh'
print(type(x))
print(type(y))
print(type(z))
print("\n")

# Case-Sensitive (Variables are case sensitive.)

print("#Case-Sensitive")
a = 5
A = "Dipesh"
print(a)
print(A)
print("\n")

# values to Multiples variables in one line.

print("#Multiples variables in one line")
x,y,z = "Orange", "Banana", "Cherry"
print("x = "+ x)
print("y = "+ y)
print("z = "+ z)
print("\n")

# Same values to Multiples variables in one line.

print("#Same values to Multiples variables in one line")
x = y = z = "Orange"
print("x = "+ x)
print("y = "+ y)
print("z = "+ z)
print("\n")

# Unpack Collection (If you have a list or tuple, you can extract the values into variable.)

print("#Unpack Collection")
fruits = ["Orange", "Banana", "Cherry"]
x,y,z = fruits
print("x = "+ x)
print("y = "+ y)
print("z = "+ z)
print("\n")