#Function to get cryptocurrency prices
import requests
import json

import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime, timedelta

currency_list = ['bitcoin','ethereum']
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

def current_price(currency_list):
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
        print(response.json())
        temp_coin = response.json() 
        price_list.update(temp_coin)
    return price_list

def historical_price (currency_list, date_list):
    #function to pull historical prices
    #need to pull each day b/c api sucks if you don't pay for this bullshit
    date_list = []
    url_list = []
    for coins in currency_list:
        for dates in date_list:
            url = 'https://api.coingecko.com/api/v3/coins/'+coins+'/history?date='+ dates
            url_list.append(url)
    return None

def date_list():
    now = datetime.now(tz=None)
    date_list = []
    x = now
    for days in range (14):
        date_list.append(x)
        x = now - timedelta(days = days)
    return date_list

def historical_graph(price_list):
    #graph for price?
    return None

