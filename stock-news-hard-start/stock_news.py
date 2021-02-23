STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "APIKEY"
NEWS_API_KEY = "APIKEY"
PERCENT_THRESHOLD = 5

TWILIO_ACCOUNT_SID = "ACCOUNTSID"
TWILIO_AUTH_TOKEN = "TWILIOAUTHTOKEN"
SENDING_PHONE_NUM = "SENDINGPHONENUM"
went_up = False

import requests
import datetime as dt
import math
import os
from twilio.rest import Client

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_price_response = requests.get(STOCK_ENDPOINT, params=parameters)
stock_price_response.raise_for_status()
stock_price_response = stock_price_response.json()
daily_data = stock_price_response["Time Series (Daily)"]

# get the exact date of today in the right format
now = str(dt.datetime.now())
now_date = now.split(" ")[0]
print(now_date)

now_time = dt.datetime.now()

yesterday_date = "2021-02-19"
day_before_yesterday_date = "2021-02-18"

# get the closing price for yesterday and day before yesterday and find the difference
yesterday_close_price = float(daily_data[yesterday_date]["4. close"])
day_before_yesterday_close_price = float(daily_data[day_before_yesterday_date]["4. close"])

# if the positive difference between yesterday's and day before yesterday's price is positive or negative 5%
# meaning if there is a 5% decrease or increase in yesterday's price from day before yesterday then print get news
if yesterday_close_price > day_before_yesterday_close_price:
    went_up = True
diff = math.fabs(yesterday_close_price - day_before_yesterday_close_price)
percent = round(diff/day_before_yesterday_close_price * 100)
print(day_before_yesterday_close_price)
print(yesterday_close_price)
print(diff)
print(percent)


def get_news():
    parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=parameters)
    news_response.raise_for_status()
    news_response_json = news_response.json()
    # get the first three articles and extract the headline and brief from it
    articles = news_response_json["articles"][:3]
    headlines = [{f"Headline": f"{article['title']}", "Brief": f"{article['description']}"} for article in articles]
    # send text after getting the articles
    send_text(headlines)

def send_text(headlines):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    if went_up:
        percentage_show = f"🔺{percent}%"
    else:
        percentage_show = f"🔻{percent}%"

    message = client.messages \
        .create(
        body=f"{STOCK}: {percentage_show}\n"
             f"Headline: {headlines[0]['Headline']}\n"
             f"Brief: {headlines[0]['Brief']}",
        from_= SENDING_PHONE_NUM,
        to="TOPHONENUM"
    )

if percent >= PERCENT_THRESHOLD:
   # get the first three article for the company name
    get_news()

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

