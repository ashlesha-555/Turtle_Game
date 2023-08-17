import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=450)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_on=False
            scoreboard.game_over()

    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()