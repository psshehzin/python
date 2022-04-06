import requests
import datetime
endpoint1="https://pixe.la/v1/users"
user="shehzin"
token="pixelatoken"
graphid="graph1"
# parameters={
#     "token": "pixelatoken",
#     "username": "shehzin",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# reqstatus=requests.post(url=endpoint1,json=parameters)
# print(reqstatus.text)
graphendpoint=f"{endpoint1}/{user}/graphs"
# parameters={
#     "id": "graph1",
#     "name": "Hour tracker",
#     "unit": "Hours",
#     "type": "float",
#     "color": "shibafu"
# }
header={
    "X-USER-TOKEN": token
}
# response=requests.post(url=graphendpoint,headers=header,json=parameters)
# print(response.text)
pixupdate=f"{endpoint1}/{user}/graphs/{graphid}"
# parameters={
#     "date": 
#     "name": "Hour tracker",
#     "unit": "Hours",
#     "type": "float",
#     "color": "shibafu"
# }
qty=input("productivehours today: ")
day=datetime.datetime.today().strftime("%Y%m%d")
parameters={
    "date": day,
    "quantity": qty

}
response=requests.post(url=pixupdate,json=parameters,headers=header)
print(response.text)