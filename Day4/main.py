rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
game_options = [rock, paper, scissors]
computer_choice = random.randint(0, len(game_options) - 1)

if user_choice < 0 or user_choice > 3:
    print("Invalid Choice")
else:
    print(f"{game_options[user_choice]}\n")
    print(f"Computer chose: {game_options[computer_choice]}\n")

    match (user_choice, computer_choice):
        case (0, 1) | (1, 2) | (2, 0):
            print("You lost!")
        case (0, 2) | (1, 0) | (2, 1):
            print("You won!")
        case _ if user_choice == computer_choice:
            print("Draw!")
        case _:
            print("Invalid choice!")