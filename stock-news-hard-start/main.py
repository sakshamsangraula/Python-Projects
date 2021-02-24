STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "SECRET"
NEWS_API_KEY = "SECRET"
PERCENT_THRESHOLD = 5

TWILIO_ACCOUNT_SID = "SECRET"
TWILIO_AUTH_TOKEN = "SECRET"
SENDING_PHONE_NUM = "SECRET"
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

# use the .items() function to loop over the dictionary
data_without_dates = [info for (date, info) in daily_data.items()]

yesterday_data = data_without_dates[0]
yesterday_close_price = float(yesterday_data["4. close"])
day_before_yesterday = data_without_dates[1]
day_before_yesterday_close_price = float(day_before_yesterday["4. close"])



# if the positive difference between yesterday's and day before yesterday's price is positive or negative 5%
# meaning if there is a 5% decrease or increase in yesterday's price from day before yesterday then print get news
if yesterday_close_price > day_before_yesterday_close_price:
    went_up = True
diff = math.fabs(yesterday_close_price - day_before_yesterday_close_price)
percent = round(diff/day_before_yesterday_close_price * 100)


def get_news():
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    if went_up:
        percentage_show = f"🔺{percent}%"
    else:
        percentage_show = f"🔻{percent}%"
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_response_json = news_response.json()
    # get the first three articles and extract the headline and brief from it
    articles = news_response_json["articles"][:3]
    headlines = [ f"{STOCK}: {percentage_show}\nHeadline: {article['title']}\n"
                  f"Brief: {article['description']}" for article in articles]
    # send text after getting the articles
    print(headlines)
    send_text(headlines)

def send_text(headlines):

    print(headlines[0])
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for headline in headlines:
        message = client.messages \
            .create(
            body= headline,
            from_= SENDING_PHONE_NUM,
            to="SECRET"
        )

if percent > PERCENT_THRESHOLD:
   # get the first three article for the company name if the percent difference is more than 5
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

