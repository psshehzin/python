#in line 67 give your password for mail
import requests
import datetime
import smtplib
import os
user="mewtwo199619@yahoo.com"
UTCISTDIFF="+05:30"
LAT=10.015861
LONG=76.341866
def isnear(islat,islon):
    if (-5<(islat-LAT)<5 and -5<(islon-LONG)<5):
        return True
    else:
        return False

def utcistconverter(time,utcdiff):
    hour=int(time.split(":")[0])
    minute=int(time.split(":")[1])
    if utcdiff[0]=='+':
        hour=hour+int(utcdiff[1:].split(":")[0])
        minute=minute+int(utcdiff[1:].split(":")[1])
        if minute>=60:
            hour=hour+1
            minute=minute-60
        if hour>24:
            hour=hour-24
    else:
        hour=hour-int(utcdiff[1:].split(":")[0])
        minute=minute-int(utcdiff[1:].split(":")[1])
        if minute<0:
            minute=60+minute
            hour=hour-1
        if hour<0:
            hour=24+hour
    if hour in range(0,10):
        hour="0"+str(hour)
    if minute in range(0,10):
        minute="0"+str(minute)
    return(":".join([str(hour),str(minute)]))
parameters={
"lat": LAT,
"lng": LONG,
"formatted": 0
}

sunrisset=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
sunrisset.raise_for_status()
sunrisetime=sunrisset.json()["results"]["sunrise"]
sunsettime=sunrisset.json()["results"]["sunset"]
time=datetime.datetime.now()
sunrisetimeformfunc=sunrisetime.split("T")[1].split("+")[0]
sunsettimeformfunc=sunsettime.split("T")[1].split("+")[0]
#params required in format 00:00,+00:00
sunriseist=utcistconverter(sunrisetimeformfunc,UTCISTDIFF)
hourrise=int(sunriseist.split(":")[0])
sunsetist=utcistconverter(sunsettimeformfunc,UTCISTDIFF)
hourset=int(sunsetist.split(":")[0])
#formatting time
hournow=int(time.hour)
if not (hourrise<hournow<hourset):
    isspos=requests.get(url="http://api.open-notify.org/iss-now.json")
    isspos.raise_for_status()
    longiss=float(isspos.json()["iss_position"]["longitude"])
    latiss=float(isspos.json()["iss_position"]["latitude"])
    if (isnear(latiss,longiss)):
        with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
            connection.starttls()
            connection.login(user=user,password=os.environ.get("yahoopass"))
            connection.sendmail(from_addr=user, to_addrs="shehzinps@gmail.com",msg="subject:Space station above\n\nHi Shehz\nLook at the sky and see how SpaceStation  me shines for you :p\nwith low MEW")




