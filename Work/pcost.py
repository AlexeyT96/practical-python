# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
total_cost = 0
for line in f:
    row = line.split(',')
    total_cost = total_cost + int(row[1])*float(row[2])
f.close()
print('Total cost ', total_cost)

