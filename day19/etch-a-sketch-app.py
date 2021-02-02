from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.back(20)

def move_right():
    # tim.right(20)
    # decrease position so goes right start with 180 and goes right (left to right)
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)



def move_left():
    # tim.left(20)
    # ex - start at 0 and adding 20 turns left as 90 is upright (right to left)
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    # put the pen back down so we can draw after clearing the screen
    tim.pendown()

# start listening for events
screen.listen()

# listen for key pressed
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key = "d", fun = move_right)
screen.onkeypress(key = "a", fun=move_left)
screen.onkeypress(key = "c", fun=clear_screen)


# don't let the screen disappear until we click on the screen
screen.exitonclick()