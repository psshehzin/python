import pandas
# data=pandas.read_csv("squirreldata.csv")
# colors=[]
# count={}
# colorlist=data["Primary Fur Color"].to_list()
# for color in colorlist:
#     if color not in colors:
#         colors.append(color)
#         count[color]=1
#     else:
#         count[color]+=1
# countlist=[]
# for color in colors:
#     countlist.append(count[color])
# dict={"colors":colors,"number of squirels":countlist}
# df=pandas.DataFrame(dict)
# df.to_csv("colordat.csv")
data=pandas.read_csv("squirreldata.csv")
countgraysq=len(data[data["Primary Fur Color"]=="Gray"])
countredsq=len(data[data["Primary Fur Color"]=="Cinnamon"])
countblacksq=len(data[data["Primary Fur Color"]=="Black"])
dict={"squirrel color":["Gray","Black","Red"], "Squirrel count":[countgraysq,countredsq,countblacksq]}    
df=pandas.DataFrame(dict)
df.to_csv("squirrelcolordat.csv")