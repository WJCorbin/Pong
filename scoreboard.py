from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.score2, align="center", font=("Courier", 60, "normal"))

    def increase_score(self, player):
        if player == 1:
            self.score1 += 1
        if player == 2:
            self.score2 += 1
