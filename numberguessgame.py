import random  

print(" Welcome to the Number Guessing Game!") 
print("I'm thinking of a number between 1 and 100...")


secret_number = random.randint(1, 100)
print(f"[DEBUG] Secret number is: {secret_number}")  #Testing only
attempts = 0

while True:
    
    guess = input("Enter your guess: ")

    
    if not guess.isdigit():
        print(" Please enter a valid number.")
        continue 

    guess = int(guess)
    attempts += 1

    #now we can start with if else loop to compare the guessed number with the secret number created by random.randint

    
    if guess < secret_number:
        print(" Too low! Try again.")
    elif guess > secret_number:
        print(" Too high! Try again.")
    else:
        print(f" Correct! The number was {secret_number}.")
        print(f" You guessed it in {attempts} tries.")
        break
