import csv

#List to store values
marks =[]
#List to store details
students =[]


#function to collect input, data collection logic.
def get_students():
  students =[]

  num = int(input("How many students? "))

  for i in range(num):
    name = input("Enter name: ")
    mark = int(input("Enter mark: "))

    student = {
      "name": name,
      "mark": mark
    }

    students.append(student)

  return students  

#Analyze students
def analyze_students(students):
  total =0
  highest =None
  lowest =None
  fails =[]
  passes =[]
  w =[]

  for student in students:
    mark = student['mark']
    total +=mark

    if highest is None or mark > highest["mark"]: # we compare this way coz highest is now a dictionary.
      highest = student

    if lowest is None or mark < lowest["mark"]:
      lowest = student

    if mark < 50:
      fails.append(student["name"])

    else:
      passes.append(student["name"])  


  average = total / len(students)

  return{
    "total": total,
    "average": average,
    "highest": highest,
    "lowest": lowest,
    "fails": fails,
    "passes": passes
  }  

#Print Report 
def print_report(students, stats):
  print("\n---REPORT---")
  print("Total: ", stats["total"])
  print("Average:", stats["average"])

  print("\nTop Performer: ", stats["highest"]["name"], "-", stats["highest"]["mark"])

  print("\nLowest Performer: ", stats["lowest"]["name"], "-", stats["lowest"]["mark"])

  print("Qualified Students: ", stats["passes"])
  print("Failed Students: ", stats["fails"])      


#Save to a text file
def save_to_txt(students):
  with open("Students_report.txt", "w") as file:
    file.write("STUDENT REPORT\n") 
    file.write("======================\n")

    for student in students:
      line = f"{student['name']} - {student['mark']}\n"
      file.write(line)


  print("Report saved to students_report.txt")    

#Save to a csv file
def save_to_csv(students):
  with open("Students_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "mark"]) #header row 

    for student in students:
      writer.writerow([student["name"], student["mark"]])

  print("Report saved to students_report.csv")    

#Main program execution
def main():
  students = get_students()
  stats = analyze_students(students)   
  print_report(students, stats)
  save_to_txt(students)
  save_to_csv(students)

if __name__ == "__main__":
  main()   
