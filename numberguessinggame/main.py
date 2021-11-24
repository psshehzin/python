import random
from os import system
choice='y'
while(choice=='y'):
    numbers=[i for i in range(0,101)]
    cnum=random.choice(numbers)
    gameon=True
    system("Clear")
    y=input("Do you want to play easy (e) or hard (h) ")
    y.lower()
    if y=='h':
        count=5
    else:
        count=10
    print(f"You will be having max {count} attempts")
    while(gameon):
        print("guess the computers choice its between 1 and 100")
        num=int(input())
        system("clear")
        if num<cnum:
            print(f"{num} Too low")
        elif num>cnum:
            print(f"{num} Too high")
        elif num==cnum:
            print(f"great job you won the computers choice was {cnum}")
            break
        count=count-1
        if count==0:
            print(f"You are out of attempts looser you loose booo computers choice was {cnum}")
            break
    choice=input("Do you wnat to go for another round y or n ")
    system("Clear")
