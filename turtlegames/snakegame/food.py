from turtle import Turtle
import random
SNAKE_STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().shapesize(0.5)
        super().penup()
        super().color("yellow")
        super().speed("fastest")
        self.X,self.Y=self.new_food_poss(SNAKE_STARTING_POSITIONS)
       
    def new_food_poss(self,snakecords):
        X=random.randint(-290,290)
        Y=random.randint(-290,290)
        while (X,Y) in snakecords:
            X=random.randint(-290,290)
            Y=random.randint(-290,290)
        self.goto(x=X,y=Y)
        return X,Y

        

