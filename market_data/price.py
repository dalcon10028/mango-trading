import aiohttp
import asyncio

from market_data.settings import BINANCE_MARKET_DATA_ENDPOINT


async def get_klines(session: aiohttp.ClientSession, symbol: str) -> dict:
    """
    Get klines for a symbol
    https://developers.binance.com/docs/binance-spot-api-docs/rest-api/public-api-endpoints#klinecandlestick-data
    :param session:
    :param symbol:
    :return:
    """
    payload = {
        'windowSize': '1d',
    }
    print(payload)

    async with session.get(
        f'ticker?symbol={symbol}',
        ssl=False,
    ) as response:
        json = await response.json()
        return json


async def main():
    async with aiohttp.ClientSession(base_url=BINANCE_MARKET_DATA_ENDPOINT) as session:
        klines = await get_klines(session, 'BTCUSDT')
        print(klines)


if __name__ == '__main__':
    asyncio.run(main())