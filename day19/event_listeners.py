from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

# to start listening for events we need to tell screen to start listening for events
screen.listen()

# now the screen has headphones on and is now listening

# So, now we give it some sound (keystrokes etc, and then it can call another function (comprehend function etc))
screen.onkey(key="space", fun=move_forwards)

# WHEN USING FUNCTIONS THAT YOU DIDN'T CREATE LIKE onkey USE KEYWORDS ARGUMENT (specifying key = and fun = )

screen.exitonclick()
