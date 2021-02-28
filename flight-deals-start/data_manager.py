import requests
import os

Sheets_API_URL = os.environ.get("SHEETS_API_URL")


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.response = requests.get(url=Sheets_API_URL)
        self.response_json = self.response.json()

    def get_info_list(self):
        # get the city list from google sheets
        info_list = self.response_json["prices"]
        return info_list

    def put_iata_codes(self, sheets_data):
        for dict in sheets_data:
            iata_params = {
                "price": {
                    "iataCode": dict["iataCode"]
                }
            }
            requests.put( url=f"{Sheets_API_URL}/{dict['id']}", json=iata_params)


