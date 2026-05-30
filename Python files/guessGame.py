import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = int(input("Take a guess: ")) 
      
        if user_guess.lower() == "hint":
            if number_to_guess % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")
            continue

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input! Please enter a number or type 'hint' for a hint.")
            continue


        attempts += 1

        if user_guess < number_to_guess:
            if number_to_guess - user_guess <= 10:
                print("You're getting warm! Try a higher number.")
            else:
                print("Too low! Try a higher number.")

        elif user_guess > number_to_guess:
            if user_guess - number_to_guess <= 10:
                print("You're getting warm! Try a lower number.")
            else:
                print("Too high! Try a lower number.")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
guessing_game()        

