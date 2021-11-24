import turtle as t
import random
def rand_Color():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    temp=(r,g,b)
    return temp
t.colormode(255)
tim=t.Turtle()
angle=5
times=360/angle
sc=t.Screen()
tim.speed("fastest")
i=0
while(i!=times):
    tim.color(rand_Color())
    tim.circle(100)
    tim.left(angle)
    i=i+1
sc.exitonclick()
