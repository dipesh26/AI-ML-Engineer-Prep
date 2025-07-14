#  Creating a Class and Object
class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand    #Instance Attribute
        self.model = model    #Instance Attribute
        self.color = color    #Instance Attribute
        self.price = price    #Instance Attribute
    
    def car_info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nColor : {self.color}\nPrice : {self.price}")

car_1 = Car("Toyota","Forturner","White",4000000)
car_2 = Car("Tata","Harrier","Black",3000000)
car_3 = Car("Mahindra","Thar","Black",2600000)

car_1.car_info()
print("---------------")
car_2.car_info()
print("---------------")
car_3.car_info()
print("---------------")