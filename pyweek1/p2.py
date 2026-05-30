import csv

num_students = int(input("How many Students? "))

#List to store values
marks =[]

#Accepts inputs
for i in range(num_students):
  mark= int(input("Enter mark: "))
  if mark>=100:
   print("Incorrect input!!")
  else :
    marks.append(mark)
   
total =0
average =0
percentage =0

passes =0
fails  =0

#grading
grade_A =0
grade_B =0
grade_C =0
grade_D =0
grade_F =0

highest = None
lowest = None

#Calculates total, loops through the list,passes the number of students who failed and those who passed
for mark in marks:
  total= total + mark 

  if mark>= 50:
    passes +=1
  else:
    fails +=1 

  if mark >=80:
    grade_A +=1
  elif mark >=70:
    grade_B +=1
  elif mark >=60:
    grade_C +=1
  elif mark >=50:
    grade_D +=1
  else:
    grade_F +=1           

    #Highest logic
  if highest is None or mark > highest:
    highest = mark

  if lowest is None or mark < lowest:
    lowest = mark    

   #Secures data to void unnecessary errors 
if num_students ==0:
  print("No students entered.")
else:
 average = total /num_students

percentage =(passes / num_students) * 100

print("Total: ", total)
print("Average: ", average)  

print("Passes: ",passes)
print("Fails: ",fails)
print("Highest: ",highest)
print("Lowest: ", lowest)
print(f"Pass Percentage: {percentage: .2f}%")
print("A:", grade_A)
print("B:", grade_B)
print("C:", grade_C)
print("D:", grade_D)
print("F:", grade_F)

#Save details to csv file

def save_to_csv(marks):
 with open("Std.csv", "w")as file:
   writer =csv.writer(file)
   writer.writerow(["mark"])
   writer.writerow(["highest", "89"])

   for student in student:
     writer.writerow(["mark"], 0)

   print("Report saved successfully")  

def main():
  save_to_csv(marks)    

if __name__ =="__main__":
  main()
