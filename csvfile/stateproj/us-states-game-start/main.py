from os import stat
from turtle import Turtle,Screen,onscreenclick
import pandas
import turtle
# turtle function to get x,y vordintaes of area of click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# onscreenclick(get_mouse_click_coor)
screen=Screen()
image="blank_states_img.gif"
screen.addshape(image)
bg=Turtle()
bg.shape(image)
data=pandas.read_csv("50_states.csv")
xcors=(data.x).to_list()
ycors=(data.y).to_list()
states=(data.state).to_list()
datadict={}
for i in range(len(states)):
    datadict[states[i]]=(xcors[i],ycors[i])
#maincodestart
wturtle=Turtle()
wturtle.hideturtle()
game_on=True
correct=0
leng=len(states)
while(game_on and correct<50):
    statechoice=screen.textinput(title=f"states found {correct}/{leng}",prompt="Enter the US state name first letter caps or exit to exit")
    if statechoice in states:
        wturtle.penup()
        wturtle.goto(datadict[statechoice])
        wturtle.pendown()
        wturtle.write(statechoice, move=False, align="center", font=["Arial",8, 'normal'])
        correct+=1
        states.remove(statechoice)

    elif statechoice=="exit":
        print("the states that were not guessed can be found in statesmissed.csv")
        dict={"states missed":states}
        df=pandas.DataFrame(dict)
        df.to_csv("statesmissed.csv")
        game_on=False
        
# easy way to access x cordintaes
# turtle.mainloop()
# row=data[data.state=="Hawaii"]
# print(row)
# print(int(row.x))

