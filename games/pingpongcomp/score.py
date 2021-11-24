from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,300)
        self.p1s=0
        self.p2s=0
        self.pendown()
        self.hideturtle()
        self.color("yellow")
        self.write(arg=f"{self.p2s} : {self.p1s}", move=False, align="center", font=["Arial",20, 'normal'])
    def update(self):
        self.clear()
        self.write(arg=f"{self.p2s} : {self.p1s}", move=False, align="center", font=["Arial",20, 'normal'])
        
