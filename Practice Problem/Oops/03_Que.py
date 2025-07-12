# Qs. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

import math

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * (self.r ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
radius = int(input("Enter the radius: "))    
c1 = Circle(radius)
print(f"Area : {c1.area()}")
print(f"Perimeter : {c1.perimeter()}")