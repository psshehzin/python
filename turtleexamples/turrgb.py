from turtle import Turtle,Screen, delay
import random
import turtle
tim=Turtle()
sc=Screen()
turtle.colormode(255)
for _ in range(1000):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    temp=(r,g,b)
    turtle.color((temp))
sc.exitonclick()