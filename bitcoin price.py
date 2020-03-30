#Function to get cryptocurrency prices
import requests
import json

coin_url = 'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(coin_url)

x = response.json() #prob need to take this out when you can think later

def coin_list(json):
    #function to grab the json of all cryptos on coingecko 
    #and make into a string of cryptos
    currency_list = []
    for names in range(len(json)):
        currency_list.append(json[names]["name"])
    return currency_list

def get_universe_price(currency_list):
    #function to get all the current prices based on the currency list fetched earlier
    #need to figure out best way to fetch each price and append into json
    url_list = []
    price_list ={}
    for coins in currency_list:
        url ='https://api.coingecko.com/api/v3/simple/price?ids='+coins+'&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true'
        url_list.append(url)
    for coins in url_list:
        response = requests.get(coins)
        print(response.json())
        price_list[coins] = response.json()
    print(price_list) 



currency_list = coin_list(x)

get_universe_price(currency_list)
