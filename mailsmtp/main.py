import smtplib
import datetime
import random
import os
user="mewtwo199619@yahoo.com"
with open("quotes.txt",mode="r") as file:
    quotes=file.readlines()
todays_quote=random.choice(quotes)
date=datetime.datetime.now()
year=date.year
day=date.weekday()
print(day)
if (day==1):
    with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
        connection.starttls()
        connection.login(user=user,password=os.environ.get("yahoopass"))
        connection.sendmail(from_addr=user, to_addrs="shehzinps@gmail.com",msg=f"subject:Mondays quote\n\n{todays_quote}")