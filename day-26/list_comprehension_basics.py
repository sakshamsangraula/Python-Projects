# original way
# list = [1, 2, 3]
# new_list = []
#
# for num in list:
#     new_num = num + 1
#     new_list.append(new_num)
#
# print(new_list)

# new way
# SYNTAX: new_list = [ new_keyword for keyword in list ]
# list = [1, 2, 3]
# new_list = [n+1 for n in list]
# print(new_list)

# with letters
# name = "Saksham"
# new_list = [letter for letter in name]
# print(new_list)

# with range
# new_list = [ num*2 for num in range(1, 5)]
# print(new_list)

# names = ["Saksham", "Jeff", "Andy", "Sundar"]
# # short_names = [name for name in names if len(name) < 5]
# # print(short_names)
# capital_names = [name.upper() for name in names if len(name) > 5]
# print(capital_names)

# Squared numbers
# list = [1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in list]
# print(squared_numbers)

# find even numbers
# list = [1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [num for num in list if num % 2 == 0]
# print(even_numbers)

# Read the numbers from both files

# list_1 = []
# with open("file1.txt") as file1:
#     list_1 = file1.readlines()
#
# list_2 = []
# with open("file1.txt") as file2:
#     list_2 = file2.readlines()
#
# common_list = [int(num) for num in list_1 if num in list_2]
# print(common_list)

# list_2 = []
# with open("./file2.txt") as second_file:
#     list_2.append((second_file.read()))
# print(list_2)

#################### List Comprehension Dictionary ########################3
# names = ["Saksham", "Serena", "Indra", "Andy", "Satya", "Sundar"]
# # create a dictionary and assign each name with a random score
# import random
# names_dict = {name:random.randint(1,100) for name in names}
#
# # USE <DICT>.ITEMS() WHEN ACCESSING KEY AND VALUE
# passed_students = {student:score for (student, score) in names_dict.items() if score > 60}
# print(passed_students)

# Dictionary Pracice: dictionary with words and their length
# sentence = "Hello, my name is Saksham!"
# words_list = sentence.split()
#
# words_dict = {word:len(word) for word in words_list}
# print(words_dict)

# convert a dictionary of temp to fahrenheit
# weather = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# fahrenheit_weather = {day: round((5/9 * temp) + 32, 1)  for (day, temp) in weather.items()}
# print(fahrenheit_weather)

# Iterating over pandas dataframe
student_dict = {
    "Student": ["Saksham", "Andy", "Sundar"],
    "Score": [99, 98, 97]
}
import pandas
# create a dataframe
df = pandas.DataFrame(student_dict)
# loop through the rows of the data frame
for (index, row) in df.iterrows():
    if row.Student == "Saksham":
        print(row["Score"])


