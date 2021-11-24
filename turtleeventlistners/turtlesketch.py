from turtle import Turtle,Screen
tim=Turtle()
def forwardm():
    tim.forward(5)
def backwordm():
    tim.backward(5)
def left():
    tim.left(5)
def right():
    heading=tim.heading()-5
    tim.setheading(heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
sc=Screen()
sc.listen()
sc.onkeypress(key="w",fun=forwardm)
sc.onkeypress(key="s",fun=backwordm)
sc.onkeypress(key="a",fun=left)
sc.onkeypress(key="d",fun=right)
sc.onkey(key="c",fun=clear)

sc.exitonclick()