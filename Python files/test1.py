# class_instance.py
class Dog:
    def __init__(self, name, age):
        self.name = name   #instance attribute
        self.age = age

#create instance
miles = Dog("Miles", 4)
bella = Dog("Bella", 3)

print(miles.name, miles.age)  #Miles 4
print(bella.name, bella.age)  #Bella 3
