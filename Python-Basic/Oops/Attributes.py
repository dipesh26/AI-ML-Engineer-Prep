# Attributes are  the variables that belongs to an object. They store information about the object like name, ages, color, etc...
# Two types of Attributes - 1) Instance Attribute, 2) Class Attribute
# --------------------------------------------------------------------------------------------------------------------------------

#  Instance Attribute
# Defined using "Self" inside the __init__() Function
class Car:
    def __init__(self, brand, color):
        self.brand = brand   #Instance Attribute
        self.color = color   #Instance Attribute

car_1 = Car("Toyota", "Red")
car_2 = Car("Mahindra", "Black") 

print(car_1.brand)
print(car_2.brand)
# -----------------------------------------------------------------------------


# Class Attribute
# Defined outside the __init__() Function, Directly inside the Class.
class Student:

    College_name = "Sage University"     #Class Attributes

    def __init__(self, name, marks):
        self.name = name     #Instance Attribute
        self.marks = marks   #Instance Attribute

student_1 = Student("DIPESH", 96)
student_2 = Student("DEVANG", 78)

print(student_1.College_name)  #Class Attributes Calling
print(student_1.name)          #Instance Attribute Calling