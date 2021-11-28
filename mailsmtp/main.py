import smtplib
import datetime
import random
user="mewtwo199619@yahoo.com"
with open("quotes.txt",mode="r") as file:
    quotes=file.readlines()
todays_quote=random.choice(quotes)
date=datetime.datetime.now()
year=date.year
day=date.weekday()
print(day)
if (day==5):
    with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
        connection.starttls()
        connection.login(user=user,password="PASSWORD")
        connection.sendmail(from_addr=user, to_addrs="shehzinps@gmail.com",msg=f"subject:Mondays quote\n\n{todays_quote}")