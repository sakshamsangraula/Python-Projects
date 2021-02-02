from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Choose a color to see if your turtle wins the race: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start = False
# loop through the colors and make that many turtles
x = -235
y = -30
for i in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.color(colors[i])
    y += 20
    turtles.append(new_turtle)

if user_bet:
    start = True

while start:
    for turtle in turtles:
        # if turtle goes over the right screen (x coordinate is over 230) then
        if turtle.xcor() > 230:
            start = False
            color = turtle.pencolor()
            if color == user_bet:
                print(f"You won! The {color} turtle won")
            else:
                print(f"You lost! The {color} turtle won")
            break

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()