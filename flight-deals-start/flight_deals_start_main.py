#This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

# create a DataManager object to find a list of cities
data_manager = DataManager()
flight_search = FlightSearch()

# create a FlightSearch object to get more information on the IATA code for the cities
sheets_data = data_manager.get_info_list()

# if row iatacode is blank then fill it in
prices = []
if sheets_data[0]["iataCode"] == "":
    new_sheets_data = sheets_data
    for row in new_sheets_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])

    sheets_data = new_sheets_data
    data_manager.put_iata_codes(sheets_data)


for row in sheets_data:
    print("Calling get price.....")
    prices.append(flight_search.get_price(row))

print(prices)

    # put the iatacodes in google sheets

# iata_codes = flight_search.get_iata_code(cities_list)
# data_manager.put_iata_codes(iata_codes)

