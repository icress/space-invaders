from turtle import Turtle


class Invader(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.right(90)
        self.x_move = 2
        self.y_move = 0.5
        self.shapesize(stretch_wid=2, stretch_len=2)

    def move(self):
        self.goto(x=self.xcor() + self.x_move, y=self.ycor() - self.y_move)

    def bounce_x(self):
        self.x_move *= -1

