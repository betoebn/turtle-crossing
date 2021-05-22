from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle("turtle")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)
        self.player.color("blue")

    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def y_pos(self):
        return self.player.ycor()

    def start_again(self):
        self.player.goto(STARTING_POSITION)

