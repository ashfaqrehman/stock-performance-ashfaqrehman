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

def test_save_portfolio(portfolio_csv):
    """
    Given that the save portfolio method is called with the following
    data, assert that a CSV file is written in the expected format.

    The portfolio
    """
    data = [{'symbol': 'MSFT', 'company_name': 'Microsoft Corporation', 'units': 10, 'cost': 99.66,
             'latest_price': 119.89, 'book_value': 996.6, 'market_value': 1198.9, 'gain_loss': 202.3, 'change': 0.203}]
    portfolio_report.save_portfolio(data, filename=portfolio_csv)


    expected = ('symbol,company_name,units,cost,latest_price,book_value,market_value,gain_loss,change\r\n'
                'MSFT,Microsoft Corporation,10,99.66,119.89,996.6,1198.9,202.3,0.203\r\n')
    with open(portfolio_csv, 'r', newline='') as file:
        result = file.read()
        assert result == expected, (
            f'Expecting the file to contain: \n{result}'
        )
