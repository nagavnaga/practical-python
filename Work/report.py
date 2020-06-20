# report.py
#
# Exercise 2.4
import sys

from fileparse import parse_csv
from stock import Stock
# from tableformat import TableFormatter, CSVTableFormatter, HTMLTableFormatter
import tableformat

def read_portfolio(filename: str):
    with open(filename) as file:
        portfolio = parse_csv(file, types=[str, int, float], select=['name','shares','price'])
        portfolio = [Stock(*share.values()) for share in portfolio]
    # with open(filename, 'rt') as file:
    #     rows = csv.reader(file)
    #     headers = next(rows)
    #     types = [str, int, float]
    #     for row in rows:
    #         # record = dict(zip(headers, row))
    #         # holding = {
    #         #     'name': record['name'],
    #         #     'shares': int(record['shares']),
    #         #     'price' : float(record['price']),
    #         # }
    #         holding = {name:func(value) for name, func, value in zip(headers, types, row)}
    #         portfolio.append(holding)
    return portfolio


def read_prices(filename: str) -> dict:
    with open(filename) as file:
        prices = dict(parse_csv(file,has_headers=False, types=[str, float]))
    # prices = {}
    # with open(filename, 'r') as file:
    #     rows = csv.reader(file)
    #     for row in rows:
    #         if row:
    #             prices[row[0]] = float(row[1])

    return prices


def currency(price, type='$'):
    price = str(f"{price:.2f}")
    return type + price


def make_report(portfolio, prices):
    """
    :param prices:
    :param portfolio:
    :return:
    """
    invested = 0
    current_invested_value = 0

    row = []
    for stock in portfolio:

        change = prices[stock.name] - stock.price
        summary = (stock.name,stock.share, prices[stock.name], change)
        row.append(summary)
    return row


def print_report(reportdata, columns, formatter):

    """
    Print a nicely formated table from a list of ('Name', 'Shares', 'Price', 'Change') tuples

    """
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print('{:>10} {:>10} {:>10} {:>10}'.format(*headers))
    # print('---------- ' * len(headers))
    formatter.headings(columns)

    # for name, shares, price, change in reportdata:
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

        # print('{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}'
        #       .format(name=row[0], shares=row[1],
        #               price=currency(row[2]), change=row[3]))


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    my_stocks = read_portfolio(portfolio_filename)

    current_price = read_prices(prices_filename)

    # Generation report data
    report = make_report(my_stocks, current_price)
    # output of the report
    formatter = tableformat.create_formatter(fmt)
    print_report(report,["name", "shares"], formatter)


def main(argv):
    # stocks_file = r'Data/portfolio.csv'
    # current_price_file = r'Data/prices.csv'
    if len(argv) != 3:
        raise SystemExit('Usage: %s portfolio_file pricefile' % argv[0])
    portfolio_filename = argv[1]
    prices_filename = argv[2]
    portfolio_report(portfolio_filename, prices_filename)


if __name__ == '__main__':
    main(sys.argv)



