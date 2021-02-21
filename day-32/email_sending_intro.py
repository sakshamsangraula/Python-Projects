# Send an email from a google account to another google account
import smtplib

# email = "pythoncodetesting123@gmail.com"
# password = "pythoncodetesting1()"

# # establish a connection object of the sender email server
# connection = smtplib.SMTP("smtp.gmail.com")
# # make sure to start tls when sending the email
# connection.starttls()
# # login to the email sender
# connection.login(user=email, password=password)
# # finally send the email to the receiver
# connection.sendmail(from_addr=email, to_addrs="python.coding.email@gmail.com",
#                     msg="Subject:Python Email\n\n Hey hey this is python email")
# # close the connection
# connection.close()

# another way to send emails without having to close the connection (it will automatically close it)
# import smtplib
# email = "pythoncodetesting123@gmail.com"
# password = "pythoncodetesting1()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection_obj:
#     connection_obj.starttls()
#     connection_obj.login(user=email, password=password)
#     connection_obj.sendmail(from_addr=email, to_addrs="python.coding.email@gmail.com",
#                             msg="Subject:Coding\n\nPython is great!")


# Using datetime module in python
# import datetime as dt
#
# time_rn = dt.datetime.now()
# year = time_rn.year
# month = time_rn.month
# day_of_week = time_rn.weekday()
# print(f"This year is {year}, and is month  {month} and the day of the week is {day_of_week}")
#
# my_DOB = dt.datetime(year=2000, month=12, day=20, hour=5)
# print(my_DOB)