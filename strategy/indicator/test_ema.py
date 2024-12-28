from strategy.indicator import ema
from pandas import Series


def test_ema():
    prices = Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result: Series = ema(prices, 5)
    assert result[0] == 1
    assert 8 < result.iloc[-1] < 9

