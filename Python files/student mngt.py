class Student:
    def displayInfo(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.regNo}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

    def isFinalYear(self):
        return self.year >= 3

def main():
    student1 = Student()
    student2 = Student()

    student1.name ="Sarah"
    student1.regNo ="S123"
    student1.course ="ICT"
    student1.year = 6


    student2.name ="Felix"
    student2.regNo ="B002"
    student2. course= "CS"
    student2.year =2

    print("Student1 Details: ")
    student1.displayInfo()
    print(f"Final Yeaar: {student1.isFinalYear()}")

    print("Student2 Details: ")
    student2.displayInfo()
    print(f"Final Year: {student2.isFinalYear()}")

if __name__ == "__main__":
    main()
