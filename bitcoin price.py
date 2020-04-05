#Function to get cryptocurrency prices
import requests
import json

import matplotlib.pyplot as plt
import seaborn as sns

import datetime

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
        url ='https://api.coingecko.com/api/v3/simple/price?ids='+coins+'&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true'
        url_list.append(url)
    for coins in url_list:
        response = requests.get(coins)
        print(response.json())
          #need to figure out best way to fetch each price and append into json 
          #FUCK FUCK FUCK HOW DO YOU MAKE JSON INTO DICT AND ADD IT TO PRICE_LIST DICT?
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

def historical_graph(price_list):
    #graph for price?
    return None

price_list =  current_price(currency_list)

print(price_list)

