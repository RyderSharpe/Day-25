from turtle import Turtle



FONT = ("courier", 10, "bold")

class TheScore(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.hideturtle()  # Hide the turtle object
        self.penup()

    def update_score(self):
        self.clear()
        self.goto(-320.0, 250)
        self.write(f"{self.score}/50", align="center", font=("courier", 20, "normal"))


    def increase_score(self):
        self.score += 1
