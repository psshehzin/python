from turtle import Turtle,Screen, turtles
from random import choice
color=["red","green","blue","grey","black","orange","yellow"]
angles=[0,90,180,270]
limit=int(input("no of random steps: "))
tim=Turtle()
sc=Screen()
tim.pensize(10)
tim.shape("circle")
tim.speed("fastest")
for i in range(limit):
    tim.color(choice(color))
    tim.right(choice(angles))
    tim.forward(20)
    
sc.exitonclick()