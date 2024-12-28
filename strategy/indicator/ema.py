import pandas as pd


def ema(prices: pd.Series, period: int) -> pd.Series:
    """
    Calculate the Exponential Moving Average (EMA) for a given list of prices.

    Args:
       prices (list or pd.Series): List or Pandas Series of price data.
       period (int): The period over which to calculate the EMA.

    Returns:
       pd.Series: EMA values as a Pandas Series.
    """

    return prices.ewm(span=period, adjust=False).mean()
