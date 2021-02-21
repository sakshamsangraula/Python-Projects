import requests
from datetime import datetime
import math
import smtplib
import time

MY_LAT = 3 # Your latitude
MY_LONG = -78 # Your longitude
EMAIL = "pythoncodetesting123@gmail.com"
PASSWORD = "pythoncodetesting1()"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def is_dark():
    time_now_hour = 24
    print(f"sunrise is {sunrise} sunset is {sunset} time rn is {time_now_hour}")

    if time_now_hour >= sunset or time_now_hour <= sunrise:
        return True

def is_close():
    # if the latitude position is + or - within the latitude position and same with longitude then return True
    lat_check = math.fabs(MY_LAT - parameters["lat"])
    lng_check = math.fabs(MY_LONG - parameters["lng"])

    if lat_check <= 5 and lng_check <= 5:
        return True

# put the code inside a while loop so it runs always and also include a time function
# while True:
#     time.sleep(60)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
if is_close() and is_dark():
    print("both dark and close")
    with (smtplib.SMTP("smtp.gmail.com")) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="saksham.sangraula@acmutd.co",
                            msg="Subject:Look Up\n\nYou might see an ISS overhead")

# BONUS: run the code every 60 seconds.



