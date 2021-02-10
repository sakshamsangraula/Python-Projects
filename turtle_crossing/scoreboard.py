from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_BOLD = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.update_level()
        self.penup()


    def update_level(self):
        # clear previous entry
        self.penup()
        self.clear()
        self.goto(-210, 220)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT_BOLD)






