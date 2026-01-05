##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import random

import pandas, smtplib
my_email = "hpaks23@gmail.com"
my_password = "glzatfmojxgmhezj"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def get_birthday_letter(name):
    try:
        file_name = "letter_templates/"+random.choice(letters)
        print(f"filename:{file_name}")
        with open(file=file_name,mode="r") as birthday_file:
            body = birthday_file.read()
            return body.replace("[NAME]",name)
    except:
        return "Happy Birthday!!"

# 4. Send the letter generated in step 3 to that person's email address.
def send_email(name,email):
    smtp = smtplib.SMTP("smtp.gmail.com",port=587)
    smtp.starttls()
    smtp.login(user=my_email, password=my_password)
    body = get_birthday_letter(name)
    smtp.sendmail(from_addr=my_email,
                  to_addrs=email,
                  msg="Subject:Happy Birthday\n\n"+body)


date = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
for index,row in data.iterrows():
    if row['day'] == date.day and row['month']== date.month:
        send_email(row['name'],row['email'])


