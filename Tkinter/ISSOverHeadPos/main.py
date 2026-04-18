import smtplib
from platform import system
from time import sleep

import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

my_email = "hpaks23@gmail.com"
my_password = "glzatfmojxgmhezj"
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def iss_pos_over_me():
    response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
    response.raise_for_status()
    data = response.json()
    longitude = float(data['longitude'])
    latitude = float(data['latitude'])
    if abs(longitude - MY_LONG) < 6 and abs(latitude - MY_LAT) < 6:
        if check_if_its_dark():
            send_email()

def check_if_its_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour <= sunrise

def send_email():
    smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(user=my_email,password=my_password)
    smtp.sendmail(to_addrs="hpaks01@gmail.com",
                  from_addr=my_email,
                  msg="Subject:ISS over you/n/n Look up!!"
                  )

while True:
    iss_pos_over_me()
    print(datetime.now())
    sleep(60)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



