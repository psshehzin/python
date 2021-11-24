#from colorgram import extract
# import colorgram
# colors=extract("histart.jpg",20)
# for i in colors:
#     rgb=i.rgb
#     colorlist.append((rgb.r,rgb.g,rgb.b))
import turtle as t
from random import choice
colorlist=[(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]

gridsize=int(input("enter the size of grid needed: "))
t.colormode(255)
sc= t.Screen()
tim=t.Turtle()
tim.hideturtle()
tim.speed("fastest")
xy=gridsize*20//2
i=xy*-1
while(i!=xy):
    tim.penup()
    tim.setx(xy*-1)
    tim.sety(i)
    tim.pendown()
    for _ in range(gridsize):
        tim.dot(15,choice(colorlist))
        tim.penup()
        tim.forward(20)
        tim.pendown()
    i=i+20
sc.exitonclick()

