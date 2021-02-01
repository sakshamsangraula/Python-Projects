# import colorgram as c
#
# # extract 40 colors from the image
# colors = c.extract('hirst-painting.jpg', 40)
# rgb_colors = []
# # loop through the colors and print each tuple
# for color in colors:
#     rgb_list = []
#     rgb_list.append(color.rgb.r)
#     rgb_list.append(color.rgb.g)
#     rgb_list.append(color.rgb.b)
#     rgb_tuple = tuple(rgb_list)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]
from turtle import Turtle, Screen
import random
import turtle
turtle.colormode(255)
tortue = Turtle()

# hide all the lines and also the turtle
tortue.penup()
tortue.hideturtle()

num_dots = 101
tortue.speed("fastest")
# start at the bottom left
tortue.setheading(220)
tortue.forward(350)
tortue.setheading(0)

for dot in range(1, num_dots):
    # add a dot and move forward to keep adding dots unless the dot is 10,20, or other multiples of 10
    # show a dot
    tortue.dot(20, random.choice(color_list))
    tortue.forward(50)

    # if the dot is a multiple of 10 then go up and left to the starting point
    if dot % 10 == 0:
        tortue.setheading(90)
        tortue.forward(50)
        tortue.setheading(180)
        tortue.forward(500)
        tortue.setheading(0)

# make sure the screen stays on until it is clicked and then it disappears
screen = Screen()
screen.exitonclick()
