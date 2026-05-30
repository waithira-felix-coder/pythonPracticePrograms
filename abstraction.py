class Student:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print(f"Name: {self.name}, Reg No: {self.reg_no}")

s1 = Student("Alice", "CS001")
s2 = Student("Bob", "CS002")
s3 = Student("Charlie", "CS003")
s1.display()
s2.display()
s3.display()