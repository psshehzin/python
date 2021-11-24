from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.goto(0,295)
        self.pendown()
        self.color("yellow")
        self.write(f"Level : {self.score}", move=False, align="center", font=FONT)
    def update(self):
        self.clear()
        self.penup()
        self.goto(0,295)
        self.pendown()
        self.write(f"SCORE : {self.score}", move=False, align="center", font=FONT)
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(f"GAME OVER SUCKER YOUR SCORE : {self.score}", move=False, align="center", font=FONT)