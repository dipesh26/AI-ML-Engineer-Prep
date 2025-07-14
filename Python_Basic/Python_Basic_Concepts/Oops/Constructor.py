# All Classes have a function called __init__(), which is always executed when the object is being initiated.

# Creating a class
class Student:
    # __init__() Function
    def __init__(self, name, marks):   #Constructor
        self.name = name       #Instance Attribute
        self.marks = marks     #Instance Attribute
    
    def stud_info(self):
        print(f"Name : {self.name}\nMarks : {self.marks}")

# Creating a Object
student_1 = Student("Dipesh",89)   #Object 1
student_2 = Student("Devang",56)   #Object 2

student_1.stud_info()
print("---------------")
student_2.stud_info()
