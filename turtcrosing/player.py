from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)
        self.color("white")
    def move(self):
        self.fd(MOVE_DISTANCE)
    def moveb(self):
        self.backward(MOVE_DISTANCE)
    def didwin(self):
        if self.ycor()>=FINISH_LINE_Y:
            self.goto(0, -280)
            return True
        else:
            return False
        

    
