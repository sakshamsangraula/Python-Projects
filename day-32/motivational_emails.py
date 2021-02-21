# read the data from quotes.txt
with open("quotes.txt", mode="r") as quotes_file:
    # read the content as a list using the readlines function
    quotes_list = quotes_file.readlines()

# if the day is Saturday then pick a random quote from the list and send the quote in an email to me
import datetime as dt
import smtplib
import random

day_of_week = dt.datetime.now().weekday()
if day_of_week == 5:
    quote = random.choice(quotes_list)
    email = "pythoncodetesting123@gmail.com"
    password = "pythoncodetesting1()"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="saksham.sangraula@acmutd.co",
                            msg=f"Subject:Motivational Quote\n\n{quote}")

