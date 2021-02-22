
import requests
import os
from twilio.rest import Client

api_key = os.environ.get("API_KEY")

MY_LAT = -19.881740
MY_LONG = -43.928200

parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# call the api so that we only get the hourly forecast for 48 hours
result = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
result.raise_for_status()
data = result.json()

# loop through all the first 12 hours and if the hour's weather id is less than 700
# tell the user to bring an umbrella
# for hour in range(0, 12):
#     weather_id = data["hourly"][hour]["weather"][0]["id"]
#     if weather_id < 700:
#         print("Bring an umbrella!")

# Use the splice method in python to do the same thing
# make a list that has first 12 hourly data
hourly_splice = data["hourly"][:12]


will_rain = False
# loop through the data and get info from there
for hour_data in hourly_splice:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    # send a text message to the verified number using twilio if it will rain today
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It might rain today, Bring an umbrella ☂",
        from_= os.environ.get("FROM_PHONE"),
        to= os.environ.get("TO_PHONE")
    )

    # print status so we can make sure that the message was sent
    print(message.status)