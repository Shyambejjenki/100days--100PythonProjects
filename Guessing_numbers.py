import random
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)  # Random number between 1 and 10
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The number was {secret_number}.")
