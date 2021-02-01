import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
turtle = Turtle()
turtle.speed("fastest")

def generate_random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0, 255)
    return (r, b, g)
# make a circle
# for _ in range(37):
#     turtle.color(generate_random_color())
#     turtle.circle(100)
#     turtle.left(10)

def draw_spirograph(num_gaps):
    # loop until we have covered the number of circles we need to draw (the number of gaps we need to fill)
    for _ in range (int(360/num_gaps)):
        turtle.color(generate_random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 5)

draw_spirograph(5)

# make sure screen is visible until we click on it
screen = Screen()
screen.exitonclick()