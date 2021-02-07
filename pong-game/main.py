# create a screen (800 by 600) and black background
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
# turn off animation by setting tracer to 0
screen.tracer(0)

# listen to screen
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.onkey(key="w", fun=l_paddle.lp_up)
screen.onkey(key ="s", fun=l_paddle.lp_down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

is_game_on = True
while is_game_on:
    # sleep for the value of move_speed every time we go inside a loop
    time.sleep(ball.move_speed)
    # only update the screen after the work is done
    # (ex- after the paddle moves to the right so we don't see the movement)
    screen.update()
    ball.move()

    # bounce back if it collides with the top and bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # if it collides with the paddle then increase the speed
        ball.bounce_x()


    # missed the ball in the right side (give point to the left side)
    if ball.xcor() >= 380:
        score_board.l_score_up()
        ball.reset()

    # missed the ball in the left side (give point to the right side)
    if ball.xcor() <= -380:
        score_board.r_score_up()
        ball.reset()


# exit the screen on click only
screen.exitonclick()