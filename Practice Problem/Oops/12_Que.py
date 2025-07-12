# Add a static method to the Car class that returns a general description of a car.

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def car_info(self):
        print(f"Brand : {self.__brand}")
        print(f"Model : {self.model}")

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol and Deisel"
    
    @staticmethod
    def general_description():
        return "This is the General Description of a Car"
    
class ElectricCar(Car):
    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

# car1 = ElectricCar("Mahindra","XUV400 EV","39.4 kWh")
# car2 = Car("Toyota","Fortuner")
# car3 = Car("Tata","Nexon")

# car1.car_info()
# print(f"Battery Size : {car1.battery_size}")
# print(f"Type : {car1.fuel_type()}\n")

# car2.car_info()
# print(f"Type : {car2.fuel_type()}\n")

# print(Car.total_car,"\n")

print(Car.general_description())