from turtle import Turtle,Screen
from random import choice
color=["red","green","blue","grey","black","orange","yellow","violet"]
tim=Turtle()
sc=Screen()
angle=120
for i in range(3,10):
    angle=(180*(i-2))/i
    ang=180-angle
    tim.color(choice(color))
    for j in range(i):
        tim.forward(100)
        tim.right(ang)
    angle=angle+30

sc.exitonclick()