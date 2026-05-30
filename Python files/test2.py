# class_instance.py
class Employee:
      company = "TechCorp"   #class attribute
      def __init__(self, name):
         self.name = name  #instance attribute

a = Employee("Alice")
b = Employee("Bob")

print(a.name, a.company)     #Alice TechCorp
print(b.name, b.company)     #Bob TechCorp

# change class attribute 
Employee.company ="NewC0"
print(a.company, b.company)   #NewCo  NewCo
