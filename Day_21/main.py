from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create paddle
r_paddle = Paddle((460, 0))
l_paddle = Paddle((-470, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()