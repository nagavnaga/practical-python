# report.py
#
# Exercise 2.4
import csv
portfolio = []
prices = {}
invested =0
current_invested_value =0


def read_portfolio(filename):
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price' : float(row[2])
            }

            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    with open(filename,'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])

    return prices


my_stocks = read_portfolio('Data/portfolio.csv')
current_price = read_prices('Data/prices.csv')

for stock in my_stocks:
    invested += stock['shares'] * stock['price']
    current_invested_value += stock['shares'] * current_price[stock['name']]

print(invested)
print(current_invested_value)

print(f'Your gain/loss is: {current_invested_value - invested}')
