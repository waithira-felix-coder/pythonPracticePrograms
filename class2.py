#variables
age = 20
age =40
name = "fidelis"
print(age, name)

#exercise (check in a patient Smith)
print("")
print(" Exer1 patient details")
name ="John Smith"
age =20
text =" He is a new patient"
print(name, age, text)


#receiving input from the user through terminal
print("")
print(" Input through terminal!!")
name= input("What's your name? ")
print("Hello " + name)


#Type conversion(converts birth year to an int)works through terminal
print("")
print(" No. of years count")
birth_year = input("Enter your birth year: ")
age= 2025 - int(birth_year) #here  PERFECT!!(I converted the string into an integer since we can't subtract a sring from an int in python)
print(age)


#float/int/boolean
##Exercise for a simple calculator
print("")
print(" SimpleCalculator Exercise")
no1 =input("First:")
no2 =input("Second:")
sum = int(no1) + int(no2)#converted the strings 1st &2nd into integers , if we worked with them as strings the o/p=First(4)Second(3) =43
print(sum)
#sum = float(no1) + float(no2)# also correct for adding floats or float to int.
#print("Sum: " + str(sum))


#strings
course = 'Python for beginners'
print(course.upper()) #returns the str in uppercase 
print(course) #retuns the normal str
print(course.lower()) #returns thee str in lowercase
print(course.find('t'))#returns the index of the letter 't'=2
print(course.find('for')) #returns the index of word 'for'=7
print(course.replace('for', '4')) #replace the word for with 4
print('Python' in course)# checks whether this str(python) is contained in course


#Arithmetic Operations
print(10 + 3) #addoper.
print(10 - 3)# suboper.
print(10 * 3) #multoper.
print(10 / 3) # divoper.
print(10 // 3) #divoper. does not return reminders==whole number.
print(10 % 3) # returns the reminder of the division
print(10 ** 3) # returns the power of 10 by 3

#Argumented assignmented operator
x = 10
x = x +3 # returns addition
x += 3 #retuns the same answer but using a less code(A.A.O)


#Operator Precedence ==BODMAS
x = 10 + 3 * 2 #=16
x = (10 + 3) * 2 #=26

#Comparison Operators == Boolean Expressions/values
x = 3 > 2#greater than
x = 3>=2
x = 3 < 2 #less than
x = 3 <=2
x = 3 == 2 #equal to
x = 3 != 2
print(x)


#Logical Operators
# and=returns true if both conditions are true. eg 
price =16
print(price >10 and price <30) #=True
# or= returns true if one of the conditions is true
price =5
print(price> 10 or price< 30) #=True coz one condition is true
# not= inverses any value that is given
price=5
print( not price >10) #=True coz it's the inverse.


#If statements
print()
print(" If statements" )    
temp =35
if temp >30:
  print("It's a hot day")
  print("Drink plenty of water.")
  print("")

elif temp> 20:
  print("It's a nice day.")
  print("")

elif temp> 10:
  print("It's a it cold.")
  print("")

else:
  print("It's really cold !!.")
print("Done")
print("")


#Exercise: a weight converter program.
  


