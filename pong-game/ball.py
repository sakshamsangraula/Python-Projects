from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
       # change the y distance to a negative direction so it bounces back in opposite direction
       self.y_move *= -1

    def bounce_x(self):
        # negate the x values to move to opposite direction
        self.x_move *= -1
        # also reduce the move speed by about 10% so that the time sleeps less and ball goes faster
        self.move_speed *= 0.9

    def reset(self):
        # make the ball go back to the center
        self.goto(0, 0)
        # reset the move_speed to 0.1 so it doesn't keep decreasing and eventually become negative
        self.move_speed = 0.1
        # make the ball go to the opposite direction
        self.bounce_x()



