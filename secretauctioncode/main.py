from os import system
auc={}
ch="yes"
while(ch=="yes"):
    name=input("enter your name: ")
    bid=int(input("put in your bid ammount :RS "))
    auc[name]=bid
    ch="are there more bidders yes or no: "


    while not(ch.lower()=="yes" or ch.lower()=="no"):
        ch=input("please type either yes or no: ")
    system("clear")

bids=[i for i in auc.values()]
winbid=max(bids)
for i,j in auc.items():
    if j==winbid:
        print(f"{i} has won the bid, Bid ammount was {j}")

