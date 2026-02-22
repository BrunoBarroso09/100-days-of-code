def right():
    turn_left()
    turn_left()
    turn_left()


def run():
    turn_left()
    while wall_on_right():
        move()
    right()
    move()
    right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        run()
    else:
        move()