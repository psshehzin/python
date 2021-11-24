
from os import system
import random
import words
import time
b="welcome to hangman yoo"
words.wordstarerr(b,0.5)
print("")
print("you got 3 second before the game and it can be any of us")
print(words.words)
time.sleep(3)
system("clear")
a=random.choice(words.words)
b=[i for i in a]
c=["_" for i in a]
dead=0
d=[]
s="DEAD"
k=0
print(" ".join(c))
print("")
while (dead!=1):
    ch=input("bring it on: ")
    system("clear")

    if ch not in b:
        d.append(s[k])
        words.wordstarerr("".join(d),0.1)
        k=k+1
        if len(d)==4:
            words.wordstarerr("yoo DEAD lost ",0.5)
            break
        
    else:
        for i,j in enumerate(b):
            if(j==ch):
                c[i]=ch
        if c==b:
            print(" ".join(c),0.1)
            words.wordstarerr("hell yea won",0.5)
            break


   
    print(" ".join(c))
    print("")
    





