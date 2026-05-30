class Person:
    def __init__(self, name):
        self.name = name

    def role(self):
        print("I am a person")

class Lecturer(Person):
    def role(self):
        print("I am a lecturer")

l = Lecturer("Dr. Smith")
l.role()
p = Person("John Doe")
p.role()
