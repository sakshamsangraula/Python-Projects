from snakepart1 import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
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

food = Food()
score_board = ScoreBoard()
is_game_on = True
while is_game_on:
    # update the screen and wait for a millisecond
    screen.update()
    time.sleep(0.1)
    snake.move()

    # if the snake head is very close to the food then collide
    if snake.head.distance(food) < 15:
        food.refresh()
        # increase the length of the snake
        snake.extend()
        score_board.increase_score()

    # if the snake's head goes over the boundaries then set game on to false
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        # print game over in the screen
        score_board.game_over()

    # if the head touches itself then the game is over
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                score_board.game_over()

screen.exitonclick()