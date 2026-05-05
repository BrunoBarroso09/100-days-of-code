from turtle import Turtle, Screen

class Draw:
    def __init__(self):
        self.timmy = Turtle()
        self.timmy.color("red")
        self.timmy.shape("turtle")
        self.screen = Screen()

    def draw(self):
        colors = ['red', 'green', 'blue', 'black', 'orange', 'purple', 'brown']
        for sides, color in zip(range(3,10), colors):
            self.timmy.color(color)
            self.draw_polygon(sides, 100)
        self.exit()

    def draw_polygon(self, sides, length):
        angle = 360 / sides
        for _ in range(sides):
            self.timmy.forward(length)
            self.timmy.right(angle)

    def exit(self):
        self.screen.exitonclick()

graph = Draw()
graph.draw()