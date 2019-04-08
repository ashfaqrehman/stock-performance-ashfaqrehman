"""
Tests I/O disk operations.
"""
from collections import OrderedDict

from portfolio import portfolio_report



# Note: the portfolio_csv argument found in the tests below
#       is a pytest "fixture". It is defined in conftest.py

def test_read_portfolio(portfolio_csv):
    """
    Given that the read_portfolio is called, assert that
    the data the expected data is returned.
    """
    expected = [
        OrderedDict([
            ('symbol', 'AAPL'),
            ('units', '100'),
            ('cost', '154.23'),
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('units', '600'),
            ('cost', '1223.43')
        ])
    ]

    assert portfolio_report.read_portfolio(portfolio_csv) == expected, (
        'Expecting to get the data stored in the portfolio_csv '
        'fixture as a Python data structure.'
    )

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
            "AMZN":
            {"quote":{"symbol":"AMZN", "companyName":"Amazon.com Inc.", "latestPrice":1837.28}}
            }
        )
    expected = [
        OrderedDict([
            ('symbol', 'AAPL'),
            ('companyName', 'Apple Inc.'),
            ('latestPrice', 197)
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('companyName', 'Amazon.com Inc.'),
            ('latestPrice', 1837.28)
        ])
    ]

    assert get_latest_market_price(url) == expected

def test_build_portfolio():
    """
    Given that the build_portfolio is called, assert that
    the data the expected data is returned.
    """
    data_csv = [
        OrderedDict([
            ('symbol', 'AAPL'),
            ('units', '100'),
            ('cost', '154.23')
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('units', '600'),
            ('cost', '2000')
        ])
    ]
    data_api = [
        OrderedDict([
            ('symbol', 'AAPL'),
            ('companyName', 'Apple Inc.'),
            ('latestPrice', 197)
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('companyName', 'Amazon.com Inc.'),
            ('latestPrice', 1837.28)
        ])
    ]

    expected = [
        OrderedDict([
            ('symbol', 'AAPL'),
            ('company_name', 'Apple Inc.'),
            ('units', '100'),
            ('cost', '154.23'),
            ('latest_price', 197),
            ('book_value', 15423.0),
            ('market_value', 19700.0),
            ('gain_loss', 4277.0),
            ('change', 0.277)
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('company_name', 'Amazon.com Inc.'),
            ('units', '600'), ('cost', '2000'),
            ('latest_price', 1837.28),
            ('book_value', 1200000.0),
            ('market_value', 1102368.0),
            ('gain_loss', -97632.0),
            ('change', -0.081)
        ])
    ]

    assert portfolio_report.build_portfolio(data_csv, data_api) == expected

def test_save_portfolio(portfolio_csv):
    """
    Given that the save portfolio method is called with the following
    data, assert that a CSV file is written in the expected format.

    The portfolio
    """
    data = [{
        'symbol': 'MSFT',
        'company_name': 'Microsoft Corporation',
        'units': 10, 'cost': 99.66,
        'latest_price': 119.89,
        'book_value': 996.6,
        'market_value': 1198.9,
        'gain_loss': 202.3,
        'change': 0.203
    }]
    portfolio_report.save_portfolio(data, filename=portfolio_csv)


    expected = 'symbol,company_name,units,cost,latest_price,book_value,' \
        'market_value,gain_loss,change\r\nMSFT,Microsoft Corporation,' \
        '10,99.66,119.89,996.6,1198.9,202.3,0.203\r\n'
    with open(portfolio_csv, 'r', newline='') as file:
        result = file.read()
        assert result == expected, (
            f'Expecting the file to contain: \n{result}'
        )
