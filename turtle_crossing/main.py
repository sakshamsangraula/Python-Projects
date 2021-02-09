from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

import time

screen = Screen()
# turn off animation
screen.tracer(0)
player = Player()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Saksham's Turtle Crossing")

# start listening
screen.listen()
# move turtle up and down based on the up and down arrow keys
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)
screen.onkey(key="Left", fun=player.left)
screen.onkey(key="Right", fun=player.right)

is_game_on = True
car_manager = CarManager()
score_board = ScoreBoard()

while is_game_on:
    # time.sleep(score_board.time_speed)
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detect collision with a car then end the game
    total_cars = car_manager.return_cars()
    for car in total_cars:
        if player.distance(car) < 25:
            score_board.game_over()
            is_game_on = False

    # if the player goes over the finish line then increase the score and the speed of the cars
    if player.ycor() > 280:
        # go back to the center
        player.restarting_position()
        score_board.level_up()
        car_manager.increase_speed()


screen.exitonclick()