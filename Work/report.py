# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            dict = {}
            dict['name'] = row[0]
            dict['shares'] = int(row[1])
            dict['price'] = float(row[2])
            portfolio.append(dict)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')

