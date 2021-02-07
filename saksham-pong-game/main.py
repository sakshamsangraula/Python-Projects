from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

import time

# make the screen (800 by 600)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Saksham Pong Game")
# turn off animation (we will update the screen later on to turn it on)
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()

# LISTEN TO THE INPUT (START LISTENING)
screen.listen()

# move the paddle
screen.onkey(key="Up", fun=r_paddle.right_up)
screen.onkey(key="Down", fun=r_paddle.right_down)
screen.onkey(key="w", fun=l_paddle.left_up)
screen.onkey(key="s", fun=l_paddle.left_down)


is_game_on = True
while is_game_on:
    # sleep for some time so the ball doesn't move really really fast
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()

    # detect collision with the wall and bounce back in the y direction
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # if the ball hits the paddle then bounce back in the x direction
    if ball.distance(r_paddle) < 50 and ball.xcor() > 315 or (ball.distance(l_paddle) < 50 and ball.xcor() < -315):
        ball.bounce_x()


    # if the ball goes over the bounds to the left, increase score of the right side
    # and reset the ball to the center
    if ball.xcor() < -380:
        score_board.r_score_up()
        ball.reset_pos()

    # if the ball goes over the bounds to the right, increase score of the left side
    # and reset the ball to the center
    if ball.xcor() > 380:
        score_board.l_score_up()
        ball.reset_pos()

    if score_board.get_l_score() > 5 or score_board.get_r_score() > 5:
        is_game_on = False
        score_board.find_winner()


screen.exitonclick()