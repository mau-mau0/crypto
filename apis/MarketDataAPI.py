from requests import Session
import pandas as pd


class MarketData:
    # https://docs.kucoin.com/ - API Documentaion

    def __init__(self):
        self.apiurl = "https://api.kucoin.com"  # base url for kucoin
        self.session = Session()

    # returns all tickers
    def getAllTickers(self):
        url = self.apiurl + "/api/v1/market/allTickers"
        r = self.session.get(url)
        data = r.json()["data"]["ticker"]
        df = pd.DataFrame.from_dict(data, orient="columns")
        return df.loc[  # .loc[slice:slice, ['choose what columns show']]
            :,
            [
                "symbolName",
                "buy",
                "sell",
                "changeRate",
                "changePrice",
                "high",
                "low",
                "vol",
                "last",
                "averagePrice",
            ],
        ]

    # returns a single trading pair ex. 'BTC-USDT'
    def getTicker(self, symbol):
        url = self.apiurl + "/api/v1/market/orderbook/level1"
        parameters = {"symbol": symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()["data"]
        # dictionary to dataframe
        df = pd.DataFrame.from_dict(data, orient="index", columns=[symbol])
        return df

    # returns the 24hr stats for a trading pair
    def get24hrStats(self, symbol):
        url = self.apiurl + "/api/v1/market/stats"
        parameters = {"symbol": symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()["data"]
        df = pd.DataFrame.from_dict(data, orient="index", columns=[symbol])
        return df

    # returns the order book for a trading pair
    def getPartOrderBook(self, symbol, amount):  # does not required API KEY
        # amount can be 20 pieces of data or 100 pieces of data
        url = self.apiurl + "/api/v1/market/orderbook/level2_" + amount
        parameters = {"symbol": symbol, "amount": amount}
        r = self.session.get(url, params=parameters)
        bids = r.json()["data"]["bids"]
        asks = r.json()["data"]["asks"]
        dfBids = pd.DataFrame.from_dict(bids, orient="columns")
        dfAsks = pd.DataFrame.from_dict(asks, orient="columns")
        dfAsks.columns = ["", "Asks"]
        dfBids.columns = ["", "Bids"]
        return dfBids, dfAsks

    # returns the fiat price of a symbol
    def getFiatPrice(self, symbol):
        url = self.apiurl + "/api/v1/prices"
        parameters = {"symbol": symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()["data"][symbol]
        return data


marketData = MarketData()
