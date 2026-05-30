name = input("Enter your name: ")
mark1= int(input("Enter m1: "))
mark2=int(input("Enter m2: "))
mark3=int(input("Enter m3: "))

total= mark1+mark2+ mark3
average= total / 3.0

print(name)
print( total)
print(average)
if(average>=50):
  print("Congrats,You passed")
else:
  print("You failed!!")
