import datetime as dt
import pandas
import smtplib
import random
import details

MY_EMAIL = details.email
MY_PASSWORD = details.password


this_month = dt.datetime.now().month
this_day = dt.datetime.now().day

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient="records")

for data in data_list:
    if data['month'] == this_month and data['day'] == this_day:
        with open(f"letter_templates/letter_"
                  f"{random.randint(1,3)}.txt") as letter:
            content = letter.read()
            wishes = content.replace('[NAME]', data['name'])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, "dhesika@myyahoo.com"
                                , msg=f"Subject: Birthday wishes\n\n{wishes}")
