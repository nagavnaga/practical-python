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
import report

# portfolio = r'Data/portfolio.csv'
# missing = r'Data/missing.csv'
# new_file = 'Data/portfoliodate.csv'

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = portfolio


def portfolio_cost(filename):
    # with open(filename, 'rt') as file:
    #     rows = csv.reader(file)
    #     headers = next(rows)
    #     total = 0.0
    #     for rowno, row in enumerate(rows,start=1):
    #         record = dict(zip(headers, row))
    #         try:
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             share_cost = nshares * price
    #         except ValueError:
    #             print(f"Row {rowno}: Not able to process {row}")
    #         total += share_cost
    portfolio = report.read_portfolio(filename)
    total = sum([stock.cost for stock in portfolio])

    return total


def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s portfoliofile' % argv[0])

    filename = argv[1]
    cost = portfolio_cost(filename)
    print('Total cost:', cost)


if __name__ == '__main__':
    main(sys.argv)
