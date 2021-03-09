from bs4 import BeautifulSoup
import requests
import smtplib
import os
from email.message import EmailMessage

URL = os.environ.get("PRODUCT_URL")
TARGET_PRICE = 200
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
TO_ADDRESS = os.environ.get("TO_ADDRESS")

# scrape the html page and get the product name and the price information
header = {
    "User-Agent": os.environ.get("USER_AGENT"),
    "Accept-Language": os.environ.get("ACCEPT_LANGUAGE")
}
response = requests.get(url=URL, headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
price = soup.find(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
product_name = soup.find(name="h1", id="title", class_="a-size-large a-spacing-none").getText()
product_name = product_name.strip("\n")
product_name = product_name.strip("b'")
amazon_price = float(price.split("$")[1])

# send an email with the product name and price when the price in amazon is less than the target price
if amazon_price < TARGET_PRICE:
    smtp_server = "smtp.gmail.com"
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        msg = EmailMessage()
        main_message = f"{product_name.encode('utf-8')} is now ${amazon_price}\n{URL}!!\nBuy it now!"
        msg.set_content((main_message))
        msg['Subject'] = 'Amazon Price Alert!'
        msg['From'] = USERNAME
        msg['To'] = TO_ADDRESS
        connection.send_message(msg)
