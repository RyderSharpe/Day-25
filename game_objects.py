from turtle import Turtle
import pandas


FONT = ("courier", 20, "bold")
class Map(Turtle):
    locations = pandas.read_csv("50_states.csv")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def guess_to_map(self, user_guess, x_value, y_value):
        self.goto(x_value, y_value)
        self.pendown()
        # write text
        self.write(user_guess, align="center", font=("Arial", 10, "normal"))

    def win(self):
        self.goto(-250, 0)
        self.write("YOU HAVE WON.", font=('Arial', 50, 'normal'))
        self.goto(-250, -50)
        self.write("CLICK TO EXIT.", font=('Arial', 20, 'normal'))

