from turtle import Screen
from paddle import Padle
from score import Score
import time
from ball import Ball
def checkcollission(paddle,ball,player):
    dis=ball.ball.distance(paddle.turtle.position())
    if dis<54:
        ball.xspeed=ball.xspeed*-1
        sc.update()
        if ball.xspeed<0:
            b=-1
        else:
            b=1
        if (ball.speed>0.05):
            ball.speed=ball.speed-0.01
        elif(ball.speed>0.03):
            ball.speed=ball.speed-0.0015
        elif(ball.speed>0.01):
            ball.speed=ball.speed-0.0005
        if 37<=dis<54:
            if ball.ball.ycor()>paddle.turtle.ycor():
                ball.xspeed=6*b
                ball.yspeed=8
            else:
                ball.xspeed=6*b
                ball.yspeed=-8
        elif 20<dis<37:
            if ball.ball.ycor()>paddle.turtle.ycor():
                ball.xspeed=7*b
                ball.yspeed=6
            else:
                ball.xspeed=7*b
                ball.yspeed=-6
        else:
            ball.xspeed=10*b
            ball.yspeed=0
        print(ball.xspeed,ball.yspeed)
    else:
        ball.move()
        ball.move()
        if player==1:
            score.p1s=score.p1s+1
            score.update()
            ball.resetr()
            sc.update()
            time.sleep(3)
        else:
            score.p2s=score.p2s+1
            score.update()
            ball.resetl()
            sc.update()
            time.sleep(3)
        
speed=0.1    
gameon=True
xlim=350
up1="w"
down1="s"
up2="Up"
down2="Down"
sc=Screen()
sc.bgcolor("black")
sc.setup(width=800,height=700)
sc.tracer(0)
paddle=Padle(sc,xlim)
paddle1=Padle(sc,xlim*-1)
score=Score()
sc.update()
time.sleep(0.5)
ball=Ball()
sc.update()
sc.listen()
sc.onkey(fun=paddle.moveup,key=up1)
sc.onkey(fun=paddle.movedown,key=down1)
sc.onkey(fun=paddle1.moveup,key=up2)
sc.onkey(fun=paddle1.movedown,key=down2)
while(gameon):
    ball.move()
    cxcor=ball.ball.xcor()
    if (cxcor)>=332:
        checkcollission(paddle,ball,2)
    elif (cxcor)<=-332:
        checkcollission(paddle1,ball,1)
    sc.update()
    time.sleep(ball.speed)
sc.exitonclick()
# while(True):
#     if i<30:
#         b=Ball()
#         balls.append(b)
#     for ball in balls:
#         ball.move()

#     sc.update()
#     time.sleep(0.01)
#     i=i+1