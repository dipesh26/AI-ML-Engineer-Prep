# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        average = sum / len(self.marks)
        print(f"Average: {average}")

marks = []
stud_name = str(input("Enter your Name: "))
for i in range(1,4):
    mark = int(input(f"Enter Subject {i} Mark : "))
    marks.append(mark)

s1 = Student(stud_name, marks)
s1.avg()