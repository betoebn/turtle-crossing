import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

car = CarManager()


screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()
    if player.y_pos() > 280:
        scoreboard.score += 1
        scoreboard.track_score()
        player.start_again()
        car.create_cars()
        car.difficulty()
    for i in range(0, 75):
        if car.cars[i].distance(player.player) <= 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
