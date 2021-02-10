# # get the data from the weather_data.csv file and include it in a list
#
# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # PYTHON INBUILT CSV LIBRARY IS HELPFUL
#
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         temperature = row[1]
# #         if temperature != "temp":
# #             temperature = int(temperature)
# #             temperatures.append(temperature)
# #     print(temperatures)
#
# # USING CSV WAS A LOT OF WORK SO LET'S USE PANDAS INSTEAD
# # import pandas
# #
# # data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # IN PANDAS:
#     # DATA FRAME = TABLE
#     # SERIES = COLUMN
#
# # USING PANDAS functions
# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(f"Turned data to a dictionary\n{data_dict}")
#
# # calculate the average temperature
#     # get the temperatures in a list
# temperatures = data["temp"]
# temp_list = temperatures.to_list()
# print(temp_list)
#
#     # find and print the average
# sum = 0
# for val in temp_list:
#     sum+= val
# average = sum / len(temp_list)
# print(f"The average is: {(average)}")
# print(f"The rounded average is: {round(average)}")
#
# print(data["temp"].mean())
# # find the max value in the column
# print(data["temp"].max())
#
# # Get data from columns
# # data[COLUMN_NAME] OR data.COLUMN_NAME
#
# # Get data in Row
# print(data[data.day == "Monday"])
#
# # which row of data had the highest temperature of the week
#
# # get the highest temp
# highest_temp = data["temp"].max()
# # find the row
# print(data[data.temp == highest_temp])
#
#
# # get monday's temp and convert it to fahrenheit
# monday = data[data.day == "Monday"]
# # convert the value to an int
# monday_temp = int(monday.temp)
# print(monday_temp)
# print(f"Monday's temperature in celsius is: {monday_temp}")
# # convert the temp to fahrenheit
# monday_temp_fahrenheit = (monday_temp * (9/5)) + 32
# print(f"Monday's temperature in fahrenheit is: {monday_temp_fahrenheit}")
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "grades": [68, 80, 90]
# }
# saksham_data_frame = pandas.DataFrame(data_dict)
# # output the data frame to a csv file
# saksham_data_frame.to_csv("new_from_data_frame.csv")

# Problem: find the count of squirrels with grey, red, and black fur

# read the csv file and store the data frame in a variable
import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# find how MANY rows there are that have Primary Fur Color as gray
grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# find how MANY rows there are that have Primary Fur Color as cinnamon
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# find how MANY rows there are that have Primary Fur Color as gray
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

# # get the color of the fur and get the count
# grey_row = squirrel_data
# grey_count = 0
# red_count = 0
# black_count = 0
# # loop through the entire column and increment each time there is a color like gray, cinnamon etc
# for color in squirrel_data["Primary Fur Color"]:
#     if color == "Gray":
#         grey_count += 1
#     elif color == "Cinnamon":
#         red_count += 1
#     elif color == "Black":
#         black_count += 1

# create a data frame and output the new data frame in a new file called "squirrel_count.csv"
dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}
data_frame = pandas.DataFrame(dict)
data_frame.to_csv("squirrel_count.csv")