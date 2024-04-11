import ccxt

# 从OKX交易所获取数据
exchange = ccxt.okx()
markets = exchange.load_markets()
# print(markets)

# 获取交易对的价格
ticker = exchange.fetch_ticker('BTC/USDT')
print(ticker)