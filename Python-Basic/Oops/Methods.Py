# A Method is a function that is defined inside a class & acts on an objects.

# Instance Method
# Defined inside the class using "def start(self):"
print("# Instance Method")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def stud_info(self):     # Method
        print(f"Name : {self.name}\nMarks : {self.marks}")

s1 = Student("Dipesh",78)
s1.stud_info()
print("-------------------")


# Class Method (Acts on class, not objects)
# Use "@CLassmethod" & "cls" instead of "self"
print("# Class Method")
class Dog:
    species = "Canien"

    @classmethod
    def show_species(cls):
        print(f"Species : {cls.species}")

Dog.show_species()
print("-------------------")

# Static Method (No "Self" or "cls" - like a normal function inside a class)
# Use "@staticmethod"
print("# Static Method")
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
print(f"Sum : {Math.add(4,5)}")
print("-------------------")


# Example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit : {amount}   Balance : {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw : {amount}   Balance : {self.balance}")
        else:
            print("Insufficient Balance!")

account_1 = BankAccount("Dipesh", 30000)
account_1.deposit(1000)
account_1.withdraw(1000)