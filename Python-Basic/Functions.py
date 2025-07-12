# How to define the function.
def my_function():
    print("Hello My name is Dipesh")

my_function()

# Arguments in functions.
def my_function(fname):
    print("Hello " + fname)

my_function("Dipesh")

# Default Arguments
def my_function(country = "India"):
    print("I am from "+country)

my_function("Swedan") 
my_function("Norway") 
my_function() 
my_function("Brazil") 

# Passing a list as an Arguments.
def my_function(food):
    for i in food:
        print(i)

fruits = ['Apple','Banana','Cherry']
my_function(fruits)

# Return Value
def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(4))
print(my_function(5))

# Pass Statement
def my_function():
    pass

# Keywords Arguments
def my_function(*,x,y):
    print(x*y)

my_function(x=3, y=4)