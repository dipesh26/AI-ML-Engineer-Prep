# Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def format(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

format(
    Name = str(input("Enter the Name: ")),
    Middle_Name = str(input("Enter the Middle Name: ")),
    Surname = str(input("Enter the Surname: "))
)