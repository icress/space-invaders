from turtle import Turtle


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.color('white')
        self.penup()
        self.left(90)

    def move_right(self):
        self.goto(x=self.xcor() + 20, y=self.ycor())

    def move_left(self):
        self.goto(x=self.xcor() - 20, y=self.ycor())

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)

