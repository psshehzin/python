# link to api doc:https://openweathermap.org/api/one-call-api
import os
from twilio.rest import Client
parameters={
    "lat": 10,
    "lon": 76.5,
    "appid": os.environ.get("WEATHER_APIKEY"),
    "exclude": "current,minutely,daily"
}
from datetime import datetime
import requests
rep=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
rep.raise_for_status()
data=rep.json()["hourly"]
lcont=0
for i in data[:12]:
    if (i["weather"][0]["id"])<700:
        print(f"it can rain in {lcont} hours")
        account_sid = "ACdad524c3600e2f8b4fd3f7e5fb0793c1"
        auth_token = os.environ.get("TULIOSECTOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                              body=f'it might rain in {lcont} hours from now',
                              from_='+12285919351',
                              to='+916282649049'
                          )

        print(message.status)
        break
    lcont+=1
