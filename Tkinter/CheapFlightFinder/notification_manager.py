import smtplib


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.userName = "akslearnpython@gmail.com"
        self.password = "qkpmzvkiazjigqmr"
        self.to_mail = "hpaks01@gmail.com"

    def notification_email(self, data):
        smtp = smtplib.SMTP("smtp.gmail.com", port=587)
        smtp.starttls()
        smtp.login(user=self.userName, password=self.password)
        smtp.sendmail(from_addr=self.userName,
                      to_addrs=self.to_mail,
                      msg=f"Subject:Plan your next trip\n\n{data}")
