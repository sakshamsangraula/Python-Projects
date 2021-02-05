from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.random_move()

    def random_move(self):
        position_x = random.randint(-270, 270)
        position_y = random.randint(-270, 270)
        self.penup()
        self.goto(position_x, position_y)



