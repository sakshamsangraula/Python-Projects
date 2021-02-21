# ##################### Extra Hard Starting Project ######################
#
# # 1. Update the birthdays.csv
#
# # 2. Check if today matches a birthday in the birthdays.csv
# import datetime as dt
# import pandas
# import random
# import smtplib
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
#
# df = pandas.read_csv("birthdays.csv")
# for index, row in df.iterrows():
#     # see if today matches a birthday
#     if row["year"] == year and row["month"] == month and row["day"] == day:
#        name = row["name"]
#        send_to = row["email"]
#
#
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# # pick a random letter from the letter templates
# random_letter = f"./letter_templates/letter_{random.randint(1,3)}.txt"
#
# with open(random_letter) as birthday_letter:
#     # loop through the letter contents
#     # for line in birthday_letter:
#     #     print(line)
#     #     if "[Name]" in line:
#     #         line.replace("[Name]", name)
#     #         print(f"After{line}")
#     content = birthday_letter.read()
#     content = content.replace("[NAME]", name)
# print(f"Updated content{content}")
# with open(random_letter, mode="w") as birthday_letter:
#     birthday_letter.write(content)
#
# # 4. Send the letter generated in step 3 to that person's email address.
# email="pythoncodetesting123@gmail.com"
# password="pythoncodetesting1()"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email,
#                         to_addrs=send_to,
#                         msg=f"Subject:Happy Birthday!\n\n{content}")
#
#
#


# imports
import datetime as dt
import pandas
import random
import smtplib

# constants
EMAIL = "pythoncodetesting123@gmail.com"
PASSWORD = "pythoncodetesting1()"
today = dt.datetime.now()
now_date_tuple = (today.month, today.day)

# get data from the file
data = pandas.read_csv("birthdays.csv")
# create a dictionary with a tuple as a key and the entire row as the value
birthday_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

# if the day and month right now is in the file then write the letter
if now_date_tuple in birthday_dict:
    # get the letter file randomly
    letter_file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # open the file and read the contents
    with open (letter_file_path) as file:
        contents = file.read()
        # replace the name placeholder with the real name and DON'T FORGET TO SET THE OUTPUT TO THE VARIABLE
        contents = contents.replace("[NAME]", birthday_dict[now_date_tuple]["name"])

# send the email to the receiver with the contents in the letter
with (smtplib.SMTP("smtp.gmail.com")) as connection:
    print(type(birthday_dict[now_date_tuple]["email"]))
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs="saksham.sangraula@gmail.com",
                        msg=f"Subject:Happy Birthday!\n\n{contents}")