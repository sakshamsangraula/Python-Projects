from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Saksham's Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# create a snake object
snake = Snake()
food = Food()
score_board = ScoreBoard()

# listen for screen events to control the snake
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        score_board.increment_score()
        # add segment to the snake to make it longer
        snake.extend_snake()
        food.random_move()

    # if the snake's head goes over the boundary then it's game over
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset_score_board()
        snake.reset_snake()

    # last check: if the snake's head collides with any of the snake segments (snake body) then it's game over
    # for _ in snake.segments:
    # check the head with segment other than the first one
    check_segments = snake.segments[1::]
    for segment in check_segments:
        if snake.head.distance(segment) < 10:
            score_board.reset_score_board()


screen.exitonclick()