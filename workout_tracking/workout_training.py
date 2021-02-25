# imports
import requests
import datetime as dt
import os

# Constants
APP_ID = os.environ.get("APP_ID_WORKOUT")
API_KEY = os.environ.get("API_KEY")
EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")
SHEETS_ENDPOINT = os.environ.get("SHEETS_ENDPOINT")
print(f"app id is {APP_ID} and api key is {API_KEY} and eendpoint is {EXERCISE_ENDPOINT},"
      f"sheets endpoint is {SHEETS_ENDPOINT}")
ID = 2

# use the natural language for api documentation
exercise_params = {
    "query": input("Tell me which exercises you did: ")
}
# all the values should be a string
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_headers)
exercise_response_json = exercise_response.json()
exercises_list = exercise_response_json["exercises"]

# calculate the date and time now
now = dt.datetime.now()
date = now.date()
# format the date in the correct format
formatted_date = date.strftime("%m/%d/%Y")
time = str(now.time()).split(".")
formatted_time = time[0]

# get the first row
second_row = requests.get(url="https://api.sheety.co/31d36a2889de2ae9ef7977069805f0d2/workoutsProject/workouts/2").json()
second_row_values = second_row["workout"]
keys = []
for key in second_row_values:
    keys.append(key.title())


# get the exercise name, duration, and calories from the response
index = 0
for exercise in exercises_list:
    ID+=1
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    # create parameters to create a row in spreadsheet
    sheets_params = {
        # MAKE SURE ALL THE KEYS ARE LOWERCASE (took a long time to figure this out lol)
            "workout": {
                "date": formatted_date,
                "time": formatted_time,
                "exercise": exercise_name,
                "duration": duration,
                "calories": calories,
            }
    }

    sheets_header = {
        "Content-Type": "application/json"
    }

    sheets_row_creation = requests.post(url=SHEETS_ENDPOINT,
                                        json=sheets_params,
                                        headers=sheets_header,
                                        auth = ('user', 'pass'))
    print(sheets_row_creation.status_code)

    # add these values to google sheets
