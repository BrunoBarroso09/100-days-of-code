from hangman_art import stages, logo2, logo3
from hangman_words import word_list
import random

print(logo3)

#Variables
choice = random.choice(word_list)
print(choice)
length_choice = len(choice)
end_game = False
life = 6

print("\nGuess the word to win!\n")

display = []
wrong = []
for i in range(len(choice)):
    display += "_"

while not end_game:

        guess = input("Guess a letter: ").lower()

        if guess in wrong:
            print(f"{' '.join(display)}")
            print(stages[life])
            print(f"You've already guessed with the letter '{guess}', pick another letter.")
        else:
            wrong.append(guess)

            for position in range(length_choice):
                letter = choice[position]
                if letter == guess:
                    display[position] = letter

            print(f"{' '.join(display)}")

            if "_" not in display:
                end_of_game = True
                print("\nYou won!")
                print(logo2)

            if guess not in choice:
                life -= 1

            if not end_game:
                print(stages[life])
                if guess not in choice:
                    print(f"The letter '{guess}' is not in the word, you lost 1 life.")

            if life == 0:
                end_of_game = True
                print("You lose.")
                print(f"\nThe word was '{choice}'")