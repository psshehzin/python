import menu


def choice():
    ch = input("What would you like? (espresso/latte/cappuccino/reports/):")
    return ch
def getmoney(user_choice):
    print("insert the coins")
    q=int(input("how many quarters"))
    d=int(input("How many dimes"))
    n=int(input("How many nickeles"))
    p=int(input("How many pennies"))
    tot=q*0.25+d*0.1+n*0.05+p*0.01
    if tot <  menu.MENU[user_choice]["cost"]:
        print(f"Sorry {user_choice} cost is {menu.MENU[user_choice]['cost']} you only inserted {tot}")
        return 0,False
    elif tot>=menu.MENU[user_choice]["cost"]:
        chg=tot-menu.MENU[user_choice]["cost"]
        print(f"your drink will be brewed now and hers your change {chg}")
        return menu.MENU[user_choice]["cost"], True
    


def reports(ch, money):
    print(f"Water: {ch['water']}")
    print(f"Milk: {ch['milk']}")
    print(f"Cofee: {ch['coffee']}")
    print(f"Money: {money}")
def brew(user_choice, local_resources,money):
    brewd=True
    current_resources={}
    for i in local_resources:
        current_resources[i]=local_resources[i]
    for i in local_resources:
        if i not in menu.MENU[user_choice]["ingredients"]:
            continue
        if local_resources[i]<menu.MENU[user_choice]["ingredients"][i]:
            print(f"you do not have enough {i}")  
            brewd=False
        else:
            current_resources[i]=current_resources[i]-menu.MENU[user_choice]["ingredients"][i]
    
            
    if brewd:
        cash, mon=getmoney(user_choice)
        money=money+cash
        if mon:
            brewd=True
            print(f"here you go a {user_choice}")
            return current_resources, money
        else:
            brewd=False
            print("you are short on money" )
            return local_resources, money
        
local_resources=menu.resources
done=True
cash=0
while(done):
    user_choice = choice()
    if user_choice == 'reports':
        reports(local_resources,cash)
    elif user_choice in ["cappuccino","latte","espresso"]:
        local_resources, cash=brew(user_choice, local_resources,cash)
        print(local_resources)
    elif user_choice=="oFF":
        done=False
    else:
        print("Please select one from the available brews: cappuccino, latte or espresso ")

