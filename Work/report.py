# report.py
#
# Exercise 2.4
import sys

from fileparse import parse_csv
from stock import Stock
import tableformat


def read_portfolio(filename: str):
    with open(filename) as file:
        portfolio = parse_csv(file, types=[str, int, float], select=['name','shares','price'])
        portfolio = [Stock(*share.values()) for share in portfolio]
    return portfolio


def read_prices(filename: str) -> dict:
    with open(filename) as file:
        prices = dict(parse_csv(file,has_headers=False, types=[str, float]))

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

    row = []
    for stock in portfolio:

        change = prices[stock.name] - stock.price
        summary = (stock.name,stock.share, prices[stock.name], change)
        row.append(summary)
    return row


def print_report(reportdata, formatter):

    """
    Print a nicely formatted table from a list of ('Name', 'Shares', 'Price', 'Change') tuples

    """
    headers = ['Name', 'Shares', 'Price', 'Change']
    formatter.headings(headers)

    # for name, shares, price, change in reportdata:
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    my_stocks = read_portfolio(portfolio_filename)

    current_price = read_prices(prices_filename)

    # Generation report data
    report = make_report(my_stocks, current_price)
    # output of the report
    formatter = tableformat.create_formatter(fmt)
    print_report(report,  formatter)


def main(argv):
    if len(argv) != 3:
        raise SystemExit('Usage: %s portfolio_file pricefile' % argv[0])
    portfolio_filename = argv[1]
    prices_filename = argv[2]
    portfolio_report(portfolio_filename, prices_filename)


if __name__ == '__main__':
    main(sys.argv)
