import ccxt


exchange = ccxt.okx()
markets = exchange.load_markets()
print(markets)