import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "dhesika.info@gmail.com"
MY_PASSWORD = "rnatmzhhdspbyjte"

MY_LAT = 9.944720
MY_LONG = 78.130783


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude <= MY_LAT + 5 and iss_longitude >= MY_LAT - 5) and (
            iss_latitude >= MY_LONG - 5 and iss_latitude <= MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if time_now > sunset and time_now < sunrise:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="dhesika@myyahoo.com",
                            msg="Subject: ISS Overhead\n\nLook Up👆\n"
                                "ISS is above you in the sky.")
