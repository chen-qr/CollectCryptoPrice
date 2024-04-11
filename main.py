import asyncio
import ccxt.async_support as ccxt


async def fetch_data(exchange_id):
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class()
    try:
        ticker = exchange.fetch_ticker('BTC/USDT')
        print(f"{exchange_id} has fetched.")
        print(ticker)
    except Exception as e:
        print(f"{exchange_id} failed to fetch.")
        print(e)
    finally:
        await exchange.close()


async def collect():
    collect_exchanges = ["okx", "binance"] # 从两个OKX和币安两个交易所同时获取数据
    tasks = [fetch_data(exchange_id) for exchange_id in collect_exchanges]
    await asyncio.gather(*tasks) # 异步并发处理任务


if __name__ == "__main__":
    asyncio.run(collect())