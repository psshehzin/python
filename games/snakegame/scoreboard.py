from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("./highscore.txt") as file:
            self.highscore=int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,295)
        self.pendown()
        self.color("yellow")
        
        
    def score_update(self):
        self.score=self.score+1
        self.clear()
        self.penup()
        self.goto(0,295)
        self.pendown()
        self.write(f"SCORE : {self.score}  HighScore : {self.highscore}", move=False, align="center", font=["Arial",20, 'normal'])
    def reset(self):
        self.clear()
        if self.highscore<self.score:
            self.highscore=self.score
            with open("./highscore.txt",mode="w") as file:
                file.write(f"{self.highscore}")
            self.score=0
            self.pendown()
        self.score=0
score=Scoreboard()