##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import datetime
import smtplib
import random
import pandas
user="mewtwo199619@yahoo.com"
numberofletters=3
letterdirectory="letter_templates"
now=datetime.datetime.now()
day=now.day
month=now.month
birthdays=pandas.read_csv("birthdays.csv")
for ind,dates in birthdays.iterrows():
    if dates.day==day and dates.month==month:
        letter=f"./{letterdirectory}/letter_{random.randint(1,numberofletters)}.txt"
        with open(letter, mode="r") as letter:
            message=letter.read()
            message=message.replace('Angela', "Mewtwo")
            message=message.replace('All my love,', "With lots of psychic love and confusion,")
            message=message.replace('[NAME]', dates.names)
            touser=dates.email
            with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
                connection.starttls()
                connection.login(user=user,password=os.environ.get("yahoopass"))
                connection.sendmail(from_addr=user, to_addrs=touser,msg=f"subject:Happy Birthday!!! \n\n{message}")
                


