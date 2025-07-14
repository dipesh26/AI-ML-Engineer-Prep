# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print(f"Name : {self.brand}")
        print(f"Model : {self.model}")
    
class ElectricCar(Car):
    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

car1 = ElectricCar("Mahindra","XUV400 EV","39.4 kWh")
car1.car_info()
print(f"Battery Size : {car1.battery_size}")