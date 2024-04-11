import ccxt

# 从OKX交易所获取数据
exchange = ccxt.okx()
markets = exchange.load_markets()
print(markets)