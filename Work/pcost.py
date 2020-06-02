# pcost.py
#
# Exercise 1.27
"""
The columns in portfolio.csv correspond to the
stock name, number of shares, and purchase price of a single stock holding.
Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

Hint:
     To convert a string to an integer, use int(s).
     To convert a string to a floating point, use float(s).
"""
import gzip
import csv
import sys

portfolio = r'Data/portfolio.csv'
missing = r'Data/missing.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = portfolio

def portfolio_cost(filename):
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        total = 0
        for row in rows:
            try:
                share_cost = int(row[1]) * float(row[2])
            except ValueError:
                print(f"Not able to process {row}")
            total += share_cost

    print(f"Total cost  {total}")


if __name__ == '__main__':
    # portfolio_cost(portfolio)
    portfolio_cost(filename)
