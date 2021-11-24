import random
from os import system
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def addval(i,pacards):
    for i in range(0,i):
        pacards.append(random.choice(cards))
    return pacards
compcard=[]
usercard=[]
compcard=addval(2,compcard)
usercard=addval(2,usercard)
choice='y'
while(sum(compcard)<17):
    compcard=addval(1,compcard)
    if 11 in compcard and sum(compcard)>21:
        compcard.remove(11)
        compcard.append(1)

while(choice=='y'):
    system("clear")
    print(f"     computers first card is {compcard[0]}")
    print(f"     you have the cards {usercard}, and totla scor: {sum(usercard)}")
    choice=input("Type y to get another card or n to pass ")
    if choice=='y':
        usercard=addval(1,usercard)
        if sum(usercard)>21 and 11 not in usercard:
            print(f"Bust you loose went sum over 21, your cards {usercard} total {sum(usercard)} ")
            break
        elif sum(usercard)>21 and 11 in usercard:
            usercard.remove(11)
            usercard.append(1)
            if sum(usercard)>21:
                print(f"Bust you loose went sum over 21, your cards {usercard} total {sum(usercard)} ")
                break
    else:
        if sum(usercard)>sum(compcard):
            print(f"you won, Your cards {usercard} and total is {sum(usercard)} and computers cards are {compcard} and total {sum(compcard)}")
            break
        elif sum(usercard)<sum(compcard):
            if sum(compcard)>21:
                print(f"you won openent went bust his cards {compcard} and total {sum(compcard)} and your cards {usercard} and total is {sum(usercard)}")           
            else:
                print(f"you Loose, Your cards {usercard} and total is {sum(usercard)} and computers cards are {compcard} and total {sum(compcard)}")
        elif sum(usercard)==sum(compcard):
            print(f"Draww your cards and total {usercard} {sum(usercard)} computers cards and total {compcard} {sum(compcard)}")
    