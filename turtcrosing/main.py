import time
from turtle import Screen
from player import Player
from car_manager import CarManager,STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard
score=Scoreboard()
def detect_collision(turtle,cars):
    for car in cars:
        if -20<car.xcor()<20:    
            if -20<(car.ycor()-turtle.ycor())<20:
                if -40<(turtle.xcor()-car.xcor())<40:
                    return False
        else:
            continue
    return True
screen = Screen()
screen.setup(width=600, height=800)
turtle=Player()
screen.tracer(0)
screen.listen()
screen.bgcolor("black")
cars=[]
game_is_on = True
flag=0
time1=0.1
while game_is_on:
    if flag==0:
       cars.append(CarManager(STARTING_MOVE_DISTANCE))
       flag+=1
    else:
        if flag==5:
            flag=0
        else:
            flag+=1
    if len(cars)>=24:
        screen.onkey(fun=turtle.move,key="Up")
        screen.onkey(fun=turtle.moveb,key="Down")
    didcross=turtle.didwin()
    if didcross:
        score.score+=1
        score.update()
        if time1>0.00:
            time1-=0.02
    game_is_on=detect_collision(turtle,cars)
    if not game_is_on:
        score.game_over()
    CarManager.move(cars)
    if (len(cars)>24):
        cars.pop(0)
    screen.update()
    if not len(cars)<24:
        time.sleep(time1)
screen.exitonclick()