from turtle import Screen, Turtle
import random


class Spirograph:

    def __init__(self, size):
        self.timmy = Turtle()
        self.timmy.shape("turtle")
        self.timmy.speed("fastest")
        self.size = size
        self.r = ()
        self.g = ()
        self.b = ()
        self.screen = Screen()
        self.screen.colormode(255)

    def random_color(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        random_color = (self.r, self.g, self.b)
        return random_color

    def draw(self):
        for angle in range(0, 360, 5):
            self.timmy.color(self.random_color())
            self.timmy.circle(self.size)
            self.timmy.setheading(angle)

    def exit(self):
        self.screen.exitonclick()


spiro = Spirograph(100)
spiro.draw()
spiro.exit()