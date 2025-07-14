# Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print(f"Name : {self.brand}")
        print(f"Model : {self.model}")

car1 = Car("Mahindra", "XUV 700")
car1.car_info()