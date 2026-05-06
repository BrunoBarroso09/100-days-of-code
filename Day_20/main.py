from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()#Create snake


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()# Move snake

screen.exitonclick()