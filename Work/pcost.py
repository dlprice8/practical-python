# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    Total_Cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        line_num = 0
        for line in rows:
            line_num += 1
            row = line
            try:
                shares = int(row[1])
            except ValueError:
                print(f"Missing value on line {line_num}: {line}")
            price = float(row[2])
            Total_Cost += shares * price
        return Total_Cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost:', cost)