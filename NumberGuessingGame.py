# to import random module
import random
# to create a range of random numbers between 1-10
n = random.randrange(1,100)
# to take a user input to enter a number
guess = int(input("Enter any number: "))
while n!= guess: # means if n is not equal to the input guess
    # if guess is smaller than n
    if guess < n:
        print("Too low")
        # to again ask for input
        guess = int(input("Enter number again: "))
    # if guess is greater than n
    elif guess > n:
        print("Too high!")
        # to again ask for the user input
        guess = int(input("Enter number again: "))
    # if guess gets equals to n terminate the while loop
    else:
        break
print("you guessed it right!!")



=============================================================
========================= OR ================================
=============================================================

import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too low!")
    elif guess > secret_number:
        print("📈 Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
