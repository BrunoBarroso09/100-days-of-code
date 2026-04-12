import random

run = True
while run:
    computer_choice = random.randint(1,11)
    if 0 == computer_choice:
        print(computer_choice)
        run = False