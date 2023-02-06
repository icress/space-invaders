from turtle import Turtle

FONT = ("Arial", 40, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 0)
        self.hideturtle()
        self.pencolor('white')

    def game_over(self):
        self.write('GAME OVER', align='center', font=FONT)

    def win(self):
        self.write('YOU WIN', align='center', font=FONT)