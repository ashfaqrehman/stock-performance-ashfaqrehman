"""
Tests IEX API.
"""

from portfolio.portfolio_report import get_portfolio_iex_api

def test_get_iex_api(requests_mock):
    url = (
        'https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,fb&types=quote'
    )

    requests_mock.get(
        url,
        json={
            "AAPL":{"quote":{"symbol":"AAPL", "companyName":"Apple Inc.", "latestPrice":189.95}},
            "FB":{"quote":{"symbol":"FB", "companyName":"Facebook Inc.", "latestPrice":166.62}}
            }
        )
    expected = [('AAPL'), ('FB')]

    assert get_portfolio_iex_api(url) == expected
