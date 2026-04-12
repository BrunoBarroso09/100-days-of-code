from art import logo
import random
import sys

def guess_the_number():
    print(f'{logo}'
          "Welcome to the Number Guessing Game! \n"
          "I'm thinking of a number between 1 and 100.")
    guess_number = random.randint(1, 100)
    print(f'pssst, the correct answer is {guess_number}')
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty == "easy" else 5
    run = True
    while run:
        if attempts == 0:
            print("You lose!")
            print(f'The correct answer is {guess_number}')
            run = False
            sys.exit()
        print(f'You have {attempts} attempts to guess the number.')
        guess = int(input("Make a guess: "))
        if guess > guess_number:
            attempts -= 1
            print("Too high.")
        elif guess < guess_number:
            attempts -= 1
            print("Too low.")
        else:
            print(f'You guessed correctly! The number was {guess_number}.')
            run = False

guess_the_number()