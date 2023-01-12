import csv

with open('linear_regression.csv', 'r') as f_in:
    reader = csv.reader(f_in)
    data = list(zip(*reader))

with open('linear_regression.csv', 'w', newline='') as f_out:
    writer = csv.writer(f_out)

    writer.writerows(data)
