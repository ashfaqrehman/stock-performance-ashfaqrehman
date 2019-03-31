#!/usr/bin/env python
import csv
"""
Generates performance reports for your stock portfolio.
"""




def read_portfolio(filename='portfolio.csv'):
    """Returns portfolio data from a CSV file."""
    # TODO: Read the CSV file with the filename above,
    #       and return the data.
    data = list()
    with open('portfolio.csv', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


def save_portfolio(data, filename='portfolio.csv'):
    """Saves portfolio data from a CSV file."""
    # TODO: Save the provided data to the provided filename.


def main():
    """
    Entrypoint into program.
    """
    source = 'portfolio.csv'
    target = 'report1.csv'

    data = read_portfolio(source)

    with open(target, 'w', newline='') as file:
        writer = csv.DictWriter(file, ['symbol', 'units','cost'])
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write all the rows at once



if __name__ == '__main__':
    main()
