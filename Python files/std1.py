# Student Management System with Grades

# List to store student records
students = []

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student_id = input("Enter student ID: ")
    grade = float(input("Enter student grade (0-100): "))
    
    # Determine pass/fail
    status = "Passed" if grade >= 50 else "Failed"
    
    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
        "status": status
    })
    print(f"Student {name} added successfully! Status: {status}\n")

# Function to view all students
def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("Student Records:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, "
              f"Grade: {student['grade']}, Status: {student['status']}")
    print()

# Function to update a student
def update_student():
    student_id = input("Enter the student ID to update: ")
    for student in students:
        if student['id'] == student_id:
            student['name'] = input("Enter new name: ")
            student['age'] = input("Enter new age: ")
            student['grade'] = float(input("Enter new grade (0-100): "))
            student['status'] = "Passed" if student['grade'] >= 50 else "Failed"
            print("Student record updated successfully!\n")
            return
    print("Student ID not found.\n")

# Function to delete a student
def delete_student():
    student_id = input("Enter the student ID to delete: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Student record deleted successfully!\n")
            return
    print("Student ID not found.\n")

# Main menu
def main():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
        main()

