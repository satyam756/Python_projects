# Object Oriented Programming in python 
# capitalize class-name
    # brand = None
    # model = None
    # __init__(self,args) constructor 
    # self - context


class Car:
    
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand # 2 __ private
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description(): # self is not required as object will not call only throw class
        return "Cars are Amazing means of transport"
    @property
    def model(self):
        return self.__model

# ElectricCar class

class ElecticCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElecticCar("Tesla","Model S", "85KWH")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElecticCar))
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())


# My_Car = Car("Toyota","Corolla")
# print(My_Car.fuel_type())

# print(Car.total_car)



class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricC(Battery,Engine,Car):
    pass

my_new_tesla = ElectricC("Tesla","Modle S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())












# print(My_Car.brand)
# print(My_Car.model)
# print(My_Car.full_name())

# my_new_car = Car("Tata","Safari")

# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())
