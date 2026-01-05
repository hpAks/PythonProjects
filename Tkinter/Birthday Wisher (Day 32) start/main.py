import smtplib

my_email = "hpaks23@gmail.com"
password = "glzatfmojxgmhezj"

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hpaks01@gmail.com",
            msg="Subject:Hello\n\n "+quote
        )


import datetime as dt, pandas
import random

if dt.datetime.now().weekday()==3:
    with open(file="quotes.txt", mode="r") as quote_file:
        quote = quote_file.readline(random.randint(0,100))
        send_email(quote)



