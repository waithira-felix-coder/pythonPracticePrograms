### Strings. I/O and Branching
# String literals
print("Hello, World!")

a= "\nme"
z ='you'
#concatenate the strings #
b = "\nmyself"
c = a +b
d = a + " " + b
silly = a * 3
print(c)
print(d)
print(silly)

### Indexing and Slicing ###
s = "abcde"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

## eg.2 ##
greeting = "\nHello, World!"
print(greeting[0]) #H
print(greeting[7]) #W
print(greeting[-1]) #!
print(greeting[0:5]) #Hello
print(greeting[7:12]) #World!

##Slice and step ##
s = "abcdefgh"
print(s[3:6]) #def
print(s[3:]) #defgh
print(s[3:6:2])#df
print(s[:]) #abcdefgh
print(s[::-1]) #hgfedcba
print(s[4:1:-2]) #aceg

## Input/Output and Branching ##

verb = input ("Enter a verb: ")
print("I can " + verb + " better than you!") #replace verb with user input
print((verb+ ' ')*5) #repeat verb 5 times


##Example: Newton's method for cube root approximation ##
number = float(input("Enter a number: "))
guess = number / 3
while abs(guess**3 - number) >= 0.001:
  guess = (2 * guess + number / (guess ** 2)) / 3
print("The cube root of " + str(number) + " is approximately " + str(guess))


## Example of branching ##
age = int(input("Enter your age: "))
if age < 18:
  print("You are a minor.")
elif age < 65:
  print("You are an adult.")
else:
  print("You are a senior citizen.")

## Example of branching with nested if statements ##
secret = 5
guess = int(input("Guess the secret number: "))
if guess > secret:
  print("Your guess is too high")
elif guess < secret:
  print("Your guess is too low")
elif guess == secret:
  print("Congratulations! You guessed the secret number.")
else:
  print("Sorry, that's not the secret number.")

#equal = (secret == guess)
#print(equal)