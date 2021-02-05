# from turtle import Turtle, Screen
# import time
#

from turtle import Turtle, Screen
from snake import Snake
import time
# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Saksham Snake Game")

screen.tracer(0)

# listen for events after creating the snake

screen.listen()

snake = Snake()



# make sure the snake turns to the appropriate direction based on the keyboard input
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
