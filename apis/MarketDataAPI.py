import requests
from requests import Session
import pandas as pd


class MarketData:
    # https://docs.kucoin.com/ - API Documentaion

    def __init__(self):
        self.apiurl = "https://api.kucoin.com"  # base url for kucoin
        # self.headers = {
        #     "KC-API-SIGN": signature,
        #     "KC-API-TIMESTAMP": str(now),
        #     "KC-API-KEY": api_key,
        #     "KC-API-PASSPHRASE": passphrase,
        #     "KC-API-KEY-VERSION": "2",
        # }
        self.session = Session()

    # returns all tickers
    def getAllTickers(self):
        url = self.apiurl + "/api/v1/market/allTickers"
        r = self.session.get(url)
        data = r.json()["data"]
        return data

    # returns a single trading pair ex. 'BTC-USDT'
    def getTicker(self, symbol):
        url = self.apiurl + "/api/v1/market/orderbook/level1"
        parameters = {"symbol": symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()["data"]
        df = pd.DataFrame.from_dict(data, orient="index")  # dictionary to dataframe
        return df

    # returns the order book for a trading pair
    def getPartOrderBook(self, symbol, amount):  # does not required API KEY
        # amount can be 20 pieces of data or 100 pieces of data
        url = self.apiurl + "/api/v1/market/orderbook/level2_" + amount
        parameters = {"symbol": symbol, "amount": amount}
        r = self.session.get(url, params=parameters)
        data = r.json()["data"]
        return data

    # returns the full order book for a trading pair
    def getFullOrderBook(self, symbol):  # needs headers and API key
        url = self.apiurl + "/api/v3/market/orderbook/level2"
        parameters = {"symbol": symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()
        return data

    # returns the fiat price of a symbol
    def getFiatPrice(self, symbol):
        url = self.apiurl + "/api/v1/prices"
        parameters = {"symbol": symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()["data"][symbol]
        return data


marketData = MarketData()

print(marketData.getTicker("ETH-USDT"))
print(marketData.getFiatPrice("ETH"))
