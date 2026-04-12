from art import logo
import random
import sys
import os
root = os.path.abspath(os.path.dirname(__file__) + '/..')
sys.path.append(root)
from clear_terminal import TerminalClear

def chose_winner(user, computer):
    run_choice = True
    while run_choice:
        if sum(computer) < 17 and sum(computer) < 21:
            other_choice = random.randint(1, 11)
            computer.append(other_choice)
        else:
            run_choice = False
            print(f'Computer final hand: {computer}, final score: {sum(computer)}')

            if sum(computer) == sum(user):
                print("Draw")
            elif sum(user) <= 21 < sum(computer):
                print("User Win")
            elif sum(user) > 21 >= sum(computer):
                print("Computer Won")
            elif sum(user) < 21 and sum(user) < sum(computer) <= 21:
                print("Computer Won")
            else:
                print("User Win")

def new_game():
    start_game = input("Do you want to play again? Type 'y' or 'n':")
    if start_game.lower() == "y":
        TerminalClear().clear()
        blackjack()
    else:
        sys.exit()

def blackjack():
    run = True
    print(logo)
    option = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if option.lower() == "n":
        TerminalClear().clear()
    else:
        user_hand = []
        computer_hand = []
        first_choice = random.randint(1,11)
        second_choice = random.randint(1,11)
        user_hand.append(first_choice)
        user_hand.append(second_choice)
        if sum(user_hand) == 21:
            print(f'Your cards: {user_hand}, current score: {sum(user_hand)}')
            print(f'YOU WIN!! BLACKJACK!!🃏')
            run = False
        elif sum(user_hand) > 21:
            print("Computer Won")
        else:
            while run:
                computer_hand.append(first_choice)
                print(f'Your cards: {user_hand}, current score: {sum(user_hand)}')
                print(f'Computer first card: {computer_hand[0]}')
                other_card = input("Type 'y' to get another card, type 'n' to pass:")
                if other_card.lower() == "y":
                    new_choice = random.randint(1,11) # 6 1 6 7 = 20
                    user_hand.append(new_choice)
                    if sum(user_hand) > 21:
                        print(f'You lose! Your cards: {user_hand}, current score: {sum(user_hand)}')
                        run = False
                    elif sum(user_hand) == 21:
                        print(f'User Win! Your cards: {user_hand}, current score: {sum(user_hand)}')
                        new_game()
                else:
                    print(f'Your final hand: {user_hand}, current score: {sum(user_hand)}')
                    run = False
            chose_winner(user_hand, computer_hand)
    new_game()
blackjack()