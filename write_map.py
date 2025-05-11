from turtle import Turtle

FONT = ("Arial", 8, "normal")

class Write_answer(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write(self, x, y, state):
        self.goto(x,y)
        super().write(arg=state, align="center", font=FONT)

    def write_missed (self, x, y, state):
        self.goto(x,y)
        self.color("cyan")
        super().write(state, align="center", font=FONT)