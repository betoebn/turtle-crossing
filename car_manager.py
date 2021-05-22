import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def move(self):
        for i in range(0, 75):
            self.cars[i].forward(MOVE_INCREMENT)

    def create_cars(self):
        for i in range(0, 75):
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.goto(random.randint(350, 2500), random.randint(-250, 250))
            car.color(random.choice(COLORS))
            car.setheading(180)
            self.cars.append(car)

    def difficulty(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT += 10
