from turtle import Turtle


class Blaster(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=0.2)
        self.color('skyblue')

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor() + 10)
