from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Your score is: {self.score}", move=False, align="center", font=FONT)
