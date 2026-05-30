# This prints a text
print("Hello World")
print(5//3)
#This assigns felix with a value Mwangi
felix = "Mwangi"
#This prints the variable type of felix
print(type(felix))
#This deletes the varible felix
del felix


#Conditional logic
print(5==4)
#e.g
Dylan_Age = 20
Adult_Age = 18
print(Dylan_Age >= Adult_Age)

#If statements
Tylan =5
Age_of_kindergerten =5

if Tylan <Age_of_kindergerten:
  print("Tylan should be in pre-school")
elif Tylan == Age_of_kindergerten:
  print("Tylan is in kindergerten")
else:
  print("Tylan should be in another class")


  #Functions
  #functin to print something multiple times
  def print_kevin():
    text = "Kevin has a great channel"
    print(text)
    print(text)
    print(text)
    print_kevin()  

    #same example
  def print_kevin(text):
    print(text)
    print(text)
    print(text)

    print_kevin("Kevin has a great channel!!")  


    #If statements in a function
    def school_age_calculator(age,name):
      if age <5:
        print("Enjoy your time!" ,name, "it's only", age)
      elif age ==5:
        print("Enjoy Kindergerten", name)
      else:
        print("They grew up so fast!")

    school_age_calculator(3, "Thomas")        

    #function to know what age you will be in 10yrs
    def add_ten_to_age(age):
      new_age = age +10
      return new_age
    How_Old_will_I_Be = add_ten_to_age(4)
    print(How_Old_will_I_Be)

    #Loops
    #while loop
    x = 0
    while (x*5):
      print (x)
      x= x+1

      #for loop to print range btw 5&10
      for x in range(5,10):
        print(x)

#for loop to print all days of a week
days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]

for d in days:
  print(d)
  #breaks at Thur
  days =["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]

  for d in days:
    if(d=="Thur"):break #'continue' -this will not print thur
    print(d)

    # access the matyh library
    import math
    print("pi is", math.pi)