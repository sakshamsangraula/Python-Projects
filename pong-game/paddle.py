from turtle import Turtle


class Paddle(Turtle):
    # the paddle class inherits from the turtle class
    def __init__(self, position):
        # inheriting from the turtle class already makes a turtle
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, pos):
            self.shape("square")
            self.color("white")
            self.penup()
            self.shapesize(stretch_len=1, stretch_wid=5)
            self.goto(pos)

    def up(self):
        y_up = self.ycor() + 30
        self.goto(self.xcor(), y_up)

    def down(self):
        y_up = self.ycor() - 30
        self.goto(self.xcor(), y_up)

    def lp_up(self):
        y_up = self.ycor() + 30
        self.goto(self.xcor(), y_up)

    def lp_down(self):
        y_up = self.ycor() - 30
        self.goto(self.xcor(), y_up)


