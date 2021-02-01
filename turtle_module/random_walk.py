import turtle as t
from turtle import Turtle, Screen
import random

turtle = Turtle()
t.colormode(255)

def random_color():
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    color_tuple = (red, blue, green)
    return color_tuple

colors = ["blue", "deep sky blue", "green yellow", "red", "yellow", "magenta", "dark violet", "medium purple"]
# increase the thickness
turtle.pensize(15)
turtle.speed("fastest")
# randomly go to any direction
# for _ in range(0, 101):
#     rand_num = random.randint(-100,70)
#     # go forwards or backwards depending on negative or positive value
#     # switch to right or left depending on random angles
#     turtle.forward(rand_num)
#     turtle.right(rand_num)
#     # randomly choose a color
#     turtle.color(random.choice(colors))

directions = [0, 90, 180, 270]
for _ in range(200):
    turtle.color(random_color())
    turtle.forward(25)
    turtle.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()