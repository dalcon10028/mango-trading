import ssl
import asyncio
import certifi

from yarl import URL
from typing import List, Optional
from pydantic.dataclasses import dataclass
from websockets.asyncio.client import connect
from market_data.settings import BINANCE_STREAM_ENDPOINT


@dataclass
class KlineRequestParams:
    """
    Request parameters for Kline data
    https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/public-api-requests#klines
    """
    symbol: str
    interval: str
    startTime: Optional[int]
    endTime: Optional[int]
    timezone: str = 9  # Default: 0 (UTC)
    limit: Optional[int] = None # Default 500; max 1000


async def receive_klines(symbols: List[str] = ["btcusdt"]):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())

    query = {
        "stream": "!ticker@arr"
    }

    # {
    #   "e": "24hrTicker",  // Event type
    #   "E": 1672515782136, // Event time
    #   "s": "BNBBTC",      // Symbol
    #   "p": "0.0015",      // Price change
    #   "P": "250.00",      // Price change percent
    #   "w": "0.0018",      // Weighted average price
    #   "x": "0.0009",      // First trade(F)-1 price (first trade before the 24hr rolling window)
    #   "c": "0.0025",      // Last price
    #   "Q": "10",          // Last quantity
    #   "b": "0.0024",      // Best bid price
    #   "B": "10",          // Best bid quantity
    #   "a": "0.0026",      // Best ask price
    #   "A": "100",         // Best ask quantity
    #   "o": "0.0010",      // Open price
    #   "h": "0.0025",      // High price
    #   "l": "0.0010",      // Low price
    #   "v": "10000",       // Total traded base asset volume
    #   "q": "18",          // Total traded quote asset volume
    #   "O": 0,             // Statistics open time
    #   "C": 86400000,      // Statistics close time
    #   "F": 0,             // First trade ID
    #   "L": 18150,         // Last trade Id
    #   "n": 18151          // Total number of trades
    # }
    payload = {
        "e": "24hrTicker",
        "E": 1672515782136,
        "s": "BNBBTC",
        "p": "0.0015",
        "P": "250.00",
        "w": "0.0018",
        "x": "0.0009",
        "c": "0.0025",
        "Q": "10",
        "b": "0.0024",
        "B": "10",
        "a": "0.0026",
        "A": "100",
        "o": "0.0010",
        "h": "0.0025",
        "l": "0.0010",
        "v": "10000",
        "q": "18",
        "O": 0,
        "C": 86400000,
        "F": 0,
        "L": 18150,
        "n": 18151
    }
    url = f"{BINANCE_STREAM_ENDPOINT}/ws/!ticker@arr"
    async with connect(url, ssl=ssl_context) as websocket:
        message = await websocket.recv()
        print(message)
        # await websocket.send(payload)
        # message = await websocket.recv()
        # print(message)


if __name__ == "__main__":
    asyncio.run(receive_klines())
