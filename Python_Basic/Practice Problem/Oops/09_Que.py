# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def car_info(self):
        print(f"Brand : {self.__brand}")
        print(f"Model : {self.model}")

    def get_brand(self):
        return self.__brand
    
class ElectricCar(Car):
    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

car1 = ElectricCar("Mahindra","XUV400 EV","39.4 kWh")
# car1.car_info()
# print(f"Battery Size : {car1.battery_size}")
print(f"Brand : {car1.get_brand()}")