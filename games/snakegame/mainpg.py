import snake
import time
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
from turtle import Turtle
def draw_border(width):
    tim=Turtle()
    tim.color("blue")
    tim.hideturtle()
    tim.speed("fastest")
    tim.penup()
    tim.goto(width,0)
    tim.pendown()
    tim.left(90)
    tim.fd(width)
    for i in range(3):
        tim.left(90)
        tim.fd(2*width)
    tim.left(90)
    tim.fd(width)
speed="fastest"
WIDTH=295  
UP="w"
DOWN="s"
LEFT="a"
RIGHT="d"
sc=Screen()
sc.setup(width=800,height=800)
sc.bgcolor("black")
sc.title("The Snake")
draw_border(WIDTH)
score=Scoreboard()
score.write(f"SCORE :  HighScore : {score.highscore} ", move=False, align="center", font=["Arial",20, 'normal'])
sc.update()
fd=Food()
sc.listen()
snakeob=snake.Snake()
sc.onkeypress(fun=snakeob.up,key=UP)
sc.onkeypress(snakeob.down,DOWN)
sc.onkeypress(snakeob.left,LEFT)
sc.onkeypress(snakeob.right,RIGHT)
sc.tracer(0)
while(True):
    
    temp=snakeob.move()
    time.sleep(0.04)
    sc.update()
# if (snakeob.heading.xcor() in range(fd.X-15,fd.X+16) and snakeob.heading.ycor() in range(fd.Y-15,fd.Y+16)):
    if snakeob.heading.distance((fd.X,fd.Y))<15:
        score.score_update()
        sc.update()
        snakeob.add_snake(temp)
        fd.X,fd.Y=fd.new_food_poss(snakeob.snake_position)
        sc.update()
    if (snakeob.heading.xcor()>300 or snakeob.heading.xcor()<-300) or (snakeob.heading.ycor()>300 or snakeob.heading.ycor()<-300):
        score.reset()
        score.write(f"SCORE : {score.score}  HighScore : {score.highscore}", move=False, align="center", font=["Arial",20, 'normal'])
        snakeob.reset()
        sc.update()
       
        
    
    for i in snakeob.snake_position[1:]:
        flag=0
        if (snakeob.heading.distance(i)<8):
            score.reset()
            flag=1
            score.write(f"SCORE : {score.score}  HighScore : {score.highscore}", move=False, align="center", font=["Arial",20, 'normal'])
            snakeob.reset()
            sc.update()
            
    if flag==1:
        break
    
sc.exitonclick()
