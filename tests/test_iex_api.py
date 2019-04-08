"""
Tests IEX API.
"""
from collections import OrderedDict
from portfolio.portfolio_report import get_latest_market_price

def test_get_iex_api(requests_mock):
    """
    Tests IEX API.
    """
    url = (
        'https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,fb&types=quote'
    )

    requests_mock.get(
        url,
        json={
            "AAPL":
            {"quote":{"symbol":"AAPL", "companyName":"Apple Inc.", "latestPrice":197}},
            "SQ":
            {"quote":{"symbol":"SQ", "companyName":"Square Inc.", "latestPrice":75}}
            }
        )
    expected = [
        OrderedDict([
            ('symbol', 'AAPL'),
            ('companyName', 'Apple Inc.'),
            ('latestPrice', 197)
        ]),
        OrderedDict([
            ('symbol', 'SQ'),
            ('companyName', 'Square Inc.'),
            ('latestPrice', 75)
        ])
    ]

    assert get_latest_market_price(url) == expected
