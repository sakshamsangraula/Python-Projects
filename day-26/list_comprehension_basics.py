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

list_1 = []
with open("file1.txt") as file1:
    list_1 = file1.readlines()

list_2 = []
with open("file1.txt") as file2:
    list_2 = file2.readlines()

common_list = [int(num) for num in list_1 if num in list_2]
print(common_list)

# list_2 = []
# with open("./file2.txt") as second_file:
#     list_2.append((second_file.read()))
# print(list_2)
