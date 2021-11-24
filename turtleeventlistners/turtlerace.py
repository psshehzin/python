from turtle import Turtle,Screen, heading
import random
is_raceon=True
colors=["red","yellow","blue","green","purple"]
y_cor=[-80,-50,-20,10,40]
sc=Screen()
sc.setup(500,500)
turtles=[]
tim=Turtle()
tim.penup()
tim.goto(x=200,y=100)
tim.right(90)
tim.pendown()
tim.fd(200)
tim.color("white")
for i in range(0,5):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-200,y=y_cor[i])
    turtles.append(new_turtle)
b_color=sc.textinput(title="user_bet",prompt="Enter your bet color")

while(is_raceon):
    fw=random.randint(0,10)
    tuno=random.randint(0,4)
    turtles[tuno].forward(fw)
    if turtles[tuno].xcor()>180:
        win_color=turtles[tuno].color()[0]
        break
if win_color==b_color:
    print(f"Your bet {win_color} turtle won")
else:
    print(f"You loose {win_color} turtle won")
sc.exitonclick()
# new_turtle=Turtle()
# larry=Turtle()
# brian=Turtle()
# hugh=Turtle()
# sc=Screen()
# sc.setup(width=500,height=400)
# new_turtle.penup()
# new_turtle.color("red")
# new_turtle.shape("turtle")
# larry.color("blue")
# larry.penup()
# larry.shape("turtle")
# brian.color("green")
# brian.penup()
# brian.shape("turtle")
# hugh.color("yellow")
# hugh.penup()
# hugh.shape("turtle")
# new_turtle.goto(x=-200,y=-25)
# larry.goto(x=-200,y=75)
# brian.goto(x=-200,y=25)
# hugh.goto(x=-200,y=-75)
# bet_color=sc.textinput(title="your bet",prompt="which color do you bet on")
# sc.exitonclick()