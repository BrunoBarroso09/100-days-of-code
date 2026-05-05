from turtle import Screen, Turtle

timmy = Turtle()
timmy.color("red")
timmy.shape("turtle")

for _ in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()