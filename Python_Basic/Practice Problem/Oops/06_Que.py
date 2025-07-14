# Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model =  model

car1 = Car("Mahindra","XUV 700")
car2 = Car("Tata","Harrier")
print(car1.brand)
print(car2.model)