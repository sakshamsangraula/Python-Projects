from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# create lots of cars that will move from right to left
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.create_car()
        self.move_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        # make sure that 1 in 7 cars are created each time the while room is ran in the main.py file
        rand_num = random.randint(1, 7)
        if rand_num == 7:
            # car manager has cars just like snake has segments
            self.car = Turtle(shape="square")
            self.car.penup()
            self.car.setheading(180)
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.color(random.choice(COLORS))
            self.cars.append(self.car)
            self.y_pos = random.randint(-250, 250)
            self.car.goto(300, self.y_pos)

    def move_car(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += 10

    def return_cars(self):
        return self.cars












