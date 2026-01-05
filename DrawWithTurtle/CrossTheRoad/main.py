import random
import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_managers = []
for i in range(0,10):
    car_manager = CarManager()
    car_managers.append(car_manager)


screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in range(0, random.randint(0,len(car_managers))):
        if player.distance(car_managers[i]) < 20:
            game_is_on = False
            player.write("GAME OVER", False,"center",("Courier",40,"bold"))
            screen.exitonclick()
        car_managers[i].move_ahead()

    if player.ycor() == 280:
        scoreboard.update_score()

screen.exitonclick()
