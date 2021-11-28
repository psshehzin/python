from turtle import Turtle
class Padle:
    def __init__(self,screen,xcor,plate_length=5):
        self.plate_length=plate_length
        tim=Turtle()
        tim.shape("square")
        tim.color("white")
        tim.shapesize(stretch_wid=plate_length,stretch_len=1)
        tim.penup()
        tim.goto(xcor,0)
        self.turtle=tim
        self.positions=(xcor,0)
        self.screen=screen
    def moveup(self):
        self.positions=(self.positions[0],self.positions[1]+20)
        self.turtle.goto(self.positions)
        self.screen.update() 
    def movedown(self):
        self.positions=(self.positions[0],self.positions[1]-20)
        self.turtle.goto(self.positions)
        self.screen.update()