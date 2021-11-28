from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE=15
class Snake:
    def __init__(self):
        self.snake=[]
        self.snake_position=STARTING_POSITIONS
        for i in range(3):
            tim=Turtle()
            tim.shape("square")
            tim.color("white")
            tim.speed("fastest")
            tim.penup()
            tim.goto(x=STARTING_POSITIONS[i][0],y=STARTING_POSITIONS[i][1])
            self.snake.append(tim)
        self.heading=self.snake[0] 
    def move(self):
        self.heading.fd(MOVE)
        self.snake_position.insert(0,self.heading.position())
        temp=self.snake_position.pop()
        for i in range(1,len(self.snake)):
            self.snake[i].goto(x=self.snake_position[i][0],y=self.snake_position[i][1])
        return temp
    def add_snake(self,temp):
        tim=Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.speed("fastest")
        tim.goto(temp)
        tim.speed("fast")
        self.snake.append(tim)
        self.snake_position.append(temp)
    def reset(self):
        for sn in self.snake:
            sn.goto(x=1000,y=1000)
        self.snake.clear()
        self.snake=[]
        STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
        self.snake_position=STARTING_POSITIONS
        for i in range(3):
            tim=Turtle()
            tim.shape("square")
            tim.color("white")
            tim.speed("fastest")
            tim.penup()
            tim.goto(x=STARTING_POSITIONS[i][0],y=STARTING_POSITIONS[i][1])
            self.snake.append(tim)
        self.heading=self.snake[0]



    def up(self):
        if self.heading.heading()!=270:
            self.heading.setheading(90)
    def down(self):
        if self.heading.heading()!=90:
            self.heading.setheading(270)
    def left(self):
        if self.heading.heading()!=0:
            self.heading.setheading(180)
    def right(self):
        if self.heading.heading()!=180:
            self.heading.setheading(0)
    
