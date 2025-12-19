import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts < max_attempts:
            
            user_guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1 
            
            if user_guess < secret_number:
                print("Too small! Try to guess a bigger number.")

            elif user_guess > secret_number:
                print("Too big! Try to guess a smaller number.")
            else:
                print("Congratulations! You guessed the number correctly.")

                break

    if attempts == max_attempts and user_guess is not secret_number:
        print("Game over! You've used all attempts. The number was", secret_number, ".")

number_guessing_game()
