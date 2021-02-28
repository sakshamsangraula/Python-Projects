import requests
import datetime as dt
import os

FLIGHT_SEARCH_API_KEY = os.environ.get("TEQUILA_API_KEY")
FLIGHT_SEARCH_URL = "https://tequila-api.kiwi.com"

# This class is responsible for talking to the Flight Search API.

class FlightSearch:

    def __init__(self):
        pass

    # get the iata code
    def get_iata_code(self, city):
        header = {
            "apikey": FLIGHT_SEARCH_API_KEY
        }
        iata_params = {
            "term": city,
            "location_types": "city"
        }
        iata_code = requests.get(url=f"{FLIGHT_SEARCH_URL}/locations/query",
                                 headers=header, params=iata_params)
        iata_code_json = iata_code.json()
        output_list = iata_code_json["locations"]
        code = output_list[0]["code"]
        return code

    # get the price of the flight
    def get_price(self, row):
        print(row)
        header = {
            "apikey": FLIGHT_SEARCH_API_KEY,
            "Content-Encoding": "gzip"
        }
        now_date = dt.datetime.now()
        formatted_date_now = now_date.strftime("%m/%d/%Y")
        # use the time delta function to add 6 months (6*30 days)
        destination_date = now_date + dt.timedelta(days=180)
        formatted_destination_date = destination_date.strftime("%m/%d/%Y")
        return_min_date = destination_date + dt.timedelta(days = 7)
        formatted_return_min_date = return_min_date.strftime("%m/%d/%Y")
        return_max_date = destination_date + dt.timedelta(days = 28)
        formatted_return_max_date = return_max_date.strftime("%m/%d/%Y")

        get_price_params = {
            "fly_from": row["iataCode"],
            "date_from": formatted_date_now,
            "fly_to": "LON",
            "date_to": formatted_destination_date,
            # "return_from": formatted_return_min_date,
            # "return_to": formatted_return_max_date,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        # get the price from the api
        response = requests.get(url=f"{FLIGHT_SEARCH_URL}/v2/search", json=get_price_params, headers=header)

        print(response.status_code)


