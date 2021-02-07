from turtle import Turtle
INCREMENT = 25

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.goto(position)

    def right_up(self):
        self.y_pos += INCREMENT
        self.goto(self.x_pos, self.y_pos)

    def right_down(self):
        self.y_pos -= INCREMENT
        self.goto(self.x_pos, self.y_pos)

    def left_up(self):
        self.y_pos += INCREMENT
        self.goto(self.x_pos, self.y_pos)

    def left_down(self):
        self.y_pos -= INCREMENT
        self.goto(self.x_pos, self.y_pos)



