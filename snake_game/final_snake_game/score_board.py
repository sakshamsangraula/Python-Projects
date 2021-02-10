from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        # read the high score from the file
        file = open("data.txt")
        self.high_score = int(file.read())
        file.close()
        self.color("white")
        self.penup()
        self.update_score()

    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # write the high score to the file
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.penup()
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def increment_score(self):
        self.score += 1
        self.update_score()