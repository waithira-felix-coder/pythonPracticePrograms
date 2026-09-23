 
#This method is significantly simpler than trying to find the largest number all at once, by comparing all possible pairs of numbers (i.e., first with second, second with third, third with first). Try to rebuild the code for yourself.




#read three numbers
num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#We temporarily assume that the first number is the largest
largest_number = num1

#compare the second number with the largest number and update the largest number if necessary
if num2 > largest_number:
  largest_number = num2

#compare the third number with the largest number and update the largest number if necessary
if num3 > largest_number:
  largest_number = num3

#Display the largest number
print("The largest number is: ", largest_number)



#Python often comes with a lot of built-in functions that will do the work for you. For example, to find the largest number of all, you can use a Python built-in function called 'max()' or use 'min()' to return the lowest number. You can use it with multiple arguments.

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the lowest_number variable.

lowest_number = min(number1, number2, number3)

# Print the result.
print("The lowest number is:", lowest_number)

