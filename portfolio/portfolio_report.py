#!/usr/bin/env python
import csv
import requests
"""
Generates performance reports for your stock portfolio.
"""




def read_portfolio(filename='portfolio.csv'):
    """Returns portfolio data from a CSV file."""
    # Read the CSV file with the filename above,
    #       and return the data.
    data = list()
    with open('portfolio.csv', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def get_portfolio_iex_api(url):
    """
    Returns symbol list from the IEX API.
    """


    response = requests.get(url)
    data = response.json()

    #return data.values()
    #return data.keys()
    #return list(data.items())
    #return data['AAPL']['quote']['symbol']
    #return list(data.keys())

    return [
        (data[key]['quote']['symbol'])
        for key in data.keys()
    ]



def save_portfolio(data, filename='report.csv'):
    """Saves portfolio data from a CSV file."""
    # Save the provided data to the provided filename.
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, ['symbol', 'units', 'cost'])
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write all the rows at once
    return filename


def main():
    """
    Entrypoint into program.
    """
    source = 'portfolio.csv'
    target = 'report1.csv'
    url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,AMZ&types=quote'

    data = read_portfolio(source)
    print(type(data))
    print(data)


    save_portfolio(data, target)

    for item in range(0, len(data)):
        print(data[item]['symbol'])



    symbol_list = get_symbol_list_IEX_API(url)
    print(symbol_list)

    for item in range(0, len(data)):
        print(data[item]['symbol'] in symbol_list)



if __name__ == '__main__':
    main()
