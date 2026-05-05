from turtle import Screen, Turtle
import random

class Walker:

    def __init__(self):
        self.timmy = Turtle()
        self.timmy.color("red")
        self.timmy.shape("turtle")
        self.DIRECTIONS = [0, 90, 180, 270]
        self.r = ()
        self.g = ()
        self.b = ()
        self.timmy.pensize(5)
        self.timmy.speed("fastest")
        self.screen = Screen()
        self.screen.colormode(255)

    def random_color(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        random_color = (self.r, self.g, self.b)
        return random_color

    def random_walk(self):
        for _ in range(200):
            self.timmy.color(self.random_color())
            self.timmy.setheading(random.choice(self.DIRECTIONS))
            self.timmy.forward(30)

    def exit(self):
        self.screen.exitonclick()


random_walker = Walker()
random_walker.random_color()
random_walker.random_walk()
random_walker.exit()