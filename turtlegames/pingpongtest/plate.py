from turtle import Turtle,Screen
import time
def create_turtle():
        tim=Turtle()
        tim.shape("square")
        tim.shapesize(1)
        tim.penup()
        return tim
class Plate:
    def __init__(self,plate_length=5):
        self.plates=[]
        self.positions=[]
        self.keys={up:False,down:False}
        self.eupflag=0  
        tim=create_turtle()
        tim.goto(-251,0)
        self.plates.append(tim)
        self.positions.append((-251,0))
        for i in range(0,plate_length):
            self.extend()
    def extend(self):
        tim=create_turtle()
        if self.eupflag==0:
            tempcor=self.positions[-1]
            tim.goto(x=tempcor[0],y=tempcor[1]-20)
            self.plates.append(tim)
            self.positions.append((tempcor[0],tempcor[1]-20))
            self.eupflag=1
        else:
            tempcor=self.positions[0]
            tim.goto(x=tempcor[0],y=tempcor[1]+20)
            self.plates.insert(0,tim)
            self.positions.insert(0,(tempcor[0],tempcor[1]+20))
            self.eupflag=0
    def onclick1(self):
        self.keys[up]=True
        self.moveup()
    def onrelease1(self):
        self.keys[up]=False
    def onclick2(self):
        self.keys[down]=True
        self.movedown()
    def onrelease2(self):
        self.keys[down]=False
    def moveup(self):
        while(plate.keys[up]):
            for i in range(len(self.positions)):
                self.positions[i]=(self.positions[i][0],self.positions[i][1]+15)
                self.plates[i].goto(self.positions[i])
            sc.update()
            time.sleep(0.0166)
    def movedown(self):
        while(plate.keys[down]):
            for i in range(len(self.positions)):
                self.positions[i]=(self.positions[i][0],self.positions[i][1]-15)
                self.plates[i].goto(self.positions[i])
            sc.update()
            time.sleep(0.03)
up="w"
down="s"
plate=Plate(5)
sc=Screen()
sc.tracer(0)
sc.update()
sc.listen()
sc.onkeypress(fun=plate.onclick1,key=up)
sc.onkeyrelease(fun=plate.onrelease1,key=up)
sc.onkeypress(fun=plate.onclick2,key=down)
sc.onkeyrelease(fun=plate.onrelease2,key=down)

def addkey(self,key):
    self.keys[key]=False
def is_keypressed(self):
    print(self.keys)
    self.keys[up]=1
    self.moveup()
def is_keyreleased(self):
    print(self.keys[up])
    self.keys[up]=False
        

sc.exitonclick()
 
