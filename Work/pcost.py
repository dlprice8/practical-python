# pcost.py
#
# Exercise 1.27

Total_Cost = 0

with open('Data/portfolio.csv','rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        Total_Cost += shares * price
    print('Total Cost:', Total_Cost)
