"""
Tests I/O disk operations.
"""
from collections import OrderedDict
import pytest

import portfolio


@pytest.fixture
def portfolio_csv(tmp_path):
    """
    Creates a portfolio.csv in a temporary folder for the
    purposes of testing.
    """
    lines = [
        ('symbol,units,cost\r\n'),
        ('APPL,100,154.23\r\n'),
        ('AMZN,600,1223.43\r\n'),
    ]

    filename = tmp_path / 'portfolio.csv'
    with open(filename, 'w', newline='') as file:
        file.writelines(lines)

    return filename


def test_read_portfolio(portfolio_csv):
    """
    Given that the read_portfolio is called, assert that
    the data the expected data is returned.
    """
    expected = [
        OrderedDict([
            ('symbol', 'APPL'),
            ('units', '100'),
            ('cost', '154.23'),
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('units', '600'),
            ('cost', '1223.43')
        ])
    ]

    assert portfolio.read_portfolio(portfolio_csv) == expected, (
        'Expecting to get the data stored in the portfolio_csv '
        'fixture as a Python data object.'
    )


def test_save_portfolio(portfolio_csv):
    """
    Given that the save portfolio method is called with the following
    data, assert that a CSV file is written in the expected format.

    The portfolio
    """
    data = [{'symbol': 'MSFT', 'units': 10, 'cost': 99.66}]
    portfolio.save_portfolio(data, filename=portfolio_csv)

    expected = ['symbol,units,cost\r\n', 'MSFT,10,99.66\r\n']
    with open(portfolio_csv, 'r', newline='') as file:
        assert file.readlines() == expected, (
            f'Expecting the file to contain like: \n{expected[0]}'
        )
