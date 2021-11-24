from gam_data import data
import random
from os import system
list1=data
score=0
notdone=True
a=random.choice(list1)
list1.remove(a)
while(notdone):
  b=random.choice(list1)
  list1.remove(b)
  print(f"A: {a['name']} a {a['description']} from {a['country']}")
  print("")
  print("or")
  print("")
  print(f"B: {b['name']} a {b['description']} from {b['country']}")
  print("")
  choice=input("Who has more followers in insta A or B ")
  if choice=='A' and a['follower_count']>b['follower_count']:
    print("")
    system("clear")
    print("you where right")
    a=b
    score+=1
  elif  choice=='B' and b['follower_count']>a['follower_count']:
    print("")
    system("clear")
    print("you where right")
    a=b
    score+=1
  elif(len(list1)==0):
    print(f"you are the ultimate pro we are no match for you {score}")
  else:
    system("clear")
    print(f"you were wrong score is {score}")
    notdone=False