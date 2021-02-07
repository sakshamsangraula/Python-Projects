from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()
        self.x_inc = 10
        self.y_inc = 10
        self.color("blue")
        self.goto(0, 0)
        self.time_speed = 0.1

    def move(self):
        self.x_pos = self.xcor() + self.x_inc
        self.y_pos = self.ycor() + self.y_inc
        self.goto(self.x_pos, self.y_pos)

    def bounce_y(self):
        # bounce to the opposite y direction
        self.y_inc *= -1

    def bounce_x(self):
        # bounce to the opposite x direction
        self.x_inc *= -1
        # lower the time so the ball moves faster each time it interacts with the paddle
        self.time_speed *= 0.9

    def reset_pos(self):
        # go back to the center and move to the opposite direction
        self.goto(0, 0)
        # reset the time speed to 0.1 so that we don't keep decreasing the speed to a negative value
        self.time_speed = 0.1
        self.bounce_x()



