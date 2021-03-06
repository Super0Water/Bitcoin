#Function to get cryptocurrency prices
import requests
import json

import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime, timedelta

coin_url = 'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(coin_url)

def coin_list(json):
    #function to grab the json of all cryptos on coingecko 
    #and make into a string of cryptos
    #prob deprecate this bullshit
    currency_list = []
    for names in range(len(json)):
        currency_list.append(json[names]["name"])
    return currency_list

def current_price(currency):
    #function to get all the current prices based on the currency list fetched earlier
    url_list = []
    price_list = {}
    for coins in currency_list:
        #have to iterate because bulk coin list doesn't work all the time with the CoinGecko API
        #look at other data sources in the future
        url ='https://api.coingecko.com/api/v3/simple/price?ids='+coins+'&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true'
        url_list.append(url)
    for coins in url_list: 
        #We take the url list created above and do json request for each. Returns a dict/json
        response = requests.get(coins)
        temp_coin = response.json() 
        price_list.update(temp_coin)
    return price_list

def historical_price (currency, dates):
    #function to pull historical prices
    #need to pull each day b/c api sucks if you don't pay for this bullshit
    history = {}
    temp_history ={}
    for date in dates:
        url = 'https://api.coingecko.com/api/v3/coins/'+currency+'/history?date='+ date
        response = requests.get(url)
        temp_coin = response.json() 
        temp_history[date]= temp_coin['market_data']['current_price']['usd']
        history.update(temp_history)
    return history

def date_list():
    #gets 14 days out from current date
    now = datetime.now(tz=None) 
    dates = []
    for days in range (15):
        dates.append(now.strftime("%d-%m-%Y"))
        now = now - timedelta(days = days+1)
    return dates

def historical_graph(history):
    dates = list(history.keys())
    prices = list(history.values())

    plt.plot_date(dates,prices, linestyle='--',label='Price')
    plt.xticks(dates, rotation='vertical')
  
    plt.tight_layout()
    plt.show()
    
currency = input("Enter your Cryptocurrency: ")
x = date_list()
y = historical_price(currency,x)
historical_graph(y)