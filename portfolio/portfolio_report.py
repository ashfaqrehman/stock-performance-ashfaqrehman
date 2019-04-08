#!/usr/bin/env python
"""
Generates performance reports for your stock portfolio.
"""

import csv
from collections import OrderedDict
import time
import argparse
import requests


def read_portfolio(filename='portfolio.csv'):
    """Returns portfolio data from a CSV file."""
    # Read the CSV file with the filename above,
    #       and return the data.
    data = list()
    with open(filename, newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def save_portfolio(data, filename='report.csv'):
    """Saves portfolio data from a CSV file."""
    # Save the provided data to the provided filename.
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, [
            'symbol',
            'company_name',
            'units',
            'cost',
            'latest_price',
            'book_value',
            'market_value',
            'gain_loss',
            'change'
        ])
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write all the rows at once
    return filename

def build_iex_api_url(csv_data):
    """
    Takes in data list from csv containing the symbols
    returns build iex api url using those symbols
    """
    symbols = ''
    url = ''
    for item in enumerate(csv_data):
        symbols = symbols + item[1]['symbol'] + ','
    url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=' + symbols + '&types=quote'
    return url

def get_latest_market_price(url):
    """
    Accepts url for IEX API

    Returns the latest market price for holdings
    """
    response = requests.get(url)
    data = response.json()
    return [
        OrderedDict([
            ('symbol', data[key]['quote']['symbol']),
            ('companyName', data[key]['quote']['companyName']),
            ('latestPrice', data[key]['quote']['latestPrice'])
        ])
        for key in data.keys()
    ]


def build_portfolio(data_csv, data_api):
    """
    Accepts holdings dictionary from csv and api

    Returns portofilio dictionary
    """
    data_portfolio = []

    for key_csv in data_csv:
        not_found = True
        for key_api in data_api:
            #print(key_csv['symbol'], '==', key_api['symbol'])
            if key_csv['symbol'] == key_api['symbol']:
                not_found = False
                data_portfolio.append(
                    OrderedDict([
                        ('symbol', key_csv['symbol']),
                        ('company_name', key_api['companyName']),
                        ('units', key_csv['units']),
                        ('cost', key_csv['cost']),
                        ('latest_price', key_api['latestPrice']),
                        ('book_value', round(float(key_csv['units']) * \
                            float(key_csv['cost']), 2)),
                        ('market_value', round(float(key_csv['units']) * \
                        float(key_api['latestPrice']), 2)),
                        ('gain_loss', round((float(key_csv['units']) * \
                            key_api['latestPrice']) - \
                            (float(key_csv['units']) * \
                                float(key_csv['cost'])), 2)),
                        ('change',
                        round(((float(key_csv['units']) * key_api['latestPrice']) - \
                        (float(key_csv['units']) * float(key_csv['cost']))) / \
                        (float(key_csv['units']) * float(key_csv['cost'])), 3))
                    ])
                )
                #print("found it, skipping...")
                break #found it, skip searching the rest..."
        if not_found:
            print('Warning:', key_csv['symbol'], 'unrecognized input/symbol.')
    return data_portfolio

def main():
    """
    Entrypoint into program.
    """
    start = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', required=True)
    parser.add_argument('-t', '--target', required=True)
    args = parser.parse_args()
    source = args.source
    target = args.target


    data_csv = read_portfolio(source)
    url = build_iex_api_url(data_csv)
    data_api = get_latest_market_price(url)
    data_portfolio = build_portfolio(data_csv, data_api)
    save_portfolio(data_portfolio, target)
    end = time.time()
    print('Runtime:', round(end - start, 2), 'seconds')



if __name__ == '__main__':
    main()
