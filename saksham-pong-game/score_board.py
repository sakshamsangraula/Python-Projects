from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        # clear the previous value and write new value for the score
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_score_up(self):
        self.l_score += 1
        self.update_score()

    def r_score_up(self):
        self.r_score += 1
        self.update_score()

    def get_l_score(self):
        return self.l_score

    def get_r_score(self):
        return self.r_score

    def find_winner(self):
        self.goto(0, 0)
        self.color("yellow")
        if self.l_score > self.r_score:
            self.write(f"Left player wins with a score of {self.l_score}", align="center",
                       font=("Courier", 22, "normal"))
        elif self.r_score > self.l_score:
            self.write(f"Right player wins with a score of {self.r_score}", align="center",
                       font=("Courier", 22, "normal"))
        else:
            self.write("It's a tie!")



