# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is from battery Class"

class Engine:
    def engine_info(self):
        return "This is from Engine Class"

class ElectricCar(Battery, Engine):
    pass

car1 = ElectricCar()
print(car1.engine_info())
print(car1.battery_info())