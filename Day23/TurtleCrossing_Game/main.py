import time
from player import Player
from turtle import Turtle,Screen
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #detect collision
    for car in car_manager.all_cars:
        if player.distance(car)<25:
            scoreboard.game_over()
            game_on=False

    #successful crossing
    if player.is_at_fininshing_line():
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()