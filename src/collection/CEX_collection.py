import asyncio
import ccxt.async_support as ccxt


async def fetch_data(exchange_id):
    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class()
    try:
        ticker = await exchange.fetch_ticker('BTC/USDT')
        print(f"{exchange_id} has fetched.")
        print(ticker)
    except Exception as e:
        print(f"{exchange_id} failed to fetch.")
        print(e)
    finally:
        await exchange.close()


async def collect():
    # 从不同的中心化交易所获取数据
    # 需要注意，不同交易所，对运行节点IP所在的国家，是有不同限制要求的
    collect_exchanges = ["okx", "binanceus"]
    tasks = [fetch_data(exchange_id) for exchange_id in collect_exchanges]
    await asyncio.gather(*tasks) # 异步并发处理任务


if __name__ == "__main__":
    asyncio.run(collect())