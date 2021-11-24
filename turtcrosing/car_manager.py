from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ypos=[i for i in range(-250,260,25)]

class CarManager(Turtle):
    def __init__(self,STARTING_MOVE_DISTANCE=5):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.speed("fastest")
        randy=random.choice(ypos)
        self.goto(x=310,y=randy)
        self.color(random.choice(COLORS))
        self.moved=STARTING_MOVE_DISTANCE
    def move(cars):
        for car in cars:
            car.fd(car.moved)

