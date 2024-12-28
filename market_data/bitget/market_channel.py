import ssl
import asyncio
import certifi
import json

from typing import List, Optional
from pydantic.dataclasses import dataclass
from websockets.asyncio.client import connect
from market_data.settings import BITGET_WEBSOCKET_ENDPOINT


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

    payload = {
        "op": "subscribe",
        "args": [
            {
                "instType": "SUSDT-FUTURES",
                "channel": "ticker",
                "instId": "SBTCSUSDT"
            }
        ]
    }
    url = f"{BITGET_WEBSOCKET_ENDPOINT}/public"
    async with connect(url, ssl=ssl_context) as websocket:
        await websocket.send(json.dumps(payload))

        while True:
            message = await websocket.recv()
            print(message)
        # await websocket.send(payload)
        # message = await websocket.recv()
        # print(message)


if __name__ == "__main__":
    asyncio.run(receive_klines())
