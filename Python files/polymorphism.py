# Base class
class Car:

 def __init__(self, model):
     self.model = model
def accelerate(self):
    print(f"{self.model} is accelerating in a general way.")
# Subclass 1
class SportsCar(Car):

 def accelerate(self):
     print(f"{self.model} accelerates like a rocket!")
# Subclass 2
class ElectricCar(Car):
    def accelerate(self):
        print(f"{self.model} accelerates silently and smoothly!")
# Function that demonstrates polymorphism
def test_acceleration(car_object):
    car_object.accelerate()
    # Create different car objects
    generic_car = Car("Generic Car")
    sportscar = SportsCar("Ferrari")
    electric_car = ElectricCar("Tesla Model 3")
# Test polymorphism
test_acceleration(generic_car)
test_acceleration(sportscar)
test_acceleration(electric_car)
