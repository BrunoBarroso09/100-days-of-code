# Hurdle 1/2

def left_x3():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    left_x3()
    move()
    left_x3()
    move()
    turn_left()


# for i in range(6):
#    jump()

i = 0
while i < 6:
    if at_goal():
        done()
    else:
        jump()
        i += 1