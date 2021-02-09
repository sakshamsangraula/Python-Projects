from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def restarting_position(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), self.y_pos)

    def down(self):
        self.y_pos = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), self.y_pos)

    def left(self):
        self.x_pos = self.xcor() - MOVE_DISTANCE
        self.goto(self.x_pos, self.ycor())

    def right(self):
        self.x_pos = self.xcor() + MOVE_DISTANCE
        self.goto(self.x_pos, self.ycor())







