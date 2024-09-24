import requests
from newsFetcher import news_fetcher
from twilio.rest import Client


url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=getYourOwnKey"
response = requests.get(url)
pricing_info = response.json()['Time Series (Digital Currency Daily)']
closing_prices = [value["4. close"] for (key, value) in pricing_info.items()]


yesterdays_closing_price = float(closing_prices[0])
day_before_yesterday_closing_price = float(closing_prices[1])

price_fluctuation = yesterdays_closing_price - day_before_yesterday_closing_price

percentage_fluctuation = (price_fluctuation/yesterdays_closing_price) * 100
print(percentage_fluctuation)
sms = ""

if percentage_fluctuation > 2 :
    data = news_fetcher("Bitcoin")
    sms = f"BITCOIN: ⬆️\nHeadline: {data['headline']} \nBrief:{data['brief']} \nURL:{data['url']}\nClosing Price :{yesterdays_closing_price}"
elif percentage_fluctuation < -2 :
    data = news_fetcher("Bitcoin")
    sms = f"BITCOIN: ⬇️\nHeadline: {data['headline']} \nBrief:{data['brief']} \nURL:{data['url']} \nClosing Price :{yesterdays_closing_price}"
else:
    sms = f"Bitcoin Price is fluctuating in safe range.\nClosing Price :{yesterdays_closing_price}"


account_sid = 'getYourOwnKey'
auth_token = 'getYourOwnKey'
client = Client(account_sid, auth_token)
message = client.messages.create(
        from_='+12076790712',
        body=sms,
        to='+15062694986'
        )

