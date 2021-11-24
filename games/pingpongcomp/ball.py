from turtle import Turtle
import random
xycombos=[(8,7),(6,8),(10,0),(8,-7),(6,-8),(-8,7),(-6,8),(-10,0),(-8,-7),(-6,-8)]

class Ball:
    def __init__(self):
       tim=Turtle()
       tim.shape("circle")
       tim.shapesize(1)
       tim.color("white")
       tim.penup()
       tim.goto(-370,260)
       tim.pendown()
       for i in range(2):
            tim.forward(740)
            tim.right(90)
            tim.forward(520)
            tim.right(90)
       tim.penup()
       tim.goto(0,0)
       self.ball=tim
       xy=random.choice(xycombos)
       self.xspeed=xy[0]
       self.yspeed=xy[1]
       print(self.xspeed,self.yspeed)
       self.mleft=[(-8,7),(-6,8),(-10,0),(-8,-7),(-6,-8),(-4,6)]
       self.mright=[(8,7),(6,8),(10,0),(8,-7),(6,-8),(4,6)]
       self.speed=0.08
    def move(self):
        cycor=self.ball.ycor()
        cxcor=self.ball.xcor()
        if cxcor<-340:
            self.xspeed=self.xspeed*-1
        if cycor<-250 or cycor>250:
            self.yspeed=self.yspeed*-1
        
        self.ball.goto(cxcor+self.xspeed,cycor+self.yspeed)
    def resetl(self):
       self.ball.goto(0,0)
       xy=random.choice(self.mleft)
       self.xspeed=xy[0]
       self.yspeed=xy[1]
       self.speed=0.1
    def resetr(self):
       self.ball.goto(0,0)
       xy=random.choice(self.mright)
       self.xspeed=xy[0]
       self.yspeed=xy[1]
       self.speed=0.1

