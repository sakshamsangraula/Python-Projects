from snakepart1 import Snake
from turtle import Screen
import time

screen = Screen()
# only update the screen when we need to using update so segments are shown together
# so set tracer to 0
screen.tracer(0)

# start listening
screen.listen()

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Saksham Snake Game")

# create a snake
snake = Snake()

# use keys to move the snake
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    # update the screen and wait for a millisecond
    screen.update()
    time.sleep(0.1)
    snake.move()







screen.exitonclick()