# from turtle import Turtle, Screen
# # def __init __()
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
#
#
# screen = Screen()
# screen.exitonclick()

# install heroes because only importing doesn't work
# import heroes
# print(heroes.gen())

# whenever a number is even put the pen up so that it doesn't write anything and put the pen down to write
# the lines so that we have a dashed line

# Exercise 2
from turtle import Turtle, Screen
import random
# tortue = Turtle()
# for num in range(0, 60):
#     tortue.forward(10)
#     tortue.penup()
#     tortue.forward(10)
#     tortue.pendown()

tortue = Turtle()
shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10
}
hex_colors = ["#b472c1", "#99a4ba", "#001c54", "#0038a8", "#ffbf00", "#0039fb", "#b42006", "#c5e3e6"]
def find_angle(side):
    return 360/side

def draw_shape(side, angle):
    for num in range(0, side):
        tortue.forward(100)
        tortue.right(angle)

for shape in shapes:
    # draw a triangle
    num_sides = shapes[shape]
    angle = find_angle(num_sides)
    tortue.color(random.choice(hex_colors))
    draw_shape(num_sides, angle)


screen = Screen()
screen.exitonclick()