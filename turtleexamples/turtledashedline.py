from turtle import  Turtle, Screen
tim=Turtle()
sc=Screen()
for _ in range(10):
    # tim.color("black")
    tim.forward(10)
    tim.penup()
    # tim.color("white")
    tim.forward(10)
    tim.pendown()
    

sc.exitonclick()