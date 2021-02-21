import requests
from datetime import datetime

LAT = 51.507351
LONG = -0.127758
# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response)
#
# # raise an error if there is an error with the api response
# response.raise_for_status()
#
# # get the data
# data = response.json()
# print(data)
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude, longitude)
#
# print(iss_position)

# parameters = {
#     "lat": LAT,
#     "lng": LONG
# }
# response = requests.get("https://sunrise-sunset.org/api", params=parameters)
# # response.raise_for_status()
# print(response.json())

LATITUDE = 51.507351
LONGITUDE = -0.127758
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
json_response = response.json()
# use the split function to only get the actual hour number
sunrise = int(json_response["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(json_response["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
print(f"Rise set is: {sunrise} and sunset is {sunset} and time now is {time_now}")