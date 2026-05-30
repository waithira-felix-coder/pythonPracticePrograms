import random

while True:
 choice = input('Roll the dice? (y/n):').lower()
 if choice == 'y': 
    die1 = random.randint(1,6)
    die2 = random.randint(1,3)
    print(f'({die1}, {die2})')
 elif choice =='n':
    print('Thanks for Playing!')
    break
 else:
   print('Invalid Choice!!')
 #If user enters y
 #  Generate two random numbers
 #    Print them
 #If user enters n
 #    Print thankyou message
 #    Terminate
 # Else
 #     Print Invalid choice   