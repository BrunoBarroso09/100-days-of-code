# Hurdle 3

def left_x3():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    left_x3()
    move()
    left_x3()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()