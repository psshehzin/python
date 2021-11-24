from turtle import Turtle,Screen
import time
import random
xycombos=[(10,0),(6,8),(8,6),(8,-6),(-8,6),(-8,-6),(7,7)]
class Ball:
    def __init__(self):
       tim=Turtle()
       tim.shape("circle")
       tim.penup()
       tim.shapesize(1)
       tim.goto(0,0)
       self.ball=tim
       xy=random.choice(xycombos)
       self.xspeed=xy[0]
       self.yspeed=xy[1]
    def move(self):
        cycor=self.ball.ycor()
        cxcor=self.ball.xcor()
        if cxcor<-340 or cxcor>340:
            self.xspeed=self.xspeed*-1
        if cycor<-250 or cycor>250:
            self.yspeed=self.yspeed*-1
        
        self.ball.goto(cxcor+self.xspeed,cycor+self.yspeed)
# ball=Ball()
# sc=Screen()
# sc.tracer(0)
# for i in range(0,10000):
#     ball.move()
#     sc.update()
#     time.sleep(0.03)