from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(width=500, height=500)
bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race? Enter a color: ").lower
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-100, -60, -20, 20, 60, 100] #Position for each turtle in the y-axis
turtles = []

for turtle_number in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_number])
    new_turtle.goto(x=-250, y=y_axis[turtle_number]) #Setup each turtle in the screen
    turtles.append(new_turtle)

if bet:
    start_race = True

while start_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            start_race = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance) #move turtle forward

screen.exitonclick()