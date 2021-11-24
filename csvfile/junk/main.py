# import csv
# with open("weather_data.csv") as file:
#     lines=csv.reader(file)
#     temp=[]
#     for row in lines:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
# print(temp)
import pandas
data=pandas.read_csv("weather_data.csv")
temp=data["temp"].to_list()
# avg=sum(temp)/len(temp)
avg=data["temp"].mean()
max=data["temp"].max()
print(avg,max)
#euther data.temp or data["temp"] can be used
dayrow=data[data.temp==max]
print(dayrow)
t=int(dayrow.temp)
dict1={"names":["shehzin","ash","pikachu"],"scores":[89,76,56]}
dataf=pandas.DataFrame(dict1)
datacsv=dataf.to_csv("genarated.csv")