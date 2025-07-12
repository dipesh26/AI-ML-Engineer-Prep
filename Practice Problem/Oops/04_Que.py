# Define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role : {self.role}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",45000)

e1 = Engineer("Dipesh",22)  
print(f"Name : {e1.name}")
print(f"Age : {e1.age}")
e1.showDetails()