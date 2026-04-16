from art import *
from clear_terminal import TerminalClear
import random
from game_data import data

def get_personality():
    random_person = random.randint(0, len(data))
    name = data[random_person]['name']
    follower_count = data[random_person]['follower_count']
    desc = data[random_person]['description']
    country = data[random_person]['country']
    personality = f'{name}, a {desc}, from {country}.'
    return personality, follower_count

def main():
    profile_a, follower_a = get_personality()
    profile_b, follower_b = get_personality()
    score = 0
    run = True

    while run:
        TerminalClear().clear()
        print(logo)
        if score > 0:
            print(f'Correct answer! You have {score} points.')

        print(f"Compare: {profile_a}")
        print(vs)
        print(f"Compare: {profile_b}")
        choose = input("Who has more followers? Type 'A' or 'B'.").lower()
        if choose == 'a' and follower_a >= follower_b:
            score += 1
            profile_b, follower_b = get_personality()
        elif choose == 'b' and follower_a <= follower_b:
            score += 1
            profile_a, follower_a = get_personality()
        elif choose == 'a' and follower_a < follower_b:
            print(f"\nIncorrect, your final score is {score}.")
            run = False
        elif choose == 'b' and follower_a > follower_b:
            print(f"\nIncorrect, your final score is {score}.")
            run = False
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        main()
    elif play_again == 'n':
        print("Thanks for playing!")

main()